import Bio
from Bio import SeqIO
from Bio.Alphabet import IUPAC
from Bio.SeqUtils import GC
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls

bacteria=[]
bacteriaG=[]
for seq_record in SeqIO.parse("sequence.fasta","fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))

    bacteria.append(seq_record[1:100].seq.count('C'))
    bacteria.append(seq_record[1:500].seq.count('C'))
    bacteria.append(seq_record[500:1100].seq.count('C'))
    bacteria.append(seq_record[1100:1800].seq.count('C'))
    bacteria.append(seq_record[1800:2600].seq.count('C'))
    bacteria.append(seq_record[2600:3500].seq.count('C'))
    bacteria.append(seq_record[3500:4500].seq.count('C'))
    bacteria.append(seq_record[4500:5600].seq.count('C'))
    bacteria.append(seq_record[5600:6800].seq.count('C'))
    bacteria.append(seq_record[6800:7100].seq.count('C'))
    bacteria.append(seq_record[7100:8500].seq.count('C'))



    bacteriaG.append(seq_record[1:500].seq.count('G'))
    bacteriaG.append(seq_record[500:1100].seq.count('G'))
    bacteriaG.append(seq_record[1100:1800].seq.count('G'))
    bacteriaG.append(seq_record[1800:2600].seq.count('G'))
    bacteriaG.append(seq_record[2600:3500].seq.count('G'))
    bacteriaG.append(seq_record[3500:4700].seq.count('G'))
    bacteriaG.append(seq_record[4500:5600].seq.count('G'))
    bacteriaG.append(seq_record[5600:6800].seq.count('G'))
    bacteriaG.append(seq_record[6800:7100].seq.count('G'))
    bacteriaG.append(seq_record[7100:8500].seq.count('G'))


bacteriaCG=[]
for i in range(0,10):
    bacteriaCG.append(bacteria[i]+bacteriaG[i])

trace1=go.Scatter(x=[1,2,3,4,5,6,7,8,9,10], y=[bacteria[0],bacteria[1],bacteria[2],bacteria[3],bacteria[4],bacteria[5],bacteria[6],bacteria[7],bacteria[8],bacteria[9]])
trace2=go.Scatter(x=[1,2,3,4,5,6,7,8,9,10], y=[bacteriaG[0],bacteriaG[1],bacteriaG[2],bacteriaG[3],bacteriaG[4],bacteriaG[5],bacteriaG[6],bacteriaG[7],bacteriaG[8],bacteriaG[9]])
trace3=go.Scatter(x=[1,2,3,4,5,6,7,8,9,10], y=[bacteriaCG[0],bacteriaCG[1],bacteriaCG[2],bacteriaCG[3],bacteriaCG[4],bacteriaCG[5],bacteriaCG[6],bacteriaCG[7],bacteriaCG[8],bacteriaCG[9]])
data=[trace1,trace2]
py.plot(data, filename="BacteriaCGcount")
