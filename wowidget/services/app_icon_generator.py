from colorsys import hsv_to_rgb, rgb_to_hsv
from pathlib import Path
from typing import Final

from PIL import Image

TEMPLATE_PATH: Final[Path] = (
    Path(__file__).resolve().parents[1]
    / "assets"
    / "icons"
    / "discord-app-icon-template.png"
)


class AppIconGenerator:
    def __init__(
        self,
        template_path: Path = TEMPLATE_PATH,
    ) -> None:
        self.template_path = template_path

    def generate(
        self,
        hex_color: str,
    ) -> Image.Image:
        red, green, blue = self._parse_hex_color(hex_color)
        hue, saturation, brightness = rgb_to_hsv(
            red / 255,
            green / 255,
            blue / 255,
        )

        try:
            with Image.open(self.template_path) as source:
                template = source.convert("RGBA")
        except Exception as error:
            raise RuntimeError(
                "The Discord app icon template could not be opened."
            ) from error

        pixels = []

        for source_red, source_green, source_blue, alpha in template.getdata():
            if alpha == 0:
                pixels.append((0, 0, 0, 0))
                continue

            luminance = (
                0.2126 * source_red
                + 0.7152 * source_green
                + 0.0722 * source_blue
            ) / 255

            shading = 0.08 + (luminance * 0.92)
            tinted_red, tinted_green, tinted_blue = hsv_to_rgb(
                hue,
                saturation,
                brightness * shading,
            )

            pixels.append(
                (
                    round(tinted_red * 255),
                    round(tinted_green * 255),
                    round(tinted_blue * 255),
                    alpha,
                )
            )

        result = Image.new(
            "RGBA",
            template.size,
        )
        result.putdata(pixels)

        return result

    @staticmethod
    def save(
        image: Image.Image,
        output_path: Path,
    ) -> Path:
        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )
        image.save(
            output_path,
            format="PNG",
            optimize=True,
        )

        return output_path

    @staticmethod
    def _parse_hex_color(
        value: str,
    ) -> tuple[int, int, int]:
        normalized = value.strip().lstrip("#")

        if len(normalized) != 6:
            raise ValueError("Enter a six-digit hex color such as #6D4FE8.")

        try:
            return tuple(
                int(normalized[index : index + 2], 16)
                for index in (
                    0,
                    2,
                    4,
                )
            )
        except ValueError as error:
            raise ValueError("Enter a valid hexadecimal color.") from error
