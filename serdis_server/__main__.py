'''
__main__ module for run server package
'''

from . import app

app.run(host='0.0.0.0', port=5000)