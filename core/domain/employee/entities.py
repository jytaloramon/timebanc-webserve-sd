from datetime import date, datetime

from build import Dict


class Employee:

    def __init__(self, name: str = '', personal_code: str = '', work_code: str = '', birth_date: str = '') -> None:

        self._id = None
        self._name = name
        self._personal_code = personal_code
        self._work_code = work_code
        self._birth_date = birth_date

    def entity_dump(self) -> Dict[str, any]:
        return {
            'id': self._id,
            'name': self._name,
            'personal_code': self._personal_code,
            'work_code': self._work_code,
            'birth_date': self._birth_date
        }
