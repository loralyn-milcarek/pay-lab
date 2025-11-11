import re

def clean(card_number): 
  """
    Removes all non-digit characters from the card number string.
  """
  return re.sub(r'\D', '', card_number)