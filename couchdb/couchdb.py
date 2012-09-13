import sys
import os
import couchdb
try:
    import jsonlib2 as json
except ImportError:
    import json

server = couchdb.Server('http://oecdt.iriscouch.com/:5984')
