# have a python dictionary that has a key, value that represent the word and definition
# collect input from the user, input is a word, 
# check if the word is in the dictionary 
# print the definition 
def main():
    word_dictionary = {
        'hi' : 'a way of greeting',
        'ice' : 'frozen water',
        'pen': 'a stick have ink use to write'
    }

    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        if word in word_dictionary:
            print(word, ":", word_dictionary[word])

main()