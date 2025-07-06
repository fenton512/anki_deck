from openai import OpenAI
import io
import spacy
from gtts import gTTS
from fastapi.responses import PlainTextResponse
import csv

nlp = spacy.load("en_core_web_sm")

# Создай клиента с токеном
client = OpenAI(
    # замените на свой ключ
    api_key="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"
)


def generate_prompt(unknown_words,known_words,count):
    return f"""
You are a language tutor helping create flashcards for learning English.

Task:
For each word in the list of unknown words, create
 **translation of this word, three natural English sentences and translation of each of them into Russian** that:
- Clearly shows the meaning of the unknown word through context.
- Sentences must sound natural and be understandable to a learner.
- Do NOT define the word; use it in context.
- Try to use less words from the known words list in the sentences.
- Length of each sentence should be exactly {count} words.
- Each word, his translation and sentences with their translations should be on a new line,
 prefixed with the word itself like:
  `word;word_translation;sentence1;sentence1_translation;sentence2;sentence2_translation;sentence3;sentence3_translation`.

Unknown words: {', '.join(unknown_words)}
Known words: {', '.join(known_words)}

Output:
Translation and sentences with their translations for each unknown word, all per line, formatted as:
word;word_translation;sentence1;sentence1_translation;sentence2;sentence2_translation;sentence3;sentence3_translation
""".strip()


def request_sentences(unknown_words,known_words,count):#add arguements
    prompt = generate_prompt(unknown_words,known_words,count)# add arguements

    completion = client.chat.completions.create(
        model="gpt-4o-mini",  # Или "gpt-4o-mini", если хочешь
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return completion.choices[0].message.content

def parse_response_to_dicts(response_text):
    rows = []
    for line in response_text.strip().split('\n'):
        parts = line.split(';')
        if len(parts) == 8:
            rows.append({
                "word": parts[0],
                "word_translation": parts[1],
                "sentence1": parts[2],
                "sentence1_translation": parts[3],
                "sentence2": parts[4],
                "sentence2_translation": parts[5],
                "sentence3": parts[6],
                "sentence3_translation": parts[7],
            })
    return rows



def write_cards_to_csv(response_text):
    csv_in_memory = io.StringIO(newline="")
    fieldnames = ["word","lemma", "word_translation", "sentence1", "sentence1_translation", "sentence2", "sentence2_translation", "sentence3", "sentence3_translation"]
    writer = csv.DictWriter(csv_in_memory, fieldnames=fieldnames)
    writer.writeheader()
    for row in response_text:
        lemma = nlp(row["word"])[0].lemma_
        row_with_lemma = {
            "lemma": lemma,
            **row}
        writer.writerow(row_with_lemma)
    return PlainTextResponse(csv_in_memory.getvalue())