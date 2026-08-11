import time


async def timing_middleware(request, call_next):

    start_time = time.perf_counter()

    response = await call_next(request)

    end_time = time.perf_counter()

    process_time = end_time - start_time

    print(
        f"{request.method} {request.url.path} "
        f"-> {process_time:.4f} seconds"
    )

    return response