import pysam
samfile = pysam.AlignmentFile("sorted22.bam", "rb" )
for pileupcolumn in samfile.pileup("22", 2072700000 , None):
    print ("\ncoverage at base %s = %s" %
		(pileupcolumn.pos, pileupcolumn.n))

samfile.close()
