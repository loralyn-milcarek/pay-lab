import pytest
from ..card_type_validator import identify_card

@pytest.mark.parametrize('card_number, expected_type, prefix_validity, length_validity, number_validity', [
  # 1. Valid cards
  ('4242 4242 4242 4242', 'Visa', True, True, True),
  ('372280864074008', 'American Express', True, True, True),
  ('6011111111111117', 'Discover', True, True, True),
  ('5555555555554444', 'Mastercard', True, True, True),

  # 2. Invalid Luhn Check
  ('4532 9617 3878 9701', 'Visa', True, True, False),
  ('5111111111111110', 'Mastercard', True, True, False), 

  # 3. Invalid Prefix
  ('1234567890123456', None, False, False, False), 

  # 4. Invalid Length
  ('4242', 'Visa', True, False, True),
  ('3412345678901234', 'American Express', True, False, False),

  # 5. Edge Cases / Non-numeric / Empty Input
  ('', None, False, False, False), 
  ('4532a961738789700', 'Visa', True, True, False),
  (None, None, False, False, False), 
  ('abcd', None, False, False, False)
])
def test_identify_card_comprehensive(card_number, expected_type, prefix_validity, length_validity, number_validity):
  result = identify_card(card_number)
  assert result['type'] == expected_type
  assert result['is_valid_prefix'] == prefix_validity
  assert result['is_valid_length'] == length_validity
  assert result['is_valid_number'] == number_validity