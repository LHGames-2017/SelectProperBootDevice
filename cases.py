#-------------------------------------------------------------------------------
# Name:        cases
# Purpose:
#
# Author:      Valentin
#
# Created:     07/10/2017
# Copyright:   (c) Valentin 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import map


class Cases():
    x_ = 0
    y_ = 0
    content_ = None

    def __init__(self, x, y, content):
        self.x_ = x
        self.y_ = y
        self.content = content
