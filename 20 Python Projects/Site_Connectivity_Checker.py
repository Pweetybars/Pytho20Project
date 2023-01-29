# give program an url : it gonna tell us if it's running to not 
# Import urllib
# use urllib.request 
# write a function that take a url and then return a respond 

import urllib.request as urllib

def main(url):
    print("Checking connectivity ")

    response = urllib.urlopen(url)
    print("Connected to ", url, "successfully")
    print("The response coed was: ", response.getcode())

print("This is a site connectivity checker programm. ")
input_url = input("Input the URL of the site: ")

main(input_url)