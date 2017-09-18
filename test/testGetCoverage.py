'''
Created on Sep 11, 2017

@author: mmp
'''
import unittest, sys, os

sys.path.append('/home/mmp/workspaceGit/getCoverage')
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
        self.assertEqual(get_coverage.get_vect_files_processed()[0], "/home/mmp/workspaceGit/getCoverage/test/files/files_test_1/test2.gz")
        self.assertEqual(get_coverage.get_vect_files_processed()[1], "/home/mmp/workspaceGit/getCoverage/test/files/files_test_1/test1.gz")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()