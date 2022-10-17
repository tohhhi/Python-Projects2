from PyDictionary import PyDictionary

while True:
    word = input("Search for a word: ")

    dictionary = PyDictionary(word)

    print(dictionary.getMeanings())

    if word == "":
        break


    

# PYTHON DICTIONARY ---->

# def word_dictionary():

#     dictionary = {
#         "hi": "a way of greeting",
#         "eyes": "an organ for seeing",
#         "earth": "a planet in space"
#     }

#     while True:
#         search_word = input("Search for a word: ")
        
#         if search_word in dictionary:
#             print(f"{search_word} - {dictionary[search_word]};")
#         elif search_word == "":
#             print("Type a word please.")
#         else:
#             print("The word you search for is not in the database.")
            
            


# word_dictionary()