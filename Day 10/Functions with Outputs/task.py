def format_name(first_name, last_name):
    formated_f_name = first_name.title()
    formated_l_name = last_name.title()
    return formated_f_name, formated_l_name

f_name, l_name = format_name("anGeLa", "yu")
print(f_name, l_name)