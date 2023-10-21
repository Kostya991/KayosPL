import os

def save_input_to_file(input_text):
    with open('main.kpf', 'w') as file:
        file.write(input_text)
        file.write(itr)

def extract_text_from_console_prnt(line):
    if line.startswith("console.prnt(") and line.endswith(")"):
        text_to_print = line[13:-1]
        return text_to_print
    return None

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
        text_to_print = extract_text_from_console_prnt(itr)
        if text_to_print is not None:
            print(text_to_print)
        elif itr.lower() == 'save.file {based}':
            save_input_to_file(itr_text)
            print("file main.kpf was created")
        elif set_variable(itr):
            pass
        else:
            print(f"there is no '{itr}'")
            itr_text += itr + '\n'
