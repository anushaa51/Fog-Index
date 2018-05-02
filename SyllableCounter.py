

def syllables(word):
    word = word.lower()
    saved = word
    word = word + " "  # word extended
    length = len(word)
    ending = ["ing " ,"ed " ,"es " ,"ous " ,"tion " ,"nce " ,"ness ","ly "]  # not included in complex words

    for end in ending:
        x = word.find(end)
        if x > -1:
            x=length-x
            word = word[:-x]
    vowels = "aeiouy"
    syllableCount = 0
    if word[-1] == " ":
        word = word[:-1]
    # removing the extra " " at the end if failed and dropping last letter if e
    if word[-1] == "e":
        if word[-3:] == ("nce" or "rce"):
            syllableCount = 0
        elif word[-3] not in vowels and word[-2] not in vowels and word[-3:] != ("nce" or "rce") :
            if word[-3] != "'":

                syllableCount += 1  # e cannot be dropped as it contributes to a syllable
        word = word[:-1]
    one_syllable_beg = ["ya", "ae", "oe","ea","yo","yu","ye"]
    TwoSyllables = ["ao","uo","ia","eo","ea","uu","eous", "uou" ,"ii","io","ua","ya","yo","yu","ye"]
    OneSyllable = ["ie","ai","ae","au","aa","ee","ei","eu","iu","oa","oe","oi","ue","ui","uo","oo","yi","ay"]
    LastLetter = str()
    # last letter is null for the first alphabet
    for index, alphabet in enumerate(word):
        if alphabet in vowels :
            CurrentCombo = LastLetter+alphabet
            if len(CurrentCombo) == 1 :  # if it's the first alphabet
                if word[1] not in vowels:  # followed by a consonant, then one syllable
                    syllableCount += 1

                    LastLetter = word[1]
                else:
                    syllableCount += 1  # followed by a vowel
                    LastLetter = alphabet

            else :
                if CurrentCombo in TwoSyllables :
                    #if they're only 1 syllable at the beginning of a word, don't increment
                    if CurrentCombo == word[:2] and CurrentCombo in one_syllable_beg :
                        syllableCount+=0
                    else :
                        syllableCount += 1  # vowel combination forming 2 syllable

                    LastLetter = alphabet
                else :  # two vowels (one syllable) as well as non vowel combination
                    if CurrentCombo in OneSyllable:
                        try:
                            if CurrentCombo + word[index+1] == word[- 3:] :  # ier conributes to 2 syllables

                                syllableCount += 1
                        except IndexError :
                            syllableCount += 0

                        LastLetter = alphabet


                    else:

                        if LastLetter not in vowels:
                            syllableCount+=1
                            LastLetter = alphabet

                        else:

                            # not in vowel combination
                            LastLetter = alphabet


        else :
            LastLetter=alphabet



    if word[-2:]  ==  "sm" : syllableCount+=1



    print("Number of syllables in ",saved," is ",syllableCount)


word = input("Enter a string\n")
syllables(word)