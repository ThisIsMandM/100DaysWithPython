def format_name(f_name, l_name):
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