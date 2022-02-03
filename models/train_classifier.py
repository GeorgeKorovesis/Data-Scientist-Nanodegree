import sys
import re
import nltk
import pandas as pd
import numpy as np

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

from sklearn.externals import joblib
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.multioutput import MultiOutputClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report

from sqlalchemy import create_engine


def load_data(database_filepath):
    engine = create_engine('sqlite:///%s'%database_filepath)
    df = pd.read_sql_table('responses', engine)

    X = df.message.values; 
    
    dfCat = df.drop(['id','related','message','original','genre'], axis=1)
    y = dfCat.values
    
    categories = list(dfCat.columns)

    return X,y,categories


def tokenize(text):
    url_regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    detected_urls = re.findall(url_regex, text)
    
    for url in detected_urls:
        text = text.replace(url, "urlplaceholder")
        
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens


def build_model():

    pipeline = Pipeline([
        ('vect', CountVectorizer(tokenizer=tokenize)),
        ('tfidf', TfidfTransformer()),  
        ('clf', MultiOutputClassifier(RandomForestClassifier())),
    ])
    
#     return pipeline
    
    parameters = {
         'vect__max_df': 0.75, 
         'vect__max_features': 10000, 
         'vect__ngram_range': ((1, 1), (1, 2)),
         'vect__max_df': (0.5, 0.75, 1.0),
         'vect__max_features': (None, 5000, 10000),
         'tfidf__use_idf': (True, False),
         'clf__estimator__n_estimators': [200, 500],
         'clf__estimator__max_features': ['auto', 'sqrt', 'log2'],
         'clf__estimator__max_depth' : [4,5,6,7,8],
         'clf__estimator__criterion' :['gini', 'entropy']
        }
    
    model = GridSearchCV(pipeline, param_grid=parameters, verbose=2, n_jobs=-1, cv=2)
    return model


def evaluate_model(model, X_test, Y_test, category_names):
    y_pred = model.predict(X_test)
    accuracy = (y_pred == Y_test).mean()

    print("Accuracy:", accuracy)
    print("\nBest Parameters:", model.best_params_)
    
    for i in range(len(category_names)):
        print("----------------------------------------------------")
        print("Category: {} |".format(category_names[i]))
        print("----------------------------------------------------")
        print(classification_report(Y_test[:,i],y_pred[:,i]))
        

def save_model(model, model_filepath):
    joblib.dump(model, model_filepath)


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()