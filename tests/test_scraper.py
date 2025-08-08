# import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import scraper

def test_fetch_bbc_headlines_returns_list():
    headlines = scraper.fetch_bbc_headlines()
    assert isinstance(headlines, list)
    assert len(headlines) > 0
    assert all(isinstance(h, str) for h in headlines)

def test_headlines_are_unique():
    headlines = scraper.fetch_bbc_headlines()
    assert len(headlines) == len(set(headlines))

def test_limit_headlines():
    headlines = scraper.fetch_bbc_headlines()
    assert len(headlines) <= 10
