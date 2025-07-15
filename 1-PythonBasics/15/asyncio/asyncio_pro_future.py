#  This code will never be used by the developer 
#  You might will see written somewhere so thta you will be able to understand it 


#  It is a promise of a future result 
#  Result is to come in the future 
#  you don't know exactly when that is going to be 
#  Here we will actually create a future and we await its value 
#  What we do is we actually get the event loop 



import asyncio

async def set_future_result (future, value):
    await asyncio.sleep (2)
    # Set the result of the future
    future.set_result (value)
    print(f"Set the future's result to: {value}")


async def main():
    # Create a future object
    loop = asyncio.get_running_loop()
    future = loop.create_future()
    # Schedule setting the future's result
    asyncio.create_task(set_future_result(future, "Future result is ready"))



    # Wait for the future's result
    result = await future
    # We didn't awaited for thr task to finish we awaited the future object 
    # So inside the task we set the value of the future and here we awaited that 
    #  which means that as soon as we get the value of the future the coroutine may or may not be complete
    # This is slightly different from using a task 
    # When we use a future we are just waiting for some value to be available we are waiting for an entire coroutine to finish  
    print(f"Received the future's result: {result}")

asyncio.run(main())