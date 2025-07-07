import spacy
from spacy.tokenizer import Tokenizer
from spacy.util import compile_prefix_regex, compile_infix_regex, compile_suffix_regex
import re


def splitting(str_text):
    nlp = spacy.load("en_core_web_sm")#magic model for English language processing
    pattern = re.compile(r"^[a-zA-Z]+([-'][a-zA-Z]+)*$")# Regex pattern to match words

    tokenized = []# List to store all tokens
    clickable = []# List to store tokens that are clickable
    export = {}# Dictionary to store unique tokens and their clickable status


    infixes = nlp.Defaults.infixes

    infixes = [pattern for pattern in infixes if '-' not in pattern]

    prefix_re = compile_prefix_regex(nlp.Defaults.prefixes)
    suffix_re = compile_suffix_regex(nlp.Defaults.suffixes)
    infix_re = compile_infix_regex(infixes)

    nlp.tokenizer = Tokenizer(
        nlp.vocab,
        rules=nlp.Defaults.tokenizer_exceptions,
        prefix_search=prefix_re.search,
        suffix_search=suffix_re.search,
        infix_finditer=infix_re.finditer,
        token_match=None
    )

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

    return export
