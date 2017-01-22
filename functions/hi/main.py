import boto3
import os
import json

from base64 import b64decode

ENCRYPTED = os.environ['SECRET']
DECRYPTED = boto3.client('kms').decrypt(CiphertextBlob=b64decode(ENCRYPTED))['Plaintext']

def handle(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    print("Secret: " + DECRYPTED)
    return DECRYPTED

