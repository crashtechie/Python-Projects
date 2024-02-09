#Variables
x = False
hello = "hello, "
a = 1
b = 2.5
c = {1,2,3}
name = input("What is your name?:")
#Main
while x == False:
    if name == "":
        name
    else:
        x = True
print(hello + name + "!")
print("\n I am a ",type(name))