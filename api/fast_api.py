import openai
from fastapi import FastAPI, Query,Request
from fastapi.responses import JSONResponse
from sqlite3 import connect
from gpt import request_sentences, write_cards_to_csv, parse_response_to_dicts
import os
from fastapi.middleware.cors import CORSMiddleware
from decryptors import *
from pydantic import BaseModel
from time import sleep

app = FastAPI()
basedir = os.path.abspath(os.path.dirname(__file__))
data_file = os.path.join(basedir, 'anki_deck.db')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


# test comment
@app.get("/")
def root():
    return {"message": "FastAPI работает!"}


@app.get("/user/get")
async def get_user(login: str):
    con = connect(data_file)
    cur = con.cursor()
    ans = {
        'id': cur.execute("SELECT user_id FROM user WHERE login = ?", (login,)).fetchone(),
        'login': login,
        'encrypted_password': cur.execute("SELECT encrypted_password FROM user WHERE login = ?",
                                          (login,)).fetchone()
    }
    con.close()
    if ans['id']:
        ans['id'] = ans['id'][0]
    if ans['encrypted_password']:
        ans['encrypted_password'] = ans['encrypted_password'][0]
    return ans


@app.post("/user/post/{login}/{encrypted_password}")
async def post_user(login: str, encrypted_password: str):
    con = connect(data_file)
    cur = con.cursor()
    ids = cur.execute("SELECT user_id FROM user WHERE login = ?", (login,)).fetchone(),
    if ids:
        return {"status": 'ok', "text": f'Login "{login}" already exists.'}
    cur.execute("INSERT INTO user (login, encrypted_password) VALUES (?, ?)", (login, encrypted_password))
    con.commit()
    con.close()
    return {"status": 'ok'}


@app.get("/deck/get")
async def get_deck(deck_id: int):
    con = connect(data_file)
    cur = con.cursor()
    ans = {
        'deck_id': deck_id,
        'cards': decode_blob(cur.execute("SELECT cards FROM decks WHERE deck_id = ?",
                                         (deck_id,)).fetchall()),
        'user_id': cur.execute("SELECT user_id FROM decks WHERE deck_id = ?", (deck_id,)).fetchone()
    }
    con.close()
    if ans['cards']:
        ans['cards'] = ans['cards'][0]
    if ans['user_id']:
        ans['user_id'] = ans['user_id'][0]
    return ans


@app.post("/deck/post")
async def post_deck(user_id: int, cards: list[int] = Query()):
    con = connect(data_file)
    cur = con.cursor()
    cur.execute("INSERT INTO decks (user_id, cards) VALUES (?, ?)", (user_id, array_to_blob(cards)))
    con.commit()
    con.close()
    return {"status": 'ok'}


@app.get("/card/get")
async def get_card(card_id: int):
    con = connect(data_file)
    cur = con.cursor()
    ans = {
        'card_id': card_id,
        'word_id': cur.execute("SELECT word_id FROM cards WHERE card_id = ?", (card_id,)).fetchone(),
        'sentences': decode_blob(cur.execute("SELECT sentences FROM cards WHERE card_id = ?",
                                             (card_id,)).fetchall())
    }
    con.close()
    if ans['sentences']:
        ans['sentences'] = ans['sentences'][0]
    if ans['word_id']:
        ans['word_id'] = ans['word_id'][0]
    return ans


@app.post("/card/post")
async def post_card(word_id: int, sentences: list[str] = Query()):
    con = connect(data_file)
    cur = con.cursor()
    cur.execute("INSERT INTO cards (word_id, sentences) VALUES (?, ?)", (word_id,
                                                                         array_to_blob(sentences)))
    con.commit()
    con.close()
    return {"status": 'ok'}


@app.get("/word/get_by_word")
async def get_by_word(word: str):
    con = connect(data_file)
    cur = con.cursor()
    ans = {
        'word_id': cur.execute("SELECT word_id FROM words WHERE word = ?", (word,)).fetchone(),
        'word': word,
        'context_sentence': cur.execute("SELECT context_sentence FROM words WHERE word = ?",
                                        (word,)).fetchone(),
        'user_id': cur.execute("SELECT user_id FROM words WHERE word = ?",
                               (word,)).fetchone()
    }
    con.close()
    if ans['word_id']:
        ans['word_id'] = ans['word_id'][0]
    if ans['context_sentence']:
        ans['context_sentence'] = ans['context_sentence'][0]
    if ans['user_id']:
        ans['user_id'] = ans['user_id'][0]
    return ans


@app.get("/word/get_by_id")
async def get_by_id(word_id: int):
    con = connect(data_file)
    cur = con.cursor()
    ans = {
        'word_id': word_id,
        'word': cur.execute("SELECT word FROM words WHERE word_id = ?", (word_id,)).fetchone(),
        'context_sentence': cur.execute("SELECT context_sentence FROM words WHERE word_id = ?",
                                        (word_id,)).fetchone(),
        'user_id': cur.execute("SELECT user_id FROM words WHERE word_id = ?",
                               (word_id,)).fetchone()
    }
    con.close()
    if ans['word']:
        ans['word'] = ans['word'][0]
    if ans['context_sentence']:
        ans['context_sentence'] = ans['context_sentence'][0]
    if ans['user_id']:
        ans['user_id'] = ans['user_id'][0]
    return ans


@app.post("/word/post")
async def post_word(word: str, context_sentence: str, user_id: int, mode: str):
    con = connect(data_file)
    cur = con.cursor()
    cur.execute("INSERT INTO words (word, context_sentence, user_id)"
                " VALUES (?, ?, ?)", (word, context_sentence, user_id))
    word_id = cur.execute("SELECT word_id FROM words").fetchall()[-1][0]
    if mode == "known":
        cur.execute("INSERT INTO known_words (word_id) VALUES (?)", (word_id,))
    elif mode == "unknown":
        cur.execute("INSERT INTO unknown_words (word_id) VALUES (?)", (word_id,))
    else:
        cur.execute("INSERT INTO unwanted_words (word_id) VALUES (?)", (word_id,))
    con.commit()
    con.close()
    return {"status": 'ok'}


@app.get("/wordlist/get")
async def get_wordlist():
    con = connect(data_file)
    cur = con.cursor()
    ids = cur.execute("SELECT word_id FROM known_words").fetchall()
    words = []
    for word_id in ids:
        word = cur.execute("SELECT word FROM words WHERE word_id = ?", (word_id[0],)).fetchall()
        if word:
            words.append(word[0])
    con.close()
    return {"words": words}


class WordListRequest(BaseModel):
    unknown_words: list[str]
    known_words: list[str]
    count: int


@app.post("/wordlist/post", response_model=WordListRequest)
async def post_text(payload: WordListRequest):
    unknown_words = payload.unknown_words
    known_words = payload.known_words
    count = payload.count
    while True:
        try:
            response_text = request_sentences(unknown_words, known_words, count)
            return write_cards_to_csv(response_text)
        except openai.APIStatusError as e:
            sleep(60)


@app.options("/wordlist/post")
async def options_wordlist_post(request: Request):
    return JSONResponse(status_code=200)