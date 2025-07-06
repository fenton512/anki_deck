from fastapi import FastAPI, Query,Request
from fastapi.responses import JSONResponse
from sqlite3 import connect
from gpt import request_sentences, write_cards_to_csv, parse_response_to_dicts
import os
from fastapi.middleware.cors import CORSMiddleware
from decryptors import *
from pydantic import BaseModel
from typing import List

#fastapi  s s s s

app = FastAPI()
basedir = os.path.abspath(os.path.dirname(__file__))
data_file = os.path.join(basedir, 'anki_deck.db')
con = connect(data_file)
cur = con.cursor()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:8000/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "FastAPI работает!"}

@app.get("/user/get")
async def get_user(login: str):
    ans = {
    'id': cur.execute("SELECT user_id FROM user WHERE login = ?", (login,)).fetchone()[0],
    'login': login,
    'encrypted_password': cur.execute("SELECT encrypted_password FROM user WHERE login = ?",
                                      (login,)).fetchone()[0]
    }
    return ans


@app.post("/user/post/{login}/{encrypted_password}")
async def post_user(login: str, encrypted_password: str):
    cur.execute("INSERT INTO user (login, encrypted_password) VALUES (?, ?)", (login, encrypted_password))
    con.commit()
    return {"status": 'ok'}


@app.get("/deck/get")
async def get_deck(deck_id: int):
    ans = {
        'deck_id': deck_id,
        'cards': decode_blob(cur.execute("SELECT cards FROM decks WHERE deck_id = ?",
                                         (deck_id,)).fetchall()[0]),
        'user_id': cur.execute("SELECT user_id FROM decks WHERE deck_id = ?", (deck_id,)).fetchone()[0]
    }
    return ans


@app.post("/deck/post")
async def post_deck(user_id: int, cards: list[int] = Query()):
    cur.execute("INSERT INTO decks (user_id, cards) VALUES (?, ?)", (user_id, array_to_blob(cards)))
    con.commit()
    return {"status": 'ok'}


@app.get("/card/get")
async def get_card(card_id: int):
    ans = {
        'card_id': card_id,
        'word_id': cur.execute("SELECT word_id FROM cards WHERE card_id = ?", (card_id,)).fetchone()[0],
        'sentences': decode_blob(cur.execute("SELECT sentences FROM cards WHERE card_id = ?",
                                         (card_id,)).fetchall()[0])
    }
    return ans


@app.post("/card/post")
async def post_card(word_id: int,  sentences: list[str] = Query()):
    cur.execute("INSERT INTO cards (word_id, sentences) VALUES (?, ?)", (word_id, array_to_blob(sentences)))
    con.commit()
    return {"status": 'ok'}


@app.get("/word/get_by_word")
async def get_by_word(word: str):
    ans = {
        'word_id': cur.execute("SELECT word_id FROM words WHERE word = ?", (word,)).fetchone()[0],
        'word': word,
        'translations': cur.execute("SELECT translations FROM words WHERE word = ?",
                                    (word,)).fetchone()[0],
        'context_sentence': cur.execute("SELECT context_sentence FROM words WHERE word = ?",
                                        (word,)).fetchone()[0],
        'is_important': bool(cur.execute("SELECT is_important FROM words WHERE word = ?",
                                    (word,)).fetchone()[0]),
        'user_id': cur.execute("SELECT user_id FROM words WHERE word = ?",
                               (word,)).fetchone()[0]
    }
    return ans


@app.get("/word/get_by_id")
async def get_by_id(word_id: int):
    ans = {
        'word_id': word_id,
        'word': cur.execute("SELECT word FROM words WHERE word_id = ?", (word_id,)).fetchone()[0],
        'translations': cur.execute("SELECT translations FROM words WHERE word_id = ?",
                                    (word_id,)).fetchone()[0],
        'context_sentence': cur.execute("SELECT context_sentence FROM words WHERE word_id = ?",
                                        (word_id,)).fetchone()[0],
        'is_important': bool(cur.execute("SELECT is_important FROM words WHERE word_id = ?",
                                    (word_id,)).fetchone()[0]),
        'user_id': cur.execute("SELECT user_id FROM words WHERE word_id = ?",
                               (word_id,)).fetchone()[0]
    }
    return ans


@app.post("/word/post")
async def post_word(word: str, translations: str, context_sentence: str, is_important: bool, user_id: int, mode: str):
    cur.execute("INSERT INTO words (word, translations, context_sentence, is_important, user_id)"
                " VALUES (?, ?, ?, ?, ?)", (word, translations, context_sentence, int(is_important), user_id))
    word_id = cur.execute("SELECT word_id FROM words").fetchall()[-1][0]
    if mode == "known":
        cur.execute("INSERT INTO known_words (word_id) VALUES (?)", (word_id,))
    elif mode == "unknown":
        cur.execute("INSERT INTO unknown_words (word_id) VALUES (?)", (word_id,))
    else:
        cur.execute("INSERT INTO unwanted_words (word_id) VALUES (?)", (word_id,))
    con.commit()
    return {"status": 'ok'}

class WordListRequest(BaseModel):
    unknown_words: List[str]
    known_words:List[str]
    count: int

@app.post("/wordlist/post")
async def post_text(payload: WordListRequest):
    unknown_words = payload.unknown_words
    known_words = payload.known_words
    count = payload.count
    response_text = request_sentences(unknown_words,known_words,count)
    rows = parse_response_to_dicts(response_text)
    return write_cards_to_csv(rows)

@app.options("/wordlist/post")
async def options_wordlist_post(request: Request):
    return JSONResponse(status_code=200)

