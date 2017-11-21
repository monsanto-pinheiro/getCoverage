'''
Created on Sep 11, 2017

@author: mmp
'''
import unittest, sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from getCoverage import GetCoverage

class Test(unittest.TestCase):

    def testFiles(self):
        
        b_debug = False
        input_file = "files/files_test_1/*.gz"
        output_file = "dontcare"
        
        get_coverage = GetCoverage(b_debug)
        
        get_coverage.test_input_files(os.path.join(os.getcwd(), input_file))
        get_coverage.get_vect_files_processed()
        self.assertTrue(len(get_coverage.get_vect_files_processed()) == 2)
        self.assertTrue(get_coverage.get_vect_files_processed()[0].index("files/files_test_1/test2.gz") != -1)
        self.assertTrue(get_coverage.get_vect_files_processed()[1].index("files/files_test_1/test1.gz") != -1)


    def testReference(self):
        b_debug = False
        reference_file = "files/files_2/reference_zeros.fasta"
        get_coverage = GetCoverage(b_debug)
        get_coverage.read_reference_fasta(reference_file)
        
        self.assertTrue(get_coverage.get_dict_reference().has_key("1"))
        self.assertTrue(get_coverage.get_dict_reference().has_key("2"))
        self.assertFalse(get_coverage.get_dict_reference().has_key("3"))
        self.assertEquals(20, get_coverage.get_dict_reference()["1"])
        self.assertEquals(20, get_coverage.get_dict_reference()["2"])
        
    def testReferenceGz(self):
        b_debug = False
        reference_file = "files/files_2/reference_zeros.fasta.gz"
        get_coverage = GetCoverage(b_debug)
        get_coverage.read_reference_fasta(reference_file)
        
        self.assertTrue(get_coverage.get_dict_reference().has_key("1"))
        self.assertTrue(get_coverage.get_dict_reference().has_key("2"))
        self.assertFalse(get_coverage.get_dict_reference().has_key("3"))
        self.assertEquals(10, get_coverage.get_dict_reference()["1"])
        self.assertEquals(10, get_coverage.get_dict_reference()["2"])
        
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()