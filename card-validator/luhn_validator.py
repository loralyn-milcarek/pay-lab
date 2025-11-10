def validate_card_number(card_number):
  digits = card_number.replace(' ', '').replace('-', '')

  if not digits.isdigit():
    return False
  
  check_digit = int(digits[-1])
  running_sum = 0

  for i, digit in enumerate(reversed(digits[:-1])):
    d = int(digit)
    running_sum += (d * 2 if d < 5 else d * 2 - 9) if i % 2 == 0 else d
  
  return (running_sum + check_digit) % 10 == 0

# print(validate_card_number('17893729974')) # true
# print(validate_card_number('17893711114')) # false
