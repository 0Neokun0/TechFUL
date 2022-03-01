
number = int(input())
input_string = input()

user_list = input_string.split()
# print list


# convert each item to int type
for i in range(len(user_list)):
    # convert each item to int type
    user_list[i] = int(user_list[i])

# Calculating the sum of list elements
print( min(user_list))