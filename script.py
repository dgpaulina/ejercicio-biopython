ejercicio biopython
from Bio import SeqIO
from Bio.SeqFeature import FeatureLocation, SeqFeature
from Bio.SeqRecord import SeqRecord
def summarize_contents(filename):
  record = SeqIO.read(filename, "genbank")print("Name: ", record.name)
  
