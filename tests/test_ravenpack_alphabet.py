from ravenpack_alphabet import alphabet
import pytest

scenarios = [
    ('ana', ['a', 'a', 'n'], True),
    ('ana', ['a', 'a', 'a'], False),
    ('javier', ['a', 'r', 'e', 'i', 'v', 'j'], True),
    (' ', ['a', 'r', 'e', 'i', 'v', 'j', ' '], True),
    (' ', [], False),
    ('', ['x'], False),
]


@pytest.mark.parametrize("word_to_make,available_alphabet,expected_result", scenarios)
def test_check_word(word_to_make, available_alphabet, expected_result):
    result = alphabet.check_word(word_to_make, available_alphabet)

    assert result is expected_result
