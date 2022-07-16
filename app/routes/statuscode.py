from enum import unique
from pyparsing import Enum


@unique
class StatusCode(Enum):

    OK = 200
    CREATED = 201
    NOTFOUND = 404
    BADREQUEST = 400
    CONFLIT = 409
