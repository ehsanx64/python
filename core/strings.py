adam = "Adam"
eve = "Eve"
name = "Maria"
age = 28

def display(string):
    print(string)
    print()

def string_interpolation_f_string():
    print("** Using f-string ...")
    output = f"{adam} and {eve}"
    display(output)


def string_interpolation_percent_sign():
    print("** Using %-formatting ...")
    output = "%s is %d years old." % (name, age)
    display(output)


def string_interpolation_str_format():
    print("** Using str.format ...")
    output = "{} is {} years old.".format(name, age)
    display(output)


def demo_string_interpolation():
    print("* String Interpolation")
    string_interpolation_f_string()
    string_interpolation_percent_sign()
    string_interpolation_str_format()


demo_string_interpolation()
