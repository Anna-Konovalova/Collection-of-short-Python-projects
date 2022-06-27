#Importing libraries
import requests
from bs4 import BeautifulSoup
import webbrowser

print("This programme will generate a random Wikipedia article for you.")

while True:
    url = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    soup = BeautifulSoup(url.content, "html.parser")

    title = soup.find(class_="firstHeading").text
    print(f"{title} \nWould you like to view this article? (Please answer yes or no)")

    ans = input("").lower()
    if ans == "yes":
        url = "https://en.wikipedia.org/wiki/%s" % title
        webbrowser.open(url)
        break
    elif ans == "no":
        print("Lets find a different article!")
        continue
    else:
        print("Wrong choice!")
        break
