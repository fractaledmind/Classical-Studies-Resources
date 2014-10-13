import sys, json

def read_and_convert(f):
	v1=ord(f.read(1))
	v2=ord(f.read(1))
	return (v1*256)+v2

lista=[]
dicto={}

#lista de tuples ("label",offset_start, offset_end)
#la lista de cada label comienza en next_block + offset

def readBIN(file):
	with open(file, 'rb') as f:
		f.seek(2)
		next_block=read_and_convert(f)
		#print next_block
		offset_end=0
		f.seek(4,1)
		while 1:
			offset_start=offset_end
			if offset_start==0 and f.tell()>20: #evitamos 1er offset 0000
				break
			len_label=ord(f.read(1))
			label=f.read(len_label)
			f.seek(2,1)
			offset_end=read_and_convert(f) #start of next label in fact...
			lista.append((label,offset_start, offset_end))
			#print label, offset_start, offset_end
		for l in lista:
			print "label:",l[0]
			lenght = l[2]-l[1]
			f.seek(next_block+l[1])
			buf=f.read(lenght)
			cntx=False
			list_files=[]
			for s in buf:
				if ord(s) >= 128 and cntx ==False:
					val1=ord(s)-128
					cntx=True
				else:
					if cntx==True:
						val2=ord(s)
						cntx=False
						list_files.append("{:0>4d}".format((val1*256)+val2))
					else:
						continue
			dicto[l[0]]=list_files
		return dicto
if __name__ == "__main__":
	#file .bin in, file.json out
	with open(sys.argv[2],"w") as fo:
		json.dump(readBIN(sys.argv[1]),fo,indent=4,sort_keys=True)
		
