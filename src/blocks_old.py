##
## TODO: Global blocks list containing all blocks
##


## Depenencies
from direct.showbase.ShowBase import ShowBase

## Project modules
import clientConnection
import world


class MyApp(ShowBase):

    clientConn=0
    world=0
    nodes=[8190];

    ## Contructor
    def __init__(self):
        ## Init panda
        ShowBase.__init__(self)
        ## Init client sql connection
        self.clientConn = clientConnection.clientConnection()
        ## Init world
        self.world=world.world()


    ## Creates the list with blocks
    def prepareBlocks(self):

        for tmp_x in range(0, self.maxX):
            self.blocks.insert(tmp_x,[])
            for tmp_y in range(0, self.maxY):
                self.blocks[tmp_x].insert(tmp_y, [])
                for tmp_z in range(0, self.maxZ):
                    self.blocks[tmp_x][tmp_y].insert(tmp_z, self.loader.loadModel("models/box"))
                    # Reparent the model to render.
                    self.blocks[tmp_x][tmp_y][tmp_z].reparentTo(self.render)
                    # Apply scale and position transforms on the model.
                    self.blocks[tmp_x][tmp_y][tmp_z].setScale(1, 1, 1)

                    self.blocks[tmp_x][tmp_y][tmp_z].setPos(tmp_x, tmp_y, tmp_z)

    def drawBlocks(self):
        max_x=self.world.getMaxSize()
        
        print "max_x:",max_x, "nodes: ", 
        for tmp_x in range(1,max_x-1):
            tmp=self.world.blocks[tmp_x]
            x=tmp[0]
            y=tmp[1]
            z=tmp[2]

            print "len, ", len(self.nodes)
            self.nodes.append(self.loader.loadModel("models/box"))
            print "len, ", len(self.nodes)
            self.nodes[tmp_x].reparentTo(self.render)
            self.nodes[tmp_x].setScale(1, 1, 1)
            self.nodes[tmp_x].setPos(x, y, z)
            


    ## @DEPRECATED only for export to a csv file
    ## Prints a list with blocks to use with mysql
    def exportBlocks(self):
        tmp_i=0
        for tmp_x in range(0,self.maxX):
            for tmp_y in range(0,self.maxY):
                for tmp_z in range(0,self.maxZ):
                    print tmp_i,",",tmp_x,",",tmp_y,",",tmp_z,",",1
                    tmp_i +=1

    ## Loads the world through clientConnection
    def loadBlocks(self):
        ##
        print "startar fran main"
        data=self.clientConn.requestData();
        self.world.loadWorld(data)
        print "after loadworld: world: "
        #print "max ->>>>>>>>>",count(self.world.blocks)
        
        #print data


        

app = MyApp()
app.loadBlocks()
app.drawBlocks()
#app.prepareBlocks()
#app.printBlocks()
app.run()
