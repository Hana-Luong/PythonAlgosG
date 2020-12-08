
# Zip Arrays into Map / Helper Function

# Given two lists, create an associative array (aka hash map, an obj / dictionary) 
# containing keys from the first list, and values from the second.
# Associative lists are sometimes called maps because a key (string) maps to a value 

# Input: ["abc", 3, "yo"], [42, "wassup", True]
# Output: {
#     "abc": 42,
#     3: "wassup",
#     "yo": True,
# }
""" 
def zip_lists(keys, vals):
    return zip(keys, vals)

print(zip_lists(["abc", 3, "yo"], [42, "wassup", True])) """

# student's
def combine_list(keys,values):
    direct = {}
    for i in range(len(keys)):
        direct[keys[i]] = values[i]
    return direct
print(combine_list(["abc", 3, "yo"], [42, "wassup", True]))

#instructor
