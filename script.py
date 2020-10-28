ejercicio biopython
from Bio import SeqIO
from Bio.SeqFeature import FeatureLocation, SeqFeature
from Bio.SeqRecord import SeqRecord
import os.path

filename = "/mnt/C/Users/pauli/ejercicio-biopython/biopython-notebook/notebooks/data/ls_orchid.gbk"
def summarize_contents(filename):
  lista = []
  lista = os.path.split(filename)
  record = SeqIO.read(filename, "genbank")
  print("Name: ", record.name)
  print("Path: ", os.path.dirname(filename))
  record = list(SeqIO.parse(filename , "genbank"))
  print("Num_records: " % len(records))
  for seq_record in SeqIO.parse(filename, "genbank"):
    print("ID :",record.id)
    print("Name: ",record.name)
    print("Description: ",record.description)
