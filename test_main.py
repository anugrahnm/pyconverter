from _pytest import monkeypatch
import pytest
from main import CurrencyConverter


def test_calculate_valid():
    converter = CurrencyConverter()
    converter.amount = 100
    converter.rate = 1.25
    converter.calculate()
    assert converter.new_amount == 125


def test_calculate_invalid_zero_rate():
    converter = CurrencyConverter()
    converter.amount = 100
    converter.rate = 0
    converter.calculate()
    assert converter.new_amount == "invalid currency"

def test_calculate_invalid_none_rate():
    converter = CurrencyConverter()
    converter.amount = 100
    converter.rate = None
    converter.calculate()
    assert converter.new_amount == "invalid currency"

def test_calculate_invalid_negative_rate():
    converter = CurrencyConverter()
    converter.amount = 100
    converter.rate = -1
    converter.calculate()
    assert converter.new_amount == "invalid currency"


def test_get_input_valid(monkeypatch):

    converter = CurrencyConverter()
    inputs = iter([100, "GET", "TRY"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    converter.get_input()
    
    assert converter.amount == 100
    assert converter.initial_currency == "GET"
    assert converter.final_currency == "TRY"


def test_get_input_invalid_zero_amount(monkeypatch):

    converter = CurrencyConverter()
    inputs = iter([0, 1, "GET", "TRY"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    converter.get_input()
    
    assert converter.amount == 1
    assert converter.initial_currency == "GET"
    assert converter.final_currency == "TRY"

def test_get_input_invalid_negative_amount(monkeypatch):
    converter = CurrencyConverter()
    inputs = iter([-1, 2, "GET", "TRY"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    converter.get_input()

    assert converter.amount == 2
    assert converter.initial_currency == "GET"
    assert converter.final_currency == "TRY"

def test_get_input_invalid_string_amount(monkeypatch):
    
    converter = CurrencyConverter()
    inputs = iter(["SET",100, "SET", "GET"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    converter.get_input()

    assert converter.amount == 100
    assert converter.initial_currency == "SET"
    assert converter.final_currency == "GET"

def test_get_input_invalid_number_initial_currency(monkeypatch):

    converter = CurrencyConverter()
    inputs = iter([100, 123, "SET", "GET"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    converter.get_input()

    assert converter.amount == 100
    assert converter.initial_currency == "SET"
    assert converter.final_currency == "GET"

def test_get_input_invalid_negative_number_initial_currency(monkeypatch):

    converter = CurrencyConverter()
    inputs = iter([100, -123, "SET", "GET"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    converter.get_input()

    assert converter.amount == 100
    assert converter.initial_currency == "SET"
    assert converter.final_currency == "GET"

def test_get_input_invalid_number_final_currency(monkeypatch):    
   
    converter = CurrencyConverter()
    inputs = iter([100, "SET", 321, "GET"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    converter.get_input()

    assert converter.amount == 100
    assert converter.initial_currency == "SET"
    assert converter.final_currency == "GET"

def test_get_input_invalid_negative_number_final_currency(monkeypatch):   
    converter = CurrencyConverter()
    inputs = iter([100, "SET", -321, "GET"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    converter.get_input()

    assert converter.amount == 100
    assert converter.initial_currency == "SET"
    assert converter.final_currency == "GET"

    