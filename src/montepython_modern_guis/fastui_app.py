from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastui import AnyComponent, FastUI, prebuilt_html, components as c
from fastui.events import GoToEvent

app = FastAPI()

counter = 0


@app.get("/api/", response_model=FastUI, response_model_exclude_none=True)
async def root(request: Request) -> list[AnyComponent]:
    global counter

    match request.query_params.get("action"):
        case "inc":
            counter += 1
        case "dec":
            counter -= 1

    return [c.Page(components=[
        c.Heading(text="Counter"),
        c.Text(text=str(counter)),
        c.Button(text="+", on_click=GoToEvent(query={"action": "inc"})),
        c.Button(text="-", on_click=GoToEvent(query={"action": "dec"})),
    ])]


@app.get("/")
def index() -> HTMLResponse:
    return HTMLResponse(prebuilt_html(title="Counter"))


if __name__ == '__main__':
    from fastapi_cli.cli import dev
    dev(path=Path("./fastui_app.py"))
