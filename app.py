from flask import Flask
from optparse import OptionParser

parser = OptionParser()
parser.add_option('-h', help='Host', default='127.0.0.1')
parser.add_option('-p', help='Port', default='8080')
parser.add_option('--debug', )
