import logging
from typing import Any

from curl_fetch2py import CurlFetch2Py
from fastapi import APIRouter, HTTPException, Request
from fastapi.templating import Jinja2Templates

from api.schemas import RequestsData
from api.utils import execute_request

router = APIRouter(prefix='', tags=['API'])
templates = Jinja2Templates(directory="templates")

logging.basicConfig(level=logging.DEBUG)


@router.get('/')
async def get_main_page(request: Request) -> Any:
    """Render the main page."""
    return templates.TemplateResponse(name='index.html', context={'request': request})


@router.post('/api', summary='The main API endpoint')
async def main_logic(request_body: RequestsData) -> dict[str, str]:
    """Process the request and return the result."""
    request_type = request_body.request_type
    target = request_body.target
    data_str = request_body.data_str

    logging.debug(f"Received request: {request_body}")

    try:
        if request_type == 'curl':
            context = CurlFetch2Py.parse_curl_context(data_str)
        elif request_type == 'fetch':
            context = CurlFetch2Py.parse_fetch_context(data_str)
        else:
            raise ValueError("Unsupported request type")

        logging.debug(f"Parsed context: {context}")

        result = execute_request(context, target).strip()
        logging.debug(f"Generated result: {result}")

        return {"request_string": result}
    except Exception as e:
        logging.error(f"Error processing request: {e}")
        raise HTTPException(status_code=500, detail=str(e))
