#!/usr/bin/env python2.7


import os, sys, glob, gzip
from optparse import OptionParser
from parse.parseFile import ParseFile
from Bio import SeqIO
from constants.utils import Util

class GetCoverage(object):

	utils = Util()
	
	def __init__(self, b_degub):
		self.vect_files_processed = []
		self.fasta_handle = None
		self.b_degub = b_degub
		self.reference_dict = {}
	
	def get_dict_reference(self): return self.reference_dict
	
	def test_input_files(self, input_path):
		"""
			test if input_file is directory or file and read all files in the directory
		"""	
		
		print "Collecting files in: " + input_path
		if (os.path.isfile(input_path)):
			if (os.path.exists(input_path)): self.vect_files_processed.append(input_path)
		else:
			self.vect_files_processed = glob.glob(input_path)
		
		
	def read_reference_fasta(self, reference_file):
		"""
		test if the reference_file and ge the handle
		"""
		if (not os.path.exists(reference_file)): raise Exception("Can't locate the reference file: '" + reference_file + "'")

		### set temp file name
		temp_file_name = reference_file
		
		## create temp file
		b_temp_file = False
		if self.utils.is_gzip(reference_file):
			b_temp_file = True
			temp_file_name = self.utils.__get_temp_file__(reference_file, 10, self.utils.get_type_file(reference_file))
			cmd = "gzip -cd " + reference_file + " > " + temp_file_name
			sz_out = os.system(cmd)
			
		for rec in SeqIO.parse(temp_file_name, 'fasta'):
			self.reference_dict[rec.id] = len(str(rec.seq))
		
		###
		if (b_temp_file): os.remove(temp_file_name)

			
		
	def get_vect_files_processed(self): return self.vect_files_processed
	
	
	###
	def process_files(self, input_file, reference, output_file):
		
		## read config file
		self.test_input_files(input_file)
		
		## test fasta reference
		self.read_reference_fasta(reference)
		
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
		handle.write("\nChromosome\n" + self.__get_chromosome__(vect_data) + "Length")
		for chromosome in vect_data[0].get_vect_chromosomes():
			if (not self.reference_dict.has_key(chromosome)): raise Exception("Can't locate the chromosome '" + chromosome + "' in reference file")
			handle.write("\t%d" % (self.reference_dict[chromosome]))
		handle.write("\n")
			
		handle.write("\nCoverage\n" + self.__get_chromosome__(vect_data))
		for data_from_file in vect_data:
			handle.write(data_from_file.get_file_name())
			for chromosome in vect_data[0].get_vect_chromosomes():
				if (not self.reference_dict.has_key(chromosome)): raise Exception("Can't locate the chromosome '" + chromosome + "' in reference file")
				handle.write("\t%.2f" % (data_from_file.get_coverage(chromosome, self.reference_dict[chromosome])))
			handle.write("\n")
		
		handle.write("\nRatio >0\n" + self.__get_chromosome__(vect_data))
		for data_from_file in vect_data:
			handle.write(data_from_file.get_file_name())
			for chromosome in vect_data[0].get_vect_chromosomes():
				handle.write("\t%.1f" % (data_from_file.get_ratio_more_than(chromosome, self.reference_dict[chromosome], 0) * 100))
			handle.write("\n")

		handle.write("\nRatio >9\n" + self.__get_chromosome__(vect_data))
		for data_from_file in vect_data:
			handle.write(data_from_file.get_file_name())
			for chromosome in vect_data[0].get_vect_chromosomes():
				handle.write("\t%.1f" % (data_from_file.get_ratio_more_than(chromosome, self.reference_dict[chromosome], 9) * 100))
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
	V0.1 release 30/09/2017
		Add - 	need the reference file
				check if all chromosomes that are in the coverage are the ones that are in the reference.
				get the size of the chromosomes from the reference 
	V0.1 release 12/09/2017
		Add - coverage average base on the files <chromosome> <position> <deep coverage>:
	"""

	b_debug = False
	if (b_debug):
		input_file = "../test/files/*.depth"
		output_file = "/tmp/out_get_coverage.xls"
		reference = "../test/files/refence.fasta"
	else:
		parser = OptionParser(usage="%prog [-h] [-i] [-r] [-o]", version="%prog 0.1", add_help_option=False)
		parser.add_option("-i", "--input", type="string", dest="input", help="Input file or path with coverage files. Can be zipped.", metavar="IN_FILE")
		parser.add_option("-r", "--reference", type="string", dest="reference", help="Reference file to get the length of the chromosomes to check his name.", metavar="REF_FILE")
		parser.add_option("-o", "--output", type="string", dest="output", help="Output file name", metavar="OUT_FILE")
		parser.add_option('-h', '--help', dest='help', action='store_true', help='show this help message and exit')
	
		(options, args) = parser.parse_args()
		
		if (options.help):
			parser.print_help()
			print "Create an output file with several averages about the coverage."
			print "example: getCoverage -i /usr/local/zpto/*.gz -r reference.fasta -o resultsOut.xls"
			print 
			print "\tThe input files must be in this format '<chromosome> <position> <deep coverage>'"
			sys.exit(0)
			
		if (len(args) != 0):
			parser.error("incorrect number of arguments, no of arguments: " + str(len(args)))
	
		if not options.input:   # 
			parser.error('Name of the input files/path is not specified')
		
		if not options.reference:   # 
			parser.error('Name of the reference file not specified')

		if not options.output:   # 
			parser.error('Output file is not specified')

	get_coverage = GetCoverage(b_debug)
	if (b_debug): get_coverage.process_files(input_file, output_file, output_file)
	else: get_coverage.process_files(options.input, options.reference, options.output)




