import json

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QComboBox,
    QFrame,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

from wowidget.data.widget_slots import (
    DEFAULT_LAYOUT,
    ICON_OPTIONS,
    STAT_OPTIONS,
    SUBTITLE_OPTIONS,
)


# ──────────────────────────────────────────────────────────────────────────────
# Discord widget preview mockup
# ──────────────────────────────────────────────────────────────────────────────

_PREVIEW_CARD_STYLE = """
QFrame#DiscordPreviewCard {
    background-color: #1E1F22;
    border: 1px solid #3A3B3E;
    border-radius: 12px;
}
QLabel#PreviewHeroPlaceholder {
    background-color: #2B2D31;
    border: 1px solid #3A3B3E;
    border-radius: 8px;
    color: #5C5F66;
    font-size: 11px;
}
QLabel#PreviewTitle {
    color: #F2F3F5;
    font-size: 16px;
    font-weight: 700;
}
QLabel#PreviewSubtitleText {
    color: #B5BAC1;
    font-size: 12px;
}
QFrame#PreviewDivider {
    background-color: #3A3B3E;
    max-height: 1px;
    border: none;
}
QFrame#PreviewStatBox {
    background-color: #2B2D31;
    border: 1px solid #3A3B3E;
    border-radius: 6px;
}
QLabel#PreviewStatLabel {
    color: #87898D;
    font-size: 10px;
    font-weight: 600;
}
QLabel#PreviewStatValue {
    color: #F2F3F5;
    font-size: 13px;
    font-weight: 650;
}
"""


class _StatBox(QFrame):
    def __init__(self) -> None:
        super().__init__()
        self.setObjectName("PreviewStatBox")
        self.setFixedHeight(52)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(8, 6, 8, 6)
        layout.setSpacing(2)

        self.label = QLabel("—")
        self.label.setObjectName("PreviewStatLabel")
        self.value = QLabel("—")
        self.value.setObjectName("PreviewStatValue")

        layout.addWidget(self.label)
        layout.addWidget(self.value)


class WidgetPreviewWidget(QFrame):
    """A simplified Discord profile widget card for live preview."""

    def __init__(self) -> None:
        super().__init__()
        self.setObjectName("DiscordPreviewCard")
        self.setStyleSheet(_PREVIEW_CARD_STYLE)
        self.setFixedWidth(320)
        self._build_ui()

    def _build_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 14)
        layout.setSpacing(8)

        # Hero image placeholder
        self.hero_label = QLabel("character_model")
        self.hero_label.setObjectName("PreviewHeroPlaceholder")
        self.hero_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.hero_label.setFixedHeight(160)
        layout.addWidget(self.hero_label)

        # Character name (locked)
        self.title_label = QLabel("character_name")
        self.title_label.setObjectName("PreviewTitle")
        layout.addWidget(self.title_label)

        # Subtitle rows
        self.subtitle_labels: list[QLabel] = []
        for _ in range(3):
            lbl = QLabel("—")
            lbl.setObjectName("PreviewSubtitleText")
            layout.addWidget(lbl)
            self.subtitle_labels.append(lbl)

        # Divider
        divider = QFrame()
        divider.setObjectName("PreviewDivider")
        layout.addWidget(divider)

        # Stats 3×2 grid (columns: left, mid, right; rows top-to-bottom)
        grid_widget = QWidget()
        grid_layout = QHBoxLayout(grid_widget)
        grid_layout.setContentsMargins(0, 0, 0, 0)
        grid_layout.setSpacing(6)

        col_left = QVBoxLayout()
        col_left.setSpacing(6)
        col_mid = QVBoxLayout()
        col_mid.setSpacing(6)
        col_right = QVBoxLayout()
        col_right.setSpacing(6)

        self.stat_boxes: list[_StatBox] = []
        cols = [col_left, col_mid, col_right]
        for idx in range(6):
            box = _StatBox()
            cols[idx % 3].addWidget(box)
            self.stat_boxes.append(box)

        grid_layout.addLayout(col_left)
        grid_layout.addLayout(col_mid)
        grid_layout.addLayout(col_right)

        layout.addWidget(grid_widget)

    def update_preview(self, layout_choices: dict) -> None:
        subtitle_opts = {s["key"]: s["label"] for s in SUBTITLE_OPTIONS}
        stat_opts = {s["key"]: s["label"] for s in STAT_OPTIONS}

        for i, slot in enumerate(("subtitle_1", "subtitle_2", "subtitle_3")):
            choice = layout_choices.get(slot, {})
            text_key = choice.get("text", "")
            label_override = choice.get("label", "")
            display = label_override or subtitle_opts.get(text_key, text_key or "—")
            self.subtitle_labels[i].setText(display)

        for i, slot in enumerate(("stat_1", "stat_2", "stat_3", "stat_4", "stat_5", "stat_6")):
            choice = layout_choices.get(slot, {})
            value_key = choice.get("value", "")
            label_text = choice.get("label", "")
            self.stat_boxes[i].label.setText(label_text or stat_opts.get(value_key, "—"))
            self.stat_boxes[i].value.setText(value_key or "—")


# ──────────────────────────────────────────────────────────────────────────────
# Slot selector rows
# ──────────────────────────────────────────────────────────────────────────────

_SUBTITLE_LABELS: list[str] = sorted(
    {opt["suggested_label"] for opt in SUBTITLE_OPTIONS if opt["suggested_label"]}
)
_STAT_LABELS: list[str] = sorted(
    {opt["suggested_label"] for opt in STAT_OPTIONS if opt["suggested_label"]}
)


def _make_label_combo(labels: list[str]) -> QComboBox:
    """Return an editable combo pre-loaded with suggested labels."""
    combo = QComboBox()
    combo.setEditable(True)
    combo.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)
    combo.addItem("")
    for lbl in labels:
        combo.addItem(lbl)
    combo.setMinimumWidth(110)
    combo.setMaximumWidth(140)
    return combo


class _SubtitleSlotRow(QWidget):
    changed = Signal()

    def __init__(self, slot_number: int) -> None:
        super().__init__()
        outer = QVBoxLayout(self)
        outer.setContentsMargins(0, 0, 0, 0)
        outer.setSpacing(4)

        # Row 1: slot label + variable combo
        top = QHBoxLayout()
        top.setContentsMargins(0, 0, 0, 0)
        top.setSpacing(8)

        slot_label = QLabel(f"Subtitle {slot_number}")
        slot_label.setFixedWidth(70)
        top.addWidget(slot_label)

        self.combo = QComboBox()
        for opt in SUBTITLE_OPTIONS:
            self.combo.addItem(opt["label"], opt["key"])
        top.addWidget(self.combo, stretch=1)
        outer.addLayout(top)

        # Row 2: icon + label (indented to align with combo)
        bottom = QHBoxLayout()
        bottom.setContentsMargins(78, 0, 0, 0)
        bottom.setSpacing(8)

        bottom.addWidget(QLabel("Icon:"))
        self.icon_combo = QComboBox()
        for opt in ICON_OPTIONS:
            self.icon_combo.addItem(opt["label"], opt["key"])
        bottom.addWidget(self.icon_combo, stretch=1)

        bottom.addWidget(QLabel("Label:"))
        self.label_combo = _make_label_combo(_SUBTITLE_LABELS)
        self.label_combo.setMinimumWidth(0)
        self.label_combo.setMaximumWidth(16777215)
        bottom.addWidget(self.label_combo, stretch=1)
        outer.addLayout(bottom)

        self.combo.currentIndexChanged.connect(self._on_text_changed)
        self.icon_combo.currentIndexChanged.connect(self.changed.emit)
        self.label_combo.currentTextChanged.connect(self.changed.emit)

    def _on_text_changed(self) -> None:
        key = self.combo.currentData()
        for opt in SUBTITLE_OPTIONS:
            if opt["key"] == key:
                icon_key = opt.get("icon") or ""
                idx = self.icon_combo.findData(icon_key)
                if idx >= 0:
                    self.icon_combo.setCurrentIndex(idx)
                suggested = opt.get("suggested_label", "")
                self.label_combo.blockSignals(True)
                self.label_combo.setCurrentText(suggested)
                self.label_combo.blockSignals(False)
                break
        self.changed.emit()

    def get_choice(self) -> dict:
        return {
            "text": self.combo.currentData() or "",
            "icon": self.icon_combo.currentData() or "",
            "label": self.label_combo.currentText().strip(),
        }

    def set_choice(self, choice: dict) -> None:
        idx = self.combo.findData(choice.get("text", ""))
        if idx >= 0:
            self.combo.blockSignals(True)
            self.combo.setCurrentIndex(idx)
            self.combo.blockSignals(False)

        idx = self.icon_combo.findData(choice.get("icon", ""))
        if idx >= 0:
            self.icon_combo.blockSignals(True)
            self.icon_combo.setCurrentIndex(idx)
            self.icon_combo.blockSignals(False)

        self.label_combo.blockSignals(True)
        self.label_combo.setCurrentText(choice.get("label", ""))
        self.label_combo.blockSignals(False)


class _StatSlotRow(QWidget):
    changed = Signal()

    def __init__(self, slot_number: int, locked: bool = False) -> None:
        super().__init__()
        self._locked = locked
        outer = QVBoxLayout(self)
        outer.setContentsMargins(0, 0, 0, 0)
        outer.setSpacing(4)

        # Row 1: slot label + variable combo
        top = QHBoxLayout()
        top.setContentsMargins(0, 0, 0, 0)
        top.setSpacing(8)

        slot_label = QLabel(f"Stat {slot_number}")
        slot_label.setFixedWidth(40)
        top.addWidget(slot_label)

        self.combo = QComboBox()
        for opt in STAT_OPTIONS:
            self.combo.addItem(opt["label"], opt["key"])
        if locked:
            self.combo.setEnabled(False)
        top.addWidget(self.combo, stretch=1)
        outer.addLayout(top)

        # Row 2: icon + label (indented to align with combo)
        bottom = QHBoxLayout()
        bottom.setContentsMargins(48, 0, 0, 0)
        bottom.setSpacing(8)

        bottom.addWidget(QLabel("Icon:"))
        self.icon_combo = QComboBox()
        for opt in ICON_OPTIONS:
            self.icon_combo.addItem(opt["label"], opt["key"])
        if locked:
            self.icon_combo.setEnabled(False)
        bottom.addWidget(self.icon_combo, stretch=1)

        bottom.addWidget(QLabel("Label:"))
        self.label_combo = _make_label_combo(_STAT_LABELS)
        self.label_combo.setMinimumWidth(0)
        self.label_combo.setMaximumWidth(16777215)
        if locked:
            self.label_combo.setEnabled(False)
        bottom.addWidget(self.label_combo, stretch=1)
        outer.addLayout(bottom)

        self.combo.currentIndexChanged.connect(self._on_value_changed)
        self.icon_combo.currentIndexChanged.connect(self.changed.emit)
        self.label_combo.currentTextChanged.connect(self.changed.emit)

    def _on_value_changed(self) -> None:
        key = self.combo.currentData()
        for opt in STAT_OPTIONS:
            if opt["key"] == key:
                icon_key = opt.get("icon") or ""
                idx = self.icon_combo.findData(icon_key)
                if idx >= 0:
                    self.icon_combo.setCurrentIndex(idx)
                self.label_combo.blockSignals(True)
                self.label_combo.setCurrentText(opt.get("suggested_label", ""))
                self.label_combo.blockSignals(False)
                break
        self.changed.emit()

    def get_choice(self) -> dict:
        key = self.combo.currentData() or ""
        ptype = "text"
        for opt in STAT_OPTIONS:
            if opt["key"] == key:
                ptype = opt["type"]
                break
        return {
            "value": key,
            "icon": self.icon_combo.currentData() or "",
            "label": self.label_combo.currentText().strip(),
            "type": ptype,
        }

    def set_choice(self, choice: dict) -> None:
        idx = self.combo.findData(choice.get("value", ""))
        if idx >= 0:
            self.combo.blockSignals(True)
            self.combo.setCurrentIndex(idx)
            self.combo.blockSignals(False)

        idx = self.icon_combo.findData(choice.get("icon", ""))
        if idx >= 0:
            self.icon_combo.blockSignals(True)
            self.icon_combo.setCurrentIndex(idx)
            self.icon_combo.blockSignals(False)

        self.label_combo.blockSignals(True)
        self.label_combo.setCurrentText(choice.get("label", ""))
        self.label_combo.blockSignals(False)


# ──────────────────────────────────────────────────────────────────────────────
# Main designer page
# ──────────────────────────────────────────────────────────────────────────────

class WidgetDesignerPage(QWidget):
    """WYSIWYG Discord widget layout editor.

    Lets the user pick which WoWidget variables fill each slot on the Discord
    profile widget card, then pushes the configuration directly to Discord via
    the widget-config API — no developer portal interaction required.
    """

    back_requested = Signal()
    apply_requested = Signal(dict)  # emits layout_choices dict

    def __init__(self) -> None:
        super().__init__()
        self.setObjectName("PlainPage")
        self._build_ui()
        self._connect_signals()
        self.set_layout_choices(DEFAULT_LAYOUT)

    def _build_ui(self) -> None:
        page_layout = QVBoxLayout(self)
        page_layout.setContentsMargins(24, 22, 24, 20)
        page_layout.setSpacing(14)

        # ── Header ────────────────────────────────────────────────────────
        header = QFrame()
        header.setObjectName("GlassCard")
        header_layout = QVBoxLayout(header)
        header_layout.setContentsMargins(20, 16, 20, 16)

        title = QLabel("Widget Designer")
        title.setObjectName("PageTitle")
        subtitle = QLabel(
            "Configure your Discord profile widget layout. "
            "Changes are applied directly to Discord — "
            "no developer portal setup required."
        )
        subtitle.setObjectName("PageSubtitle")
        subtitle.setWordWrap(True)

        header_layout.addWidget(title)
        header_layout.addWidget(subtitle)
        page_layout.addWidget(header)

        # ── Two-panel body ─────────────────────────────────────────────────
        body = QFrame()
        body.setObjectName("GlassCard")
        body_layout = QHBoxLayout(body)
        body_layout.setContentsMargins(20, 18, 20, 18)
        body_layout.setSpacing(24)

        # Left: live preview
        preview_column = QVBoxLayout()
        preview_column.setSpacing(8)

        preview_title = QLabel("Preview")
        preview_title.setObjectName("SectionTitle")
        preview_column.addWidget(preview_title)

        self.preview = WidgetPreviewWidget()
        preview_column.addWidget(
            self.preview,
            alignment=Qt.AlignmentFlag.AlignTop,
        )
        preview_column.addStretch()

        body_layout.addLayout(preview_column)

        # Right: slot selectors in a scroll area
        selector_scroll = QScrollArea()
        selector_scroll.setObjectName("StatusContentScroll")
        selector_scroll.setWidgetResizable(True)
        selector_scroll.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        selector_scroll.setFrameShape(QFrame.Shape.NoFrame)

        selector_container = QWidget()
        selector_layout = QVBoxLayout(selector_container)
        selector_layout.setContentsMargins(0, 0, 0, 0)
        selector_layout.setSpacing(16)

        # Widget Top group
        top_group = QGroupBox("Widget Top")
        top_group_layout = QVBoxLayout(top_group)
        top_group_layout.setSpacing(14)

        # Fixed / locked slots
        for locked_text in (
            "Hero Image: character_model  (locked)",
            "Title: character_name  (locked)",
        ):
            lbl = QLabel(locked_text)
            lbl.setObjectName("MutedLabel")
            top_group_layout.addWidget(lbl)

        self.subtitle_rows: list[_SubtitleSlotRow] = []
        for i in range(1, 4):
            row = _SubtitleSlotRow(i)
            top_group_layout.addWidget(row)
            self.subtitle_rows.append(row)

        selector_layout.addWidget(top_group)

        # Widget Bottom group
        bottom_group = QGroupBox("Widget Bottom — Stats Grid")
        bottom_group_layout = QVBoxLayout(bottom_group)
        bottom_group_layout.setSpacing(14)

        self.stat_rows: list[_StatSlotRow] = []
        for i in range(1, 7):
            row = _StatSlotRow(i)
            bottom_group_layout.addWidget(row)
            self.stat_rows.append(row)

        selector_layout.addWidget(bottom_group)
        selector_layout.addStretch()

        selector_scroll.setWidget(selector_container)
        body_layout.addWidget(selector_scroll, stretch=1)

        page_layout.addWidget(body, stretch=1)

        # ── Action bar ─────────────────────────────────────────────────────
        action_card = QFrame()
        action_card.setObjectName("GlassCard")
        action_layout = QHBoxLayout(action_card)
        action_layout.setContentsMargins(14, 12, 14, 12)
        action_layout.setSpacing(9)

        self.apply_button = QPushButton("Apply to Discord")
        self.apply_button.setObjectName("PrimaryButton")
        self.apply_button.clicked.connect(self._emit_apply)

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.back_requested.emit)

        self.status_label = QLabel("")
        self.status_label.setWordWrap(True)
        self.status_label.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Preferred,
        )

        action_layout.addWidget(self.apply_button)
        action_layout.addWidget(self.back_button)
        action_layout.addWidget(self.status_label, stretch=1)

        page_layout.addWidget(action_card)

    def _connect_signals(self) -> None:
        for row in self.subtitle_rows:
            row.changed.connect(self._refresh_preview)
        for row in self.stat_rows:
            row.changed.connect(self._refresh_preview)

    def _refresh_preview(self) -> None:
        self.preview.update_preview(self.get_layout_choices())

    def _emit_apply(self) -> None:
        self.apply_requested.emit(self.get_layout_choices())

    # ── Public API ─────────────────────────────────────────────────────────

    def get_layout_choices(self) -> dict:
        choices: dict = {}
        for i, row in enumerate(self.subtitle_rows, start=1):
            choices[f"subtitle_{i}"] = row.get_choice()
        for i, row in enumerate(self.stat_rows, start=1):
            choices[f"stat_{i}"] = row.get_choice()
        return choices

    def set_layout_choices(self, choices: dict) -> None:
        for i, row in enumerate(self.subtitle_rows, start=1):
            slot_data = choices.get(f"subtitle_{i}", {})
            if slot_data:
                row.set_choice(slot_data)

        for i, row in enumerate(self.stat_rows, start=1):
            slot_data = choices.get(f"stat_{i}", {})
            if slot_data:
                row.set_choice(slot_data)

        self._refresh_preview()

    def load_from_json(self, json_string: str) -> None:
        """Restore slot selections from a persisted JSON string."""
        if not json_string:
            self.set_layout_choices(DEFAULT_LAYOUT)
            return
        try:
            choices = json.loads(json_string)
            self.set_layout_choices(choices)
        except (json.JSONDecodeError, TypeError):
            self.set_layout_choices(DEFAULT_LAYOUT)

    def set_apply_busy(self, busy: bool) -> None:
        self.apply_button.setEnabled(not busy)
        self.back_button.setEnabled(not busy)
        self.apply_button.setText(
            "Applying..." if busy else "Apply to Discord"
        )

    def set_status(self, message: str, *, is_error: bool = False) -> None:
        self.status_label.setObjectName(
            "StatusError" if is_error else "StatusSuccess"
        )
        self.status_label.style().unpolish(self.status_label)
        self.status_label.style().polish(self.status_label)
        self.status_label.setText(message)
