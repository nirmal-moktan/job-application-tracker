import pytest
from tracker import validate_status, validate_text, validate_date

@pytest.mark.parametrize("status, expected", [
    ("interview", "Interview"),
    ("applied", "Applied"),
    ("rejected", "Rejected"),
    ("OFFER", "Offer"),
    ("accepted", "Accepted"),
    ("Withdrawn", "Withdrawn"),
    ("no response", "No Response")
])
def test_validate_status(status, expected):
    assert validate_status(status) == expected
def test_invalid_status():
    with pytest.raises(ValueError):
        validate_status("Banana")

def test_validate_text():
    assert validate_text("   093q8459087   ") is None
def test_invalid_text():
    with pytest.raises(ValueError):
        validate_text(" ")

def test_validate_date():
    assert validate_date("2026-10-16") is None

@pytest.mark.parametrize("date", 
    ["1/12/2026", "2026-02-31"
])
def test_invalid_date(date):
    with pytest.raises(ValueError):
        validate_date(date)