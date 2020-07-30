def chack_name(name):
    user="mehran"
    if (name==user):
        print("Ok")
        return True
    else:
        print("not Match ")
        return False


input_name=input("what is your name?")
print ("ok")
chack_name(str(input_name))

print("proces is done")
