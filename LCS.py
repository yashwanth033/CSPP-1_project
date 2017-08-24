'''
To read files to create lists. Copy them in the current directory\
and remove any other .txt files from current directory.
'''

import math
import glob
import re
import os
import logging

lst = []
dct_lst = {}
filename_lst = []
path = os.getcwd()

for filename in glob.glob(os.path.join(path, '*.txt')):
	f = open(filename,'r')
	l = f.read()
	f.close()

	'''
	Lower casing and removing special characters. Assuming words to be\
	with alphabets, under_score and numeric characters only.
	'''

	l = l.lower()
	l = re.sub(r'[^a-z0-9_ \n]', '', l).split()

	'''
	Storing in dct_lst with file name as key an value a list of strings of words.\
	 Also storing filenames in a list.
	'''

	file_name = filename.split('\\')
	path_ = path.split('\\')
	file = ''
	for i in file_name:
		if i not in path_:
			file = file + i

	filename_lst.append(file)
	dct_lst[file] = l

'''
Longest common substring(LCS) is to be calulated between to dcts.
'''

def LCS(dct1, dct2):
	'''
	This LCS function takes two lists of strings and and compare those to give \
	the largest common substring(LCS) percentage.
	'''
	z = 0
	i = 0
	c = 0
	for i in range(0,len(dct1)):
		k = i
		j = 0
		c = 0
		while(k<len(dct1) and j<len(dct2)):
			while ((k<len(dct1) and j<len(dct2)) and  dct1[k]==dct2[j]):
				c += len(dct1[k])
				k += 1
				j += 1
			if(k<len(dct1) and j<len(dct2)):
				if dct1[k] != dct2[j]:
					k = i
					if c>z:
						z = c
					c = 0
					if dct1[k]!=dct2[j]:
						j += 1
		if c>z:
			z = c	
	if c>z:
		z = c
	len_dct1 = 0
	len_dct2 = 0
	for i in dct1:
		len_dct1 = len_dct1 + len(i)
	for i in dct2:
		len_dct2 = len_dct2 + len(i)
	return ((2*z)/(len_dct1+len_dct2))

'''
Comparing all the lists of files.
'''
p = ''
for i in range(0,(len(filename_lst)-1)):
	for j in range((i+1),len(filename_lst)):
		try:
			s = ('LCS between '+str(filename_lst[i])+' and '+str(filename_lst[j])+\
				' is: '+str(LCS(dct_lst[filename_lst[i]],\
				 dct_lst[filename_lst[j]])*100))
		except ZeroDivisionError:
			s = (str(filename_lst[i])+' and '+str(filename_lst[j])+' are empty.')
		p = p + '\n' + s + '\n'


log = "log file.log"
logging.basicConfig(filename=log,level=logging.DEBUG,\
	format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
logging.info('LCS SIMILARITIES \n' + p)

print(p)