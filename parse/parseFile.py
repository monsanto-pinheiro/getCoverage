'''
Created on Sep 11, 2017

@author: mmp
'''
import gzip
from parse.dataFile import DataFile

class ParseFile(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def is_gzip(self, file_name): return True if (file_name.rfind(".gz") == len(file_name) - 3) else False
    
    def parse_file(self, file_name):
        
        data_file = DataFile(file_name)
        if (self.is_gzip(file_name)): handle = gzip.open(file_name)
        else: handle = open(file_name)
        for line in handle:
            sz_temp = line.strip().lower()
            if (len(sz_temp) == 0 or sz_temp[0] == '#'): continue
            data_file.add_data(line)
        handle.close()
        return data_file