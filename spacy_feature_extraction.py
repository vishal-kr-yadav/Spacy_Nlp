from __future__ import unicode_literals, print_function
import spacy
import plac

def main(TEXTS):
    @plac.annotations(
        model=("Model to load (needs parser and NER)", "positional", None, str))
    def entity_extraction(model='en_core_web_sm'):
        nlp = spacy.load(model)
        print("Loaded model '%s'" % model)
        print("Processing %d texts" % len(TEXTS))

        extraction_list = []
        for text in TEXTS:
            doc = nlp(text)
            relations = extract_currency_relations(doc)
            for r1, r2 in relations:
                dict = {}
                dict["text"] = r1.text + " " + r2.ent_type_
                dict["entity"] = r2.text
                extraction_list.append(dict)
                # print('{:<10}\t{}\t{}'.format(r1.text, r2.ent_type_, r2.text))
        return extraction_list


    def extract_currency_relations(doc):
        # merge entities and noun chunks into one token
        spans = list(doc.ents) + list(doc.noun_chunks)
        for span in spans:
            span.merge()

        relations = []
        for money in filter(lambda w: w.ent_type_ == 'MONEY', doc):
            if money.dep_ in ('attr', 'dobj'):
                subject = [w for w in money.head.lefts if w.dep_ == 'nsubj']
                if subject:
                    subject = subject[0]
                    relations.append((subject, money))
            elif money.dep_ == 'pobj' and money.head.dep_ == 'prep':
                relations.append((money.head.head, money))
        return relations



    result = plac.call(entity_extraction)
    print("===",result)
    return result
# TEXTS = [
#     'Net income was $9.4 million compared to the prior year of $2.7 million.',
#     'Revenue exceeded twelve billion dollars, with a loss of $1b.'
# ]
# b=main(TEXTS)
# print(b)