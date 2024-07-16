import pysam
import matplotlib
matplotlib.use('Agg')  # Use the 'Agg' backend which is suitable for non-GUI environments
import matplotlib.pyplot as plt

samfile = pysam.AlignmentFile("sorted22.bam", "rb" )
d={}
for pileupcolumn in samfile.pileup("22", 16050000, 51244556):
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
    d.update({pileupcolumn.pos:m})
    key=[]
    value=[]
    
for k,v1 in d.items():
    key.append(k)
    value.append(v1)

plt.plot(key,value)
plt.show()    
plt.savefig("Base Quantification.png") 
samfile.close()