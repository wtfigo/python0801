import json

try:
    rest = open("rest.json", "r")
    print('good')
except IOError:
    print("no good")

#print(rest.read())
data = rest.read()

info = json.loads(data)
#print(info)
print('borough:', info["borough"])
Grades = info["grades"]


for item in Grades:
    print(item['grade'])
    print('score:', item["score"])

print('name:', info["name"])


text_file = open("hello.txt", "w")
text_file.write("the knights who say neeeeeeeeeeeeee")
text_file.close()


with open("1.txt", "w") as text_file:
    text_file.write("the knights who say neeeeeeeeeeeeee")

#print(len(data))
'''
for key, value in data:
    name = key
    value = xxx
    print(name,":")
    print(xxx)
#data = json.loads(rest)
#data['key']

#print(data.values())

rest.close()'''