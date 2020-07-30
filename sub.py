def chack_name(name):
    user="mehran"
    if (name==user):
        print("Ok")
        return True
    else:
        print("not Match ")
        return False

## evriting is fine 
input_name=input("what is your name?")
chack_name(str(input_name))

print("proces is done")
