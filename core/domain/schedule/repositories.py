from typing import List
from core.commom.repository import RepositoryBase
from core.domain.schedule.entities import Schedule


class ScheduleRepository(RepositoryBase):

    def __init__(self, dbfile_name: str) -> None:
        super().__init__(dbfile_name)

    def get_all(self) -> List[Schedule]:

        return list(self._data.values())

    def find_by_id(self, id: int) -> Schedule | None:

        return self._data.get(id)

    def create(self, sched: Schedule) -> Schedule:

        sched._id = self.get_v_auto_increment()
        self.set_new_data(sched._id, sched)

        return sched
