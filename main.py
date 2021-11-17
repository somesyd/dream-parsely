import spacy
from flask import Flask, render_template, request
from parts import get_pos_json
from dream import get_dream_json
from spacytextblob.spacytextblob import SpacyTextBlob

app = Flask(__name__)
# run start up scripts to load the model

nlp = spacy.load('en_core_web_sm')
nlp.add_pipe("spacytextblob")

print(nlp.pipe_names)

@app.route('/')
def hello_world():
    return render_template('index.html', message="Text Parser API")

@app.route('/pos', methods=['POST'])
def parts_of_speech():
    if request.is_json:
        data = request.get_json()['text']
        return get_pos_json(nlp, data)
    else:
        data = request.get_data(as_text=True)
        return get_pos_json(nlp, data)

@app.route('/dream', methods=['POST'])
def parse_dream():
    if request.is_json:
        data = request.get_json()['text']
        return get_dream_json(nlp, data)
    else:
        data = request.get_data(as_text=True)
        print('hello')
        return get_dream_json(nlp, data)


if __name__ == '__main__':
    app.run()
