import Bio
from Bio import SeqIO
from Bio.Alphabet import IUPAC
from Bio.SeqUtils import GC
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls

username = input("Plotly username: ")
apiKey = input("Plotly API Key: ")

tls.set_credentials_file(username, apiKey)
homo = []
chimp=[]

for seq_record in SeqIO.parse("homoSapiensMito.fasta","fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))

    homo.append(seq_record[1:100].seq.count('CG'))
    print(homo[0])
    homo.append(seq_record[100:1000].seq.count('CG'))
    homo.append(seq_record[1000:1500].seq.count('CG'))
    homo.append(seq_record[1500:2500].seq.count('CG'))
    homo.append(seq_record[2500:3000].seq.count('CG'))
    homo.append(seq_record[3000:4000].seq.count('CG'))
    homo.append(seq_record[4000:4500].seq.count('CG'))
    homo.append(seq_record[4500:6000].seq.count('CG'))
    homo.append(seq_record[6000:10000].seq.count('CG'))
    homo.append(seq_record[1000:12000].seq.count('CG'))
    homo.append(seq_record[1200:14000].seq.count('CG'))
    homo.append(seq_record[1400:15000].seq.count('CG'))
    homo.append(seq_record[1500:16000].seq.count('CG'))
    homo.append(seq_record[1600:16500].seq.count('CG'))
    print(homo[13])

for seq_record in SeqIO.parse("pantroglodytes.fasta","fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))

    chimp.append(seq_record[1:100].seq.count('CG'))
    print(chimp[0])
    chimp.append(seq_record[100:1000].seq.count('CG'))
    chimp.append(seq_record[1000:1500].seq.count('CG'))
    chimp.append(seq_record[1500:2500].seq.count('CG'))
    chimp.append(seq_record[2500:3000].seq.count('CG'))
    chimp.append(seq_record[3000:4000].seq.count('CG'))
    chimp.append(seq_record[4000:4500].seq.count('CG'))
    chimp.append(seq_record[4500:6000].seq.count('CG'))
    chimp.append(seq_record[6000:10000].seq.count('CG'))
    chimp.append(seq_record[1000:12000].seq.count('CG'))
    chimp.append(seq_record[1200:14000].seq.count('CG'))
    chimp.append(seq_record[1400:15000].seq.count('CG'))
    chimp.append(seq_record[1500:16000].seq.count('CG'))
    chimp.append(seq_record[1600:16500].seq.count('CG'))
    print(chimp[13])


trace1=go.Scatter(x=[1,2,3,4,5,6,7,8,9,10], y=[homo[0],homo[1],homo[2],homo[3],homo[4],homo[5],homo[6],homo[7],homo[8],homo[9]])
trace2=go.Scatter(x=[1,2,3,4,5,6,7,8,9,10], y=[chimp[0],chimp[1],chimp[2],chimp[3],chimp[4],chimp[5],chimp[6],chimp[7],chimp[8],chimp[9]])

data=[trace1,trace2]
py.plot(data, filename="genes")
