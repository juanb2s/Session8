fp = open("dracula.txt")
count = 0
for line in fp:
   # if "Dracula" in line:
    #    count = count + 1
    line = line.lower()
   count = count + line.count("dracula")
print(f"The word Dracula shows up {count} times!")







