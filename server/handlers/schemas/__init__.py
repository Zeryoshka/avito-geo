'''
Init module with validation schames for requests
'''

from .schemas import SetSchema, GetSchema

SET = SetSchema() # schema for SET-request
GET = GetSchema() # schema for GET-request