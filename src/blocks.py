##
## TODO: Global blocks list containing all blocks
##


## Depenencies
from direct.showbase.ShowBase import ShowBase
from pandac.PandaModules import *
import sys

## Project modules
import clientConnection
import world


class Blocks(ShowBase):

    clientConn=0
    world=0

    ## Contructor
    def __init__(self):
        ## Init panda
        ShowBase.__init__(self)
        ## Init client sql connection
        self.clientConn = clientConnection.clientConnection()
        ## Init world
        self.world=world.world()



    def drawBlocks(self):
        max_x=self.world.getMaxSize()
        
        print "max_x:",max_x, "nodes: ", 
        for tmp_x in range(0,max_x-1):
            tmp=self.world.blocks[tmp_x]
            x=tmp[0]
            y=tmp[1]
            z=tmp[2]

            tmpModel = self.loader.loadModel("models/box")

            newModel = NodePath('model')
            tmpModel.getChildren().reparentTo(newModel)
            
            newModel.reparentTo(self.render)
            newModel.setScale(1, 1, 1)
            newModel.setPos(x, y, z)

        self.render.flattenStrong()

        Node=NodePath(PandaNode("PhysicsNode"))
        Node.reparentTo(render)
        jetpackGuy=loader.loadModel("models/box")
        jetpackGuy.reparentTo(render)
        an=ActorNode("jetpack-guy-physics")
        anp=Node.attachNewNode(an)
        base.physicsMgr.attachPhysicalNode(an)
        jetpackGuy.reparentTo(anp)


        self.render.analyze()


    ## Loads the world through clientConnection
    def loadBlocks(self):
        data=self.clientConn.requestData();
        self.world.loadWorld(data)

    ## bind events for the keys
    def initKeyboard(self):
        ##escape exits
        self.disableMouse()

        self.useDrive()
        self.accept('escape', sys.exit )
        ## move the cam
#        self.accept('arrow_up-repeat', self.moveCamera )
#        self.accept('arrow_down-repeat', self.moveCamera )
#        self.accept('arrow_right-repeat', self.moveCamera )
#        self.accept('arrow_left-repeat', self.moveCamera )

    def moveCamera(self):
        self.cam


blocks = Blocks()
blocks.loadBlocks()
blocks.drawBlocks()
blocks.initKeyboard()
blocks.run()
