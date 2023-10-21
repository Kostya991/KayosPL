import os

def save_input_to_file(input_text):
    with open('main.kpf', 'w') as file:
        file.write(input_text)

def extract_text_from_console_prnt(line):
    if line.startswith('console.prnt("') and line.endswith('")'):
        text_to_print = line[14:-2]
        return text_to_print
    elif line.startswith("console.prnt('") and line.endswith("')"):
        text_to_print = line[14:-2]
        return text_to_print
    elif line.startswith("console.prnt(") and line.endswith(")"):
        var_name = line[13:-1].strip()
        if var_name in globals():
            return str(globals()[var_name])
        else:
            raise ValueError(f"Variable '{var_name}' not found")
    else:
        raise ValueError("text in console.prnt should be enclosed in either single or double quotes")

def extract_text_from_console_inpt(line):
    if line == 'console.inpt("")':
        user_input = input()
        return user_input
    elif line.startswith('console.inpt("') and line.endswith('")'):
        prompt = line[13:-2]
        user_input = input(prompt)
        return user_input
    elif line.startswith("console.inpt('") and line.endswith("')"):
        prompt = line[13:-2]
        user_input = input(prompt)
        return user_input
    elif line.startswith("console.inpt(var") and line.endswith(")"):
        var_name = line[13:-1].strip()
        if var_name in globals():
            return str(globals()[var_name])
        else:
            raise ValueError(f"Variable '{var_name}' not found")
    else:
        raise ValueError("text in console.inpt should be enclosed in either single or double quotes")



def set_variable(line):
    if line.startswith("var"):
        parts = line[3:].split('=')
        if len(parts) == 2:
            var_name = parts[0].strip().capitalize()
            var_value = parts[1].strip()
            globals()[var_name] = var_value
            print(f"variable {var_name} set to {var_value}")
            return True
    return False

line_number = 1
itr_text = ""

print("KAYOS PROGRAMMING LANGUAGE TEST")
while True:
    itr = input(f"{line_number} ")
    line_number += 1
    
    if itr == "":
        input("\n")
    else:
        try:
            if itr.startswith("console.inpt"):
                user_input = extract_text_from_console_inpt(itr)
                if user_input is not None:
                    print(f"'{user_input}'")
            elif itr.startswith("console.prnt"):
                text_to_print = extract_text_from_console_prnt(itr)
                if text_to_print is not None:
                    print(f"'{text_to_print}'")
            elif itr.lower() == 'save.file {based}':
                save_input_to_file(itr_text)
                print("file main.kpf was created")
            elif set_variable(itr):
                pass
            else:
                print(f"there is no '{itr}'")
                itr_text += itr + '\n'
        except ValueError as e:
            print(e)
