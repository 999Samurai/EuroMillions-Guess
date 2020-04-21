import requests
import json

balls = [] # Balls array
stars = [] # Stars array

URL = 'https://nunofcguerreiro.com/api-euromillions-json?result=all' # Free euromillions API
page = requests.get(URL)
cont = json.loads(page.content.decode())

for i in cont["drawns"]:
    balls.append(i["balls"].split())
    stars.append(i["stars"].split())

countballs = {}
for i in balls:
    for ball in i:
        if ball in countballs:
            countballs[ball] += 1
        else:
            countballs[ball] = 1

countstars = {}
for i in stars:
    for star in i:
        if star in countstars:
            countstars[star] += 1
        else:
            countstars[star] = 1

def mykey(t):
    return t[1]

orderedBalls = sorted(countballs.items(), key=mykey, reverse=True)
orderedStarts = sorted(countstars.items(), key=mykey, reverse=True)
givenBalls = 0
givenStars = 0

print("Numbers: ")

for ball in orderedBalls:
    if (givenBalls == 5): 
        continue
    print(ball[0])
    givenBalls += 1

print("\nStars: ")

for star in orderedStarts:
    if givenStars == 2: 
        continue
    print(star[0])
    givenStars += 1

a = input()
