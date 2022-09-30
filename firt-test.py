from asyncio import TaskGroup, run, sleep

async def coro(arg):
  print(f'start the CORO: {arg=}')
  await sleep(1)
  print(f'finished the CORO: {arg=}')

async def second_coro():
  print(f'start the second CORO')
  await sleep(10)
  print(f'finished the second CORO')
  return 1

async def main():
  async with TaskGroup() as tg:
    task = tg.create_task(second_coro())
    task_result = await task

    tg.create_task(coro(task_result))
    tg.create_task(coro(2))
    tg.create_task(coro(3))
    tg.create_task(coro(4))
    tg.create_task(coro(5))

run(main())