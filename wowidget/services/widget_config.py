import requests

from wowidget.config import DISCORD_USER_AGENT, DISCORD_WIDGET_CONFIG_BASE
from wowidget.data.widget_slots import get_stat_type, get_subtitle_type


class WidgetConfigService:
    """Creates, updates, and publishes Discord widget layout configurations.

    Uses the Bot token — the widget-config endpoints authenticate via the
    application's bot rather than an OAuth Bearer token.
    """

    BASE_URL = DISCORD_WIDGET_CONFIG_BASE
    USER_AGENT = DISCORD_USER_AGENT

    def _headers(self, bot_token: str) -> dict:
        return {
            "Authorization": f"Bot {bot_token}",
            "Content-Type": "application/json",
            "User-Agent": self.USER_AGENT,
        }

    def get_existing_config_id(
        self,
        app_id: str,
        bot_token: str,
    ) -> str:
        """Return the ID of the first existing widget config, or empty string."""
        url = f"{self.BASE_URL}/applications/{app_id}/widget-configs"
        try:
            response = requests.get(
                url,
                headers=self._headers(bot_token),
                timeout=(10, 30),
            )
        except requests.RequestException as error:
            raise RuntimeError(f"Unable to reach Discord: {error}") from error

        if not response.ok:
            return ""

        configs = response.json()
        if isinstance(configs, list) and configs:
            return str(configs[0].get("config_id", ""))
        return ""

    def create_config(
        self,
        app_id: str,
        bot_token: str,
        payload: dict,
    ) -> str:
        """POST a new widget config and return its ID."""
        url = f"{self.BASE_URL}/applications/{app_id}/widget-configs"
        try:
            response = requests.post(
                url,
                headers=self._headers(bot_token),
                json=payload,
                timeout=(10, 30),
            )
        except requests.RequestException as error:
            raise RuntimeError(f"Unable to reach Discord: {error}") from error

        if not response.ok:
            raise RuntimeError(
                f"Discord rejected the widget config creation. "
                f"Status: {response.status_code}. "
                f"Response: {response.text.strip() or 'No body.'}"
            )

        return str(response.json().get("config_id", ""))

    def update_config(
        self,
        app_id: str,
        config_id: str,
        bot_token: str,
        payload: dict,
    ) -> None:
        """PATCH an existing widget config."""
        url = f"{self.BASE_URL}/applications/{app_id}/widget-configs/{config_id}"
        try:
            response = requests.patch(
                url,
                headers=self._headers(bot_token),
                json=payload,
                timeout=(10, 30),
            )
        except requests.RequestException as error:
            raise RuntimeError(f"Unable to reach Discord: {error}") from error

        if not response.ok:
            raise RuntimeError(
                f"Discord rejected the widget config update. "
                f"Status: {response.status_code}. "
                f"Response: {response.text.strip() or 'No body.'}"
            )

    def publish_config(
        self,
        app_id: str,
        config_id: str,
        bot_token: str,
    ) -> None:
        """Publish a widget config so it goes live on Discord profiles."""
        url = (
            f"{self.BASE_URL}/applications/{app_id}"
            f"/widget-configs/{config_id}/publish"
        )
        try:
            response = requests.post(
                url,
                headers=self._headers(bot_token),
                timeout=(10, 30),
            )
        except requests.RequestException as error:
            raise RuntimeError(f"Unable to reach Discord: {error}") from error

        if not response.ok:
            raise RuntimeError(
                f"Discord rejected the widget config publish. "
                f"Status: {response.status_code}. "
                f"Response: {response.text.strip() or 'No body.'}"
            )

    def upsert_and_publish(
        self,
        app_id: str,
        bot_token: str,
        layout_choices: dict,
        existing_config_id: str = "",
    ) -> str:
        """Create or update the widget config from layout_choices, then publish.

        Returns the config_id for caching so subsequent saves use PATCH.
        """
        payload = self._build_payload(layout_choices)

        config_id = existing_config_id or self.get_existing_config_id(
            app_id,
            bot_token,
        )

        if config_id:
            self.update_config(app_id, config_id, bot_token, payload)
        else:
            config_id = self.create_config(app_id, bot_token, payload)

        self.publish_config(app_id, config_id, bot_token)

        return config_id

    def _build_payload(self, layout_choices: dict) -> dict:
        """Convert layout_choices into the Discord widget-config API payload."""
        # ── widget_top ─────────────────────────────────────────────────────
        top_components: dict = {
            "hero_image": {
                "fields": {
                    "image": self._data_field("image", "character_model"),
                }
            },
            "title": {
                "fields": {
                    "text": self._data_field("text", "character_name"),
                }
            },
        }

        for slot in ("subtitle_1", "subtitle_2", "subtitle_3"):
            choice = layout_choices.get(slot)
            if not choice:
                continue

            text_key = choice.get("text", "")
            if not text_key:
                continue

            ptype = get_subtitle_type(text_key)
            fields: dict = {"text": self._data_field(ptype, text_key)}

            label_text = choice.get("label", "")
            if label_text:
                fields["label"] = self._custom_string_field(label_text)

            icon_key = choice.get("icon", "")
            if icon_key:
                fields["icon"] = self._data_field("image", icon_key)

            top_components[slot] = {"fields": fields}

        # ── widget_bottom ──────────────────────────────────────────────────
        bottom_components: dict = {}

        for slot in ("stat_1", "stat_2", "stat_3", "stat_4", "stat_5", "stat_6"):
            choice = layout_choices.get(slot)
            if not choice:
                continue

            value_key = choice.get("value", "")
            if not value_key:
                continue

            ptype = get_stat_type(value_key)
            label_text = choice.get("label", "")

            fields = {
                "value": self._data_field(ptype, value_key),
                "label": self._custom_string_field(label_text),
            }

            icon_key = choice.get("icon", "")
            if icon_key:
                fields["icon"] = self._data_field("image", icon_key)

            bottom_components[slot] = {"fields": fields}

        # ── add_widget_preview (fixed) ─────────────────────────────────────
        add_preview_components = {
            "hero_image": {
                "fields": {
                    "image": self._data_field("image", "character_model"),
                }
            }
        }

        # ── mini_profile (fixed) ───────────────────────────────────────────
        mini_profile_components = {
            "stat": {
                "fields": {
                    "text": self._data_field("text", "character_name"),
                    "icon": self._data_field("image", "spec_icon"),
                }
            },
            "contained_image": {
                "fields": {
                    "image": self._data_field("image", "character_model"),
                }
            },
        }

        return {
            "display_name": "WoWidget",
            "surfaces": {
                "widget_top": {
                    "layout": "widget_top_hero",
                    "components": top_components,
                },
                "widget_bottom": {
                    "layout": "widget_bottom_stats",
                    "components": bottom_components,
                },
                "add_widget_preview": {
                    "layout": "add_widget_preview_hero",
                    "components": add_preview_components,
                },
                "mini_profile": {
                    "layout": "mini_profile_contained_stat",
                    "components": mini_profile_components,
                },
            },
        }

    @staticmethod
    def _data_field(presentation_type: str, value: str) -> dict:
        return {
            "value_type": "data",
            "presentation_type": presentation_type,
            "value": value,
        }

    @staticmethod
    def _custom_string_field(value: str) -> dict:
        return {
            "value_type": "custom_string",
            "presentation_type": "text",
            "value": value,
        }
