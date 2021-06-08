import json

def open_config() -> dict:
    """Opens the config.json and returns it as a dictionary."""
    with open('config.json') as config_json:
        data = json.load(config_json)
        return data


DEFAULT_FALSE_KEYS = ["red-demon", "cyclops-god", "ent-ancient", "lich-king"]
DEFAULT_TRUE_KEYS = ["hermit-god", "grand-sphinx","lord-of-the-lost-lands","skull-shrine","pentaract","cube-god","lost-sentry","aliens","ghost-ship","temple-statues","rock-dragon","dwarf-miner","killer-bee-nest","avatar","ghost-king","keyper","keyper-tower","the-gardener","leprechaun","mysterious","crystal","realm-closed","beach-bum" ,"staff-member" ,"key-pop"]