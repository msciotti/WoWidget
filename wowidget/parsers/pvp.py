from typing import Any


PVP_QUEUE_DEFAULTS: dict[str, int | str] = {
    "highest": "---",
    "2v2": "---",
    "3v3": "---",
    "shuffle": "---",
    "rbg": "---",
    "blitz": "---",
}


PVP_BRACKET_TYPES: dict[str, str] = {
    "ARENA_2V2": "2v2",
    "ARENA_3V3": "3v3",
    "SHUFFLE": "shuffle",
    "BLITZ": "blitz",
    "BATTLEGROUNDS": "rbg",
    "RATED_BATTLEGROUND": "rbg",
    "RATED_BATTLEGROUNDS": "rbg",
}


def safe_dict(value: Any) -> dict:
    return value if isinstance(value, dict) else {}


def safe_list(value: Any) -> list:
    return value if isinstance(value, list) else []


def parse_rating(value: Any) -> int | None:
    try:
        rating = int(value)
    except (TypeError, ValueError):
        return None

    return rating if rating > 0 else None


def identify_pvp_queue(bracket: dict) -> str | None:
    bracket_details = safe_dict(bracket.get("bracket"))
    bracket_type = str(bracket_details.get("type") or "").upper()

    queue = PVP_BRACKET_TYPES.get(bracket_type)

    if queue:
        return queue

    links = safe_dict(bracket.get("_links"))
    self_link = safe_dict(links.get("self"))
    href = str(self_link.get("href") or "").lower()

    if "/pvp-bracket/2v2" in href:
        return "2v2"

    if "/pvp-bracket/3v3" in href:
        return "3v3"

    if "/pvp-bracket/shuffle-" in href:
        return "shuffle"

    if "/pvp-bracket/blitz-" in href:
        return "blitz"

    if (
        "/pvp-bracket/rbg" in href
        or "/pvp-bracket/rated-battleground" in href
        or "/pvp-bracket/battlegrounds" in href
    ):
        return "rbg"

    return None


def parse_pvp_ratings(
    pvp_brackets: list,
) -> dict[str, int | str]:
    ratings = PVP_QUEUE_DEFAULTS.copy()
    highest_rating = 0

    for bracket in safe_list(pvp_brackets):
        bracket = safe_dict(bracket)
        rating = parse_rating(bracket.get("rating"))

        if rating is None:
            continue

        highest_rating = max(highest_rating, rating)

        queue = identify_pvp_queue(bracket)

        if queue is None:
            continue

        current_rating = ratings.get(queue)
        current_rating = current_rating if isinstance(current_rating, int) else 0

        ratings[queue] = max(current_rating, rating)

    if highest_rating > 0:
        ratings["highest"] = highest_rating

    return ratings


def parse_highest_pvp_rating(
    pvp_brackets: list,
) -> int | str:
    return parse_pvp_ratings(pvp_brackets)["highest"]