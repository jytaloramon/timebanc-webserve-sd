from datetime import datetime
from typing import Any, Dict
from core.domain.employee.entities import Employee


class Schedule:

    def __init__(self, moment: datetime, event_type: int, employee_id: int) -> None:

        self._id = None
        self._moment = moment
        self._event_type = event_type
        self._employee_id = employee_id

    def entity_dump(self) -> Dict[str, any]:
        return {
            'id': self._id,
            'moment': self._moment,
            'event_type': self._event_type,
            'employee_id': self._employee_id
        }
