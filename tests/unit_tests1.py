import unittest
from unittest.mock import patch
from Import_2 import lemmatization
from Import_1 import splitting
from Appearance import is_word_in_generated_sentences


class TestSplittingFunction(unittest.TestCase):

    def test_basic_sentence(self):
        text = "Hello, world! It's a beautiful day."
        result = splitting(text)

        self.assertIn("Hello", result)
        self.assertIn("world", result)
        self.assertIn("It's", result)
        self.assertIn("a", result)
        self.assertIn("beautiful", result)
        self.assertNotIn(",", result)
        self.assertNotIn("!", result)
        self.assertNotIn(".", result)

    def test_stopwords_and_punctuation(self):
        text = "The quick brown fox jumps over the lazy dog."
        result = splitting(text)
        self.assertNotIn("The", result)
        self.assertNotIn("over", result)
        self.assertNotIn("the", result)
        self.assertNotIn(".", result)
        self.assertIn("quick", result)
        self.assertIn("brown", result)
        self.assertIn("fox", result)
        self.assertIn("jumps", result)
        self.assertIn("lazy", result)
        self.assertIn("dog", result)

    def test_word_with_hyphen_and_apostrophe(self):
        text = "It's a well-known fact that e-mail is common."
        result = splitting(text)
        self.assertIn("It's", result)
        self.assertIn("well-known", result)
        self.assertIn("e-mail", result)

    def test_non_matching_tokens_excluded(self):
        text = "1234 !@#$%"
        result = splitting(text)
        self.assertEqual(result, {})

    def test_empty_string(self):
        result = splitting("")
        self.assertEqual(result, {})


class TestLemmatization(unittest.TestCase):

    @patch("spacy.load")
    def test_lemmatization_basic(self, mock_load):
        class MockToken:
            def __init__(self, lemma):
                self.lemma_ = lemma

        class MockDoc:
            def __init__(self, tokens):
                self.tokens = tokens

            def __getitem__(self, idx):
                return self.tokens[idx]

            def __len__(self):
                return len(self.tokens)

            def __iter__(self):
                return iter(self.tokens)

        class MockNLP:
            def __call__(self, text):
                if text == "running":
                    token = MockToken("run")
                elif text == "children":
                    token = MockToken("child")
                elif text == "mice":
                    token = MockToken("mouse")
                else:
                    token = MockToken("unknown")
                self.tokens = [token]
                return self

        mock_load.return_value = MockNLP()

        json_data = {
            "known_words": {
                "running": [],
            },
            "unknown_words": {
                "children": [],
            },
            "unwanted_words": {
                "mice": [],
            }
        }
        result = lemmatization(json_data)

        self.assertIn("running", result["known_words"])
        self.assertIn("child", result["known_words"]["running"])

        self.assertEqual(result["unknown_words"]["children"], "child")
        self.assertEqual(result["unwanted_words"]["mice"], "mouse")

    @patch("spacy.load")
    def test_multiple_words(self, mock_load):
        class MockToken:
            def __init__(self, lemma):
                self.lemma_ = lemma

        class MockDoc:
            def __init__(self, tokens):
                self.tokens = tokens

            def __getitem__(self, idx):
                return self.tokens[idx]

            def __len__(self):
                return len(self.tokens)

            def __iter__(self):
                return iter(self.tokens)

        class MockNLP:
            def __call__(self, text):
                lemmas_map = {
                    "cats": "cat",
                    "dogs": "dog",
                    "mice": "mouse"
                }
                token = MockToken(lemmas_map.get(text, "unknown"))
                self.tokens = [token]
                return self

        mock_load.return_value = MockNLP()

        json_data = {
            "known_words": {"cats": []},
            "unknown_words": {"dogs": []},
            "unwanted_words": {"mice": []}
        }

        result = lemmatization(json_data)

        self.assertEqual(result["known_words"]["cats"], "cat")
        self.assertEqual(result["unknown_words"]["dogs"], "dog")
        self.assertEqual(result["unwanted_words"]["mice"], "mouse")


class TestAppearance(unittest.TestCase):
    def test_word_found_exact_match(self):
        word = "run"
        sentences = ["He runs every morning."]
        self.assertTrue(is_word_in_generated_sentences(word, sentences))

    def test_word_found_case_insensitive(self):
        word = "Apple"
        sentences = ["I bought an apple yesterday."]
        self.assertTrue(is_word_in_generated_sentences(word, sentences))

    def test_word_not_found(self):
        word = "swim"
        sentences = ["He runs and jumps."]
        self.assertFalse(is_word_in_generated_sentences(word, sentences))

    def test_multiple_sentences_some_match(self):
        word = "read"
        sentences = ["They will run.", "She reads a book.", "Walking is healthy."]
        self.assertTrue(is_word_in_generated_sentences(word, sentences))

    def test_empty_sentences(self):
        word = "apple"
        sentences = []
        self.assertFalse(is_word_in_generated_sentences(word, sentences))


if __name__ == "__main__":
    unittest.main()
