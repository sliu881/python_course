
def greeting():
    first_name = input("Enter your first name: ")
    last_name =input ("Input your last name: ")
    if first_name =="":
        print("your first name is missing.")
    if last_name == "":
        print("your last name is missing.")

    if first_name =="" and last_name =="":
        return 0
    print(f"Hello, {first_name} {last_name} ")

greeting()


