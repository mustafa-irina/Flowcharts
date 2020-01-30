from Block import Block

class Algorithm:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.ListBlocks = []

    def addBlock(self, id, name, text, way):
        array = self.ListBlocks
        for i in range(len(array)):
            if (array[i].id == id):
                return Exception
        self.ListBlocks.append(Block(id, name, text, way))

    def findBlockByID(self, id):
        for i in range(len(self.ListBlocks)):
            if (self.ListBlocks[i].id == id):
                return i
        return -1

    def getBlokToString(self, j):
        j = self.findBlockByID(j)
        if (j == -1):
            return "Block not found"
        block = self.ListBlocks[j]
        s = '['
        for i in range(len(block.way)):
            if (i == len(block.way) - 1):
                s = s + str(block.way[i]) + ']'
            else:
                s = s + str(block.way[i]) + ", "
        output = "ID = " + str(block.id) + "\nName = " + block.name + "\nText = " + block.text + "\nWays = " + s
        return output

    def blockExist(self, blockId):
        for i in range(len(self.ListBlocks)):
            if (self.ListBlocks[i].id == blockId):
                return True
        return False