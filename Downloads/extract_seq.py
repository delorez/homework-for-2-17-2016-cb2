#!/user/bin/python
import sys
import re

id_file = sys.argv [1]
seq_file = sys.argv [2]
required_ids = set()
f = open (id_file, 'r')

for line in f:
	line = line.rstrip('\n')
	required_ids.add(line)

f.close()

f = open(seq_file, 'r')

lastid = ''
lastseq = ''

for  line in f:
	m=re.search('^\\>sp\\|(.*)\\|', line)
	if m :
		current_id = m.group(1)
		if (lastid and (lastid in required_ids)):
			sys.stdout.write(lastseq)
		lastid = current_id
		lastseq = line
#		else:
#			sys.stdout.write (lastseq)
#			lastseq = line
#			lastid = current_id
	else: #In sequence
		lastseq = lastseq + line



#list((lastid) . intersection (required_ids))

#[x for x in lastid if x in required_ids]	
#print x

#' '.join (str(x) for x in (set(lastid()) & set(required_ids())))	

#' '.join (str(x) for x in (set(current_id()) & set(required_ids())))

#list (set(current_id()) & set(required_ids()))



#for each line in the file:
#	l = line
#	if (l startswith ">"):
#		#Two conditions
#		#1st condition first line
#		if (lastid is FALSE): 
#			id=getidfromline(l)
#			lastid = id
#			lastseq = l

#		#Any other line with >
#		else:
#			print lastseq
#			lastseq = l
#			lastid = getidfromline(l)
#	else: #In sequence
#		lastseq = lastseq + l

#print lastseq 


##Given a line it returns id
#getidfromline()

#tip if id in required_ids
