import asyncio
from time import time

async def start_strongman(name, power):

    print(f'Силач {name} начал соревнование')
    for i in range(5):
        await asyncio.sleep(power)
        print(f'Силач {name} поднял шар №{i+1}')

    print(f'Силач {name} закончил соревнование')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Pavel', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task1
    await task2
    await task3


start = time()
asyncio.run(start_tournament())
finish = time()
print(f'Время работы: {finish - start}')
