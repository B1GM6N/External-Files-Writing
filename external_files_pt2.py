
def writing():
    file = open('empty_', 'w')
    print("Opening file.")
    print("What do you want to add?")
    add = input(">")
    file.write(f"{add}\n")
    file.write("You just added to a file.")
    file.close()
    print("printing file")
    file = open('empty_', 'r')
    pr = file.read()
    print(pr)
    print("closed file")
print("We are going to write in an empty file.")
while True:
    writing()
    y = input("Type 'y' if you want to go again")
    if y == 'y':
        print(" ")
    elif y != 'y':
        print("bye")
        break