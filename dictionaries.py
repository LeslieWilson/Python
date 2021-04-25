#dictionaries are used to associate keys and values so if you know the key you can access the value. ralf is the key the value is his age
#if you want to access a value you can use subscript notation
#for dictionaries you need to access the keys themsel es
#

friend_ages = {"ralf": 39, "adam":30}

print(friend_ages["ralf"])

#you can change an element

friend_ages["ralf"] = 22

print(friend_ages["ralf"])

#when you're using a dictionary to represent multiple things like multiple burritos its good to have a list of dictionaries
#

friends=[
    {"name": "leslie", "age": 20},
    {"name": "larisa", "age": 24}
]

print(friends[1]["name"])

#this is how you access something in a list of dictionaries

student_attendance= {"leslie": 96, "lele":80, "wang":100}

for student in student_attendance:
    print("%s has the attendance" % student) 
    print(student_attendance[student])

    #but there is a better way 


for student, attendance in student_attendance.items():
    print("%s has the attendance" % student) 
    print(attendance)