from ..token_generator import TokenVault

def test_tokenize_returns_consistent_token():
  vault = TokenVault()
  card_number = '4242'
  token = vault.tokenize(card_number)
  token_duplicate = vault.tokenize(card_number)
  assert token == token_duplicate

def test_tokenize_returns_unique_token():
  vault = TokenVault()
  token = vault.tokenize('4242')
  token_unique = vault.tokenize('4242424242424242')
  assert token != token_unique

def test_detokenize_returns_same_number():
  vault = TokenVault()
  token = vault.tokenize('4242')
  card_number = vault.detokenize(token)
  card_number_duplicate = vault.detokenize(token)
  assert card_number == card_number_duplicate

def test_detokenize_returns_unique_token():
  vault = TokenVault()
  token = vault.tokenize('4242')
  token_unique = vault.tokenize('4242424242424242')
  assert vault.detokenize(token) != vault.detokenize(token_unique)

def test_detokenize_returns_none():
  vault = TokenVault()
  assert vault.detokenize('tok_000') == None

def test_is_valid_token_validates_token():
  vault = TokenVault()
  token = vault.tokenize('4242')
  assert vault.is_valid_token(token) == True
  assert vault.is_valid_token('tok_000') == False