from typing import List
from core.commom.repository import RepositoryBase
from core.domain.schedule.entities import Schedule


class ScheduleRepository(RepositoryBase):

    def __init__(self) -> None:
        super().__init__()

    def getAll(self) -> List[Schedule]:

        return list(self._data.values())

    def findById(self, id: int) -> Schedule | None:

        return self._data.get(id)

    def create(self, sched: Schedule) -> Schedule:

        sched._id = self.get_v_auto_increment()

        self._data[sched._id] = sched

        return sched
