import asyncio

async def fetch_data(id, sleep_time):
    print (f"Coroutine {id} starting to fetch data.") 
    await asyncio.sleep(sleep_time)
    print(f"coroutine has fetched data for id: {id}")
    return {"id": id, "data": f"Sample data from coroutine {id}"}

async def main():
    #  Quick way to concurrently run multiple coroutines 
    # Run coroutines concurrently and gather their return values
    results = await asyncio.gather(fetch_data(1, 2), fetch_data(2, 1), fetch_data (3, 3))
    # Process the results
    for result in results:
        print(f"Received result: {result}")

asyncio.run (main ())

# asyncio.run: Creates a new event loop, runs the specified coroutine (main() in this case), and closes the loop when done.


#  Worst thing about gather is that it is not as good at error handling and it is not going to cancel other coroutines if one of them to fail,so
# it could get some weired state in the application  


#  Task Group  has build in error handling so it is preffered over gather 