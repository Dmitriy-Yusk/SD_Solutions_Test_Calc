from typing import Dict


class SimpleCalcResultFormatter:
    @staticmethod
    def format(data) -> Dict:
        return {'result': data}


class ColorCalcResultFormatter:
    # RED color is usually used for errors, so for ODD values I decided to use BLUE
    # GREEN color is not really visible, so I decided to use YELLOW
    _ODD_COLOR: str = 'blue'
    _EVEN_COLOR: str = 'purple'

    @classmethod
    def format(cls, data) -> dict:
        color = cls._EVEN_COLOR if data % 2 == 0 else cls._ODD_COLOR
        return {"result": data, "color": color}
