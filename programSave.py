
class programSave:

    items = []
    fileWrite = object
    fileRead = object

    def __init__(self):
        self.fileWrite = open("todostore.txt", "a")
        self.fileRead = open("todostore.txt", "r")
        lines = self.fileRead.readlines()

        for line in lines:
            if len(line) > 2:
                splitLine = line.split("|||")
                self.items += [splitLine]

        self.fileRead.close()

    def getSaveData(self):
        return self.items

    def saveData(self, items):
        
        for item in items:
            self.fileWrite.write(item[0])
            self.fileWrite.write("|||")
            self.fileWrite.write(item[1])
            self.fileWrite.write("|||")
            self.fileWrite.write(item[2])
            self.fileWrite.write("\na\n")