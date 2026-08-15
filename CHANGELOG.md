# Changelog

## 1.2.0 — Midnight Season 2

### Changed

- Updated raid progression to track Midnight Season 2 content:
  - The Venomous Abyss (8 bosses)
  - The Tidebound Grotto (1 boss)

## 1.1.0 — UI Refresh, PvP Expansion, and Raid Progression

### Added

- Added queue-specific PvP widget variables:
  - `solo_score` for Solo Shuffle
  - `two_score` for 2v2 Arena
  - `three_score` for 3v3 Arena
  - `blitz_score` for Battleground Blitz
  - `rbg_score` for Rated Battlegrounds
- Added `heroic_score` for Heroic raid progression.
- Added `normal_score` for Normal raid progression.
- Added the built-in Icon Generator for creating custom Discord application icons.
- Added live icon previews with color-picker and hex-code support.
- Added a Portrait Folder button to the Portrait Editor.
- Added copy controls to the Widget Variables documentation.
- Added a reusable release announcement banner to the documentation website.

### Improved

- Redesigned PvP data collection to query supported bracket endpoints directly instead of relying exclusively on Blizzard's PvP summary response.
- Updated PvP variables to use text presentation so ratings display in full without abbreviation or comma formatting.
- Updated raid parsing to expose Mythic/default, Heroic, and Normal progression independently.
- Redesigned the WoWidget home page and removed redundant character-stat panels.
- Converted the Portrait Editor to a horizontal layout so the preview and all controls remain visible together.
- Restyled the Icon Generator and color picker to match WoWidget's visual theme.
- Improved generated icon handling for brightness, grayscale, white, gray, and black colors.
- Added forgiving hex-code input with automatic formatting.
- Reorganized Widget Variables documentation into clearer categories.
- Simplified Widget Setup by linking to the dedicated Widget Variables reference.
- Reorganized documentation navigation to make Widget Variables easier to locate.

### Changed

- Replaced the **Minimize to Tray** home-page button with **Icon Generator**.
- Moved **Settings** to the final position in the home-page action row.
- Moved FAQ under the Support navigation section.
- Promoted Widget Variables to a direct navigation item.

## 1.0.1

- Added support for the `a_icon` Discord User Variable for achievement icons.
- Added achievement icon configuration to the Widget Editor documentation.
- Documented the `a_icon` widget variable in the reference guide.
- Added the achievement icon asset for Discord widget rendering.

## 1.0.0 — Release Candidate 1

- Standardized public Discord User Variable names across the application and
  documentation.
- Added support for the documented character level variable.
- Defaulted the documentation website to dark mode while preserving the light
  theme toggle.
- Completed the core setup, usage, reference, FAQ, troubleshooting, and About
  documentation.
- Corrected parser exception handling for Python 3.
- Corrected the Cloudflare worker's repository identifier.
- Tightened release exclusions for local documentation environments and build
  output.
