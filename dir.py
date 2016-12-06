# Assumptions:
# We are implementing a file-search function.
# the function looks for files in the current directory and its subdirectories for which the name matches a prefix of length 1
# the string match is case sensitive
# Note:
# 1. All file names are in lower case.
# 2. For longer prefix search, we can add trie.
# for example:
# searchFile('a') returns all files that have names starting with letter 'a', case sensitive.

from collections import defaultdict
import random
import string
import sys

class File(object):
	def __init__(self,name):
		self.name = name

class Folder(object):
	def __init__(self,name):
		self.name = name
		#folders
		self.fmap = defaultdict(Folder)
		#documents
		self.dmap = []

	def addFolder(self, folder):
		self.fmap[folder.name] = folder

	def addFile(self,filename):
		self.dmap.append(File(filename))

	def searchFile(self, s):
		res = []
		self.searchFileHelper(res, [], self, s)
		return res

	def searchFileHelper(self, res, parentpath, directory, s):
		if len(directory.dmap) > 0:
			fileMatch = ['%s/%s' % (("/".join(parentpath + [directory.name])), f.name) for f in directory.dmap if f.name[0] == s]
			for f in fileMatch:
				res.append(f)
		for f in directory.fmap.values():
			self.searchFileHelper(res,parentpath + [directory.name], f, s)

	def printFolders(self):
		print(self.fmap.keys())

	def printFiles(self):
		for f in self.dmap:
			print(f.name),
		print('\b')

def addFilestoFolder(files, folder):
	for f in files:
		folder.addFile(f)

#creat root folder and initiate folders and files
root = Folder('Root')
files,folders = [],[]
foldernames = ['Folder' + str(i) for i in range(10)]

# generating random files
for i in range(10):
	files.append([''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6))+'.txt' for x in range(100)])

# populating folders
for foldername in foldernames:
	folders.append(Folder(foldername))
for i in range(len(files)):
	addFilestoFolder(files[i],folders[i])

# for simplicity, there are two folders under root
root.addFolder(folders[0])
root.addFolder(folders[1])

# constructing simple folder structure
for i in range(2,len(folders)):
	if i%2 == 0:
		folders[0].addFolder(folders[i])
	else:
		folders[1].addFolder(folders[i])

# add empty folders for corner cases
folders[0].addFolder(Folder('EmptyFolder_X'))
folders[1].addFolder(Folder('EmptyFolder_Y'))

# tests:
def printRes(res):
	for i in res:
		print(i)

# change test string here.
sys.stdout.write('Search for files start with character(a-z0-9,lowercase) ...\n')

s = raw_input().strip()

sys.stdout.write('(Default) Searching for files start with %s in Root ...\n' % (s))
res1 = root.searchFile(s)

sys.stdout.write('Search for files starts with %s, %s files found\n' % (s,len(res1)))

printRes(res1)

print('\n')

sys.stdout.write('Let\'s change to a different folder and search for the same prefix. \n')
sys.stdout.write('Input choices Folder0 to Folder9, type 0 - 9  \n')

n = int(raw_input().strip())
res2 = folders[n].searchFile(s)
if n:
	sys.stdout.write('Search for files starts with %s in %s, %s files found\n' % (s,folders[n].name, len(res2)))
	printRes(res2)
else:
	sys.stdout.write('I guess you don\'t want to search in a different folder' % (s,folders[n].name, len(res2)))

print('\n')
sys.stdout.write('Please press Enter again')

x = raw_input()
print('\n')
sys.stdout.write('Nir, it was very nice talking to you today! Thank you very much! ')

print('\n')