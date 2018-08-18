dic_of_lists={"john":[87],"alice":[98],"bob":[55],"charlie":[45],"dave":[72]}

def gradeScores(Grade):
    if Grade >= 90 and Grade <= 150:
        return("an A")

    elif Grade >= 80 and Grade < 90:
        return("a B")

    elif Grade >= 70 and Grade < 80:
        return("a C")

    elif Grade >= 60 and Grade < 70:
        return("a D")

    else:
        return("an F")


#to loop through the dictionary
for key,value in dic_of_lists.items():
    name = key
    Grade = value[0]
    ABC = gradeScores(Grade)
    print (name,'has got a', Grade, 'on the test which tranlates to :', ABC)
