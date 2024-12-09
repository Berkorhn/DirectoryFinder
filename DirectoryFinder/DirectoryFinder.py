import requests

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

foundUrls = []

def FindDirecties(url):
    with open("wordlist.txt", "r") as listFile:
        for line in listFile:
            word = line.strip()
            testUrl = url + "/" + word
            response = request(testUrl)
            if response:
                print("Found URL --> " + testUrl)
                foundUrls.append(word)

url = ""   #Target url
FindDirecties(url)

for foundUrl in foundUrls:
    FindDirecties(url + "/" + foundUrl)
