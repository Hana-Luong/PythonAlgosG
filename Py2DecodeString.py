# String Decode  
# Given an encoded string, decode the string into its original format

# Input: "a3b2c1d3"
# Output: "aaabbcddd"

#Student's Solution

str = "a3b2c1d3"

def reverse_string(str):
    result = ""
    for x in range(len(str)):
        if x % 2 == 1:
            result += int(given_string[x]) * given_string[x-1]
    return result

print(reverse_string(str))

# instructor's Solution
encoded = "a3b2c1d3"

def decode(stringy_string):
    print(stringy_string)
decode(encoded):
    print(stringy_string)
    dictionary = {}
    result = ""
    for idx in range(len(encoded))
        print(dix, stringy_string)
        if idx % 2 == 0:
            print("I am even")
            dictionary[encoded[idx]]=""
        else:
            print("I am odd")
            dictionary[encoded[idx]] = int(encoded[idx])
    for key in dictionary:
        print(key,dictionary[key])
        result += key * dictionary[key]

