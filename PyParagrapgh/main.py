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

        for line in text_file:
            words = line.split()
            sentences = line.split(".")
            num_words += len(words)
            sentence_count += len(sentences)

    #Outputing Results to the Screen
    print("Paragraph Analysis")
    print(f"Word count in File {number} is {num_words}")
    print(f"Sentence count is in File {number} is {sentence_count}")


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

