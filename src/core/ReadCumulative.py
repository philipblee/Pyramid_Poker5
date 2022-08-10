import csv
import logging

# #PARAMETERS
# logging.basicConfig(format='%(asctime)s:%(levelno)s:%(funcName)s:%(message)s',
#                     filemode="w", filename="output.txt", level=logging.INFO)
from operator import itemgetter
class ReadCumulative():
    """ class reads cumulative_output file and stores into attribute item """
    def __init__(self):
        import os
        rel_path = "OldFiles/cumulative_output.csv"
        cwd = os.getcwd()
        print (cwd)
        with open(rel_path, "r") as e:
            reader = csv.reader(e)
            self.item = list(reader)
        # sorted(self.item, key=itemgetter(2))
        # print (self.item)

ReadCumulative()