import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

'''
_executor = ThreadPoolExecutor(1)

def sync_blocking():
    time.sleep(2)

async def hello_world():
    await loop.run_in_executor(_executor, sync_blocking)

loop = asyncio.get_event_loop()
loop.run_until_complete(hello_world())
loop.close()
'''
_executor = ThreadPoolExecutor(1)
async def hello(v1):
    print("do some action")

loop = asyncio.get_event_loop()
loop.run_until_complete(hello(''))
loop.close()

