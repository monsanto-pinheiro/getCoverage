'''
Created on Sep 11, 2017

@author: mmp
'''
import unittest, sys, os, gzip
from parse.parseFile import ParseFile
from getCoverage import GetCoverage

class Test(unittest.TestCase):

    def testFile(self):
         
        b_debug = False
        input_file = "files/EVA001_S66.depth"
        reference_file = "files/ref_H3.fasta"
        
        get_coverage = GetCoverage(b_debug)
        parse_file = ParseFile()
        data_file = parse_file.parse_file(os.path.join(os.getcwd(), input_file))
        get_coverage.read_reference_fasta(reference_file)
               
        self.assertEqual(len(data_file.get_vect_chromosomes()), 8)
        self.assertEqual(data_file.get_vect_chromosomes()[0], "1")
        self.assertEqual(data_file.get_vect_chromosomes()[-1], "8")
        self.assertEqual(get_coverage.get_dict_reference()["1"], 2280)
        self.assertEqual(get_coverage.get_dict_reference()["8"], 838)
        self.assertEqual("%.2f" % data_file.get_coverage(data_file.get_vect_chromosomes()[0], get_coverage.get_dict_reference()["1"]), "7.78")
        self.assertEqual("%.2f" % data_file.get_coverage(data_file.get_vect_chromosomes()[-1], get_coverage.get_dict_reference()["8"]), "33.57")
        self.assertEqual("%.2f" % data_file.get_ratio_more_than(data_file.get_vect_chromosomes()[0], get_coverage.get_dict_reference()["1"], 9), "0.32")
        self.assertEqual("%.2f" % data_file.get_ratio_more_than(data_file.get_vect_chromosomes()[-1], get_coverage.get_dict_reference()["8"], 9), "0.96")
        self.assertEqual("%.2f" % data_file.get_ratio_more_than(data_file.get_vect_chromosomes()[0], get_coverage.get_dict_reference()["1"], 1), "0.98")
        self.assertEqual("%.2f" % data_file.get_ratio_more_than(data_file.get_vect_chromosomes()[-1], get_coverage.get_dict_reference()["8"], 1), "1.00")
        self.assertEqual(data_file.get_file_name(), "EVA001_S66")
         
    def testFile_1(self):
        b_debug = False
        input_file = "files/EVA003_S91.depth.gz"
        reference_file = "files/ref_H3.fasta"
         
        get_coverage = GetCoverage(b_debug)
        parse_file = ParseFile()
        data_file = parse_file.parse_file(os.path.join(os.getcwd(), input_file))
        get_coverage.read_reference_fasta(reference_file)
                
        self.assertEqual(len(data_file.get_vect_chromosomes()), 8)
        self.assertEqual(data_file.get_vect_chromosomes()[0], "1")
        self.assertEqual(data_file.get_vect_chromosomes()[-1], "8")
        self.assertEqual(get_coverage.get_dict_reference()["1"], 2280)
        self.assertEqual(get_coverage.get_dict_reference()["8"], 838)
        self.assertEqual("%.2f" % data_file.get_coverage(data_file.get_vect_chromosomes()[0], get_coverage.get_dict_reference()["1"]), "905.41")
        self.assertEqual("%.2f" % data_file.get_coverage(data_file.get_vect_chromosomes()[-1], get_coverage.get_dict_reference()["8"]), "1752.53")
        self.assertEqual("%.2f" % data_file.get_ratio_more_than(data_file.get_vect_chromosomes()[0], get_coverage.get_dict_reference()["1"], 9), "1.00")
        self.assertEqual("%.2f" % data_file.get_ratio_more_than(data_file.get_vect_chromosomes()[-1], get_coverage.get_dict_reference()["8"], 9), "1.00")
        self.assertEqual("%.2f" % data_file.get_ratio_more_than(data_file.get_vect_chromosomes()[0], get_coverage.get_dict_reference()["1"], 1), "1.00")
        self.assertEqual("%.2f" % data_file.get_ratio_more_than(data_file.get_vect_chromosomes()[-1], get_coverage.get_dict_reference()["8"], 1), "1.00")
        self.assertEqual(data_file.get_file_name(), "EVA003_S91")
 
    def testFile_2(self):
        b_debug = False
        input_file = "files/EVA003_S91.depth"
        reference_file = "files/ref_H3.fasta"

        get_coverage = GetCoverage(b_debug)
        parse_file = ParseFile()
        data_file = parse_file.parse_file(os.path.join(os.getcwd(), input_file))
        get_coverage.read_reference_fasta(reference_file)
               
        self.assertEqual(len(data_file.get_vect_chromosomes()), 8)
        self.assertEqual(data_file.get_vect_chromosomes()[0], "1")
        self.assertEqual(data_file.get_vect_chromosomes()[-1], "8")
        self.assertEqual(get_coverage.get_dict_reference()["1"], 2280)
        self.assertEqual(get_coverage.get_dict_reference()["8"], 838)
        self.assertEqual("%.2f" % data_file.get_coverage(data_file.get_vect_chromosomes()[0], get_coverage.get_dict_reference()["1"]), "905.41")
        self.assertEqual("%.2f" % data_file.get_coverage(data_file.get_vect_chromosomes()[-1], get_coverage.get_dict_reference()["8"]), "1752.53")
        self.assertEqual("%.2f" % data_file.get_ratio_more_than(data_file.get_vect_chromosomes()[0], get_coverage.get_dict_reference()["1"], 9), "1.00")
        self.assertEqual("%.2f" % data_file.get_ratio_more_than(data_file.get_vect_chromosomes()[-1], get_coverage.get_dict_reference()["8"], 9), "1.00")
        self.assertEqual("%.2f" % data_file.get_ratio_more_than(data_file.get_vect_chromosomes()[0], get_coverage.get_dict_reference()["1"], 1), "1.00")
        self.assertEqual("%.2f" % data_file.get_ratio_more_than(data_file.get_vect_chromosomes()[-1], get_coverage.get_dict_reference()["8"], 1), "1.00")
        self.assertEqual(data_file.get_file_name(), "EVA003_S91")

    def testFile_with_zeros(self):
        b_debug = False
        input_file = "files/files_2/EVA001_S67_zeros.depth"
        reference_file = "files/files_2/reference_zeros.fasta"
        
        get_coverage = GetCoverage(b_debug)
        parse_file = ParseFile()
        data_file = parse_file.parse_file(os.path.join(os.getcwd(), input_file))
        get_coverage.read_reference_fasta(reference_file)
       
        self.assertEqual(len(data_file.get_vect_chromosomes()), 2)
        self.assertEqual(data_file.get_vect_chromosomes()[0], "1")
        self.assertEqual(data_file.get_vect_chromosomes()[-1], "2")
        self.assertEqual(get_coverage.get_dict_reference()["1"], 20)
        self.assertEqual(get_coverage.get_dict_reference()["2"], 20)
        self.assertEqual("%.2f" % data_file.get_coverage("1", get_coverage.get_dict_reference()["1"]), "5.00")
        self.assertEqual("%.2f" % data_file.get_coverage("2", get_coverage.get_dict_reference()["2"]), "5.00")
        self.assertEqual("%.2f" % data_file.get_ratio_more_than("1", get_coverage.get_dict_reference()["1"], 9), "0.00")
        self.assertEqual("%.2f" % data_file.get_ratio_more_than("2", get_coverage.get_dict_reference()["2"], 9), "0.00")
        self.assertEqual("%.2f" % data_file.get_ratio_more_than("1", get_coverage.get_dict_reference()["1"], 1), "1.00")
        self.assertEqual("%.2f" % data_file.get_ratio_more_than("2", get_coverage.get_dict_reference()["2"], 1), "1.00")

    def testFile_with_zeros(self):
        b_debug = False
        input_file = "files/files_2/EVA001_S67_zeros_2.depth"
        reference_file = "files/files_2/reference_zeros.fasta"
        
        get_coverage = GetCoverage(b_debug)
        parse_file = ParseFile()
        data_file = parse_file.parse_file(os.path.join(os.getcwd(), input_file))
        get_coverage.read_reference_fasta(reference_file)
       
        self.assertEqual(len(data_file.get_vect_chromosomes()), 2)
        self.assertEqual(data_file.get_vect_chromosomes()[0], "1")
        self.assertEqual(data_file.get_vect_chromosomes()[-1], "2")
        self.assertEqual(get_coverage.get_dict_reference()["1"], 20)
        self.assertEqual(get_coverage.get_dict_reference()["2"], 20)
        self.assertEqual("%.2f" % data_file.get_coverage("1", get_coverage.get_dict_reference()["1"]), "4.50")
        self.assertEqual("%.2f" % data_file.get_coverage("2", get_coverage.get_dict_reference()["2"]), "5.00")
        self.assertEqual("%.2f" % data_file.get_ratio_more_than("1", get_coverage.get_dict_reference()["1"], 9), "0.00")
        self.assertEqual("%.2f" % data_file.get_ratio_more_than("2", get_coverage.get_dict_reference()["2"], 9), "0.00")
        self.assertEqual("%.2f" % data_file.get_ratio_more_than("1", get_coverage.get_dict_reference()["1"], 1), "0.90")
        self.assertEqual("%.2f" % data_file.get_ratio_more_than("2", get_coverage.get_dict_reference()["2"], 1), "1.00")
        
    def testFile_with_zeros_fault(self):
        b_debug = False
        input_file = "files/files_2/EVA001_S67_zeros.depth"
        reference_file = "files/files_2/reference_zeros_fault.fasta"
        
        get_coverage = GetCoverage(b_debug)
        parse_file = ParseFile()
        data_file = parse_file.parse_file(os.path.join(os.getcwd(), input_file))
        get_coverage.read_reference_fasta(reference_file)
       
        self.assertEqual(len(data_file.get_vect_chromosomes()), 2)
        self.assertEqual(data_file.get_vect_chromosomes()[0], "1")
        self.assertEqual(data_file.get_vect_chromosomes()[-1], "2")
        self.assertEqual(get_coverage.get_dict_reference()["1"], 10)
        self.assertEqual(get_coverage.get_dict_reference()["2"], 10)
        try:
            self.assertEqual("%.2f" % data_file.get_coverage("1", get_coverage.get_dict_reference()["1"]), "10.00")
            self.fail("Must raise exception")
        except Exception as e:
            self.assertEqual("Chromosome '1' has different sizes. Coverage: 20; Reference: 10", e.message)
            
        try:
            self.assertEqual("%.2f" % data_file.get_ratio_more_than("1", get_coverage.get_dict_reference()["1"], 4), "2.00")
            self.fail("Must raise exception")
        except Exception as e:
            self.assertEqual("Chromosome '1' has different sizes. Coverage: 20; Reference: 10", e.message)
        
            
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()