from enum import unique
from pyparsing import Enum


@unique
class ScheduleType(Enum):

    start = 0
    end = 1
