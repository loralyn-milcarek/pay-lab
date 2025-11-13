import pytest
from ..bin_ranges import CARD_LOOKUP_BY_PREFIX as lookup

@pytest.mark.parametrize('prefix', [
  '34', '6011', '55', '4', '649'
])
def test_card_lookup_includes_card_types(prefix):
  assert prefix in lookup

def test_card_lookup_preserves_all_prefixes():
  assert len(lookup) == 16

def test_card_lookup_has_name_and_length():
  visa = lookup['4']
  assert visa['name'] == 'Visa'
  assert visa['lengths'] == {13, 16, 19}