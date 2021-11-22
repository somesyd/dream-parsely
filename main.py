from flask import Flask, render_template, request
from configure import start_model, add_animals, add_people
from parts import get_pos_json
from dream import get_dream_json

app = Flask(__name__)
# set up the model
nlp = start_model()
IS_PERSON = add_people(nlp)
IS_ANIMAL = add_animals(nlp)

# server
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
        return get_dream_json(nlp, data, IS_PERSON, IS_ANIMAL)
    else:
        data = request.get_data(as_text=True)
        print('hello')
        return get_dream_json(nlp, data, IS_PERSON, IS_ANIMAL)


if __name__ == '__main__':
    app.run()
