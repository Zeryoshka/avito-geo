'''
Init module of server's package
'''

from flask import Flask

app = Flask(__name__)

from .urls import app