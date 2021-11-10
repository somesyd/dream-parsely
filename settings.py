where_preps = ['aboard', 'above', 'across', 'against', 'along', 'amid', 'amidst', 'among', 'around', 'at', 'atop',
               'behind', 'below', 'beneath', 'beside', 'between', 'by', 'down', 'in', 'inside', 'into', 'near',
               'off', 'on', 'onto', 'out', 'outside', 'over', 'past', 'to', 'under', 'underneath', 'up', 'upon',
               'within', 'without']
where = [
    {'LOWER': {'IN':where_preps}},
    {'POS': 'VERB', 'OP': '!'},
    {'POS': 'ADP', 'OP': '*'},
    {'POS': 'PRON', 'OP': '*'},
    {'POS': 'VERB', 'OP': '*'},
    {'POS': 'PART', 'OP': '*'},
    {'POS': 'VERB', 'OP': '*'},
    {'POS': 'DET',  'OP': '*'},
    {'POS': 'ADJ',  'OP': '*'},
    {'POS': 'NOUN',  'OP': '+'},
    {'POS': 'ADP',  'OP': '*'},
    {'POS': 'DET',  'OP': '*'},
    {'POS': 'PRON',  'OP': '*'},
    {'POS': 'ADJ',  'OP': '*'},
    {'POS': 'ADP',  'OP': '*'},
    {'POS': 'NOUN',  'OP': '*'},
]

mood = [
    {'LOWER': 'it'},
    {'POS': 'VERB'},
    {'POS': 'DET', 'OP': '*'},
    {'POS': 'PRON', 'OP': '*'},
    {'POS': 'ADV', 'OP': '*'},
    {'POS': 'ADJ', 'OP': '*'},
    {'POS': 'NOUN', 'OP': '*'},
    {'POS': 'CCONJ', 'OP': '?'},
    {'POS': 'DET', 'OP': '*'},
    {'POS': 'ADV', 'OP': '*'},
    {'POS': 'ADJ', 'OP': '*'}

]

setting_place = [
    {'ENT_TYPE': 'NORP', 'OP': '*'},
    {'ENT_TYPE': 'FACILITY', 'OP': '*'},
    {'ENT_TYPE': 'FAC', 'OP': '*'},
    {'ENT_TYPE': 'ORG', 'OP': '*'},
    {'ENT_TYPE': 'GPE', 'OP': '*'}
]

setting_sub = [{'POS': 'ADJ', 'OP': '*'}, {'POS': 'NOUN', 'OP': '*'}]