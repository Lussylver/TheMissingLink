#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml, os


class Deck():

    def __init__(self, input_path):

        if not os.path.exists(input_path):
            print 'Error: Could not find ' + input_path
            sys.exit(1)
        else:
            with open(input_path,'r') as f:
                self.doc = yaml.load(f)
                if not 'gfisnarcode' in self.doc:
                    print 'gfisnarcode tag missing'
                    sys.exit(1)
                else:

                    if not 'speed' in self.doc["gfisnarcode"]:
                        print 'speed tag missing in gfisnarcode' + self.doc
                        sys.exit(1)
                    else:
                        self.speed = self.doc["gfisnarcode"]["speed"]

                    if not 'slicer' in self.doc["gfisnarcode"]:
                        print 'slicer tag missing in gfisnarcode' + self.doc
                        sys.exit(1)
                    else:
                        self.slicer = self.doc["gfisnarcode"]["slicer"]

                    if not 'minTimeStep' in self.doc["gfisnarcode"]:
                        print 'minTimeStep tag missing in gfisnarcode' + self.doc
                        sys.exit(1)
                    else:
                        self.minTimeStep = self.doc["gfisnarcode"]["minTimeStep"]
