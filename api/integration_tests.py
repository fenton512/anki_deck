import pytest
from fastapi.testclient import TestClient
from api.fast_api import app

client = TestClient(app)


@pytest.fixture(autouse=True)
def setup_and_teardown():
    yield


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "FastAPI работает!"}


def test_post_and_get_user():
    login = "testuser"
    password = "testpassword"

    response = client.post(f"/user/post/{login}/{password}")
    assert response.status_code == 200
    assert response.json()['status'] == "ok"

    response_get = client.get(f"/user/get?login={login}")
    assert response_get.status_code == 200
    data = response_get.json()
    assert data["login"] == login
    assert "encrypted_password" in data
    assert "id" in data


def test_get_deck():
    deck_id = 1
    response = client.get(f"/deck/get?deck_id={deck_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["deck_id"] == deck_id
    assert "cards" in data
    assert "user_id" in data


def test_post_deck():
    user_id = 1
    cards = [1, 2, 3]
    response = client.post("/deck/post", params={"user_id": user_id, "cards": cards})
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_get_card():
    card_id = 1
    response = client.get(f"/card/get?card_id={card_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["card_id"] == card_id
    assert "word_id" in data
    assert "sentences" in data


def test_post_card():
    word_id = 1
    sentences = ["sentence 1", "sentence 2"]
    response = client.post("/card/post", params={"word_id": word_id, "sentences": sentences})
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_get_by_word():
    word = "example"
    response = client.get(f"/word/get_by_word?word={word}")
    assert response.status_code == 200
    data = response.json()
    assert data["word"] == word
    assert "word_id" in data
    assert "context_sentence" in data
    assert "user_id" in data


def test_get_by_id():
    word_id = 1
    response = client.get(f"/word/get_by_id?word_id={word_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["word_id"] == word_id
    assert "word" in data
    assert "context_sentence" in data
    assert "user_id" in data


def test_post_word():
    response = client.post(
        "/word/post",
        params={
            "word": "testword",
            "translations": "trans1,trans2",
            "context_sentence": "some context",
            "is_important": "true",
            "user_id": 1,
            "mode": "known"
        }
    )
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_get_user_not_found():
    response = client.get("/user/get?login=nonexistent")
    assert (not response.json()['id'])


def test_get_deck_not_found():
    response = client.get("/deck/get?deck_id=99999")
    assert (not response.json()['user_id'])


def test_get_card_not_found():
    response = client.get("/card/get?card_id=99999")
    assert (not response.json()['word_id'])


def test_get_by_word_not_found():
    response = client.get("/word/get_by_word?word=nonexistentword")
    assert (not response.json()['word_id'])


def test_get_by_id_not_found():
    response = client.get("/word/get_by_id?word_id=99999")
    assert (not response.json()['word'])
