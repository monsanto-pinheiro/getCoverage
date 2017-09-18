#!/usr/bin/env python2.7

import os, sys, glob
from optparse import OptionParser
from parse.parseFile import ParseFile

class GetCoverage(object):

	def __init__(self, b_degub):
		self.vect_files_processed = []
		self.b_degub = b_degub

	def test_input_files(self, input_path):
		"""
			test if input_file is directory or file and read all files in the directory
		"""	
		
		print "Collecting files in: " + input_path
		if (os.path.isfile(input_path)):
			if (os.path.exists(input_path)): self.vect_files_processed.append(input_path)
		else:
			self.vect_files_processed = glob.glob(input_path)
		
		
	
	def get_vect_files_processed(self): return self.vect_files_processed
	
	###
	def process_files(self, input_file, output_file):
		
		## read config file
		self.test_input_files(input_file)
		
		parse_file = ParseFile()
		vect_data = []
		for file_to_process in self.vect_files_processed:
			print "processing file: " + file_to_process
			if (not os.path.exists(file_to_process)):
				print "File doesn't exist: " + file_to_process
				continue
			vect_data.append(parse_file.parse_file(file_to_process))

		###
		if (len(vect_data) == 0): sys.exit("There's no data to process")

		handle = open(output_file, "w")
		handle.write("\nCoverage\n" + self.__get_chromosome__(vect_data))
		for data_from_file in vect_data:
			handle.write(data_from_file.get_file_name())
			for chromosome in vect_data[0].get_vect_chromosomes():
				handle.write("\t%.2f" % (data_from_file.get_coverage(chromosome)))
			handle.write("\n")
		
		handle.write("\nRatio >0\n" + self.__get_chromosome__(vect_data))
		for data_from_file in vect_data:
			handle.write(data_from_file.get_file_name())
			for chromosome in vect_data[0].get_vect_chromosomes():
				handle.write("\t%.2f" % (data_from_file.get_ratio_more_than(chromosome, 0)))
			handle.write("\n")

		handle.write("\nRatio >9\n" + self.__get_chromosome__(vect_data))
		for data_from_file in vect_data:
			handle.write(data_from_file.get_file_name())
			for chromosome in vect_data[0].get_vect_chromosomes():
				handle.write("\t%.2f" % (data_from_file.get_ratio_more_than(chromosome, 9)))
			handle.write("\n")
		handle.close()
		print "Output saved in: " + output_file
		print "Finished..."

	def __get_chromosome__(self, vect_data): 
		sz_return = "Name"
		for chromosome in vect_data[0].get_vect_chromosomes(): sz_return += "\t" + chromosome
		return sz_return + "\n"


if __name__ == '__main__':

	"""
	V0.1 release 12/09/2017
		Add - coverage average base on the files <chromosome> <position> <deep coverage>:
	"""

	b_debug = False
	if (b_debug):
		input_file = "../test/files/*.depth"
		output_file = "/tmp/out_get_coverage.xls"
	else:
		parser = OptionParser(usage="%prog [-h] [-i] [-o]", version="%prog 0.1", add_help_option=False)
		parser.add_option("-i", "--input", type="string", dest="input", help="Input file or path with coverage files. Can be zipped.", metavar="IN_FILE")
		parser.add_option("-o", "--output", type="string", dest="output", help="Output file name", metavar="OUT_FILE")
		parser.add_option('-h', '--help', dest='help', action='store_true', help='show this help message and exit')
	
		(options, args) = parser.parse_args()
		
		if (options.help):
			parser.print_help()
			print "Create an output file with several averages about the coverage."
			print "example: getCoverage -i /usr/local/zpto/*.gz -o resultsOut.xls"
			print 
			print "\tThe input files must be in this format '<chromosome> <position> <deep coverage>'"
			sys.exit(0)
			
		if (len(args) != 0):
			parser.error("incorrect number of arguments, no of arguments: " + str(len(args)))
	
		if not options.input:   # 
			parser.error('Name of the file/path is not specified')

		if not options.output:   # 
			parser.error('Output file is not specified')

	get_coverage = GetCoverage(b_debug)
	if (b_debug): get_coverage.process_files(input_file, output_file)
	else: get_coverage.process_files(options.input, options.output)




