"""Input a name and print alternate characters"""
name=input("enter name")
#error check for name to be blank
while len(name)<1:
    name=input("Enter longer names>> ")
print(name[::2])