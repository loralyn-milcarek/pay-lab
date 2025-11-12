from .bin_ranges import CARD_LOOKUP_BY_PREFIX
from .luhn_validator import validate_card_number
from .card_number_cleaner import clean

def identify_card(card_number):
  """
  Analyzes a credit card number to determine its type and validity.
  
  Performs three core validations: prefix match against BINs, length for BIN type,
  and the Luhn algorithm check.

  :param card_number: The credit card number string (may include separators).
  :type card_number: str
  
  :returns: A dictionary with the card 'type' (str or None) and three boolean 
            validity flags: 'is_valid_prefix', 'is_valid_length', and 'is_valid_number'.
  :rtype: dict
  """
  card_number = clean(card_number)

  result = {
    'type': None,
    'is_valid_prefix': False,
    'is_valid_length': False,
    'is_valid_number': False
  }

  if not card_number.isdigit():
    return result
  
  for prefix_length in range(4, 0, -1):
    prefix = card_number[:prefix_length]
    if prefix in CARD_LOOKUP_BY_PREFIX:
      card_info = CARD_LOOKUP_BY_PREFIX[prefix]
      result['type'] = card_info['name']
      result['is_valid_prefix'] = True
      result['is_valid_length'] = len(card_number) in card_info['lengths']
      break

  result['is_valid_number'] = validate_card_number(card_number)

  return result
