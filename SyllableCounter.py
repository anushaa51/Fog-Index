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
    syllableCount = 0
    if word[-1] == " ":
        word = word[:-1]
    # removing the extra " " at the end if failed and dropping last letter if e
    if word[-1] == "e" and len(word)>=3:
        if word[-3:] == "nce" and word[-3:] == "rce":
            syllableCount = 0

        elif word[-3] not in vowels and word[-2] not in vowels and word[-3:] != "nce" and word[-3:] != "rce":
            if word[-3] != "'":
                syllableCount += 1  # e cannot be dropped as it contributes to a syllable
        word = word[:-1]

    one_syllable_beg = ["ya", "ae", "oe", "ea", "yo", "yu", "ye"]
    TwoSyllables = ["ao", "uo", "ia", "eo", "ea", "uu", "eous", "uou", "ii", "io", "ua", "ya", "yo", "yu", "ye"]
    LastLetter = str()  # last letter is null for the first alphabet
    for index, alphabet in enumerate(word):
        if alphabet in vowels:
            CurrentCombo = LastLetter + alphabet
            if len(CurrentCombo) == 1:  # if it's the first alphabet
                if word[1] not in vowels:  # followed by a consonant, then one syllable
                    syllableCount += 1
                    LastLetter = word[1]
                else:
                    syllableCount += 1  # followed by a vowel
                    LastLetter = alphabet

            else:
                if CurrentCombo in TwoSyllables:
                    # if they're only 1 syllable at the beginning of a word, don't increment
                    if CurrentCombo == word[:2] and CurrentCombo in one_syllable_beg:
                        syllableCount += 0
                    elif word[index - 2] + CurrentCombo + word[index + 1] == "tion" or word[index-2]+CurrentCombo+word[index+1] =="sion" :
                        # here io is one syllable :
                        syllableCount += 0

                    else:
                        syllableCount += 1  # vowel combination forming 2 syllables

                    LastLetter = alphabet

                else:  # two vowels as well as non vowel combination
                    if LastLetter not in vowels:
                        syllableCount += 1
                        LastLetter = alphabet

                    else:
                        LastLetter = alphabet


        else:
            LastLetter = alphabet

    if word[-3:] == "ier":  # word ending with ier has 2 syllables
        syllableCount += 1

    print(syllableCount)


word = input("Enter a string")
syllables(word)