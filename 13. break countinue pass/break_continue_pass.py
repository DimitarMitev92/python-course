# BREAK
while True:
    name = input("Enter your name: ")
    if(name != ""):
        break

# CONTINUE
phone_number = "123-456-7890"
for i in phone_number:
    if(i == "-"):
        continue
    print(i, end="")


# PASS
for i in range(1,21):
    if(i == 13):
        pass
    else:
        print(i)
