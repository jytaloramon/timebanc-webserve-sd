from datetime import datetime
from typing import Dict
from core.domain.employee.entities import Employee


class Schedule:

    def __init__(self, moment: datetime, event_type: int, employee: Employee) -> None:

        self._id = None
        self._moment = moment
        self._event_type = event_type
        self._employee = employee

    def entity_dump(self) -> Dict[str, any]:
        return {
            'id': self._id,
            'moment': self._moment,
            'eventtype': self._event_type,
            'employee': self._employee.entity_dump()
        }
