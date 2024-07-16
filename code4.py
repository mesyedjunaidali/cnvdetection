import pysam
samfile = pysam.AlignmentFile("sorted22.bam", "rb" )
for read in samfile. fetch(contig=None, start=16861625, stop=None, region=None, tid=None, until_eof=False, multiple_iterators=False, reference=None, end=None):
     print(read)

samfile.close()
