my_dict = {
    "blue": "sky",
    "double": 2,
    "half": 0.5,
    "green": "grass",
    "yellow": "sun",
    "red": "apple"
}

your_num = int(input("Enter a number: "))
to_do = input("double or half? ").lower()

# look up value
multiply_by = my_dict[to_do]

# do math!
answer = your_num * multiply_by
print("{} x {} = {}".format(your_num, multiply_by, answer))





# double_num = your_num * 2
# half_num = your_num / 2
# if to_do == "double":
#     double_num
#     print("{} doubled is {}".format(your_num, double_num))
#
# if to_do == "half":
#     half_num
#     print("{} halved is {}".format(your_num, half_num))
#
# # list to make testing faster
# to_check = ["blue", "sky", "apple", "salad"]
#
# for item in to_check:
#
#     # check if it's a key (ie: a colour in our dictionary)
#     if item in my_dict:
#        print()
#        print("{} is a key in the dictionary".format(item))
#
#        # look up the value associatied with the key
#        coloured_object = my_dict[item]
#
#        # output the value and the key (eg: the sky is blue)
#        print("The {} is {}".format(coloured_object, item))
#
#     # check if it's a value (ie: an object in our dictionary)
#     elif item in my_dict.values():
#         print("{} is a value in the dictionary".format(item))