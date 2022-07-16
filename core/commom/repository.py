import json
from typing import Any, Dict


class RepositoryBase:

    def __init__(self, dbfile_name: str) -> None:

        self._dbfile_name = dbfile_name

        filedb = open(dbfile_name, 'r')
        data = json.loads(filedb.read())
        filedb.close()

        self._v_auto_increment = data['paramer']['auto_increment']
        self._data: Dict[int, Any] = data['data']

    def get_v_auto_increment(self) -> int:

        self._v_auto_increment += 1

        return self._v_auto_increment - 1

    def update_db(self) -> None:

        data_save = dict(
            map(lambda x: (x[0], x[1].entity_dump()), self._data.items()))

        filedb = open(self._dbfile_name, 'w+')
        filedb.write(json.dumps({
            "paramer": {"auto_increment": self._v_auto_increment},
            "data": data_save})
        )
        filedb.close()

    def set_new_data(self, id: int, new_obj: Any) -> None:

        self._data[id] = new_obj
        self.update_db()
