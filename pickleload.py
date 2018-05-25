import pickle
import sys
filename = 'filename' + '.pickle'

#sys.setdefaultencoding('utf-8')

with open(filename, 'rb') as pickle_file:
    content = pickle.load(pickle_file, encoding='bytes')

