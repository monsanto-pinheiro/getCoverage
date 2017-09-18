'''
Created on Sep 11, 2017

@author: mmp
'''
import unittest, sys, os, gzip
from parse.parseFile import ParseFile

class Test(unittest.TestCase):

    def testFile(self):
        
        b_debug = False
        input_file = "files/EVA001_S66.depth"
        
        parse_file = ParseFile()
        data_file = parse_file.parse_file(os.path.join(os.getcwd(), input_file))
       
        self.assertEqual(len(data_file.get_vect_chromosomes()), 8)
        self.assertEqual(data_file.get_vect_chromosomes()[0], "1")
        self.assertEqual(data_file.get_vect_chromosomes()[-1], "8")
        self.assertEqual(data_file.get_length_chromosome(data_file.get_vect_chromosomes()[0]), 2280)
        self.assertEqual(data_file.get_length_chromosome(data_file.get_vect_chromosomes()[-1]), 838)
        self.assertEqual(data_file.get_length_chromosome("xpto"), 0)
        self.assertEqual("%.2f" % data_file.get_coverage(data_file.get_vect_chromosomes()[0]), "7.78")
        self.assertEqual("%.2f" % data_file.get_coverage(data_file.get_vect_chromosomes()[-1]), "33.57")
        self.assertEqual("%.2f" % data_file.get_ratio_more_than(data_file.get_vect_chromosomes()[0], 9), "0.32")
        self.assertEqual("%.2f" % data_file.get_ratio_more_than(data_file.get_vect_chromosomes()[-1], 9), "0.96")
        self.assertEqual("%.2f" % data_file.get_ratio_more_than(data_file.get_vect_chromosomes()[0], 1), "0.98")
        self.assertEqual("%.2f" % data_file.get_ratio_more_than(data_file.get_vect_chromosomes()[-1], 1), "1.00")
        self.assertEqual(data_file.get_file_name(), "EVA001_S66")
        
    def testFile_1(self):
        b_debug = False
        input_file = "files/EVA003_S91.depth.gz"
        
        parse_file = ParseFile()
        data_file = parse_file.parse_file(os.path.join(os.getcwd(), input_file))
       
        self.assertEqual(len(data_file.get_vect_chromosomes()), 8)
        self.assertEqual(data_file.get_vect_chromosomes()[0], "1")
        self.assertEqual(data_file.get_vect_chromosomes()[-1], "8")
        self.assertEqual(data_file.get_length_chromosome(data_file.get_vect_chromosomes()[0]), 2280)
        self.assertEqual(data_file.get_length_chromosome(data_file.get_vect_chromosomes()[-1]), 838)
        self.assertEqual(data_file.get_length_chromosome("xpto"), 0)
        self.assertEqual("%.2f" % data_file.get_coverage(data_file.get_vect_chromosomes()[0]), "905.41")
        self.assertEqual("%.2f" % data_file.get_coverage(data_file.get_vect_chromosomes()[-1]), "1752.53")
        self.assertEqual("%.2f" % data_file.get_ratio_more_than(data_file.get_vect_chromosomes()[0], 9), "1.00")
        self.assertEqual("%.2f" % data_file.get_ratio_more_than(data_file.get_vect_chromosomes()[-1], 9), "1.00")
        self.assertEqual("%.2f" % data_file.get_ratio_more_than(data_file.get_vect_chromosomes()[0], 1), "1.00")
        self.assertEqual("%.2f" % data_file.get_ratio_more_than(data_file.get_vect_chromosomes()[-1], 1), "1.00")
        self.assertEqual(data_file.get_file_name(), "EVA003_S91")

    def testFile_2(self):
        b_debug = False
        input_file = "files/EVA003_S91.depth"
        
        parse_file = ParseFile()
        data_file = parse_file.parse_file(os.path.join(os.getcwd(), input_file))
       
        self.assertEqual(len(data_file.get_vect_chromosomes()), 8)
        self.assertEqual(data_file.get_vect_chromosomes()[0], "1")
        self.assertEqual(data_file.get_vect_chromosomes()[-1], "8")
        self.assertEqual(data_file.get_length_chromosome(data_file.get_vect_chromosomes()[0]), 2280)
        self.assertEqual(data_file.get_length_chromosome(data_file.get_vect_chromosomes()[-1]), 838)
        self.assertEqual(data_file.get_length_chromosome("xpto"), 0)
        self.assertEqual("%.2f" % data_file.get_coverage(data_file.get_vect_chromosomes()[0]), "905.41")
        self.assertEqual("%.2f" % data_file.get_coverage(data_file.get_vect_chromosomes()[-1]), "1752.53")
        self.assertEqual("%.2f" % data_file.get_ratio_more_than(data_file.get_vect_chromosomes()[0], 9), "1.00")
        self.assertEqual("%.2f" % data_file.get_ratio_more_than(data_file.get_vect_chromosomes()[-1], 9), "1.00")
        self.assertEqual("%.2f" % data_file.get_ratio_more_than(data_file.get_vect_chromosomes()[0], 1), "1.00")
        self.assertEqual("%.2f" % data_file.get_ratio_more_than(data_file.get_vect_chromosomes()[-1], 1), "1.00")
        self.assertEqual(data_file.get_file_name(), "EVA003_S91")
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()