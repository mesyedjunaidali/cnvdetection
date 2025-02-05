import pysam
samfile = pysam.AlignmentFile("sorted22.bam", "rb" )
for pileupcolumn in samfile.pileup("22", 16861625 , 16861702):
    print ("\ncoverage at base %s = %s" %
		(pileupcolumn.pos, pileupcolumn.n))
           
    for pileupread in pileupcolumn.pileups:
        if not pileupread.is_del and not pileupread.is_refskip:
            # query position is None if is_del or is_refskip is set.
            print ('\tbase in read %s = %s' %
                  (pileupread.alignment.query_name,
                   pileupread.alignment.query_sequence[pileupread.query_position]))

samfile.close()
