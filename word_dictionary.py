
# def word_dictionary():

#     search_word = input("Search for a word: ")

#     dictionary = {
#         "hi": "a way of greeting",
#         "eyes": "an organ for seeing",
#         "earth": "a planet in space"
#     }
    
#     for k,v in dictionary.items():
#         if k == search_word:
#             print(f"{k} - {v};")
#             break
#     else:
#         print("Not found in dictionary.")

    
        
# word_dictionary()


def word_dictionary():

    dictionary = {
        "hi": "a way of greeting",
        "eyes": "an organ for seeing",
        "earth": "a planet in space"
    }

    while True:
        search_word = input("Search for a word: ")
        
        if search_word in dictionary:
            print(f"{search_word} - {dictionary[search_word]};")
        elif search_word == "":
            print("Type a word please.")
        else:
            print("The word you search for is not in the database.")
            
            


word_dictionary()