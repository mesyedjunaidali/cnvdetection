import pysam
import matplotlib
matplotlib.use('Agg')  # Use the 'Agg' backend which is suitable for non-GUI environments
import matplotlib.pyplot as plt
samfile = pysam.AlignmentFile("sorted22.bam", "rb" )
d={}
for pileupcolumn in samfile.pileup("22", 16861625 , 16861702):
    d.update({pileupcolumn.pos:pileupcolumn.n})


key=[]
value=[]
for k,v in d.items():
	key.append(k)
	value.append(v)
 
plt.plot(key,value)
plt.show()
plt.savefig("peak_coverage.png") 