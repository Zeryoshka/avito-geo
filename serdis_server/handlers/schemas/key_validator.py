'''
Module with marshmallow validator for keys
'''

from marshmallow.fields import String
from marshmallow import ValidationError
import re


KEY_TEMPLATE = r'[a-zA-Z_][a-zA-Z0-9_]*'


class KeyValidator(String):
    '''
    Validator for keys with a-z, A-Z, 0-9, "_" and not started with 0-9
    '''
    def _deserialize(self, value, attr, data, **kwargs) -> (list):
        try:
            result = super()._deserialize(value, attr, data, **kwargs)
        except ValidationError as error:
            raise error

        if re.fullmatch(KEY_TEMPLATE, result) is None:
            raise ValidationError(
                f'is not agree with template: {KEY_TEMPLATE}'
            )
        return result
