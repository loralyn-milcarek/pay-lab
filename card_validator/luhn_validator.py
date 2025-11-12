from .card_number_cleaner import clean

def validate_card_number(card_number):
  digits = clean(card_number)

  if not digits.isdigit():
    return False
  
  check_digit = int(digits[-1])
  running_sum = 0

  for i, digit in enumerate(reversed(digits[:-1])):
    d = int(digit)
    running_sum += (d * 2 if d < 5 else d * 2 - 9) if i % 2 == 0 else d
  
  return (running_sum + check_digit) % 10 == 0


print(validate_card_number('4242424242424242'))