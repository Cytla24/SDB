import json

class EngStudents():
    def __init__(self):
        self.studentlist = data
        self.size = 0

    def get(self,position):
        return self.studentlist["Students"][position]

    def add(self):
        self.studentlist["Students"].append({"ID" : input("ID"), "name" : input("Name"), "department" : input("Dept")})
        self.size += 1
        self.updatejson()

    def print(self):
        print(self.studentlist)

    def insert(self, position):
        self.studentlist.insert({"ID" : input("ID"), "name" : input("Name"), "department" : input("Dept")}, position)
        self.size += 1
        self.updatejson()

    def sizearray(self):
        return self.size

    def isempty(self):
        if self.size == 0:
            return True
        return False

    def delete(self, data):
        for i in self.studentlist["Students"]:
            if i["ID"] == data:
                self.studentlist["Students"].remove(data)
                self.size -= 1

    def updatejson(self):
        with open('data.txt', 'w') as outfile:
            json.dump(data, outfile)

data = {}
data["Students"] = []
with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)

x = EngStudents()
x.add()
x.add()
print(x.sizearray())
print(x.get(0))
x.print()

def main():
    return

if __name__ == "__main__":main()
