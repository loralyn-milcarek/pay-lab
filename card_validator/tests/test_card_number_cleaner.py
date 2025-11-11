from ..card_number_cleaner import clean

def test_clean_removes_dashes_spaces():
  assert clean('4242-4242-4242 4242 ') == '4242424242424242'

def test_clean_removes_non_digit_characters():
  assert clean('a!4&%2/4_2.') == '4242'

def test_clean_returns_string_from_int():
  assert clean(4242) == '4242'

def test_clean_whitespace_or_none():
  assert clean('abc') == ''
  assert clean('    ') == ''
  assert clean('-') == ''
  assert clean(None) == ''