def syllables(word):
    word = word.lower()
    word = word + " "  # word extended
    length = len(word)
    ending = ["ing ", "ed ", "es ", "ous ", "tion ", "nce ", "ness "]  # not included in complex words
    vowels = "aeiouy"

    for end in ending:
        x = word.find(end)
        if x > -1:
            x = length - x
            word = word[:-x]
    syllable_count = 0
    if word[-1] == " ":
        word = word[:-1]
    # removing the extra " " at the end if failed and dropping last letter if e
    if word[-1] == "e":
        try :
            if word[-3:] == "nce" and word[-3:] == "rce":
                syllable_count = 0

            elif word[-3] not in vowels and word[-2] not in vowels and word[-3:] != "nce" and word[-3:] != "rce":
                if word[-3] != "'":
                    syllable_count += 1  # e cannot be dropped as it contributes to a syllable
            word = word[:-1]
        except IndexError:
            syllable_count+=0

    one_syllable_beg = ["ya", "ae", "oe", "ea", "yo", "yu", "ye"]
    two_syllables = ["ao", "uo", "ia", "eo", "ea", "uu", "eous", "uou", "ii", "io", "ua", "ya", "yo", "yu", "ye"]
    last_letter = str()  # last letter is null for the first alphabet
    for index, alphabet in enumerate(word):
        if alphabet in vowels:
            current_combo = last_letter + alphabet
            if len(current_combo) == 1:  # if it's the first alphabet
                if word[1] not in vowels:  # followed by a consonant, then one syllable
                    syllable_count += 1
                    last_letter = word[1]
                else:
                    syllable_count += 1  # followed by a vowel
                    last_letter = alphabet

            else:
                if current_combo in two_syllables:
                    try:
                    # if they're only 1 syllable at the beginning of a word, don't increment
                        if current_combo == word[:2] and current_combo in one_syllable_beg:
                            syllable_count += 0
                        elif word[index - 2] + current_combo + word[index + 1] == "tion" or word[index - 2] + current_combo + \
                                word[index + 1] == "sion":  # here io is one syllable :
                            syllable_count += 0

                        else:
                            syllable_count += 1  # vowel combination forming 2 syllables

                        last_letter = alphabet
                    except IndexError:
                        syllable_count += 0

                else:  # two vowels as well as non vowel combination
                    if last_letter not in vowels:
                        syllable_count += 1
                        last_letter = alphabet

                    else:
                        last_letter = alphabet


        else:
            last_letter = alphabet

    if word[-3:] == "ier":  # word ending with ier has 2 syllables
        syllable_count += 1

    return syllable_count