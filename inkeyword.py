"""
inkeyword
"""
# coding: interpy
# friends=["leslie", "mary", "joseph"]
# print("akjh" in friends)

# movies_watched = {"godzil", "the zone", "blahnovie"}
# user_movie = raw_input("what did you watch recently")

# if user_movie in movies_watched:
#     print("Ive watched %s too" % user_movie)
# else:
#     print("ok")

number = 7
user_input = raw_input("enter y if you want to play: ")

if user_input in("y", "U"):
    user_number= int(input("guess our number:"))
    if user_number == number:
        print("you guessed %s which is correct" % 7 )
    elif abs(number - user_number) == 1:
        print("you were off by one")
    else:
        print("you guessed %s which is incorrect" % user_number)





 
