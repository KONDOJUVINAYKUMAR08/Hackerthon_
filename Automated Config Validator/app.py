'''5. Automated Config "Validator"
DevOps involves many .yaml, .json, and .ini files. 
This script takes a "Schema" and validates that all configuration files 
in a folder follow the rules (e.g., "Port" must be an integer 
between 1024-65535).

Key Libraries: yaml, json, configparser.'''
import yaml
import json

with open("Automated Config Validator/config.yaml") as f:
    data = yaml.safe_load(f)

port = data.get("port")

if not isinstance(port, int) or not (1024 <= port <= 65535):
    print("Invalid Port!!!")
else:
    print("Valid Config")
