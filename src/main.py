import os
from pathlib import Path
from fastapi import FastAPI, Request, HTTPException, Query
from fastapi.responses import Response, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from src.calculators import BasicCalculator
from src.operations import OperatorEnum, AddOperation, SubtractOperation, MultiplyOperation, DivideOperation


BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_FOLDER = os.path.join(BASE_DIR, 'static')
TEMPLATES_FOLDER = os.path.join(BASE_DIR, 'templates')

app = FastAPI()
app.mount("/static", StaticFiles(directory=STATIC_FOLDER), name="static")

templates = Jinja2Templates(directory=TEMPLATES_FOLDER)

basic_operations = {
    OperatorEnum.ADD:      AddOperation,
    OperatorEnum.SUBTRACT: SubtractOperation,
    OperatorEnum.MULTIPLY: MultiplyOperation,
    OperatorEnum.DIVIDE:   DivideOperation,
}

basic_calc = BasicCalculator(operations=basic_operations)


@app.get("/calculator", response_class=HTMLResponse)
async def calculator_page(request: Request):
    return templates.TemplateResponse("calculator.html", {"request": request})


@app.get("/api/v1/calculate")
async def calculate(
        operand1: float = Query(..., title="Operand 1"),
        operand2: float = Query(..., title="Operand 2"),
        operator: str = Query(..., title="Operator"),
        # operator: OperatorEnum = Query(..., title="Operator")
):
    try:
        result = basic_calc.calculate(operand1, operand2, operator)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
