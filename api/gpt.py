from openai import OpenAI
import io
from fastapi.responses import StreamingResponse
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
For each word in the list of unknown words, create **one natural English sentence** that:
- Clearly shows the meaning of the unknown word through context.
- The sentence must sound natural and be understandable to a learner.
- Do NOT define the word; use it in context.
- Each sentence should be on a new line, prefixed with the word itself like: `word: Sentence`.

Unknown words: {', '.join(unknown_words)}

Output:
One sentence for each unknown word, one per line, formatted as:
word: Sentence
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


def parse_response_to_cards(response_text):
    cards = []
    for line in response_text.strip().split('\n'):
        if ':' in line:
            word, sentence = line.split(':', 1)
            cards.append((word.strip(), sentence.strip()))
    return cards


def write_cards_to_csv(cards):
    csv_buffer = io.StringIO()
    writer = csv.writer(csv_buffer)
    writer.writerow(["Word"])  # заголовок
    for word in cards:
        writer.writerow([word])

    csv_buffer.seek(0)

    return StreamingResponse(
        iter([csv_buffer.getvalue()]),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=random_words.csv"}
    )
