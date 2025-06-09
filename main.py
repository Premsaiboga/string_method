# #converting the string to uppercase without using methods
def convert_to_uppercase(s):
    a = "abcdefghijklmnopqrstuvwxyz"
    b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    d = "" 
    for ch in s:
        for i in range(len(a)):
            if ch == a[i]:
                d += b[i]
                break
    return d

c = "premsai"
print(convert_to_uppercase(c))


def convert_to_lowercase(s):
    d = ""  
    for ch in s:
        if "A" <= ch <= "Z":
            d += chr(ord(ch) + 32)
        else:
            d += ch
    return d

c = "PREMSAI"
print(convert_to_lowercase(c))



# ## arrange the capital letters first
b = "chAiTnRu"
a = ""
x = ""
for i in b:
    if i.isupper():
        a+=i
    else:
        x+=i
print(a+x)


# ## removing space without using methods
def remove_spaces(s, char_to_remove=" "):
    result = ""
    for ch in s:
        if ch == char_to_remove:
            continue
        else:
            result += ch
    return result

b = "pre m @sai"
print(remove_spaces(b))

            
                
                
