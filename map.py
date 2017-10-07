#-------------------------------------------------------------------------------
# Name:        map
# Purpose:
#
# Author:      Valentin
#
# Created:     07/10/2017
# Copyright:   (c) Valentin 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from cases import *
from enum import Enum


class Map():
    cases_ = []

    def __init__(self, point, mapparam):
        for i in range(point.X - 10, point.X + 10):
            for j in range(point.Y - 10, point.Y + 10):
                content = self.trouverContent(i, j, mapparam)
                print()
                self.cases_.append(Cases(i, j, content))



    def trouverContent(self, x, y, map):
        carte = map.replace('{', '[')
        carte = carte.replace('}', ']')
        carte = eval(carte)

        x_origine = carte[0][0][1]
        y_origine = carte[0][0][2]

        i = abs(x_origine - x)
        j = abs(y_origine - y)

        return carte[i][j][0]
