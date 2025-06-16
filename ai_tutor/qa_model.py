from transformers import pipeline

def load_qa_model():
    return pipeline("question-answering", model="distilbert-base-cased-distilled-squad")