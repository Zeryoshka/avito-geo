'''
Init module with validation schames for requests
'''

from .schemas import DelSchema, LgetSchema, SetSchema, GetSchema, LsetSchema


SET = SetSchema()  # schema for SET-request
GET = GetSchema()  # schema for GET-request
LSET = LsetSchema()  # schema for LSET-request
LGET = LgetSchema()  # schema for LGET-request
DEL = DelSchema()  # schema  for DEL-request
