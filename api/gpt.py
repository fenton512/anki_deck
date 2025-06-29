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


def generate_prompt(unknown_words, dont_want_learn):
    return f"""
You are a language tutor helping create flashcards for learning English.

Task:
For each word in the list of unknown words, create
 **translation of this word, three natural English sentences and translation of each of them into Russian** that:
- Clearly shows the meaning of the unknown word through context.
- Sentences must sound natural and be understandable to a learner.
- Do NOT define the word; use it in context.
- Try to avoid words from list of don't want learn words.
- Each word, his translation and sentences with their translations should be on a new line,
 prefixed with the word itself like:
  `word;word_translation;sentence1;sentence1_translation;sentence2;sentence2_translation;sentence3;sentence3_translation`.

Unknown words: {', '.join(unknown_words)}
Don't want words: {', '.join(dont_want_learn)}

Output:
Translation and sentences with their translations for each unknown word, all per line, formatted as:
word;word_translation;sentence1;sentence1_translation;sentence2;sentence2_translation;sentence3;sentence3_translation
""".strip()


def request_sentences(unknown_words, dont_want_learn):
    prompt = generate_prompt(unknown_words, dont_want_learn)

    completion = client.chat.completions.create(
        model="gpt-4o-mini",  # Или "gpt-4o-mini", если хочешь
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return completion.choices[0].message.content


def write_cards_to_csv(response_text):
    csv_in_memory = io.StringIO(newline="")
    fieldnames = ["word", "word_translation", "sentence1", "sentence1_translation", "sentence2",
                  "sentence2_translation", "sentence3", 'sentence3_translation']
    writer = csv.DictWriter(csv_in_memory, fieldnames=fieldnames)
    writer.writeheader()
    for row in response_text:
        writer.writerow(row)
    return PlainTextResponse(csv_in_memory.getvalue())