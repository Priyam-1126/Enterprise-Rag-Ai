import requests


def test_upload():

    with open(
        "sample.pdf",
        "rb",
    ) as file:

        response = requests.post(
            "http://127.0.0.1:8000/upload/",
            files={
                "file": file,
            },
        )

    print(response.json())


if __name__ == "__main__":
    test_upload()