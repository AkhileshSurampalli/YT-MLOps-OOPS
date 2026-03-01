#list = [1, 2, 3]
#string = "mlops playlist"
#myint = 455

#print(type(myint))

#my_str = string.capitalize()
#print(my_str)

from project import chatbook

list = [1, 2, 3]

# function
a1 = len(list)
print(a1)

# call in-method
user1 = chatbook() 
# if you want to access encapsulated variable, then you need to call it with _classname
print(user1._chatbook__id)
#user1.send_msg()

# usign static method directly from class rather than object
chatbook.set_id(15)

user2 = chatbook()
print(user2._chatbook__id)

user3 = chatbook()
print(user3._chatbook__id)




#print(user1._chatbook__name)

#print(user1.get_name())
##user1.set_name("Agent X")
#print(user1.get_name())