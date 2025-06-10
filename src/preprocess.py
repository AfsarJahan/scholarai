import pandas as pd
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    """Remove stopwords and punctuation using spaCy"""
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return " ".join(tokens)

def preprocess_dataframe(df):
    """Preprocess title and abstract columns"""
    df["clean_title"] = df["title"].fillna("").apply(clean_text)
    df["clean_abstract"] = df["abstract"].fillna("").apply(clean_text)
    return df

def extract_tfidf_features(text_series, max_features=500):
    """Convert text to TF-IDF vectors"""
    tfidf = TfidfVectorizer(max_features=max_features)
    tfidf_matrix = tfidf.fit_transform(text_series)
    return tfidf_matrix, tfidf
