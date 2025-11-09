def get_last_digit(num):
  return num % 10

def drop_last_digit(num):
  return num // 10

def double_digit(digit):
  doubled = digit * 2
  return doubled if doubled < 10 else doubled - 9

def validate_check_digit(test_number):
  check_digit = get_last_digit(test_number)
  test_number = drop_last_digit(test_number)

  running_sum = 0
  should_double = True

  while test_number > 0:
    last_digit = get_last_digit(test_number)
    
    running_sum += double_digit(last_digit) if should_double else last_digit

    test_number = drop_last_digit(test_number)
    should_double = not should_double
  
  return (running_sum + check_digit) % 10 == 0

print(validate_check_digit(17893729974)) # true
print(validate_check_digit(17893711114)) # false
