import os
import subprocess
#Set name for the krakendb directory
#krakendb='HumanVirusBacteria'
import PyPluMA

class GetKrakenPlugin:
    def input(self, filename):
        self.krakendb = filename[filename.rfind('/')+1:]
        self.cwd = PyPluMA.prefix()#os.getcwd()

    def run(self):
#krakendb='Bacteria'
       subprocess.call('kraken2-build --download-taxonomy --db '+self.krakendb, shell=True)
       print('Running Kraken DB build for '+self.krakendb+'\n')
       print('This might take a while '+'\n')
       for fasta_file in os.listdir(self.cwd):
          if fasta_file.endswith('.fa') or fasta_file.endswith('.fasta'):
             print (fasta_file)
             subprocess.call('kraken2-build --add-to-library '+fasta_file +' --db '+self.krakendb,shell=True)
       subprocess.call('kraken2-build --build --db '+self.krakendb+' --threads 12',shell=True)

    def output(self, filename):
       os.system("mv "+self.krakendb+" "+filename)
