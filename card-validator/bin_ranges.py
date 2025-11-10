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