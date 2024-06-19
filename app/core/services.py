import requests

class ServiceException(Exception):
    pass


def call_external_api(url: str, text: str) -> list:
    """
    call_exernal_api(url="https://friendlybytes.net/api/blog/category/")
    
    """
    if not text:
        raise ServiceException("Der text darf nicht leer sein")

    url = f"{url}?text={text}"

    try:
        response = requests.get(url)
        data = response.json()
    except Exception as e:
        raise ServiceException(str(e))

    return data


if __name__ == "__main__":
    response = call_external_api("https://friendlybytes.net/api/blog/category/", 3)
    print(response.text)

    response = call_external_api("https://friendlybytes.net/api/blog/category/", "hallo welt ö")
    print(response.text)