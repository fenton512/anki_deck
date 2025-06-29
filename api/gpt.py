from openai import OpenAI
import io
from fastapi.responses import PlainTextResponse
import csv
from dotenv import load_dotenv
import os

# Создай клиента с токеном
client = OpenAI(
    # замените на свой ключ
    api_key="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"
)


def generate_prompt(unknown_words):
    return f"""
You are a language tutor helping create flashcards for learning English.

Task:
For each word in the list of unknown words, create
 **translation of this word, three natural English sentences and translation of each of them into Russian** that:
- Clearly shows the meaning of the unknown word through context.
- Sentences must sound natural and be understandable to a learner.
- Do NOT define the word; use it in context.
- Each word, his translation and sentences with their translations should be on a new line,
 prefixed with the word itself like:
  `word;word_translation;sentence1;sentence1_translation;sentence2;sentence2_translation;sentence3;sentence3_translation`.

Unknown words: {', '.join(unknown_words)}

Output:
Translation and sentences with their translations for each unknown word, all per line, formatted as:
word;word_translation;sentence1;sentence1_translation;sentence2;sentence2_translation;sentence3;sentence3_translation
""".strip()


def request_sentences(unknown_words):
    prompt = generate_prompt(unknown_words)

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
    fieldnames = ["word", "word_translation", "sentence1", "sentence1_translation", "sentence2", "sentence2_translation", "sentence3", "sentence3_translation"]
    writer = csv.DictWriter(csv_in_memory, fieldnames=fieldnames)
    writer.writeheader()
    for row in response_text:
        writer.writerow(row)
    return PlainTextResponse(csv_in_memory.getvalue())