#  It is little more basic and allows us to do simpler syncronization
#  The code demonstrates how to use an asyncio.Event to coordinate between two asynchronous tasks.
# The goal is to show how one task (waiter) waits for an event to be triggered by another task (setter) using an asyncio.Event object.
import asyncio


async def waiter (event):
    print("waiting for the event to be set")
    await event.wait()
    print("event has been set, continuing execution")


async def setter(event):
    await asyncio.sleep(2) # Simulate doing some work
    event.set()
    print("event has been set!")


#  Start with waiter then move to setter. When event is set then again move to waiter to complete the task 

async def main():
    event= asyncio.Event()
    # Here we create an event 
    await asyncio.gather(waiter(event), setter(event) )
    # We can await the event to be set and then we set the event 
    #  event.set() => This acts as a simple boolean flag and allow us to block other areas of code until we set this to be true 

asyncio.run(main( ))

#  Another premitive thing is condition but it is very complex 


# Result 
# waiting for the event to be set
# event has been set!
# event has been set, continuing execution