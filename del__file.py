class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, "r")

    def read_data(self):
        return self.file.read()
    
    def __del__(self):
        self.file.close()

file_obj = FileHandler("loops_constru.py")
print(file_obj.read_data())