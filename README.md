# Parse-ly :herb:
### text parser API

> If a parsley farmer is sued, can they garnish his wages? 
>  &ndash; George Carlin

#### REQUESTS

**Get parts-of-speech lists for a chunk of text**

`POST`  /pos

**Parameters (for Content-Type JSON):**

Name | Type | In | Description
-----|------|----|------------
text| string | body | the text to parse

**Code Samples:**

Python (with JSON)
```
import requests
import json

url = "https://cs361-somerfis-serve.uw.r.appspot.com/pos"
payload = { "text": "if a parsley farmer is sued, can they garnish her wages?" }

response = requests.post(url, data=json.dumps(payload) 
```

Python (with plain text)
```
url = "https://cs361-somerfis-serve.uw.r.appspot.com/pos"
text = "if a parsley farmer is sued, can they garnish her wages?"

r = requests.post(url, data=text)
```

#### RESPONSE

returns JSON
```
200 OK
{
    'count': 11, 
    'nouns': ['farmer', 'wages'], 
    'pronouns': ['they', 'her'], 
    'adjectives': ['parsley'], 
    'verbs': ['is', 'sued', 'can', 'garnish'], 
    'conjunctions': ['if'], 
    'articles': ['a']
}

```

**Possible Attributes:**
*the attribute will not appear if it results in an empty list*

key | type |description
----|------|-----------
count|int|word count of text
nouns|list|list of nouns (strings) found in text
pronouns|list|list of pronouns (strings) found in text
adjectives|list|list of adjectives (strings) found in text
verbs|list|list of verbs (strings) found in text
adverbs|list|list of adverbs (strings) found in text
prepositions|list|list of prepositions (strings) found in text
conjunctions|list|list of conjunctions (strings) found in text
articles|list|list of articles (strings) found in text
other|list|list of words (strings) that could not be categorized
