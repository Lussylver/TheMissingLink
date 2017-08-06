

class Gcode():

    def __init__(self, deck):

        #Load the gcode
        path = deck.gcodePath
        gcodefile = open(path)
        self.rawgcode = gcodefile.read()
        print self.rawgcode
