"""
to install simpy
in terminal write--> pip install simpy


SimPy Cheatsheet - A Complete Guide with Explanations
-----------------------------------------------------
SimPy is a discrete-event simulation library that helps model real-world systems 
like factories, networks, and service stations.

This script demonstrates:
✅ Creating and running a SimPy environment
✅ Using processes and events
✅ Managing shared resources
✅ Handling priority and preemptive resources
✅ Using stores for object management
"""

# Import the SimPy library
import simpy
import random

# --------------------------------------------
# 1️⃣ CREATING A SIMULATION ENVIRONMENT
# --------------------------------------------
def my_process(env):
    """A simple process that starts, waits for 5 time units, and then finishes."""
    print(f'Process started at {env.now}')  # Print the start time
    yield env.timeout(5)  # Pause for 5 time units
    print(f'Process finished at {env.now}')  # Print the finish time

# Create a SimPy environment
env = simpy.Environment()

# Add the process to the environment and run it
env.process(my_process(env))
env.run()


# --------------------------------------------
# 2️⃣ MODELING RANDOM ARRIVALS
# --------------------------------------------
def random_arrival(env):
    """Simulates a system where customers arrive at random intervals."""
    while True:
        arrival_time = random.randint(1, 5)  # Random arrival every 1-5 time units
        yield env.timeout(arrival_time)
        print(f'New customer arrived at {env.now}')

# Reset environment and run simulation for 20 time units
env = simpy.Environment()
env.process(random_arrival(env))
env.run(until=20)


# --------------------------------------------
# 3️⃣ USING RESOURCES (LIMITED AVAILABILITY)
# --------------------------------------------
def use_resource(env, resource, name):
    """Models a process that needs to access a shared resource."""
    with resource.request() as req:
        yield req  # Wait until the resource is available
        print(f'{name} acquired the resource at {env.now}')
        yield env.timeout(3)  # Use the resource for 3 time units
        print(f'{name} released the resource at {env.now}')

env = simpy.Environment()
resource = simpy.Resource(env, capacity=2)  # Create a resource with 2 slots

# Start multiple processes that will compete for the resource
for i in range(5):
    env.process(use_resource(env, resource, f'Process-{i}'))

env.run()


# --------------------------------------------
# 4️⃣ HANDLING PRIORITY REQUESTS
# --------------------------------------------
def priority_process(env, resource, name, priority):
    """Processes with different priorities request access to a shared resource."""
    with resource.request(priority=priority) as req:
        yield req  # Wait for the resource
        print(f'{name} (priority {priority}) started at {env.now}')
        yield env.timeout(2)
        print(f'{name} (priority {priority}) finished at {env.now}')

env = simpy.Environment()
priority_resource = simpy.PriorityResource(env, capacity=1)

# Start processes with different priority levels
env.process(priority_process(env, priority_resource, 'LowPriority', priority=2))
env.process(priority_process(env, priority_resource, 'HighPriority', priority=1))

env.run()


# --------------------------------------------
# 5️⃣ PREEMPTIVE RESOURCES (INTERRUPTION)
# --------------------------------------------
def preemptive_task(env, resource, name, priority):
    """Simulates a process that may be interrupted if a higher-priority task arrives."""
    with resource.request(priority=priority) as req:
        yield req  # Wait for the resource
        print(f'{name} (priority {priority}) started at {env.now}')
        yield env.timeout(4)
        print(f'{name} (priority {priority}) finished at {env.now}')

env = simpy.Environment()
preemptive_resource = simpy.PreemptiveResource(env, capacity=1)

# Start a low-priority task, then add a high-priority one
env.process(preemptive_task(env, preemptive_resource, 'LowPriority', priority=2))
env.process(preemptive_task(env, preemptive_resource, 'HighPriority', priority=1))

env.run()


# --------------------------------------------
# 6️⃣ INTERRUPTING A PROCESS
# --------------------------------------------
def interruptible_process(env):
    """A process that gets interrupted before finishing."""
    try:
        print(f'Process started at {env.now}')
        yield env.timeout(10)  # Trying to work for 10 time units
    except simpy.Interrupt:
        print(f'Process was interrupted at {env.now}')

env = simpy.Environment()
proc = env.process(interruptible_process(env))
env.timeout(5)  # Let time pass
proc.interrupt()  # Interrupt the process
env.run()


# --------------------------------------------
# 7️⃣ WORKING WITH EVENTS
# --------------------------------------------
def event_listener(env, event):
    """Waits for an event to happen."""
    yield event  # Wait until the event is triggered
    print(f'Event occurred at {env.now}')

env = simpy.Environment()
event = env.event()  # Create an event

env.process(event_listener(env, event))  # Start process waiting for event
env.timeout(5)  # Let time pass
event.succeed()  # Trigger the event
env.run()


# --------------------------------------------
# 8️⃣ USING STORES (WAREHOUSE-LIKE SYSTEMS)
# --------------------------------------------
def store_example(env, store):
    """Stores and retrieves items from a SimPy Store."""
    yield store.put('Item-A')  # Add an item to the store
    print(f'Item stored at {env.now}')
    
    item = yield store.get()  # Retrieve an item
    print(f'Item {item} retrieved at {env.now}')

env = simpy.Environment()
store = simpy.Store(env)  # Create a store

env.process(store_example(env, store))
env.run()


# --------------------------------------------
# 9️⃣ FILTERING ITEMS IN A STORE
# --------------------------------------------
def filter_example(env, store):
    """Uses a FilterStore to retrieve only specific items."""
    yield store.put('apple')
    yield store.put('banana')
    
    def is_banana(item):
        return item == 'banana'
    
    banana = yield store.get(is_banana)  # Get only 'banana'
    print(f'Retrieved: {banana} at {env.now}')

env = simpy.Environment()
filter_store = simpy.FilterStore(env)

env.process(filter_example(env, filter_store))
env.run()


# --------------------------------------------
# 🔟 CUSTOMIZING ENVIRONMENTS WITH INITIAL TIME
# --------------------------------------------
env = simpy.Environment(initial_time=100)  # Start the simulation from time 100

def delayed_process(env):
    print(f'Process starts at {env.now}')
    yield env.timeout(5)
    print(f'Process finishes at {env.now}')

env.process(delayed_process(env))
env.run()


# --------------------------------------------
# ✅ SUMMARY
# --------------------------------------------
"""
✅ How to create and run a SimPy environment.
✅ How to model random arrivals.
✅ How to manage shared resources.
✅ How to handle priority and preemptive resources.
✅ How to interrupt a process.
✅ How to use events in SimPy.
✅ How to store and retrieve objects.
✅ How to filter specific objects in a store.
"""

print("\n🎉 SimPy Cheatsheet Execution Complete! 🚀")
