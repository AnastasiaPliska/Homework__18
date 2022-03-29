import json


def get_candidates():
    with open('data/candidates.json', 'r', encoding="utf-8") as fp:
        candidates = json.load(fp)

    return candidates


def load_settings():
    with open('data/settings.json', 'r', encoding="utf-8") as fp:
        settings = json.load(fp)

    return settings
