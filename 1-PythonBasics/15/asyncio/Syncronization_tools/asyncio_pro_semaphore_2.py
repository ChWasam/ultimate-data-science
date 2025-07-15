# The code demonstrates how to use a semaphore to limit the number of tasks that can access a resource concurrently.
#  Think of a semaphore as a gatekeeper that allows only a certain number of tasks (e.g., 2) to proceed at the same time.
#  In this case, the code simulates accessing a "resource" (like a database or a file) for five tasks but restricts it so only two can access it simultaneously.


# Works very similar to lock however it allows multiple coroutines to have access to same object at the same time 
#  We can decide how many we want that to be and the eventlooop will automatically handle it 
# So it is possible that we send a bunch of different network requests we can do few at the same time or we can't do may be 1000 or 10000 at the same time 

import asyncio

async def access_resource (semaphore, resource_id):
    async with semaphore:
        # Simulate accessing a limited resource
        print (f"Accessing resource {resource_id}")
        await asyncio.sleep (1)
        # Simulate work with the resource
        print (f"'Releasing resource {resource_id}")

async def main():
    semaphore = asyncio.Semaphore(2) # Allow 2 concurrent accesses
    await asyncio.gather(*(access_resource(semaphore, i) for i in range (5)))

asyncio. run (main( ))


# How It All Works Together
# The program starts with asyncio.run(main()), which calls the main function.
# In main, a semaphore is created to allow only 2 tasks to access the resource at a time.
# Five tasks are created (with resource_id from 0 to 4) and passed to asyncio.gather to run concurrently.
# Each task tries to access the resource by entering the async with semaphore block:
# Only 2 tasks can enter at a time because of the semaphore’s limit.
# Each task prints “Accessing resource X,” waits for 1 second, then prints “Releasing resource X.”
# When a task finishes, it releases the semaphore, allowing another task to start.
# The program continues until all 5 tasks are complete.


# result

# Accessing resource 0
# Accessing resource 1
# 'Releasing resource 0
# 'Releasing resource 1
# Accessing resource 2
# Accessing resource 3
# 'Releasing resource 2
# 'Releasing resource 3
# Accessing resource 4
# 'Releasing resource 4