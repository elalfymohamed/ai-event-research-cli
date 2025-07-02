import pytest

from utilities.valid_firecrawl_key_format import is_valid_firecrawl_key_format


def test_valid_key_format():
  assert is_valid_firecrawl_key_format("fc-1234567890abcdef1234567890abcdef")
  assert  is_valid_firecrawl_key_format("fc-1234567890abcdef1234567890abcdefABCD")
  assert  is_valid_firecrawl_key_format("fc-1234567890abcdef_1234567890abcdef-AB")


def test_invalid_key_format():
    assert not  is_valid_firecrawl_key_format("fc-1234")
    assert not  is_valid_firecrawl_key_format("")
    assert not  is_valid_firecrawl_key_format(1234)
    assert not  is_valid_firecrawl_key_format(None)
    assert not  is_valid_firecrawl_key_format("fz-1234567890abcdef1234567890abcdef")
    assert not  is_valid_firecrawl_key_format("fc-1234567890abcdef 1234567890abcdef")
    assert not  is_valid_firecrawl_key_format("fc-1234567890abcdef!@#$%^&*()")


def test_edge_key_format():
    assert  is_valid_firecrawl_key_format("fc-" + "a"*32)
    assert  is_valid_firecrawl_key_format("fc-" + "a"*40)
    assert  is_valid_firecrawl_key_format("fc-" + "a"*100)
    assert not is_valid_firecrawl_key_format("fc-" + "A"*31)
   