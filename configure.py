import csv
from pathlib import Path
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob


def start_model():
    # run start up scripts to load the model
    nlp = spacy.load('en_core_web_sm')
    nlp.add_pipe("spacytextblob")
    print(nlp.pipe_names)
    return nlp

def add_people(nlp):
    # add person flags to vocab
    people_list = []
    with open('people_words.csv', newline='') as inputfile:
        for row in csv.reader(inputfile):
            people_list.append(row[0])
    IS_PERSON = nlp.vocab.add_flag(lambda text: text in people_list)
    return IS_PERSON

def add_animals(nlp):
    # add animal flags to vocab
    animal_list = []
    with open('animal_words.csv', newline='') as inputfile:
        for row in csv.reader(inputfile):
            animal_list.append(row[0])
    IS_ANIMAL = nlp.vocab.add_flag(lambda text: text in animal_list)
    return IS_ANIMAL