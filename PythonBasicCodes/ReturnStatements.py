#Return Statements in python

def cube(iNUm):
    print("cube")
    return iNUm * iNUm * iNUm

iResult = cube(3)
print(iResult)

#---------------Return statements ----------
#Without Return statements the program will be like=== below  -->>> by default python will return u a None
def square(num):
    print(num*num)
    #return None

print(square(3))


#----Emoji Converter--------
def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "\U0001F600",

        ":D": "\U0001F603"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output

message = input(">")
print(emoji_converter(message))
