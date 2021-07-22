'''
Init module of server's package
'''

from flask import Flask
from .storage_package import Storage

storage = Storage()
app = Flask(__name__)

from .urls import app