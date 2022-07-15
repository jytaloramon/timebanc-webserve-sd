from typing import Any, Dict


class RepositoryBase:

    def __init__(self) -> None:

        self._v_auto_increment = 1
        self._data: Dict[int, Any] = {}

    def get_v_auto_increment(self) -> int:

        self._v_auto_increment += 1

        return self._v_auto_increment - 1
