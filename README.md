# PyConverter

A CLI currency converter built to practise Python fundamentals — OOP, error handling, API integration, and testing.

## What it does

- Takes an amount and two currency codes as input
- Fetches the live exchange rate from the Frankfurter API
- Returns the converted amount with the exchange rate used
- Validates all user input with clear error messages

## Usage Example

```bash
uv run main.py
```

```
Amount to convert: 100
Initial Currency to convert from?: gbp
Final Currency to convert to?: eur
100 GBP is 115.65 EUR with the exchange rate of 1.1565.
```

## Running tests

```bash
uv run pytest test_main.py
```

## Built with

- Python
- Frankfurter API (no API key required)
- pytest
