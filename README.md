
# Get Coverage

Produces the coverage of different samples that lies in a specific directory, by yielding the following data:
  - mean depth of coverage per locus, 
  - % of locus size covered by at least 1-fold
  - % of locus size covered by at least 10-fold.

The input files must be in 'yyyy.depth.gz' or 'yyyy.depth' format.

Only works in python2.x

$ python getCoverage.py -h

Example of a depth file (chromosome position coverage):

	1	1	0
	1	2	0
	1	3	0
	1	4	0
	1	5	0
	1	6	0
	1	7	0


Example of a directory to process data:

	/home/xpto/depth_my_project/
						 |- depth
						 		|- sample_1.depth.gz
						 		|- sample_2.depth.gz
						 		|- sample_3.depth.gz
						 		|- another_sample_3.depth.gz
						 |- reference
						 		|- ref_h3.fasta
	$ cd /home/xpto/depth_my_project
	$ python <installed path>/getCoverage.py -i 'depth/*.depth.gz' -r reference/ref_h3.fasta -o out_result.csv
	$ python <installed path>/getCoverage.py -i 'depth/*.depth.gz' -r reference/ref_h3.fasta -o out_result.csv -c 0,9,15   

	Only works in python2.x