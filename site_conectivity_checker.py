# import urllib module
# use urllib.request to get the data from the url
# write a function that takes a url 
# returns a response



import urllib.request as urllib

url = input("Add the site your want to verify: ")


def verify_conectivity():

    
    response = urllib.urlopen(url)
    
    
    print("Checking conectivity...")

    if response.getcode() == 200:
        print(f"Connected to {url} succesfully.")
    else:
        print(f"Fail to connect to the {url}")

    


verify_conectivity()