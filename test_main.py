from _pytest import monkeypatch
import pytest
from main import calculate_new_amount, user_input


def test_calculate_new_amount():
    assert calculate_new_amount(1.28, [100, "GBP" , "INR"]) == 128
    assert calculate_new_amount(1.17, [200, "EUR" , "USD"]) == 234
    assert calculate_new_amount(0, [300, "USD" , "GBP"]) == "invalid currency"
    assert calculate_new_amount(None, [400, "USD" , "GBP"]) == "invalid currency"
    assert calculate_new_amount(-1, [500, "USD" , "GBP"]) == "invalid currency"

def test_user_input_valid(monkeypatch):
    inputs = iter([100, "USD", "EUR"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    data = user_input()
    assert data == [100, "USD", "EUR"]

def test_user_input_invalid_zero_amount(monkeypatch):
    inputs = iter([0, 1, "GET", "TRY"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    data = user_input()
    assert data == [1, "GET", "TRY"]

def test_user_input_invalid_negative_amount(monkeypatch):
    inputs = iter([-1, 2, "GET", "TRY"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    data = user_input()
    assert data == [2, "GET", "TRY"]

def test_user_input_invalid_string_amount(monkeypatch):
    inputs = iter(["SET",100, "SET", "GET"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    data = user_input()
    assert data == [100, "SET", "GET"]

def test_user_input_invalid_number_initial_currency(monkeypatch):
    inputs = iter([100, 123, "SET", "GET"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    data = user_input()
    assert data == [100, "SET", "GET"]

def test_user_input_invalid_negative_number_initial_currency(monkeypatch):   
    inputs = iter([100, -123, "SET", "GET"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    data = user_input()
    assert data == [100, "SET", "GET"]

def test_user_input_invalid_number_final_currency(monkeypatch):    
    inputs = iter([100, "SET", 321, "GET"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    data = user_input()
    assert data == [100, "SET", "GET"]

def test_user_input_invalid_negative_number_final_currency(monkeypatch):   
    inputs = iter([100, "SET", -321, "GET"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    data = user_input()
    assert data == [100, "SET", "GET"]

    