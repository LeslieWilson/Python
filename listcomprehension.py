# numbers = [1,2,3]
# doubled = []

# for num in numbers:
#     doubled.append(num*2)

# print(doubled)

#===list comprehensions- a way to define and create lists based on existing lists

# numbers = [1,2,3]
# doubled = [x*2 for x in numbers]

# print(doubled)

# number_list = [x for x in range(20) if x % 2 ==0]
# print number_list

# friends = ["sam", "liza", "sally", "larisa"]
# starts_s=[]

# for friend in friends:
#     if friend.startswith("s"):
#         starts_s.append(friend)

# print(starts_s)

# same thing in list comprehension. a new list is created when you make a list comprenehsion. two different lists two different places in memory.


friends = ["sam", "liza", "sally", "larisa"]
starts_s=[x for x in friends if x.startswith("s")]

print(starts_s)

print(friends is starts_s)

print("friends: %s " % id(friends), id(starts_s))


#  id is related to the memory address where the list is stored

