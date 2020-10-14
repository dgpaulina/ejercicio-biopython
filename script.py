ejercicio biopython
from Bio import SeqIO
from Bio.SeqFeature import FeatureLocation, SeqFeature
from Bio.SeqRecord import SeqRecord
import os.path
def summarize_contents(filename):
  record = SeqIO.read(filename, "genbank")
  print("Name: ", record.name)
  print("Path: ", os.path.dirname(filename))
  record = list(SeqIO.parse(filename , "genbank"))
  print("Records_found: " % len(records))
  records = list(SeqIO.parse(filename, "genbank"))
  len(records) print("Records id: ", records[1].id)
  location = SeqFeature.location(filename , "genebank")
  print ("Location: " , SeqFeature.location)
  records = list(SeqIO.parse(filename, "genbank"))
  len(records) print("Records id: ", records[2].id)
