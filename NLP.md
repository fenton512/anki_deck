
### Import_1
	text obtained
	1.tokenize it and add info about clickability:create a dictionary where key is a word and value is its clicability
	2.export JSON
### Import_2
	JSON obtained like this:
	`json = {`
	    `"known_words": {word:[context_sent]},` key:word from text, value:list with context sentence
	    `"unknown_words": {},`
	    `"unwanted_words": {},`
	`}`

	JSON send like this:
	`json = {`
	    `"known_words": {word:[context_sent,word_lemmatized]},` key:word from text, value:list with context sentence and lemmatized word
	    `"unknown_words": {},`
	    `"unwanted_words": {},`
	`}`








