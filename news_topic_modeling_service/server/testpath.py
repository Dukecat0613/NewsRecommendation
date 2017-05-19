import os
import sys
sys.path.append( os.path.join(os.path.dirname(__file__), '..', '..'))
import parameters

VARS_FILE = os.path.join(os.path.dirname(__file__),'..','model/vars')
print VARS_FILE

f = open(VARS_FILE, 'r')
print f
