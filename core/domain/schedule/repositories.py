from datetime import datetime
from typing import Any, Dict, List, Tuple
from core.commom.repository import RepositoryBase
from core.domain.schedule.entities import Schedule


class ScheduleRepository(RepositoryBase):

    def __init__(self, dbfile_name: str) -> None:
        super().__init__(dbfile_name)

    def _deserializable(self, data: dict[str, Any]) -> Any:

        schedue = Schedule(
            datetime.strptime(data['moment'], '%Y-%m-%d %H:%M:%S'),
            data['event_type'],
            data['employee_id']
        )
        schedue._id = data['id']

        return schedue

    def _serializable_to_save(self, data: Any) -> Tuple[int, Dict[str, any]]:

        d = data.entity_dump()
        d['moment'] = d['moment'].__str__()

        return (data._id, d)

    def get_all(self) -> List[Schedule]:

        return list(self._data.values())

    def find_by_id(self, id: int) -> Schedule | None:

        return self._data.get(id)

    def get_all_by_employee_id(self, employee_id: int) -> List[Schedule]:

        return list(filter(lambda x: x._employee_id == employee_id, self._data.values()))

    def create(self, sched: Schedule) -> Schedule:

        sched._id = self.get_v_auto_increment()
        self.set_new_data(sched._id, sched)

        return sched
