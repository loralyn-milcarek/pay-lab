# Dictionary storage of Bank Identification Numbers (BIN) and card number lengths

CARD_TYPES = {
  'American Express': {
    'ranges': [34, 37],
    'lengths': [15]
  },
  'Discover': {
    'ranges': [6011, 644, 645, 646, 647, 648, 649, 65],
    'lengths': [16, 17, 18, 19]
  },
  'Mastercard': {
    'ranges': [51, 52, 53, 54, 55],
    'lengths': [16]
  },
  'Visa': {
    'ranges': [4],
    'lengths': [13, 16, 19]
  }
}

def create_lookup_table(card_types):
  """
  Create a prefix-based lookup table from card type definitions.
  
  Args:
    card_types: Dict mapping card names to their BIN ranges and valid lengths
    
  Returns:
    Dict mapping string prefixes to card metadata (name and lengths set)
  """
  lookup_table = {}

  for name, details in card_types.items():
    lengths = set(details['lengths'])
    for prefix in details['ranges']:
      lookup_table[str(prefix)] = {
        'name': name,
        'lengths': lengths
      }

  return lookup_table

CARD_LOOKUP_BY_PREFIX = create_lookup_table(CARD_TYPES)
