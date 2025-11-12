import pytest
from ..luhn_validator import validate_card_number

@pytest.mark.parametrize('card_number', [
  '17893729974',
  '4242424242424242',
  '178 937 299 74',
  '4242-4242-4242-4242'
])
def test_luhn_validator_returns_true(card_number):
  assert validate_card_number(card_number) == True

@pytest.mark.parametrize('card_number', [
  '17893711114',
  '178937a11114',
  'abc',
  4,
  '',
  None
])
def test_luhn_validator_returns_false(card_number):
  assert validate_card_number(card_number) == False