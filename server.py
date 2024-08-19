'''
Server.py to render the App using flask and the NLP Modules.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask('Emotion Detection')

@app.route('/emotionDetector')
def emot_detector():
    '''
    Sents the request using the text_to_analyze with the module and retrieve the result in the app.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        output = 'Invalid text! Please try again!.'
    output = 'For the given statement, the system response is '
    for key, value in list(response.items())[:-1]:
        output += f'{key}: {value} '
    output += output[:-1] + f'. The dominant emotion is {response["dominant_emotion"]}.'
    return output
@app.route('/')
def render_index_page():
    '''
    Render the index.html using render_template.
    '''
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)
