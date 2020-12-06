
# String Encode
# You are given a string that may contain sequences of consecutive characters.
# Create a function to shorten a string by including the character,
# then the number of times it appears. 


# str1 = "aaaabbcddd"
# expected1 = "a4b2c1d3"

# str2 = ""
# expected2 = ""

# str3 = "a"
# expected3 = "a1"

# for i in range(len([1,2,3])):
#     print(i)



def encode_string(stringy_string):
    result = ""
    counter = {}
    #print(stringy_string) 
    for char in stringy_string:
        if char not in counter:
            counter[char] = 1
        else:
            counter[char] = +1
    #print(counter)
    for item in counter:
        #print(item)
        result += key  
        #print(counter[key])
        result +=string(counter[key])
        #print(result)
        return result

    encoded_string = encode_string("aaaabbcddd")
    print(encoded_string)


