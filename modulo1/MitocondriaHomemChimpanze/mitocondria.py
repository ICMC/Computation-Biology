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
homoG=[]
chimp=[]
chimpG=[]

for seq_record in SeqIO.parse("homoSapiensMito.fasta","fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))

    homo.append(seq_record[1:100].seq.count('C'))

    homo.append(seq_record[1:500].seq.count('C'))
    homo.append(seq_record[500:1100].seq.count('C'))
    homo.append(seq_record[1100:1800].seq.count('C'))
    homo.append(seq_record[1800:2600].seq.count('C'))
    homo.append(seq_record[2600:3500].seq.count('C'))
    homo.append(seq_record[3500:4500].seq.count('C'))
    homo.append(seq_record[4500:5600].seq.count('C'))
    homo.append(seq_record[5600:6800].seq.count('C'))
    homo.append(seq_record[6800:7100].seq.count('C'))
    homo.append(seq_record[7100:8500].seq.count('C'))


    homoG.append(seq_record[1:500].seq.count('G'))
    homoG.append(seq_record[500:1100].seq.count('G'))
    homoG.append(seq_record[1100:1800].seq.count('G'))
    homoG.append(seq_record[1800:2600].seq.count('G'))
    homoG.append(seq_record[2600:3500].seq.count('G'))
    homoG.append(seq_record[3500:4500].seq.count('G'))
    homoG.append(seq_record[4500:5600].seq.count('G'))
    homoG.append(seq_record[5600:6800].seq.count('G'))
    homoG.append(seq_record[6800:7100].seq.count('G'))
    homoG.append(seq_record[7100:8500].seq.count('G'))


for seq_record in SeqIO.parse("pantroglodytes.fasta","fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))

    chimp.append(seq_record[1:100].seq.count('C'))
    chimp.append(seq_record[1:500].seq.count('C'))
    chimp.append(seq_record[500:1100].seq.count('C'))
    chimp.append(seq_record[1100:1800].seq.count('C'))
    chimp.append(seq_record[1800:2600].seq.count('C'))
    chimp.append(seq_record[2600:3500].seq.count('C'))
    chimp.append(seq_record[3500:4500].seq.count('C'))
    chimp.append(seq_record[4500:5600].seq.count('C'))
    chimp.append(seq_record[5600:6800].seq.count('C'))
    chimp.append(seq_record[6800:7100].seq.count('C'))
    chimp.append(seq_record[7100:8500].seq.count('C'))



    chimpG.append(seq_record[1:500].seq.count('G'))
    chimpG.append(seq_record[500:1100].seq.count('G'))
    chimpG.append(seq_record[1100:1800].seq.count('G'))
    chimpG.append(seq_record[1800:2600].seq.count('G'))
    chimpG.append(seq_record[2600:3500].seq.count('G'))
    chimpG.append(seq_record[3500:4700].seq.count('G'))
    chimpG.append(seq_record[4500:5600].seq.count('G'))
    chimpG.append(seq_record[5600:6800].seq.count('G'))
    chimpG.append(seq_record[6800:7100].seq.count('G'))
    chimpG.append(seq_record[7100:8500].seq.count('G'))


homoCG=[]
chimpCG=[]
for i in range(0,10):
    homoCG.append(homo[i]+homoG[i])
    chimpCG.append(chimp[i]+chimpG[i])


trace1=go.Scatter(x=[1,2,3,4,5,6,7,8,9,10], y=[homoCG[0],homoCG[1],homoCG[2],homoCG[3],homoCG[4],homoCG[5],homoCG[6],homoCG[7],homoCG[8],homoCG[9]])
trace2=go.Scatter(x=[1,2,3,4,5,6,7,8,9,10], y=[chimpCG[0],chimpCG[1],chimpCG[2],chimpCG[3],chimpCG[4],chimpCG[5],chimpCG[6],chimpCG[7],chimpCG[8],chimpCG[9]])

data=[trace1,trace2]
py.plot(data, filename="genes")
