import enchant,sys

# requires PyEnchant library

# to be able to support Python 2 & 3
if sys.version_info[0] > 2:
    unicode = str


def __concat(object1, object2):

    if isinstance(object1, str) or isinstance(object1, unicode):
        object1 = [object1]
    if isinstance(object2, str) or isinstance(object2, unicode):
        object2 = [object2]
    return object1 + object2


def __capitalize_first_char(word):

    return word[0].upper() + word[1:]


def __split(word, language='en_US'):

    dictionary = enchant.Dict(language)
    max_index = len(word)

    if max_index < 3:
        return word

    for index, char in enumerate(word, 2):

        left_word = word[0:index]
        right_word = word[index:]

        if index == max_index - 1:
            break

        if dictionary.check(left_word) and dictionary.check(right_word):
            return [compound for compound in __concat(left_word, right_word)]

    return word


def split(compound_word, language='en_US'):

    words = compound_word.split('-')

    word = ""

    for x in words:
        word += x

    result = __split(word, language)

    if result == compound_word:
            return [result]

    return result
