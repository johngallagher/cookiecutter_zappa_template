import json

import os.path
import boto3
from base64 import b64decode

SECRETS = "secrets.json"

def secret(secret_name):
    return client_secrets()[secret_name.lower()]

def client_secrets():
    if os.path.isfile(SECRETS):
        with open(SECRETS) as f:
            return json.load(f)
    else:
        return environment_variables_lowercased()

def environment_variables_lowercased():
    return dict([(key.lower().replace('\\n', '\n'), decrypt(value)) for (key, value) in dict(os.environ).items()])

def decrypt(value):
    return boto3.client('kms').decrypt(CiphertextBlob=b64decode(value))['Plaintext']

