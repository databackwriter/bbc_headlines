import sys
import os
from unittest.mock import patch, Mock

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import scraper

# Load the saved BBC HTML once
TEST_HTML_PATH = os.path.join(os.path.dirname(__file__), "bbc_home.html")
with open(TEST_HTML_PATH, "r", encoding="utf-8") as f:
    BBC_HTML = f.read()

# Patch requests.get for all tests below
@patch("app.scraper.requests.get")
def test_fetch_bbc_headlines_returns_list(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = BBC_HTML
    mock_get.return_value = mock_response

    headlines = scraper.fetch_bbc_headlines()
    assert isinstance(headlines, list)
    assert len(headlines) > 0
    assert all(isinstance(h, str) for h in headlines)

@patch("app.scraper.requests.get")
def test_headlines_are_unique(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = BBC_HTML
    mock_get.return_value = mock_response

    headlines = scraper.fetch_bbc_headlines()
    assert len(headlines) == len(set(headlines))

@patch("app.scraper.requests.get")
def test_limit_headlines(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = BBC_HTML
    mock_get.return_value = mock_response

    headlines = scraper.fetch_bbc_headlines()
    assert len(headlines) <= 10
