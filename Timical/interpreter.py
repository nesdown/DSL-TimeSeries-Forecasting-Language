class Interpreter():
    def __init__(self):
        self.file_values_set = {}
        self.vectors_set = {}
        print("Initializer Started...")

    def File_Open(self, file_variable_binding, file_path):
        # print("\n\n\n" + str(file_path))
        with open(file_path.value[1:-1]) as f:
            file_contents = f.read()
        print(file_contents)

        self.file_values_set[file_variable_binding.value] = [file_contents]

        return "File contents read successfully."

    def Vector_Init(self, vector_name, vector_data):
        print ("Starting Vector Function")
        vector_list = vector_data.value[1:-1].split(" ")
        print ("Vectors Set is being gathered")
        self.vectors_set[vector_name.value] = [vector_list]
        print("Vector read successfully")

        return "Vector read successfully"