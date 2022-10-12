
def word_dictionary():

    search_word = input("Search for a word: ")

    dictionary = {
        "hi": "a way of greeting",
        "eyes": "an organ for seeing",
        "earth": "a planet in space"
    }
    
    for k,v in dictionary.items():
        if k == search_word:
            print(f"{k} - {v};")
            break
    else:
        print("Not found in dictionary.")

    
        
word_dictionary()