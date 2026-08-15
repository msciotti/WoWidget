import requests

from wowidget.config import DISCORD_USER_AGENT, DISCORD_WIDGET_CONFIG_BASE
from wowidget.data.widget_slots import get_stat_type, get_subtitle_type


class WidgetConfigService:
    """Creates, updates, and publishes Discord widget layout configurations.

    Uses the OAuth Bearer token (not the bot token) since the widget-config
    endpoints authenticate as the application team member, not as a bot.
    """

    BASE_URL = DISCORD_WIDGET_CONFIG_BASE
    USER_AGENT = DISCORD_USER_AGENT

    def _headers(self, access_token: str) -> dict:
        return {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "User-Agent": self.USER_AGENT,
        }

    def get_existing_config_id(
        self,
        app_id: str,
        access_token: str,
    ) -> str:
        """Return the ID of the first existing widget config, or empty string."""
        url = f"{self.BASE_URL}/applications/{app_id}/widget-configs"
        try:
            response = requests.get(
                url,
                headers=self._headers(access_token),
                timeout=(10, 30),
            )
        except requests.RequestException as error:
            raise RuntimeError(f"Unable to reach Discord: {error}") from error

        if not response.ok:
            return ""

        configs = response.json()
        if isinstance(configs, list) and configs:
            return str(configs[0].get("id", ""))
        return ""

    def create_config(
        self,
        app_id: str,
        access_token: str,
        payload: dict,
    ) -> str:
        """POST a new widget config and return its ID."""
        url = f"{self.BASE_URL}/applications/{app_id}/widget-configs"
        try:
            response = requests.post(
                url,
                headers=self._headers(access_token),
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

        return str(response.json().get("id", ""))

    def update_config(
        self,
        app_id: str,
        config_id: str,
        access_token: str,
        payload: dict,
    ) -> None:
        """PATCH an existing widget config."""
        url = f"{self.BASE_URL}/applications/{app_id}/widget-configs/{config_id}"
        try:
            response = requests.patch(
                url,
                headers=self._headers(access_token),
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
        access_token: str,
    ) -> None:
        """Publish a widget config so it goes live on Discord profiles."""
        url = (
            f"{self.BASE_URL}/applications/{app_id}"
            f"/widget-configs/{config_id}/publish"
        )
        try:
            response = requests.post(
                url,
                headers=self._headers(access_token),
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
        access_token: str,
        layout_choices: dict,
        existing_config_id: str = "",
    ) -> str:
        """Create or update the widget config from layout_choices, then publish.

        Returns the config ID (useful for caching in settings so subsequent
        saves use PATCH instead of POST).
        """
        payload = self._build_payload(layout_choices)

        config_id = existing_config_id or self.get_existing_config_id(
            app_id,
            access_token,
        )

        if config_id:
            self.update_config(app_id, config_id, access_token, payload)
        else:
            config_id = self.create_config(app_id, access_token, payload)

        self.publish_config(app_id, config_id, access_token)

        return config_id

    def _build_payload(self, layout_choices: dict) -> dict:
        """Convert the flat layout_choices dict into the Discord API payload."""
        # ── Surface 1: WIDGET_TOP (hero_overview) ─────────────────────────
        top_components: dict = {
            "hero_image": {
                "fields": {
                    "image": self._data_field(3, "character_model"),
                }
            },
            "title": {
                "fields": {
                    "text": self._data_field(1, "character_name"),
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
                fields["label"] = self._custom_string_field(1, label_text)

            icon_key = choice.get("icon", "")
            if icon_key:
                fields["icon"] = self._data_field(3, icon_key)

            top_components[slot] = {"fields": fields}

        # ── Surface 2: WIDGET_BOTTOM (stats_grid_3x2) ─────────────────────
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
                "label": self._custom_string_field(1, label_text),
            }

            icon_key = choice.get("icon", "")
            if icon_key:
                fields["icon"] = self._data_field(3, icon_key)

            bottom_components[slot] = {"fields": fields}

        return {
            "display_name": "WoWidget",
            "surfaces": {
                "1": {
                    "layout": "hero_overview",
                    "components": top_components,
                },
                "2": {
                    "layout": "stats_grid_3x2",
                    "components": bottom_components,
                },
            },
        }

    @staticmethod
    def _data_field(presentation_type: int, value: str) -> dict:
        return {
            "data": {
                "presentation_type": presentation_type,
                "value": value,
            }
        }

    @staticmethod
    def _custom_string_field(presentation_type: int, value: str) -> dict:
        return {
            "custom_string": {
                "presentation_type": presentation_type,
                "value": value,
            }
        }
