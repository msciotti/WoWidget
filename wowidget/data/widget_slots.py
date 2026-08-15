# Subtitle slot options: the "text" field must be a TEXT variable.
# Each entry may declare a default icon variable to pre-fill the icon slot.
SUBTITLE_OPTIONS = [
    {"key": "race_class",     "label": "Race / Class",             "type": "text", "suggested_label": "",           "icon": "faction_icon"},
    {"key": "realm",          "label": "Realm",                    "type": "text", "suggested_label": "Realm",      "icon": None},
    {"key": "guild",          "label": "Guild",                    "type": "text", "suggested_label": "Guild",      "icon": None},
    {"key": "spec_name",      "label": "Spec",                     "type": "text", "suggested_label": "Spec",       "icon": "spec_icon"},
    {"key": "raid_score",     "label": "Raid Progression",         "type": "text", "suggested_label": "Raid",       "icon": None},
    {"key": "heroic_score",   "label": "Heroic Progression",       "type": "text", "suggested_label": "Heroic",     "icon": None},
    {"key": "normal_score",   "label": "Normal Progression",       "type": "text", "suggested_label": "Normal",     "icon": None},
    {"key": "pvp_score",      "label": "Highest PvP Rating",       "type": "text", "suggested_label": "PvP",        "icon": None},
    {"key": "mythic_score2",  "label": "M+ Rating (Text)",         "type": "text", "suggested_label": "M+",         "icon": None},
    {"key": "last_login",     "label": "Last Login",               "type": "text", "suggested_label": "Last Login", "icon": None},
    {"key": "a_score2",       "label": "Achievement Points (Text)","type": "text", "suggested_label": "Achiev.",    "icon": "a_icon"},
]

# Stat slot options: both TEXT and NUMBER variables are valid.
# Each entry may declare a default icon variable.
STAT_OPTIONS = [
    {"key": "spec_name",     "label": "Spec",                      "type": "text",   "suggested_label": "Spec",            "icon": "spec_icon"},
    {"key": "gear_score",    "label": "Item Level",                "type": "number", "suggested_label": "Item Level",       "icon": None},
    {"key": "mythic_score",  "label": "M+ Rating",                 "type": "number", "suggested_label": "M+ Rating",        "icon": None},
    {"key": "mythic_score2", "label": "M+ Rating (Text)",          "type": "text",   "suggested_label": "M+ Rating",        "icon": None},
    {"key": "raid_score",    "label": "Raid Progression",          "type": "text",   "suggested_label": "Raid",             "icon": None},
    {"key": "heroic_score",  "label": "Heroic Progression",        "type": "text",   "suggested_label": "Heroic",           "icon": None},
    {"key": "normal_score",  "label": "Normal Progression",        "type": "text",   "suggested_label": "Normal",           "icon": None},
    {"key": "pvp_score",     "label": "Highest PvP Rating",        "type": "text",   "suggested_label": "PvP Rating",       "icon": None},
    {"key": "solo_score",    "label": "Solo Shuffle",              "type": "text",   "suggested_label": "Solo Shuffle",     "icon": None},
    {"key": "two_score",     "label": "2v2 Arena",                 "type": "text",   "suggested_label": "2v2 Arena",        "icon": None},
    {"key": "three_score",   "label": "3v3 Arena",                 "type": "text",   "suggested_label": "3v3 Arena",        "icon": None},
    {"key": "blitz_score",   "label": "Battleground Blitz",        "type": "text",   "suggested_label": "Blitz",            "icon": None},
    {"key": "rbg_score",     "label": "Rated Battlegrounds",       "type": "text",   "suggested_label": "Rated BG",         "icon": None},
    {"key": "character_level","label": "Level",                    "type": "number", "suggested_label": "Level",            "icon": None},
    {"key": "a_score",       "label": "Achievement Points",        "type": "number", "suggested_label": "Achiev. Points",   "icon": "a_icon"},
    {"key": "a_score2",      "label": "Achievement Points (Text)", "type": "text",   "suggested_label": "Achiev. Points",   "icon": "a_icon"},
    {"key": "mount_score",   "label": "Mounts",                    "type": "number", "suggested_label": "Mounts",           "icon": None},
    {"key": "pet_score",     "label": "Pets",                      "type": "number", "suggested_label": "Pets",             "icon": None},
    {"key": "feats_score",   "label": "Feats of Strength",         "type": "number", "suggested_label": "Feats of Strength","icon": None},
    {"key": "rep_score",     "label": "Exalted Reputations",       "type": "number", "suggested_label": "Exalted Reps",     "icon": None},
    {"key": "title_score",   "label": "Titles",                    "type": "number", "suggested_label": "Titles",           "icon": None},
    {"key": "last_login",    "label": "Last Login",                "type": "text",   "suggested_label": "Last Login",       "icon": None},
]

# Optional icon variables that can be attached to subtitle and stat slots.
ICON_OPTIONS = [
    {"key": "",             "label": "None"},
    {"key": "spec_icon",    "label": "Spec Icon"},
    {"key": "faction_icon", "label": "Faction Icon"},
    {"key": "a_icon",       "label": "Achievement Icon"},
]

# Sensible out-of-the-box defaults matching the existing documentation layout.
DEFAULT_LAYOUT = {
    "subtitle_1": {"text": "race_class",   "icon": "faction_icon", "label": ""},
    "subtitle_2": {"text": "realm",        "icon": "",             "label": "Realm"},
    "subtitle_3": {"text": "guild",        "icon": "",             "label": "Guild"},
    "stat_1":     {"value": "spec_name",      "icon": "spec_icon", "label": "Spec"},
    "stat_2":     {"value": "gear_score",     "icon": "",          "label": "Item Level"},
    "stat_3":     {"value": "mythic_score",   "icon": "",          "label": "M+ Rating"},
    "stat_4":     {"value": "raid_score",     "icon": "",          "label": "Raid Prog."},
    "stat_5":     {"value": "pvp_score",      "icon": "",          "label": "PvP Rating"},
    "stat_6":     {"value": "character_level","icon": "",          "label": "Level"},
}

# Fast lookup: variable key → presentation type string ("text" or "number")
_SUBTITLE_TYPE: dict[str, str] = {s["key"]: s["type"] for s in SUBTITLE_OPTIONS}
_STAT_TYPE: dict[str, str] = {s["key"]: s["type"] for s in STAT_OPTIONS}


def get_stat_type(key: str) -> str:
    return _STAT_TYPE.get(key, "text")


def get_subtitle_type(key: str) -> str:
    return _SUBTITLE_TYPE.get(key, "text")
