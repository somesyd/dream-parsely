import json
from spacy.matcher import Matcher
from ego import ego
from symbols import noun, place, thing
from characters import person, propname
from settings import where, mood, setting_place, setting_sub


class Dream:
    def __init__(self, nlp, text):
        self.nlp = nlp
        self.text = text
        self.doc = nlp(self.text)
        self.ego_matcher = Matcher(vocab=self.nlp.vocab)
        self.symbol_matcher = Matcher(vocab=self.nlp.vocab)
        self.character_matcher = Matcher(vocab=self.nlp.vocab)
        self.setting_matcher = Matcher(vocab=nlp.vocab)
        self.setting_submatcher = Matcher(vocab=nlp.vocab)
        self.ego = []
        self.ego_sentiment = []
        self.settings = []
        self.sub_settings = []
        self.symbols = []
        self.characters = []
        self.sentiment = []
        self.doc_sentiment = None
        # run set-up
        self.set_up_matchers()
        self.parse_ego()
        self.parse_symbols()
        self.parse_characters()
        self.parse_setting()
        self.add_sentiment()

    def set_up_matchers(self):
        # matches 'I' statements based on ego.py dict settings
        self.ego_matcher.add('ego', patterns=[ego], greedy='LONGEST')

        # matches nouns and named-entities
        self.symbol_matcher.add('symbols', patterns=[noun, place, thing], greedy='LONGEST')

        # matches proper nouns and person entities
        self.character_matcher.add('characters', patterns=[person, propname], greedy='LONGEST')

        # matches settings by named-entity or prepositional start
        self.setting_matcher.add('setting', patterns=[where, mood, setting_place], greedy='LONGEST')
        self.setting_submatcher.add('sub-setting', patterns=[setting_sub], greedy='LONGEST')

    def parse_ego(self):
        list_of_spans = self.ego_matcher(self.doc, as_spans=True)
        for span in list_of_spans:
            self.ego.append(span.text)

    def parse_symbols(self):
        list_of_spans = self.symbol_matcher(self.doc, as_spans=True)
        for span in list_of_spans:
            if span.text not in self.symbols:
                self.symbols.append(span.text)

    def parse_characters(self):
        list_of_spans = self.character_matcher(self.doc, as_spans=True)
        for span in list_of_spans:
            if span.text not in self.characters:
                self.characters.append(span.text)

    def parse_setting(self):
        list_of_spans = self.setting_matcher(self.doc, as_spans=True)
        list_of_settings = [] # temp list to catch sub-spans
        for span in list_of_spans:
            if span.text not in self.settings:
                self.settings.append(span.text)
                list_of_settings.append(span)
        for span in list_of_settings:
            sub = self.setting_submatcher(span, as_spans=True)
            for s in sub:
                if s.text not in self.sub_settings:
                    self.sub_settings.append(s.text)

    def add_sentiment(self):
        self.doc_sentiment = (self.doc._.polarity, self.doc._.subjectivity)
        for token in self.doc:
            if (token._.polarity != 0 or token._.subjectivity != 0):
                self.sentiment.append((token.text, token._.polarity, token._.subjectivity))


def remove_empty_attributes(obj):
    for key, value in list(obj.items()):
        if not value:
            del obj[key]
    return obj

def get_dream_json(nlp, data):
    dream = Dream(nlp, data)
    obj = dream.__dict__
    # delete extraneous sections of the object
    del obj['text']
    del obj['nlp']
    del obj['doc']
    del obj['ego_matcher']
    del obj['symbol_matcher']
    del obj['character_matcher']
    del obj['setting_matcher']
    del obj['setting_submatcher']
    obj = remove_empty_attributes(obj)
    return json.dumps(obj)
