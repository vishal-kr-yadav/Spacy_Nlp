import spacy_basic
import spacy_feature_extraction
from flask import Flask, render_template, request,json

app=Flask(__name__)

@app.route('/')
def signUp():
    return render_template('homepage.html')

@app.route('/', methods=['POST'])
def signUpUser():
    option =  request.form['options'];
    search = request.form['search'];
    if option == "tokenization":
        result = spacy_basic.tokenization(search)
        return json.dumps(result)

    if option == "text_lematization":
        result = spacy_basic.text_lematization(search)
        return json.dumps(result)

    if option == "text_labelling":
        result = spacy_basic.text_labelling(search)
        return json.dumps(result)

    if option == "text_similarity":
        result = spacy_basic.text_similarity(search)
        return json.dumps(str(list(result)))

    if option == "extract_currency":
        result = spacy_feature_extraction.main([search])
        return json.dumps(result)

if __name__ == "__main__":
    app.run()
