import requests
import json

response = requests.get('http://jsonplaceholder.typicode.com/posts')
#print(response.text)
#data = response.text

data = json.loads(response.text)
#data['key']

#print(data)
print(type(data))
l = (len(data)) -1

for d1 in data[l:]:
    d2 = d1['id']
    print(d2)
'''
for item in data:
    print(item)

fh = open("1.json", "w")
#lines_of_text = ["One line of text here", "and another line here", "and yet another here", "and so on and so forth"]
fh.write(data)
fh.close()
'''


'''
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
    '''

#Grades = info["grades"]



