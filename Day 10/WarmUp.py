"""def format_name(f_name, l_name):
    formated_f_name = str(f_name).title()
    formated_l_name = str(l_name).title()
    return f"{formated_l_name} {formated_f_name}"

formated_string = format_name(f_name= "MARKA", l_name ="DeorcY")
print(formated_string)

def function1 (text):
    return text + text + text
def function2 (text):
    return text.title()


output = function1("history")

output2 = function2(output)

print(output2)

"""
# Part 2
# Docstring:

def format_name(f_name, l_name):
    """Take a first and last name format it to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name(input("What is your first name?"), input("What is your last name")))
