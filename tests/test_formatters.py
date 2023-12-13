from src.formatters import ColorCalcResultFormatter


def test_color_calc_result_formatter_odd():
    result = ColorCalcResultFormatter.format(5)
    assert result == {"result": 5, "color": ColorCalcResultFormatter._ODD_COLOR}


def test_color_calc_result_formatter_even():
    result_data = ColorCalcResultFormatter.format(10)
    assert result_data == {"result": 10, "color": ColorCalcResultFormatter._EVEN_COLOR}
