import pysam
import matplotlib
matplotlib.use('Agg')  # Use the 'Agg' backend which is suitable for non-GUI environments
import matplotlib.pyplot as plt

samfile = pysam.AlignmentFile("sorted22.bam", "rb")
d = {}

for pileupcolumn in samfile.pileup("22", 16861625 , 16861702):
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
    d.update({pileupcolumn.pos: m})

key = []
value = []

for k, v1 in d.items():
    key.append(k)
    value.append(v1)

plt.plot(key, value)
plt.savefig("output_plot_pysam3.png")  # Save the plot to a file
