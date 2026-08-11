from fastapi import FastAPI, BackgroundTasks, Depends
from middleware import timing_middleware
import time
import asyncio


app = FastAPI(
    title="Day 21 Async FastAPI",
    version="1.0"
)


# -----------------------------
# Middleware
# -----------------------------

@app.middleware("http")
async def timing(request, call_next):

    return await timing_middleware(request, call_next)


# -----------------------------
# Background Task
# -----------------------------

def write_log():

    with open("api_log.txt", "a") as file:
        file.write("API request completed\n")


# -----------------------------
# Dependency Injection
# -----------------------------

def get_api_info():

    return "Day 21 FastAPI"


# -----------------------------
# Synchronous API
# -----------------------------

@app.get("/api/v1/sync")
def sync_api(
    background_tasks: BackgroundTasks,
    info: str = Depends(get_api_info)
):

    time.sleep(2)

    background_tasks.add_task(write_log)

    return {
        "message": "Synchronous API",
        "info": info
    }


# -----------------------------
# Asynchronous API
# -----------------------------

@app.get("/api/v1/async")
async def async_api(
    background_tasks: BackgroundTasks,
    info: str = Depends(get_api_info)
):

    await asyncio.sleep(2)

    background_tasks.add_task(write_log)

    return {
        "message": "Asynchronous API",
        "info": info
    }