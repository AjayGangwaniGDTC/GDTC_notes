#Task: Count how many times each rating (1–5) appears across all courses.

#importing the library
import json

data = {
    "feedback": [
        {"course": "Python", "ratings": [5, 4, 5, 3]},
        {"course": "Java", "ratings": [4, 4, 5]},
        {"course": "C++", "ratings": [3, 2, 4, 4]}
    ]
}

#creating an empty dictionary to store data
count = {}
for i in data['feedback']:
    #traversing the rating list in feedback list
    for rating in i['ratings']:
        #checking if the rating key is present in count dictionary or not if it is present then incrementing it by 1 else giving its count as 1
        if rating in count:
            count[rating] += 1
        else:
            count[rating] = 1

#loading the output into a new json file
with open("count_occurences.json","w") as file:
    json.dump(count, file, indent=2)

