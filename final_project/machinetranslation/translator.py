import json
import os
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com')

def englishToFrench(english_text):
    '''Translates English to French'''
    if (len(english_text) < 1): #check for null inputs
        return "Error"
    try:
        translation = language_translator.translate(
            text=english_text,
            model_id='en-fr')
        french_text = json.dumps(translation.get_result()) #dump text to a json string
        french_text = french_text.split('\"') #split into a list
        return french_text[5] #retun first translation in the list
    except ApiException as ex:
        return "Method failed with status code " + str(ex.code) + ": " + ex.message

def frenchToEnglish(french_text):
    '''Translates French to English'''
    if (len(french_text) < 1): #check for null inputs
        return "Error"
    try:
        translation = language_translator.translate(
            text=french_text,
            model_id='fr-en')
        english_text = json.dumps(translation.get_result(), indent=2)
        english_text = english_text.split('\"') #split into a list
        return english_text[5]
    except ApiException as ex:
        return "Method failed with status code " + str(ex.code) + ": " + ex.message