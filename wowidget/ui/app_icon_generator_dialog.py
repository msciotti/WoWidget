from io import BytesIO
from pathlib import Path

from PIL import Image
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPixmap
from PySide6.QtWidgets import (
    QColorDialog,
    QDialog,
    QFileDialog,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
)

from wowidget.services.app_icon_generator import AppIconGenerator
from wowidget.storage.database import get_app_data_directory
from wowidget.ui.theme import APP_STYLESHEET

DEFAULT_ICON_COLOR = "#6D4FE8"


class AppIconGeneratorDialog(QDialog):
    def __init__(
        self,
        parent=None,
    ) -> None:
        super().__init__(parent)

        self.generator = AppIconGenerator()
        self.generated_image: Image.Image | None = None

        self.setObjectName("IconGeneratorDialog")
        self.setWindowTitle("Icon Generator")
        self.setMinimumWidth(440)
        self.setStyleSheet(APP_STYLESHEET)

        window_layout = QVBoxLayout(self)
        window_layout.setContentsMargins(
            18,
            18,
            18,
            18,
        )

        content_card = QFrame()
        content_card.setObjectName("GlassCard")

        layout = QVBoxLayout(content_card)
        layout.setContentsMargins(
            22,
            20,
            22,
            20,
        )
        layout.setSpacing(12)

        title = QLabel("Icon Generator")
        title.setObjectName("SectionTitle")

        description = QLabel(
            "Choose a color and save the PNG for upload in the "
            "Discord Developer Portal."
        )
        description.setObjectName("MutedLabel")
        description.setWordWrap(True)

        color_row = QHBoxLayout()
        color_row.setSpacing(8)

        self.color_button = QPushButton("Choose Color")
        self.color_button.clicked.connect(self._choose_color)

        self.hex_input = QLineEdit(DEFAULT_ICON_COLOR)
        self.hex_input.setMaxLength(7)
        self.hex_input.setPlaceholderText(DEFAULT_ICON_COLOR)
        self.hex_input.textEdited.connect(self._update_preview_from_hex)
        self.hex_input.editingFinished.connect(self._normalize_hex_input)

        color_row.addWidget(self.color_button)
        color_row.addWidget(
            self.hex_input,
            stretch=1,
        )

        self.preview_label = QLabel()
        self.preview_label.setFixedSize(
            256,
            256,
        )
        self.preview_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.preview_label.setObjectName("InnerCard")

        button_row = QHBoxLayout()
        button_row.setSpacing(8)

        self.save_button = QPushButton("Save Icon")
        self.save_button.setObjectName("PrimaryButton")
        self.save_button.clicked.connect(self._save)

        close_button = QPushButton("Close")
        close_button.clicked.connect(self.accept)

        button_row.addWidget(self.save_button)
        button_row.addWidget(close_button)

        self.status_label = QLabel("")
        self.status_label.setObjectName("MutedLabel")
        self.status_label.setWordWrap(True)

        layout.addWidget(title)
        layout.addWidget(description)
        layout.addLayout(color_row)
        layout.addWidget(
            self.preview_label,
            alignment=Qt.AlignmentFlag.AlignHCenter,
        )
        layout.addLayout(button_row)
        layout.addWidget(self.status_label)

        window_layout.addWidget(content_card)

        self._apply_color(QColor(DEFAULT_ICON_COLOR))

    def _choose_color(
        self,
    ) -> None:
        initial = QColor(self.hex_input.text().strip())

        if not initial.isValid():
            initial = QColor(DEFAULT_ICON_COLOR)

        original = QColor(initial)
        dialog = QColorDialog(initial, self)
        dialog.setObjectName("WoWidgetColorDialog")
        dialog.setWindowTitle("Choose WoWidget Icon Color")
        dialog.setOption(
            QColorDialog.ColorDialogOption.DontUseNativeDialog,
            True,
        )
        dialog.setOption(QColorDialog.ColorDialogOption.ShowAlphaChannel, False)
        dialog.setStyleSheet(APP_STYLESHEET)

        for label in dialog.findChildren(QLabel):
            if label.text().strip().lower().startswith("html"):
                label.setText("Hex:")

        dialog.currentColorChanged.connect(self._apply_color)

        if dialog.exec() == QDialog.DialogCode.Accepted:
            self._apply_color(dialog.currentColor())
            return

        self._apply_color(original)

    def _update_preview_from_hex(
        self,
        value: str,
    ) -> None:
        normalized = self._normalized_hex(value)

        if normalized is None:
            return

        self._apply_color(QColor(normalized))

    def _normalize_hex_input(
        self,
    ) -> None:
        normalized = self._normalized_hex(self.hex_input.text())

        if normalized is None:
            return

        self._apply_color(QColor(normalized))

    @staticmethod
    def _normalized_hex(
        value: str,
    ) -> str | None:
        normalized = value.strip().lstrip("#").upper()

        if len(normalized) != 6:
            return None

        try:
            int(normalized, 16)
        except ValueError:
            return None

        return f"#{normalized}"

    def _apply_color(
        self,
        color: QColor,
    ) -> None:
        if not color.isValid():
            return

        normalized = color.name().upper()

        if self.hex_input.text() != normalized:
            self.hex_input.blockSignals(True)
            self.hex_input.setText(normalized)
            self.hex_input.blockSignals(False)

        try:
            self.generated_image = self.generator.generate(normalized)
        except Exception as error:
            self.generated_image = None
            self.save_button.setEnabled(False)
            self.status_label.setText(str(error))
            return

        buffer = BytesIO()
        self.generated_image.save(
            buffer,
            format="PNG",
        )

        pixmap = QPixmap()
        pixmap.loadFromData(buffer.getvalue(), "PNG")

        self.preview_label.setPixmap(
            pixmap.scaled(
                self.preview_label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
        )
        self.save_button.setEnabled(True)
        self.status_label.setText("Preview updates automatically as the color changes.")
        self._update_color_button(color)

    def _save(
        self,
    ) -> None:
        if self.generated_image is None:
            QMessageBox.information(
                self,
                "Icon Generator",
                "Choose a valid color before saving the icon.",
            )
            return

        normalized = self.hex_input.text().strip().lstrip("#").upper()
        output_directory = get_app_data_directory() / "generated-icons"
        output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        suggested_path = output_directory / f"WoWidget-{normalized}.png"

        selected_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Discord App Icon",
            str(suggested_path),
            "PNG Images (*.png)",
        )

        if not selected_path:
            return

        output_path = Path(selected_path)

        if output_path.suffix.lower() != ".png":
            output_path = output_path.with_suffix(".png")

        try:
            self.generator.save(
                self.generated_image,
                output_path,
            )
        except Exception as error:
            QMessageBox.critical(
                self,
                "Save Failed",
                str(error),
            )
            return

        self.status_label.setText(f"Icon saved to {output_path}")

    def _update_color_button(
        self,
        color: QColor,
    ) -> None:
        text_color = "#000000" if color.lightness() > 150 else "#FFFFFF"
        self.color_button.setStyleSheet(
            "QPushButton {"
            f"background-color: {color.name()};"
            f"color: {text_color};"
            "}"
        )
