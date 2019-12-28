import sys
import os
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"}

for num in range(0, 450, 50):
    r = requests.get(
        f"https://www.hackerrank.com/rest/contests/master/tracks/algorithms/challenges?offset={num}&limit=50&track_login=true", headers=headers).json()
    for item in r['models']:
        print(item['name'])
        filename = "code/database.txt"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "a") as f:
            f.write(item['name'] + "\n")
            f.close()

sys.exit('Problem names are present at code/database.txt')

