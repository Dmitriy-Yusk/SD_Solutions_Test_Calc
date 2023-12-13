from typing import Dict


class SimpleCalcResultFormatter:
    @classmethod
    def format(cls, data) -> Dict:
        return {'result': data}
