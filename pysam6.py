import pysam
over=0
samfile = pysam.AlignmentFile("sorted22.bam", "rb" )
for pileupcolumn in samfile.pileup("22", 16861625 , 16861702):
	over=pileupcolumn.n
	if over>0:
		break
print (pileupcolumn.pos)

samfile.close()

