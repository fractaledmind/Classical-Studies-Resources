#script to process list of works and authors in TLG *.bin files
#Currently, only:
#                 list1geo.bin (geographical epithets)
#                 list1dat.bin (dates)
#                 list1epi.bin (epithets)
# there are 4 versions to each (list1, list2... list4) 
# cannot for sure ascertain the difference (I cmp them and many are the same
# but the files in different order. I use number 4 for all.

import sys, json

def read_and_convert(f):
	#function to convert two bytes encoded in ascii to a number
	#TLG encodes integers this way
	#ascii 0x18 | ascii 0x00 = 0x1800
	#guess there should be a better way to do this...
	
	v1=ord(f.read(1)) #read high order byte
	v2=ord(f.read(1)) #read low order byte
	return (v1*256)+v2

lista=[] #list of labels (geo or epi or whatever). We use a tuple to hold (label, start, end)
dicto={} #our dictionary to convert to json

def readBIN(file):
	#as far as I can tell the file is structured as follows
	# 00 00 (2 bytes)
	# address of start of block with list of files (2 bytes) ---> we read this in next_block
	# each label points to a block that holds the list of files
	# 00 00 (2 bytes)
	# here comes our first label...
	# two bytes to point to start of block listing the files
	# 1 byte for lenght of label
	# (lenght of label) bytes to hold the string
	# 00 00 (2 bytes)
	#
	# we first make a list with label, start of block (we keep track of
	# this value for next label) and end of block
	#
	# then we read each block and disect each two bytes to convert ascii to
	# file name. This is quite strange:
	# first byte has its high bit set (10000000) which means we have to 
	# take the next byte also (we use cntx flag for this)
	# We use a flag because first byte should be >= 128 but second byte
	# can be anything, so we need to know if this is the first or the 
	# second byte
	#
	# To convert this mess to a number we have to unset first high byte
	# (I simple take 128 from it) * 256 + next byte. 
	# we then format it to pad ceros and etc 23 >> 0023
	#
	# all this can be done in a better way...
		
	with open(file, 'rb') as f:
		f.seek(2)  #first two bytes we don't care
		next_block=read_and_convert(f) # we read the base address of our list
		offset_end=0 # we need this to record start of label (which in turn is the end of previous label)
		f.seek(4,1) #for first label we can skip this
		while 1: #don't know how to stop...
			offset_start=offset_end #start is = to end of previous label
			if offset_start==0 and f.tell()>20: #ugly hack to avoid the first label's offset (which is 00), pos of file ahead of 1st label  
				break
			len_label=ord(f.read(1))  #get the label string lenght
			label=f.read(len_label) #read the label
			f.seek(2,1) #advance 2 bytes (00 00 )
			offset_end=read_and_convert(f) #start of next label in fact...
			lista.append((label,offset_start, offset_end))
		for l in lista:
			print "label:",l[0] #we iterate over labels
			lenght = l[2]-l[1] #end - start to calculate lenght of block
			f.seek(next_block+l[1])
			buf=f.read(lenght) #we read the chunk
			cntx=False # we need this flag to ensure we're reading the high byte (>128)
			list_files=[]
			for s in buf:
				if ord(s) >= 128 and cntx ==False:  #>128 and it's the first byte
					val1=ord(s)-128 #we unset the high order bit
					cntx=True #we prepare for next byte (it can range 0.. 255)
				else:
					if cntx==True: #we've just read a previous high order byte
						val2=ord(s)
						cntx=False #we unset the flag for the next
						list_files.append("{:0>4d}".format((val1*256)+val2)) #we format it to pad with 0
					else:
						continue
			dicto[l[0]]=list_files #we append list to dictionary key = label
		return dicto
if __name__ == "__main__":
	#run with python distillbin list_geo/epi.bin file.json
	with open(sys.argv[2],"w") as fo:
		json.dump(readBIN(sys.argv[1]),fo,indent=4,sort_keys=True) 
		
