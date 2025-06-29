import spacy

nlp = spacy.load("en_core_web_sm")


def is_word_in_generated_sentences(word, sentences):
    word_lemma = nlp(word)[0].lemma_
    for sentence in sentences:
        sentence_lemmas = [token.lemma_ for token in nlp(sentence)]
        if word_lemma in sentence_lemmas:
            return True
    return False
