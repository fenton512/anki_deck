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

def parse_response_to_dicts(response_text):
    rows = []
    for line in response_text.strip().split('\n'):
        parts = line.split(';')
        if len(parts) == 4:
            rows.append({
                "word": parts[0],
                "sentence1": parts[1],
                "sentence2": parts[2],
                "sentence3": parts[3],
            })
    return rows



def write_cards_to_csv(response_text):
    csv_in_memory = io.StringIO(newline="")
    fieldnames = ["word", "sentence1", "sentence2", "sentence3"]
    writer = csv.DictWriter(csv_in_memory, fieldnames=fieldnames)
    writer.writeheader()
    for row in response_text:
        writer.writerow(row)
    return PlainTextResponse(csv_in_memory.getvalue())
