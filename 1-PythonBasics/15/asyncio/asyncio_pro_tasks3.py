#  Worst thing about gather is that it is not as good at error handling and it is not going to cancel other coroutines if one of them to fail,so
# it could get some weired state in the application  


#  Task Group  has build in error handling so it is preffered over gather 

#  If any task fails (raises an exception), the TaskGroup cancels all other tasks in the group and propagates the exception, ensuring proper cleanup.

# When exiting the async with block (either normally or due to an exception), the TaskGroup ensures all tasks complete or are canceled. It waits for all tasks to finish and handles any exceptions that occur.

# If any task raises an unhandled exception, the TaskGroup cancels all other tasks and raises an asyncio.exceptions.TaskGroupError containing the exceptions.

# async with asyncio.TaskGroup() as tg:

# This creates a TaskGroup context. Inside this block, tasks are created using _tg.create_task(fetch_data(i, sleep_time)), and the TaskGroup ensures all tasks complete before exiting the block. 
# The tasks run concurrently, and their results can be accessed after the block.



# enumerate(iterable, start=0) takes an iterable (e.g., a list) and returns an iterator of tuples, where each tuple contains an index (starting from start) and the corresponding element from the iterable.
# By default, the index starts at 0, but you can customize it with the start parameter.



#  async is used in " async with asyncio.TaskGroup() as tg: "because TaskGroup is an asynchronous context manager, requiring asynchronous handling.
# Research suggests that without async, the code would fail with an error, as TaskGroup does not support synchronous context management.

# Why Use async with asyncio.TaskGroup?
# The async keyword is essential in async with asyncio.TaskGroup() as tg: because asyncio.TaskGroup is designed as an asynchronous context manager.
#  This means it uses coroutines (__aenter__ and __aexit__) for setup and cleanup, which must be handled asynchronously.
#  Using async with ensures tasks are properly awaited and managed, especially for concurrent operations.



# What Happens Without async?
# If you omit async and use a regular with statement, the code will likely raise an AttributeError because TaskGroup lacks the synchronous __enter__ and __exit__ methods. 
# This mismatch means you cannot use TaskGroup in a synchronous context, as it is built for asynchronous programming.



import asyncio

async def fetch_data(id, sleep_time):
    print (f"Coroutine {id} starting to fetch data.") 
    await asyncio.sleep(sleep_time) # Simulate a network request or IO operation
    return {"id": id, "data": f"Sample data from coroutine {id}"}
        

async def main():
    tasks = []
    # TaskGroup is an asynchronous context manager, requiring asynchronous handling.
    async with asyncio.TaskGroup() as tg:
        # asyncio.TaskGroup() provides build in error handling 
        # if any of the tasks inside TaskGroup fails it automatically cancels all the other tasks 
        # Helps in large applications where we want to be more robust 
        for i, sleep_time in enumerate([ 1, 2, 3], start=1):
            task = tg.create_task(fetch_data(i, sleep_time))
            tasks.append(task)

    # After the Task Group block, all tasks have completed
    print(tasks[0])
    results = [ task.result() for task in tasks]
    for result in results:
        print (f"Received result: {result}")


asyncio.run(main())

# Result 

# Coroutine 1 starting to fetch data.
# Coroutine 2 starting to fetch data.
# Coroutine 3 starting to fetch data.
# Received result: {'id': 1, 'data': 'Sample data from coroutine 1'}
# Received result: {'id': 2, 'data': 'Sample data from coroutine 2'}
# Received result: {'id': 3, 'data': 'Sample data from coroutine 3'}






















