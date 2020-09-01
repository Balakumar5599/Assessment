def color_pair(color_string):
    count=[]
    distinct_char=set(color_string)
    for char in distinct_char:
        count.append(color_string.count(char))
    for item in count:
        if item%2!=0:
            return False
    else:
        return True

color_string=input("Enter the string: ")
print("Pair for all character:",color_pair(color_string))
