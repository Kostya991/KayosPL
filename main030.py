# main.py

class Interpreter:
    def __init__(self):
        self.variables = {}
        self.functions = {}


    def run(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()

        use_akabase = False
        for line in lines:
            if "@use:akabase" in line:
                use_akabase = True
                break

        if not use_akabase:
            print("ERROR: @use:akabase not found")
            return

        start_section = False
        for line in lines:
            if line.strip() == "start:":
                start_section = True
            elif line.strip() == "end":
                start_section = False
            elif start_section:
                self.process_start_line(line)

        if start_section:
            print("ERROR: Missing 'end' command")

    def process_start_line(self, line):
        if line.startswith("@"):  # Ignore lines starting with @
            return

        if line.startswith("console.prnt"):
            parts = line[line.find("(")+1:line.rfind(")")].strip('\'"').split(',')
            variable_name = parts[0].strip()
            if variable_name in self.variables:
                print(self.variables[variable_name])
            else:
                print(f"ERROR: Variable {variable_name} not defined")
        elif line.startswith("var"):
            parts = line.split("=")
            if len(parts) == 2:
                variable_name = parts[0].strip()[3:]
                variable_value = parts[1].strip().strip('"\'')
                self.variables[variable_name] = variable_value
            else:
                print(f"ERROR: Invalid var command: {line}")
        elif line.startswith("console.inpt"):
            variable_name = line[line.find("(")+1:line.rfind(")")].strip('\'"')
            value = input(f"{variable_name} ")
            self.variables[variable_name] = value
        else:
            print(f"ERROR: Unknown command in START block: {line}")

if __name__ == "__main__":
    interpreter = Interpreter()
    interpreter.run("main.txt")
