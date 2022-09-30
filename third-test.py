from asyncio import TaskGroup, run, sleep
from random import randint

async def agen():
  for val in range(10):
    yield val

async def coro(val):
  r = randint(1, 3)
  await sleep(r)
  match r:
    case 1:
      raise TypeError()
    case 2:
      print('sucess!')
    case _:
      raise KeyError()

  print(val)

async def main():
  async with TaskGroup() as tg:
    [tg.create_task(coro(val)) async for val in agen()]
    tg.create_task(coro(99))

run(main())