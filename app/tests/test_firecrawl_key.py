import pytest
from utilities.valid_firecrawl_key_format import is_valid_firecrawl_key_format


@pytest.mark.parametrize("key", [
    "fc-1234567890abcdef1234567890abcdef",
    "fc-1234567890abcdef1234567890abcdefABCD",
    "fc-1234567890abcdef_1234567890abcdef-AB"
])
def test_valid_key_format(key):
    assert is_valid_firecrawl_key_format(key)


@pytest.mark.parametrize("key", [
    "fc-1234",
    "",
    1234,
    None,
    "fz-1234567890abcdef1234567890abcdef",
    "fc-1234567890abcdef 1234567890abcdef",
    "fc-1234567890abcdef!@#$%^&*()"
])
def test_invalid_key_format(key):
    assert not is_valid_firecrawl_key_format(key)


@pytest.mark.parametrize("key, expected", [
    ("fc-" + "a"*32, True),
    ("fc-" + "a"*40, True),
    ("fc-" + "a"*100, True),
    ("fc-" + "A"*31, False)
])
def test_edge_key_format(key, expected):
    assert is_valid_firecrawl_key_format(key) == expected
