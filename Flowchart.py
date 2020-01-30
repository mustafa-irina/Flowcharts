from Algorithm import Algorithm

class Flowchart:
    def __init__(self):
        self.ListAlgorithms = []

    def setAlghoritm(self, id, name):
        if (self.algExist(id)):
            print("An algorithm with ID = " + str(id) + " exists, id changed ID = " + str(id + 1) + ';')
            self.setAlghoritm(id + 1, name)
        else:
            algorithm = Algorithm(id, name)
            self.ListAlgorithms.append(algorithm)

    def addBlock(self, idAlg, idBlock, name, text, way):
        if (self.algExist(idAlg) == False):
            print("Algorithm not found")
        elif (self.blockExist(idAlg, idBlock)):
            print("ID = " + str(idBlock) + " for block busy, id changed ID = " + str(idBlock + 1))
            self.addBlock(idAlg, idBlock + 1, name, text, way)
        else:
            self.ListAlgorithms[self.findAlgorithmByID(idAlg)].addBlock(idBlock, name, text, way)

    def findAlgorithmByID(self, id):
        for i in range(len(self.ListAlgorithms)):
            if (self.ListAlgorithms[i].id == id):
                return i
        return -1

    def blockExist(self, algId, blockId):
        bE = False
        index = self.findAlgorithmByID(algId)
        if (index == -1):
            return False
        return (self.algExist(algId) and self.ListAlgorithms[index].blockExist(blockId))

    def algExist(self, algId):
        for i  in range(len(self.ListAlgorithms)):
            if (self.ListAlgorithms[i].id == algId):
                return True
        return False

    def getState(self, i, j):
        i = self.findAlgorithmByID(i)
        if (i == -1):
            print("Algorithm not found")
            return
        print(self.ListAlgorithms[i].getBlokToString(j))

if __name__ == "__main__":
    f = Flowchart()
    f.setAlghoritm(0, "tits")
    f.addBlock(0, 0, "one", "sosi", [1, 2])
    f.addBlock(0, 1, "two", "sam sosi", [-1])
    f.addBlock(0, 1, "3", "ok", [-1])
    f.getState(11, 10)