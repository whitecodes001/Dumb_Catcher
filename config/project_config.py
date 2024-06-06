import json
import os

CONFIG_DIR = os.path.dirname(os.path.realpath(__file__))
ACCOUNT_CONFIG_PATH = os.path.join(CONFIG_DIR, "account_config.json")
TOKEN_FILE_PATH = os.path.join(os.path.dirname(CONFIG_DIR), "token.txt")

with open(ACCOUNT_CONFIG_PATH) as account_config_file:
    account_configs = json.load(account_config_file)

with open(TOKEN_FILE_PATH) as token_file:
    token_lines = token_file.read().splitlines()

for line in token_lines:
    token, guild_id = line.split()
    account_config = {
        "TOKEN": token,
        "GUILD_ID": guild_id
    }
    account_configs.append(account_config)