#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from authomatic.providers import oauth2
from authomatic import Authomatic
import os
import logging
import boto3
from base64 import b64decode

kms = boto3.client('kms')
# Encrypted env vars
GOOGLE_OAUTH_CLIENT_ID = kms.decrypt(CiphertextBlob=b64decode(os.environ.get('GOOGLE_OAUTH_CLIENT_ID')))['Plaintext']
GOOGLE_OAUTH_CONSUMER_SECRET = kms.decrypt(CiphertextBlob=b64decode(os.environ.get('GOOGLE_OAUTH_CONSUMER_SECRET')))['Plaintext']
AUTHOMATIC_SALT = kms.decrypt(CiphertextBlob=b64decode(os.environ.get('AUTHOMATIC_SALT')))['Plaintext']
GOOGLE_CREDS = kms.decrypt(CiphertextBlob=b64decode(os.environ.get('GOOGLE_CREDS')))['Plaintext']
# env vars
BUCKET = os.environ.get('BUCKET')
ANNO_PATH = os.environ.get('ANNO_PATH')

#Global vars
DEFAULT_MAX_AGE = 20
SPREADSHEET_URL_TEMPLATE = 'https://docs.google.com/spreadsheets/u/1/d/%s/export?format=csv&gid=0'
DOC_URL_TEMPLATE = 'https://www.googleapis.com/drive/v3/files/%s/export?mimeType=text/html'


LOG_FORMAT = '%(levelname)s:%(name)s:%(asctime)s: %(message)s'
LOG_LEVEL = logging.WARNING

SPEAKERS = {
    'HILLARY CLINTON': 'speaker dem',
    'TIM KAINE': 'speaker dem',
    'DONALD TRUMP': 'speaker gop',
    'MIKE PENCE': 'speaker gop'
}

# Drive keys
AUTHORS_GOOGLE_DOC_KEY = '1s0Vs4c41kp8mCvGnIFbdPK9YI9t18u0c2kvh6W1eZBw'
TRANSCRIPT_GDOC_KEY = '19J7LB38ePACZnvs3PrFA0jcV_x1kRRgXlAIMPaS6zD4'

authomatic_config = {
    'google': {
        'id': 1,
        'class_': oauth2.Google,
        'consumer_key': GOOGLE_OAUTH_CLIENT_ID,
        'consumer_secret': GOOGLE_OAUTH_CONSUMER_SECRET,
        'scope': ['https://www.googleapis.com/auth/drive',
                  'https://www.googleapis.com/auth/userinfo.email',
                  'https://www.googleapis.com/auth/drive.scripts',
                  'https://www.googleapis.com/auth/documents',
                  'https://www.googleapis.com/auth/script.external_request',
                  'https://www.googleapis.com/auth/script.scriptapp',
                  'https://www.googleapis.com/auth/script.send_mail',
                  'https://www.googleapis.com/auth/script.storage',
                  'https://www.googleapis.com/auth/spreadsheets'],
        'offline': True,
    },
}

authomatic = Authomatic(authomatic_config, AUTHOMATIC_SALT)
