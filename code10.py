import pysam
import csv

sample = "NA19240"
chromo = "14"

samfile = pysam.AlignmentFile("sorted22.bam", "rb")
with open('sorted.csv','w') as f:
	writer = csv.writer(f)
	writer.writerow(['Rowkey','chrom','start','end','sample','Type-of-reads','Length-of 			reads','Mapping-Quality','Sequence-Quality','CIGAR'])
	sqlen = 0
	for data in samfile.fetch("22", 16861625 , 16861702):
		data = str(data)
		read = data.split('\t')
		start = int(read[3])
		seqlen = len(read[9])
		if int(read[1])%2==1:
			rType = "Paired-end"
		else:
			rType = "Single-end"
		mapq = read[4]
		squal = read[10]
		cigar = read[5]
		end = start+seqlen
		rowkey=chromo+":"+str(start)+":"+str(end)+":"+sample
		
		writer.writerow([rowkey,chromo,start,end,sample,rType,seqlen,mapq,squal,cigar])
