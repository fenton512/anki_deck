import spacy

nlp = spacy.load("en_core_web_sm")  # Load the English model

json_data = {
    "known_words": {"were": ["context_sentence"]},
    "unknown_words": {},
    "unwanted_words": {},
}

for word in json_data["known_words"]:
    doc = nlp(word)  # Process the string with spaCy or treat it as magic
    lemma = doc[0].lemma_  # Get the lemma of the first token
    json_data["known_words"][word].append(lemma)

for word in json_data["unknown_words"]:
    doc = nlp(word)  
    lemma = doc[0].lemma_  
    json_data["unknown_words"][word] = lemma

for word in json_data["unwanted_words"]:
    doc = nlp(word)  
    lemma = doc[0].lemma_  
    json_data["unwanted_words"][word] = lemma

"""json_data is updated to include the lemmas of the words in each category"""