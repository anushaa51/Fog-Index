from WSCount import wordcount, sentencecount, counting


def main():
    try :
        fog_index_calculated = ((wordcount()/sentencecount()) + counting())*0.4
        gunning_fog_index = ((wordcount()/sentencecount()) + 100*(counting()/wordcount()))*0.4
    except ZeroDivisionError :
        fog_index_calculated = gunning_fog_index = 0
    new_file = open("FogIndex.txt", "w+")

    new_file.write("The Fog Index of the given text document is " + str(fog_index_calculated) + "\n")
    new_file.write("The Gunning Fog Index of the given document is " + str(gunning_fog_index)+"\n")
    new_file.write("Total number of sentences = " + str(sentencecount())+"\n")
    new_file.write("Total number of words = " + str(wordcount()) + "\n")
    new_file.write("Total number of words with 3 or more syllables =" + str(counting()) + "\n")
    new_file.close()



if __name__ == '__main__':
    main()