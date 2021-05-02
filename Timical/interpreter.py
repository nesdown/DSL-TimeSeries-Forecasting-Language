class Interpreter():
    def __init__(self):
        self.value_set = {}
        print("Initializer Started...")

    def File_Open(self, file_variable_binding, file_path):
        # print("\n\n\n" + str(file_path))
        with open(file_path.value[1:-1]) as f:
            file_contents = f.read()
        print(file_contents)

        self.value_set[file_variable_binding.value] = [file_contents]

        return "File contents read successfully."
