

class Gcode():

    def __init__(self, deck):

        #Load the gcode
        path = deck.gcodePath
        gcodefile = open(path)
        self.rawgcode = gcodefile.read()

        #Transform gcode to array

    def gcode_to_array(self):
        print "Yahya, there you go"
