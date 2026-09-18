with open("data.txt","r+") as file:
        line = file.read()
        print(line)
        msg = "I am fine2"
        file.writelines(msg)

with open("data.txt","r++") as file:
        line = file.read()
        print(line)