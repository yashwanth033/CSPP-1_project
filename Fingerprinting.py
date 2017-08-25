import math
import glob
import re
import os
import logging

import os
pat = os.getcwd()
pat = pat + '\word.txt'

kgram_len_lst = []
dct_lst = {}
filename_lst = []
path = os.getcwd()

'''
List of stop words inserted in a list.
'''

f = open(pat,'r')
stop_word = set(f.read().split())
f.close()

'''
To read files to create lists. Copy them in the current directory\
and remove any other .txt files from current directory.
'''

for filename in glob.glob(os.path.join(path, '*.txt')):
	if filename != pat:
		f = open(filename,'r')
		fw = f.read()
		f.close()

		'''
		Lower casing and removing special characters. Assuming words to be\
		with alphabets, under_score and numeric characters only.
		'''

		fw = fw.lower()
		fw = re.sub(r'[^a-z0-9_ \n]', '', fw).split()

		'''
		remove stop words and make a string of all rest of the words.
		'''
		lw = []
		for i in fw:
			if i not in stop_word:
				lw.append(i)

		l = "".join(lw)


		'''
		Storing in dct_lst with file name as key an value a string.\
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
Taking k as 5 to calculate k-grams and p as 99991 to get 0-mod p.
'''
k = 5
p = 10

def hash(x):
	'''
	Hash function to calculate hash values of k-grams.
	'''
	h = 0
	for i in range(0,5):
		h = h + (ord(x[i]))*(k**(5-i))
	return h

def k_Gram(l):
	'''
	k gram function takes a string and returns a list of k grams \
	with length 5.
	'''
	ls = []
	for i in range(0,len(l)-4):
		ls.append(l[i:i+5])
	return ls

def p_mod(ls):
	'''
	p mod function takes a list of hash values and gives us p mod values\
	(p = 991) list.
	'''
	pm = []
	for i in ls:
		if i%p==0:
			pm.append(i)
	return pm

'''
Converting strings to k-grams.
'''
for i in dct_lst:
	dct_lst[i] = k_Gram(dct_lst[i])
	kgram_len_lst.append(len(dct_lst[i]))

'''
Converting k-grams to hashes.
'''
for i in dct_lst:
	for j in range(0,len(dct_lst[i])):
		dct_lst[i][j] = hash(dct_lst[i][j])

'''
Stores signatures in lists for each file.
'''
for i in dct_lst:
	dct_lst[i] = p_mod(dct_lst[i])

def Fngprnt(dct1, dct2, den):
	'''
	This finger print function takes two lists of p-mods and \
	and compare those to give the match percentage.
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
				c += 1
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
	return ((2*z)/(den))

p = ''
for i in range(0,(len(filename_lst)-1)):
	for j in range((i+1),len(filename_lst)):
		try:
			d = kgram_len_lst[i] + kgram_len_lst[j]
			s = ('Fingerprint match between '+str(filename_lst[i])+' and '+str(filename_lst[j])+\
				' is: '+str(Fngprnt(dct_lst[filename_lst[i]],\
				 dct_lst[filename_lst[j]],d)*100))
		except ZeroDivisionError:
			s = (str(filename_lst[i])+' and '+str(filename_lst[j])+' are either empty or are too small with little length.')
		p = p + '\n' + s + '\n'

log = "log file.log"
logging.basicConfig(filename=log,level=logging.DEBUG,\
	format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
logging.info('FINGER PRINT SIMILARITIES \n' + p)

print(p)