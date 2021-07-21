'''
__main__ module for run server package
'''

from . import app

app.run(host='127.0.0.1', port=5000)