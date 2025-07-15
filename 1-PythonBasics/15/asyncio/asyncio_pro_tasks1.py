import asyncio

async def fetch_data(id, sleep_time):
    print (f"Coroutine {id} starting to fetch data.") 
    await asyncio.sleep(sleep_time)
    print(f"coroutine has fetched data for id: {id}")
    return {"id": id, "data": f"Sample data from coroutine {id}"}

async def main():
# Create tasks for running coroutines concurrently
    # Task: A wrapper around a coroutine that schedules it to run in the event loop.
    task1 = asyncio.create_task(fetch_data(1, 1))
    task2 = asyncio.create_task(fetch_data(2,3))
    task3 = asyncio.create_task(fetch_data(3,5))

    #  execution doesn't depend on await. whoever will have less delay the remaining execution will happen first 

    result1 = await task1 # main() reaches await task1, which pauses main() until task1 completes.
    result2 = await task2
    print("wasam")
   
    result3 = await task3
 
    #  If we do wanna wait for one task to finish before moving on to the next one  we can use the await syntax  
   
    task4 = asyncio.create_task(fetch_data(4,1))
    # Creates a new task for fetch_data(4, 1) and schedules it.
    result4 = await task4
    #  Won't start the 4th one untill 1 , 2 and 3 are done 


#  those you want to run asyncronously, create task for them together 
#  those you want to run syncronously, create task for them seperates from other  

    print(result1, result2, result3, result4)

asyncio.run (main ())

# asyncio.run: Creates a new event loop, runs the specified coroutine (main() in this case), and closes the loop when done.
