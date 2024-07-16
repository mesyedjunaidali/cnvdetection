import pysam
import xlsxwriter
samfile = pysam.AlignmentFile("sorted22.bam", "rb")
workbook = xlsxwriter.Workbook('sorted12878_22.xlsx')
worksheet = workbook.add_worksheet()
worksheet.set_column('A:A', 30)
worksheet.set_column('B:B', 25)
worksheet.set_column('C:C', 25)
worksheet.set_column('D:D', 25)
bold=workbook.add_format({'bold': True})
worksheet.write('A1', 'SAMPLEID', bold)
worksheet.write('B1', 'COORDINATE', bold)
worksheet.write('C1', 'COUNT', bold)
worksheet.write('D1', 'QUANTIFICATION', bold)
over=0
samfile = pysam.AlignmentFile("sorted22.bam", "rb" )
for pileupcolumn in samfile.pileup("22", 16050001, 51244568):
    over=pileupcolumn.n
    if over>0:
        break
start=pileupcolumn.pos

i=1
for pileupcolumn in samfile.pileup("22", 16050001, 51244568):
     a=t=g=c=0
     for pileupread in pileupcolumn.pileups:
        if not pileupread.is_del and not pileupread.is_refskip:
            v=pileupread.alignment.query_sequence[pileupread.query_position]
            if v=='A':
                a=a+1  
            elif v=='T':
                t=t+1
            elif v=='G':
                g=g+1
            else:
                c=c+1
     m=max(a,t,g,c)
     worksheet.write(i, 0,"NA12878_HighCoverage_Chrom22")
     worksheet.write(i, 1,pileupcolumn.pos)
     worksheet.write(i, 2,pileupcolumn.n)
     worksheet.write(i, 3,m)
     i=i+1
workbook.close()
