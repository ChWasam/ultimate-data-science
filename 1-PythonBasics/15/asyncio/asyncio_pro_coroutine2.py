import asyncio

# Define a coroutine that simulates a time-consuming task
async def fetch_data(delay, id):
    print("Fetching data... id:" , id)
    await asyncio.sleep(delay) # Simulate an I/0 operation with a sleep
    print("Data fetched, id:", id)
    return {"data": "Some data", "id": id} # Return some data


# Define another coroutine that calls the first coroutine
async def main():
    task1 = fetch_data(2, 1)
    task2 = fetch_data(2, 2)
    result1 = await task1
    print (f"Received result: {result1}")
    result2 = await task2
    print (f"Received result: {result2}")


# Run the main coroutine
asyncio. run (main ())

#  Tasks are still not concurrent because they are still taking 4 sec. They should take 2 sec 
#  Means we haven't really got any performance benefits here 
#  we need to create tasks inorder to speed up the process and run both of these tasks at the same time 