## This class contains all blocks

class world:
    maxX = 64
    maxY = 64
    maxZ = 2
    blocks=[]

    def __init__(self):
        return

    def getMaxX(self):
        return self.maxX
    def getMaxY(self):
        return self.maxY
    def getMaxZ(self):
        return self.maxZ

    def getMaxSize(self):
        return self.maxX*self.maxY*self.maxZ

    

    def loadWorld(self,data):
        #print data
        self.blocks=data
        

    ## Prints a list with blocks to use with mysql
    def exportWorld(self):
        tmp_i=0
        print self.blocks
        #for tmp_x in range(0,self.maxX):
        #    print tmp_x," - ", self.blocks[tmp_x]




        