array = ["Hello", "2", "world", ":=)"]
newArray = []
for i in range(0, len(array)):
    if len(array[i]) <= 3:
        newArray.append(array[i])
print(newArray)