import requests


def test_chat():

    response = requests.post(
        "http://127.0.0.1:8000/chat/",
        json={
            "question": "What is AI?"
        },
    )

    print(response.json())


if __name__ == "__main__":
    test_chat()