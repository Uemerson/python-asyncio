from asyncio import TaskGroup, run, sleep

async def agen():
  for val in range(10):
    yield val

async def coro(val):
  from random import randint
  await sleep(randint(1, 3))
  print(val)

async def main():
  async with TaskGroup() as tg:
    [tg.create_task(coro(val)) async for val in agen()]
    tg.create_task(coro(99))

run(main())