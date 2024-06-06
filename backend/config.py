import json
import os

CONFIG_DIR = os.path.dirname(os.path.realpath(__file__))
CONFIG_FILE_PATH = os.path.join(CONFIG_DIR, "..", "config", "config.json")
ACCOUNT_CONFIG_PATH = os.path.join(CONFIG_DIR, "..", "config", "account_config.json")

with open(CONFIG_FILE_PATH) as config_file:
    common_config = json.load(config_file)

USER_ID = common_config['USER_ID']
GATEWAY_URL = common_config['GATEWAY_URL']

with open(ACCOUNT_CONFIG_PATH) as account_config_file:
    account_configs = json.load(account_config_file)