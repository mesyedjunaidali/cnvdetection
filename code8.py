import pysam
import csv

over = 0
samfile = pysam.AlignmentFile("sorted22.bam", "rb")

for pileupcolumn in samfile.pileup("22", 16050000, 51244556):
    over = pileupcolumn.n
    if over > 0:
        break

start = pileupcolumn.pos

with open('test2.csv', 'w') as f:
    thewriter = csv.writer(f)
    
    for pileupcolumn in samfile.pileup("22", start, 51244556):
        a = t = g = c = 0

        for pileupread in pileupcolumn.pileups:
            if not pileupread.is_del and not pileupread.is_refskip:
                v = pileupread.alignment.query_sequence[pileupread.query_position]
                if v == 'A':
                    a += 1
                elif v == 'T':
                    t += 1
                elif v == 'G':
                    g += 1
                else:
                    c += 1

        m = max(a, t, g, c)
        d=''
        if((a>t)and(a>g)and(a>c)):d="A";
        elif((t>a)and(t>g)and(t>c)) :d="T";
        elif((c>a)and(c>g)and(c>t)) :d="C";
        elif((g>a)and(g>t)and(g>c)) :d="G";
        thewriter.writerow([pileupcolumn.pos, d])
