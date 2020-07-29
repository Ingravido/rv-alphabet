def check_word(word_to_make, available_alphabet):
    if not word_to_make:
        return False

    letters_repository = __make_letters_repository(available_alphabet)

    letter_not_available = any(__is_letter_unavailable(letter, letters_repository) for letter in word_to_make)

    return letter_not_available is False


def __make_letters_repository(available_alphabet):
    letters_repository = {}
    for letter in available_alphabet:
        letters_repository[letter] = (letters_repository[letter] + 1) if letter in letters_repository else 1

    return letters_repository


def __is_letter_unavailable(letter, letters_repository):
    if letter in letters_repository:
        if letters_repository[letter] == 0:
            return True
        else:
            letters_repository[letter] -= 1
            return False
    else:
        return True
