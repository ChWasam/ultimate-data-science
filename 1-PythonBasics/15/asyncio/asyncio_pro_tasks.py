import asyncio

async def fetch_data(id, sleep_time):
    print (f"Coroutine {id} starting to fetch data.") 
    await asyncio.sleep(sleep_time)
    return {"id": id, "data": f"Sample data from coroutine {id}"}

async def main():
# Create tasks for running coroutines concurrently

    # create_task is yeh ho ga kah jab bhi ausa time mila ga to yeh chal jai ga 
    task1 = asyncio.create_task(fetch_data (1, 2)) # The other code will run according to its number in a flow but create_task  will schedule it in a way that it start executing it in the backward and as soon as it is done it will stop the next code to execute and take the turn instead  
    task2 = asyncio.create_task(fetch_data(2,3))
    task3 = asyncio.create_task(fetch_data(3,1))

    result1 = await task1
    result2 = await task2
    result3 = await task3

    print(result1, result2, result3)

asyncio. run (main ())

#  It is going to take 3 sec in total 