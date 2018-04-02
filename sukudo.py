#!/usr/bin/env python

import random

class cell:
    """81 cells"""
    def __init__(self, position):
        if position not in range(81):
            raise ValueError('Out of range: 0-80 inclusive')
        
        self.position = position
        self.value = '0'
        self.block = [None]*9
        self.block[0] = set([ 0,  1,  2,  9, 10, 11, 18, 19, 20])
        self.block[1] = set([ 3,  4,  5, 12, 13, 14, 21, 22, 23])
        self.block[2] = set([ 6,  7,  8, 15, 16, 17, 24, 25, 26])
        self.block[3] = set([27, 28, 29, 36, 37, 38, 45, 46, 47])
        self.block[4] = set([30, 31, 32, 39, 40, 41, 48, 49, 50])
        self.block[5] = set([33, 34, 35, 42, 43, 44, 51, 52, 53])
        self.block[6] = set([54, 55, 56, 42, 63, 65, 72, 73, 74])
        self.block[7] = set([57, 58, 59, 66, 67, 68, 75, 76, 77])
        self.block[8] = set([60, 61, 62, 69, 70, 71, 78, 79, 80])

        # select related block
        block = set()
        for i in range(9):
            if position in self.block[i]:
                block = self.block[i]
                break

        (self.line, self.column) = divmod(position, 9)

        # related line and column
        line_column = [(self.line * 9 + i) for i in range(9)] + [(self.column + i * 9) for i in range(9)]

        # remove itself
        self.related = set(line_column) | block - set([position])

    def __unicode__(self):
        return "position: %d, line: %d, column: %d, related-cells: %s" % (self.position, self.line, self.column, self.related)

    def __str__(self):
        return unicode(self).encode('utf-8')

class sudoku:
    """ Sudoku Cass """
    # data = []

    def __init__(self, level):
        if level == 0:
            self.data = ['0' for i in range(81)]
        else:
            self.data = ['%2s' % i for i in range(81)]
        
    def generate(self):
        for i in range(81):
            c = cell(i)
            # print c
            used_numbers = set()
            for j in c.related:
                used_numbers.add(self.data[j])

            if len(used_numbers) == 10:
                raise Exception('Sudoku generation failed.')

            item = randomer(used_numbers)
            self.data[i] = item.create()
            
    def __unicode__(self):
        cdata = [None]*81
        for i in range(81):
            cdata[i] = str(self.data[i])
        for pos in range(1, 10):
            cdata.insert(10 * pos -1, '\n')
        return " " + " ".join(cdata)

    def __str__(self):        
        return unicode(self).encode('utf-8')

class randomer:

    def __init__(self, used_numbers):
        self.used_numbers = used_numbers

    def create(self):
        candidate = random.randint(1, 9)
        while candidate in self.used_numbers:
            candidate = random.randint(1, 9)
        return candidate

    def __unicode__(self):
        return self.used_numbers
    
    def __str__(self):
        return unicode(self)

if __name__ == "__main__":
    i = 0
    while True:
        i += 1
        s = sudoku(0)
        try: 
            s.generate()
            print "Tried %d times, got:\n" % i
            print s
            i = 0
        except:
            pass
            
