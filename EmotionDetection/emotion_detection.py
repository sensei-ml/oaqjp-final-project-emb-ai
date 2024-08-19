import requests
import json

def emotion_detector(text_to_analyze):
    '''
    Retrieve the Watson NLP Library functions.
    ---------
    Input: text to analize (str).
    Return: Text atribute of the response object received. 
    '''
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    MYOBJ = {'raw_document': {'text': text_to_analyze}}
    HEADERS = {'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock'}
    RESPONSE = requests.post(URL, json = MYOBJ, headers = HEADERS)
    FORMATTED_RESPONSE = json.loads(RESPONSE.text)
    emotions_values = FORMATTED_RESPONSE['emotionPredictions'][0]['emotion']
    emotions_values['dominant_emotion'] = max(emotions_values, key = emotions_values.get)
    if RESPONSE.status_code == 400:
        return None
    else:
        return emotions_values
