#  Let's say we have a shared resource (database, table , file or anything else )
#  we wanna make sure that no 2 coroutines are working on it at the same time as it can lead to an error 
#  We wanna really wait for one entire operation to finish for the next one completes 
#  we wanna lock it off and is only be using it from one coroutine at a time 
#  so we create a lock 
#  when we create a lock we have the ability to acquire the lock and we do that with this code "async with lock:"





import asyncio


# A  shared variable shared_resource
shared_resource = 0
# shared_resource measn => May be it is a database it is a table or it is a file anything 
#  We wanna make sure that no two coroutines are working on it on the same time 
#  If two coroutines are modifying the same file we could get some kind of error 
#  idea is to lock it off and only be using one coroutine at a time 
#  For the we create a lock 

# An asyncio Lock
lock = asyncio.Lock()



async def modify_shared_resource():
    global shared_resource
    #  The acquire a above given lock we we use the below given code 
    async with lock:
        # async context manager (async with lock)=> it will check if any other coroutine is using the lock
        # if it is , then it is going to w8 untill that coroutine is finish 
        #  If it is not then then it will come into this block of code 
        #  The idea is whatever we put inside this context manager needs to finish executing before the lock will be realeased 

        #  here we are saying that we want all of this to finish before we realease the lock 

        # Critical section starts
        print(f"Resource before modification: {shared_resource}")
        shared_resource += 1 # Modify the shared resource 
        await asyncio.sleep (1)
        # Simulate an I0 operation
        print (f"Resource after modification: {shared_resource}")
        # Critical section ends


async def main():
    await asyncio.gather(*(modify_shared_resource() for _ in range(5)))
    # Effect: The * unpacks the 5 coroutines from the generator expression, effectively turning asyncio.gather(*(modify_shared_resource() for _ in range(5))) into something like asyncio.gather(coroutine1, coroutine2, coroutine3, coroutine4, coroutine5).



asyncio.run(main())

#  The idea is eventhough we executed the coroutines concurrently we are locking their access to this  resource => shared_resource so that one could be accessing it at the time 






#  Complete  Execution and Behavior
# When you run this code, here's what happens:

# The main function creates 5 coroutines, each calling modify_shared_resource.
# These 5 coroutines run concurrently, meaning they all start at the same time, but because of the lock, only one can enter the critical section at a time.
# The first coroutine acquires the lock, prints "Resource before modification: 0", increments shared_resource to 1, waits for 1 second (due to await asyncio.sleep(1)), prints "Resource after modification: 1", and then releases the lock.
# While the first coroutine is waiting for 1 second, the other 4 coroutines are waiting for the lock, so they can't proceed yet.
# Once the first coroutine releases the lock, the second coroutine acquires it and repeats the process (prints 1, increments to 2, waits, prints 2).
# This continues until all 5 coroutines have completed their critical sections.
# The total time to run the program is approximately 5 seconds, because each coroutine holds the lock for about 1 second, and they can't overlap in the critical section.






# Result 

# Resource before modification: 0
# Resource after modification: 1
# Resource before modification: 1
# Resource after modification: 2
# Resource before modification: 2
# Resource after modification: 3
# Resource before modification: 3
# Resource after modification: 4
# Resource before modification: 4
# Resource after modification: 5







# # A simple function that takes multiple arguments
# def print_names(name1, name2, name3):
#     print(name1, name2, name3)

# # A list of names
# names = ["Alice", "Bob", "Charlie"]

# # Without unpacking
# print_names(names)  # Error: expects 3 arguments, got 1 (the whole list)

# # With unpacking
# print_names(*names)  # Works: prints "Alice Bob Charlie"