This is simple N.L.P web Applications using SPACY.  
Why Spacy?  
- Fastest in the world   
 
    - spaCy excels at large-scale information extraction tasks. It's written from the ground up in carefully memory-managed Cython. Independent research has confirmed that spaCy is the fastest in the world. If your application needs to process entire web dumps, spaCy is the library you want to be using.  

- Get things done  

    - spaCy is designed to help you do real work — to build real products, or gather real insights. The library respects your time, and tries to avoid wasting it. It's easy to install, and its API is simple and productive. We like to think of spaCy as the Ruby on Rails of Natural Language Processing.  
    
-  Deep learning  
    -   spaCy is the best way to prepare text for deep learning. It interoperates seamlessly with TensorFlow, PyTorch, scikit-learn, Gensim and the rest of Python's awesome AI ecosystem. With spaCy, you can easily construct linguistically sophisticated statistical models for a variety of NLP problems.  
    
As of now, five features were added to the application.  
- Tokenization 
- Text Lematization 
- Entity Extraction 
- Text Similarity 
- Feature-Based Extraction

- **Tokenization** : Before executing any NLP based operation, the first step is to tokenize the text.  
    - example:   
        - Let's say your text is : **Apple is looking at buying U.K. startup for $1 billion**  
        - Then tokenization of the text will look like : **['Apple', 'is', 'looking', 'at', 'buying', 'U.K.', 'startup', 'for', '$', '1', 'billion']**  
          
- **Text Lematization** : The process of reducing the different forms of a word to one single form, for example, reducing "builds", "building", or "built" to the lemma "build".  
    - example: 
        -   Let's say your text is : **Apple is looking at buying U.K. startup for $1 billion** 
        -   Then lematization for corresponding to text are: **[{'text': 'Apple', 'lemma': 'apple'}, {'text': 'is', 'lemma': 'be'}, {'text': 'looking', 'lemma': 'look'}, {'text': 'at', 'lemma': 'at'}, {'text': 'buying', 'lemma': 'buy'}, {'text': 'U.K.', 'lemma': 'u.k.'}, {'text': 'startup', 'lemma': 'startup'}, {'text': 'for', 'lemma': 'for'}, {'text': '$', 'lemma': '$'}, {'text': '1', 'lemma': '1'}, {'text': 'billion', 'lemma': 'billion'}]**  
        
- **Entity Extraction** : Entity extraction, also known as entity name extraction or named entity recognition, is an information extraction technique that refers to the process of identifying and classifying key elements from text into pre-defined categories.  
    - example: 
        - Let's say your text is : **Apple is looking at buying U.K. startup for $1 billion**  
        - Then the output of the entity extraction : **[{'label': 'ORG', 'text': 'Apple'}, {'label': 'GPE', 'text': 'U.K.'}, {'label': 'MONEY', 'text': '$1 billion'}]**  
        
 
- **Text Similarity** : Similarity between each token of the text.
    - example: 
        - Let's say your text is : **Dog Cat candle**  
        - Then the output of text similarity is : **[{'text_2': 'dog', 'text_1': 'dog', 'similarity': 1.0}, {'text_2': 'cat', 'text_1': 'dog', 'similarity': 0.53906965}, {'text_2': 'banana', 'text_1': 'dog', 'similarity': 0.28761008}, {'text_2': 'dog', 'text_1': 'cat', 'similarity': 0.53906965}, {'text_2': 'cat', 'text_1': 'cat', 'similarity': 1.0}, {'text_2': 'banana', 'text_1': 'cat', 'similarity': 0.48752153}, {'text_2': 'dog', 'text_1': 'banana', 'similarity': 0.28761008}, {'text_2': 'cat', 'text_1': 'banana', 'similarity': 0.48752153}, {'text_2': 'banana', 'text_1': 'banana', 'similarity': 1.0}]**  
          
          
- **Feature-Based Extraction** : Based on some keywords it will extract the entity.
    - example:
        - Let's say your text is : **Apple is looking at buying U.K. startup for $1 billion**  
        - Then the output is :   
                        Expected output:  
                   Net income      MONEY   $9.4 million  
                   the prior year  MONEY   $2.7 million  
                   Revenue         MONEY   twelve billion dollars  
                    a loss          MONEY   1b   
    
   
**Script and its significance:**  
spacy_basic.py: some basic functionality of spacy library were written inside this script.  
spacy_feature_extraction: functionality of feature extraction.  
app.py: flask application.  

**Flow** :  
- Run the flask application using : python3 app.py  
- When you entered the text and submit the search, it will goes to backend and using ajax call it will call the another api function within flask app and from there the control is transfered to javascript and at last javascript will show the result using alert window.  

 
        
    

  
    

  



