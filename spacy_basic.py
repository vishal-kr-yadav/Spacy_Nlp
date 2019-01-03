from __future__ import unicode_literals, print_function
import spacy
import plac


def tokenization(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    tokenize_list=[]
    for token in doc:
        tokenize_list.append(token.text)
    return tokenize_list

# result=tokenization(u'Apple is looking at buying U.K. startup for $1 billion')
# print(result)

def text_lematization(text):

    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    lematization_list=[]

    for token in doc:
        dict = {}
        dict["text"]=token.text
        dict["lemma"]=token.lemma_
        lematization_list.append(dict)
    return lematization_list

# result=text_lematization(u'Apple is looking at buying U.K. startup for $1 billion')
# print(result)

def text_labelling(text):

    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    labelling_list=[]
    for ent in doc.ents:
        dict={}
        dict["text"]=ent.text
        dict["label"]=ent.label_
        labelling_list.append(dict)
    return labelling_list


# result=text_labelling(u'Apple is looking at buying U.K. startup for $1 billion')
# print(result)

def text_similarity(text):
    nlp = spacy.load('en_core_web_sm')  # make sure to use larger model!
    tokens = nlp(text)
    print(tokens)
    similarity_list=[]
    for token1 in tokens:
        for token2 in tokens:
            dict={}
            dict["text_1"]=token1.text
            dict["text_2"]=token2.text
            dict["similarity"]=token1.similarity(token2)
            similarity_list.append(dict)
    return similarity_list

# result=text_similarity(u'dog cat banana')
# print(result)

