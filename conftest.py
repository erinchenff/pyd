import pytest
import requests

from page.web import Web


# def verify_request():
#     response = requests.get('http://selenium:4444',timeout=0.5)
#     print(response)
# verify_request()

@pytest.fixture
def main_page():
    page = Web.main_page()
    yield page
    Web.quit()


