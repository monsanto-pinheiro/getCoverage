'''
Created on Oct 23, 2016

@author: mmp
'''

import os, random, pickle, gzip

class Util(object):
	'''
	classdocs
	'''
	EXTENSION_ZIP = ".gz"
	TEMP_DIRECTORY = "/tmp"
	COUNT_DNA_TEMP_DIRECTORY = "countDNABox"
	
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
	
	
