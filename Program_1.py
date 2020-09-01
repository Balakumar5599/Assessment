def color_pair(color_string):
    count=[]
    for char in color_string:
        count.append(color_string.count(char))
    for item in count:
        if item%2!=0:
            return False
    return True

color_string=input("Enter the color string: ")
print(color_pair(color_string))
