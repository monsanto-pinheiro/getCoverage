'''
Created on Oct 23, 2016

@author: mmp
'''

import os, random, pickle, gzip
from Bio import SeqIO

class Util(object):
	'''
	classdocs
	'''
	FORMAT_FASTA = "fasta"
	FORMAT_FASTQ = "fastq"
	EXTENSION_ZIP = ".gz"
	TEMP_DIRECTORY = "/tmp"
	COVERAGE_TEMP_DIRECTORY = "getCoverage"
	
	def __init__(self):
		'''
		Constructor
		'''
		pass

	def get_temp_file(self, file_name, sz_type):
		main_path = os.path.join(self.TEMP_DIRECTORY, self.COUNT_DNA_TEMP_DIRECTORY)
		if (not os.path.exists(main_path)): os.makedirs(main_path)
		while 1:
			return_file = os.path.join(main_path, "count_dna_" + file_name + "_" + str(random.randrange(100000, 999999, 10)) + "_file" + sz_type)
			if (not os.path.exists(return_file)): return return_file
		
			
	def remove_temp_file(self, sz_file_name):
		if os.path.exists(sz_file_name) and len(sz_file_name) > 0 and sz_file_name.find(self.TEMP_DIRECTORY) == 0:
			cmd = "rm " + sz_file_name
			os.system(cmd)

	def copy_file(self, path_origin, path_destination):
		if os.path.exists(path_origin):
			cmd = "cp " + path_origin + " " + path_destination
			os.system(cmd)

	def write_class(self, sz_file_name, class_to_write, b_zip):
		if (b_zip): output = gzip.open(sz_file_name + self.EXTENSION_ZIP, 'wb')
		else: output = open(sz_file_name, 'wb')
		### write a file...
		pickle.dump(class_to_write, output)
		output.close()


	def read_class(self, sz_file_name, sz_old_class_name = "", sz_new_class_name = ""):
		b_zip = False
		if (not os.path.exists(sz_file_name)):
			## try the gzip file
			if (os.path.exists(sz_file_name + self.EXTENSION_ZIP)): 
				b_zip = True
				sz_file_name = sz_file_name + self.EXTENSION_ZIP
			else: raise Exception("Error: file ' " + sz_file_name + "' does not exist to read the class")
		
		if (b_zip): output = gzip.open(sz_file_name, 'rb')
		else: output = open(sz_file_name, 'rb')
		class_to_return = pickle.load(output)
		output.close()
		if (b_zip): os.unlink(sz_file_name)
		return class_to_return

	def is_integer(self, n_value):
		try:
			int(n_value)
			return True
		except ValueError: 
			return False


	def is_float(self, n_value):
		try:
			float(n_value)
			return True
		except ValueError: 
			return False

	def is_gzip(self, file_name): return True if (file_name.rfind(".gz") == len(file_name) - 3) else False
	
	def get_type_file(self, file_name):
		"""
		return 'fasta' or 'fastq' 
		raise exception if can't detecte
		"""
		if (self.is_gzip(file_name)): handle = gzip.open(file_name)
		else: handle = open(file_name)
		for record in SeqIO.parse(handle, self.FORMAT_FASTQ):
			handle.close() 
			return self.FORMAT_FASTQ
		handle.close()
		
		if (self.is_gzip(file_name)): handle = gzip.open(file_name)
		else: handle = open(file_name)
		for record in SeqIO.parse(handle, self.FORMAT_FASTA):
			handle.close() 
			return self.FORMAT_FASTA
		handle.close()
		
		raise Exception("Can't detect file format for the file '" + file_name + "'")
	
	
	def __get_temp_file__(self, file_name, index_file_to_process, sz_type):
		main_path = os.path.join(self.TEMP_DIRECTORY, self.COVERAGE_TEMP_DIRECTORY)
		if (not os.path.exists(main_path)): os.makedirs(main_path)
		while 1:
			return_file = os.path.join(main_path, "seq_dna_" + str(index_file_to_process) + "_" + str(random.randrange(10000, 99999, 10)) + "_file." + sz_type)
			if (not os.path.exists(return_file)): return return_file

