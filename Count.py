import re

FileObject = open("TestDocument.txt", "r")
FileText = FileObject.read()
Number_Of_Words = len(re.findall("[a-zA-Z]+", FileText))  # Regex to match all words
Number_Of_Sentences = len(re.split("[.!?]+]", FileText))

print(Number_Of_Words)
print(Number_Of_Sentences-1)