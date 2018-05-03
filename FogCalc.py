from WSCount import wordcount, sentencecount,counting

def main():
    try :
        fog_index_calculated = ((wordcount()/sentencecount()) + counting())*0.4
        gunning_fog_index = ((wordcount()/sentencecount()) + 100*(counting()/wordcount()))*0.4
    except ZeroDivisionError :
        fog_index_calculated = gunning_fog_index = 0
    print("The Fog Index of the given text document is ", fog_index_calculated)
    print("The Gunning Fog Index of the given document is ",gunning_fog_index)
    print("Total number of sentences = ", sentencecount())
    print("Total number of words = ",wordcount())
    print("Total number of words with 3 or more syllables =",counting())



if __name__ == '__main__':
    main()