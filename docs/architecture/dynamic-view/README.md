A user submits a text to generate an Anki deck. The frontend sends the text to the FastAPI backend, which processes the text, interacts with the NLP module to extract words, queries the database for known/unknown words, and finally returns a downloadable deck.
In our production environment, this scenario takes approximately X seconds to execute end-to-end 
![Uploading image.png…]()
