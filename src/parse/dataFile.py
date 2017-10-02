'''
Created on Sep 11, 2017

@author: mmp
'''
from constants.utils import Util
import os


class DataFile(object):
    '''
    classdocs
    '''
    util = Util();

    def __init__(self, file_name):
        '''
        Constructor
        '''
        self.file_name = file_name
        self.vect_chromosomes = []
        self.dict_data = {}
        self.dict_data_coverage = {}
        self.previous_position = -1
        
    def get_vect_chromosomes(self): return self.vect_chromosomes
    def get_dict_data(self): return self.dict_data
    
    def add_data(self, line):
        if (len(line) == 0 or line[0] == '#'): return
        vect_data = line.split()
        if (len(vect_data) != 3): raise Exception("File: " + self.file_name + "\nThis line must have three values '" + line + "'")
        if (not self.util.is_integer(vect_data[1])): raise Exception("File: " + self.file_name + "\nLine: '" + line + "'\nThe locus need to be integer")
        if (not self.util.is_integer(vect_data[2])): raise Exception("File: " + self.file_name + "\nLine: '" + line + "'\nThe coverage need to be integer")
        if (not self.dict_data.has_key(vect_data[0])): 
            self.vect_chromosomes.append(vect_data[0])
            self.dict_data[vect_data[0]] = [[vect_data[1], vect_data[2]]]
            self.previous_position = int(vect_data[1])
        else:
            if (int(vect_data[1]) <= (self.previous_position)): raise Exception("File: " + self.file_name + "\nLine: '" + line + "'\nThe locus need to be greater than the predecessor in the file")
            self.dict_data[vect_data[0]].append([vect_data[1], vect_data[2]])
            self.previous_position = int(vect_data[1])
        
    def get_coverage(self, sz_chromosome, length_chromosome):
        if (self.dict_data_coverage.has_key(sz_chromosome)): return self.dict_data_coverage[sz_chromosome]
        if (length_chromosome == 0): return 0
        if (len(self.dict_data[sz_chromosome]) > length_chromosome): 
            raise Exception("Chromosome '%s' has different sizes. Coverage: %d; Reference: %d" % (sz_chromosome, len(self.dict_data[sz_chromosome]), length_chromosome))
        sum_total = 0
        for data_ in self.dict_data[sz_chromosome]: sum_total += int(data_[1])
        self.dict_data_coverage[sz_chromosome] = sum_total / float(length_chromosome)
        return self.dict_data_coverage[sz_chromosome]
    
    def get_ratio_more_than(self, sz_chromosome, length_chromosome, value):
        if (length_chromosome == 0): return 0
        if (len(self.dict_data[sz_chromosome]) > length_chromosome): 
            raise Exception("Chromosome '%s' has different sizes. Coverage: %d; Reference: %d" % (sz_chromosome, len(self.dict_data[sz_chromosome]), length_chromosome))
        sum_total = 0
        for data_ in self.dict_data[sz_chromosome]: sum_total += (1 if (int(data_[1]) > value) else 0)
        return sum_total / float(length_chromosome)
    
    def get_file_name(self):
        sz_return = os.path.basename(self.file_name)
        if (sz_return.rfind(".gz") == len(sz_return) - 3): sz_return = sz_return[:-3]
        if (sz_return.rfind(".") != -1): sz_return = sz_return[:-1 * (len(sz_return) - sz_return.rfind("."))]
        return sz_return

