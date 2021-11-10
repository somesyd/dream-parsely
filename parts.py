import json

class POS:
    def __init__(self):
        self.count = 0
        self.nouns = []
        self.pronouns = []
        self.adjectives = []
        self.verbs = []
        self.adverbs = []
        self.prepositions = []
        self.conjunctions = []
        self.articles = []
        self.other = []

    def add(self, token):
        special_chars = list('[@_!#$%^&*()<>?/\|}{~:]')
        if (token.text.isnumeric()):
            return
        elif (token.text in special_chars or token.pos_ in ['PUNCT', 'SPACE']):
            # removed 'PART'
            return
        elif (token.pos_ in ['NOUN', 'PROPN']):
            self.count += 1
            self.nouns.append(token.text)
        elif (token.pos_ in ['PRON']):
            self.count += 1
            self.pronouns.append(token.text)
        elif (token.pos_ in ['ADJ']):
            self.count += 1
            self.adjectives.append(token.text)
        elif (token.pos_ in ['VERB', 'AUX']):
            self.count += 1
            self.verbs.append(token.text)
        elif (token.pos_ in ['ADV']):
            self.count += 1
            self.adverbs.append(token.text)
        elif (token.pos_ in ['ADP']):
            self.count += 1
            self.prepositions.append(token.text)
        elif (token.pos_ in ['CONJ', 'SCONJ', 'CCONJ']):
            self.count += 1
            self.conjunctions.append(token.text)
        elif (token.pos_ in ['DET']):
            self.count += 1
            self.articles.append(token.text)
        else:
            self.count += 1
            self.other.append(token.text)

def remove_empty_attributes(obj):
    for key, value in list(obj.items()):
        if not value:
            del obj[key]
    return obj

def get_pos_json(model, data):
    doc = model(data)
    data_pos = POS()
    for token in doc:
        data_pos.add(token)
    obj = data_pos.__dict__
    obj = remove_empty_attributes(obj)
    return json.dumps(obj)


