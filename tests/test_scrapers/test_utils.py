from app.scrapers._utils import nutrion_facts_to_int, pretiffy_strings_list, time_details_in_minutes
import pytest
from ..utils import SomeElement

def test_nutrion_facts_to_int():
    assert nutrion_facts_to_int("11g") == 11
    assert nutrion_facts_to_int("13") == 13

def test_prettify_strings_list():
    raw_strings_list = [SomeElement(text="Do this, shis this \n , this and this    "), SomeElement(text="AAAnd this \nhello     ")]
    pretiffied_strings_list = ["Do this, shis this  , this and this", "AAAnd this hello"]
    assert pretiffy_strings_list(raw_strings_list) == pretiffied_strings_list

def test_time_details_in_minutes():
    assert time_details_in_minutes(["1 hr 20 mins", "2 hr"]) == [80, 120]
    assert time_details_in_minutes(["40 mins", "1 hr"]) == [40, 60]