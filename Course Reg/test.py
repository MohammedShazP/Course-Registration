def string_split(st):
    # new = st.split()
    # first_name = new[0]
    # second_name = new[1]
    # return f"first name is {first_name}. Second name is {second_name}."
    return st[::-1]

string = "Sharat Kumar"

print(string_split(string))