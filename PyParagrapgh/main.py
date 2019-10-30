#Improting libraries for the file
import os
import string

global file_num
file_num = 1
#Function that helps in opening and reading the file
def load_file(filepath, number):
 

    #Opening the file to read data
    with open(filepath, "r") as text_file:

        #Variable
        num_words  = 0
        sentence_count = 0
        char_count = 0
        wordsCount = []

        for line in text_file:
            words = line.split()
            sentences = line.split(".")
            num_words += len(words)
            sentence_count += len(sentences)
            for c in line:
                if c.isspace() != True:
                    char_count += 1
            average = round(char_count/num_words, 2)
            for sentence in sentences:
                Words = sentence.split(" ")
                wordsCount.append(len(Words))
            average_sentence = round(sum(wordsCount)/len(wordsCount), 1)
    
    #Outputing Results to the Screen
    print(f"Paragraph Analysis File Number {number}")
    print("-------------------------------------")
    print(f"Approximate Word Count: {num_words}")
    print(f"Approximate Sentence Count: {sentence_count}")
    print(f"Approximate Letter Count: {average}")
    print(f"Average Sentence Length: {average_sentence}")
    print("\n")


#Defining file path
file1 = os.path.join('Resources', 'paragraph_1.txt')
file2 = os.path.join('Resources', 'paragraph_2.txt')
file3 = os.path.join('Resources', 'paragraph_3.txt')

#Getting data from the file
load_file(file1, file_num)
file_num += 1
load_file(file2, file_num)
file_num += 1
load_file(file3, file_num)

