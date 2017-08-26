'''
This piece of code would read files given and store the words\
in dictionaries along with their frequency and compare this with\
other file's dictionary to give cosine similarity.
'''


'''
To read files to create lists. Copy them in the current directory\
and remove any other .txt files from current directory.
'''

import math
import glob
import re
import os
import logging

import os
pat = os.getcwd()
pat = pat + '\word.txt'

lst = []
dct_lst = {}
filename_lst = []
path = os.getcwd()

for filename in glob.glob(os.path.join(path, '*.txt')):
	if filename != pat:
		f = open(filename,'r')
		l = f.read()
		f.close()

		'''
		Lower casing and removing special characters. Assuming words to be\
		with alphabets, under_score and numeric characters only.
		'''

		l = l.lower()
		l = re.sub(r'[^a-z0-9_ \n]', '_', l)
		l = l.split()

		'''
		Storing in dct_lst with file name as key an value a dict with words\
		 and thier frequency. Also storing filenames in a list.
		 '''

		file_name = filename.split('\\')
		path_ = path.split('\\')
		file = ''
		for i in file_name:
			if i not in path_:
				file = file + i

		filename_lst.append(file)
		dct_lst[file]  = {}

		for i in l:
			if i not in dct_lst[file]:
				dct_lst[file][i] = l.count(i)

class Bag:

	def similarity(dct1, dct2):

		'''
		fuction that takes two dcts of words and thier frequencies and \
		return their cosine similarity.
		'''

		sum_similarity = 0
		sum_cosine = 0
		product_cosine = 1
		for i in dct1:
			if i in dct2:
				sum_similarity = sum_similarity + (dct1[i]*dct2[i])
		for i in dct1:
			sum_cosine = sum_cosine + (dct1[i]**2)
		product_cosine = product_cosine*math.sqrt(sum_cosine)
		sum_cosine = 0
		for i in dct2:
			sum_cosine = sum_cosine + (dct2[i]**2)
		product_cosine = product_cosine*math.sqrt(sum_cosine)
		cos_similarity = sum_similarity/product_cosine
		return (100*cos_similarity)
'''
Comparing each dct of words in loop and printing the similarity percentage.
'''
p = ''
for dct1 in range(0,(len(filename_lst)-1)):
	for dct2 in range((dct1+1),len(filename_lst)):
		try:
			s = ('Simlarity between '+str(filename_lst[dct1])+' and '+\
				str(filename_lst[dct2])+' is: '+str(Bag.similarity\
					(dct_lst[filename_lst[dct1]],dct_lst[filename_lst[dct2]])))
		except ZeroDivisionError:
			s = (str(filename_lst[dct1])+' and '+str(filename_lst[dct2])+\
				' One or both files are empty.')
		p = p + '\n' + s + '\n'


log = "log file.log"
logging.basicConfig(filename=log,level=logging.DEBUG,\
	format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
logging.info('BAG OF WORDS \n' + p)

print(p)