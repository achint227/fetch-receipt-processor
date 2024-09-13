# generated by fastapi-codegen:
#   filename:  api.yml
#   timestamp: 2024-09-12T21:02:19+00:00

from __future__ import annotations

from typing import Optional

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import constr

from .controller import get_points, process_receipt
from .models import (Receipt, ReceiptsIdPointsGetResponse,
                     ReceiptsProcessPostResponse)

app = FastAPI(
    title="Receipt Processor",
    description="A simple receipt processor",
    version="1.0.0",
)

store = {}

favicon_path = "app/favicon.png"


@app.get("/")
def get_app_root():
    return {"message": "Fetch Receipt processor"}


@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return FileResponse(favicon_path)


@app.post(
    "/receipts/process",
    response_model=None,
    responses={"200": {"model": ReceiptsProcessPostResponse}},
)
def post_receipts_process(body: Receipt) -> Optional[ReceiptsProcessPostResponse]:
    """
    Submits a receipt for processing
    """
    return ReceiptsProcessPostResponse(id=process_receipt(store, body))


@app.get(
    "/receipts/{id}/points",
    response_model=None,
    responses={"200": {"model": ReceiptsIdPointsGetResponse}},
)
def get_receipts_id_points(
    id: constr(pattern=r"^\S+$"),
) -> Optional[ReceiptsIdPointsGetResponse]:
    """
    Returns the points awarded for the receipt
    """
    return ReceiptsIdPointsGetResponse(points=get_points(store, id))
