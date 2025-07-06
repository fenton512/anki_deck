import spacy
import re

#fastapi



def splitting(str_text):
    nlp = spacy.load("en_core_web_sm")#magic model for English language processing
    pattern = re.compile(r"^[a-zA-Z]+([-'][a-zA-Z]+)*$")# Regex pattern to match words

    tokenized = []# List to store all tokens
    clickable = []# List to store tokens that are clickable
    export = {}# Dictionary to store unique tokens and their clickable status

    doc = nlp(str_text)

    for token in doc:
        tokenized.append(token.text)
        # Skip punctuation, stopwords, and non-matching tokens
        if token.is_punct or token.is_stop or not pattern.match(token.text):
            continue
        clickable.append(token.text)
    # Create a dictionary to store unique tokens and their clickable status
    for token in tokenized:
        if token not in export:
            if token in clickable:
                export[token] = True
            else:
                export[token] = False

    """so export is a dictionary where:
    - keys are unique tokens from the text
    - values are booleans indicating if the token is clickable (not punctuation, not a stopword, and matches the pattern)
    The dictionary is built from the original text, ensuring that each token is processed only once."""