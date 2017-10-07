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
            for j in range(point.Y - 10,point.Y + 10):
                content = self.trouverContent(i, j, mapparam)
                casesAccessibles = self.trouverCasesAccessibles(i, j, mapparam)
                self.cases_.append(Cases(cases[i], cases[j], content, casesAccessibles))



    def trouverContent(self, x, y, map):
        for k in range (0, map.length):
            if map[k]['X'] == x and map[k]['Y'] == y:
                return map[k]['Content']

    def trouverCasesAccessibles(self, x, y, map):
        cases = []
        for n in range(0, map.length):
            if (map[k]['X'] == x + 1 and map[k]['Y'] == y) or (map[k]['X'] == x and map[k]['Y'] == y - 1) or (map[k]['X'] == x - 1 and map[k]['Y'] == y) or (map[k]['X'] == x and map[k]['Y'] == y + 1) :
                cases.append(map[k])

        return cases



