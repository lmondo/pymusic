# -*- coding:utf-8 -*-

import numpy as np


class Scale:
    keys = {1: 'A', 2: 'A#', 3: 'B', 4: 'C', 5: 'C#', 6: 'D', 7: 'D#', 8: 'E', 9: 'F', 10: 'F#', 11: 'G', 12: 'G#'}
    nums = {'A': 1, 'A#': 2, 'B': 3, 'C': 4, 'C#': 5, 'D': 6, 'D#': 7, 'E': 8, 'F': 9, 'F#': 10, 'G': 11, 'G#': 12}
    major = [1, 3, 5, 6, 8, 10, 12]
    minor = [1, 3, 4, 6, 8, 9, 11]

    """
        Music Scale
    """
    def __init__(self, scaleKey='C', scaleName='major'):
        self.scaleKey = scaleKey.upper()
        self.scaleName = scaleName.lower()
        self.scl = self.makeScl()


    def makeScl(self):
        keyNum =Scale.nums[self.scaleKey] - 1

        if self.scaleName == 'major':
            scl = Scale.major
        elif self.scaleName == 'minor':
            scl = Scale.minor
        else:
            print('no exist such a scale {}'.format(self.scaleName))
            scl = Scale.major

        return [Scale.keys[(num-1+keyNum)%12 + 1] for num in scl]
        
    def show(self):
        print(self.scl)

    
    def ck(self, scaleKey):
        self.scaleKey = scaleKey.upper()
        self.scl = self.makeScl()
    
    def cs(self, scaleName):
        self.scaleName = scaleName
        self.scl = self.makeScl()



