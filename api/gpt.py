from openai import OpenAI
import io
from fastapi.responses import PlainTextResponse
import csv

# Создай клиента с токеном
client = OpenAI(
    # замените на свой ключ
    api_key="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"
)


def generate_prompt(unknown_words):
    return f"""
You are a language tutor helping create flashcards for learning English.

Task:
For each word in the list of unknown words, create **three natural English sentences** that:
- Clearly shows the meaning of the unknown word through context.
- Sentences must sound natural and be understandable to a learner.
- Do NOT define the word; use it in context.
- Each group of sentence should be on a new line, prefixed with the word itself like: `word;Sentence1;Sentence2;Sentence3`.

Unknown words: {', '.join(unknown_words)}

Output:
Three sentences for each unknown word, all per line, formatted as:
word;Sentence1;Sentence2;Sentence3
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



def write_cards_to_csv(response_text):
    csv_in_memory = io.StringIO(newline="")
    fieldnames = ["word", "sentence1", "sentence2", "sentence3"]
    writer = csv.DictWriter(csv_in_memory, fieldnames=fieldnames)
    writer.writeheader()
    for row in response_text:
        writer.writerow(row)
    return PlainTextResponse(csv_in_memory.getvalue())
