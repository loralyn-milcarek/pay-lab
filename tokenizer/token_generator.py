import uuid

class TokenVault:
  """
  Simple in-memory token vault for PCI compliance simulation.
  The vault would be a separate, secured database in a production scenario.
  """

  def __init__(self):
    self._vault = {}  
    self._reverse_lookup = {}

  def tokenize(self, card_number: str) -> str:
    """
    Replace real card number with a secure token.
    Returns: tok_xxxxxxxxxxxxxxxx (token string)
    """
    if card_number in self._reverse_lookup:
      return self._reverse_lookup[card_number]

    token = f"tok_{uuid.uuid4()}"
    self._vault[token] = card_number
    self._reverse_lookup[card_number] = token
    
    return token

  def detokenize(self, token: str) -> str | None:
    """
    Retrieve original card number from token.
    Returns: Original PAN or None if token is invalid
    """
    return self._vault[token] if self.is_valid_token(token) else None

  def is_valid_token(self, token: str) -> bool:
    """
    Check if token exists in vault
    """
    return token in self._vault
