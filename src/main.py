import os
from pathlib import Path
from fastapi import FastAPI, Request, HTTPException, Query
from fastapi.responses import Response, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from src.calculators import BasicCalculator, AdvancedCalculator, Tokenizer
from src.operations import get_basic_operations, get_extended_operations
from src.formatters import SimpleCalcResultFormatter, ColorCalcResultFormatter


BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_FOLDER = os.path.join(BASE_DIR, 'static')
TEMPLATES_FOLDER = os.path.join(BASE_DIR, 'templates')

app = FastAPI()
app.mount("/static", StaticFiles(directory=STATIC_FOLDER), name="static")

templates = Jinja2Templates(directory=TEMPLATES_FOLDER)

basic_operations = get_basic_operations()
extended_operations = get_extended_operations()

basic_calc = BasicCalculator(operations=basic_operations)
advanced_calc = AdvancedCalculator(operations=extended_operations, tokenizer_class=Tokenizer)


@app.get("/calculator", response_class=HTMLResponse)
async def calculator_page(request: Request):
    return templates.TemplateResponse("calculator.html", {"request": request})


@app.get("/api/v1/calculate")
async def calculate(
        operand1: float = Query(..., title="Operand 1"),
        operand2: float = Query(..., title="Operand 2"),
        operator: str = Query(..., title="Operator"),
):
    try:
        calc_result = basic_calc.calculate(operand1, operand2, operator)

        result = SimpleCalcResultFormatter.format(calc_result)

        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/api/v2/calculate")
async def calculate(
        expression: str
):
    try:
        calc_result = advanced_calc.calculate(expression)

        result = SimpleCalcResultFormatter.format(calc_result)

        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except IndexError as e:
        raise HTTPException(status_code=400, detail=str('Not enough operands'))


@app.get("/api/v3/calculate")
async def calculate(
        expression: str
):
    try:
        calc_result = advanced_calc.calculate(expression)

        result = ColorCalcResultFormatter.format(calc_result)

        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except IndexError as e:
        raise HTTPException(status_code=400, detail=str('Not enough operands'))
