import asyncio
import time
import httpx


BASE_URL = "http://127.0.0.1:8000"

NUMBER_OF_REQUESTS = 5


# --------------------------------
# Synchronous Test
# Requests run one by one
# --------------------------------

async def test_sync():

    async with httpx.AsyncClient() as client:

        start = time.perf_counter()

        for _ in range(NUMBER_OF_REQUESTS):

            await client.get(
                f"{BASE_URL}/api/v1/sync"
            )

        end = time.perf_counter()

        return end - start


# --------------------------------
# Asynchronous Test
# Requests run concurrently
# --------------------------------

async def test_async():

    async with httpx.AsyncClient() as client:

        start = time.perf_counter()

        tasks = [
            client.get(
                f"{BASE_URL}/api/v1/async"
            )
            for _ in range(NUMBER_OF_REQUESTS)
        ]

        await asyncio.gather(*tasks)

        end = time.perf_counter()

        return end - start


# --------------------------------
# Run Benchmark
# --------------------------------

async def main():

    print("Running Sync Test...")

    sync_time = await test_sync()

    print("Running Async Test...")

    async_time = await test_async()

    print("\n-----------------------------")
    print("Performance Results")
    print("-----------------------------")

    print(
        f"Sync Time  : {sync_time:.2f} seconds"
    )

    print(
        f"Async Time : {async_time:.2f} seconds"
    )

    improvement = (
        (sync_time - async_time)
        / sync_time
    ) * 100

    print(
        f"Improvement: {improvement:.2f}%"
    )


asyncio.run(main())