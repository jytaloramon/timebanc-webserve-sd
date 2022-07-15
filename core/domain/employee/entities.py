from datetime import date, datetime

from build import Dict


class Employee:

    def __init__(self, name: str = '', personal_code: str = '', work_code: str = '', birth_date: date = datetime.now()) -> None:

        self._id = None
        self._name = name
        self._personal_code = personal_code
        self._work_code = work_code
        self._birth_date = birth_date

    def entity_dump(self) -> Dict[str, any]:
        return {
            'id': self._id,
            'name': self._name,
            'personalcode': self._personal_code,
            'workcode': self._work_code,
            'birthdate': self._birth_date
        }

    """
    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def personal_code(self) -> str:
        return self._personal_code

    @property
    def work_code(self) -> str:
        return self._work_code

    @property
    def birth_date(self) -> date:
        return self._birth_date
    """
