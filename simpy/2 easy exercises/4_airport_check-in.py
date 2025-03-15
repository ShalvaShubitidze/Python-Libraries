'''
==================================================
4️⃣ Airport Check-in Simulation
==================================================
📌 Scenario:
An airport has 2 check-in counters. Passengers arrive randomly and queue up. 
Each check-in takes 6 minutes, and only one passenger can be served per counter at a time.

🔹 **Concepts Used:** 
   - Resource (to represent the check-in counters)
   - Timeout (to simulate time delays like arrival and check-in)
   - Process (to simulate the passengers' actions)
'''

'''
🧠 **Think About It!**
Before looking at the solution, try to answer:
1. How can we ensure passengers are served at a check-in counter one at a time, even when there are multiple counters?
2. How do we simulate random arrival times for passengers at the airport?
3. How can we manage the time passengers spend in the queue and checking in?
'''

'''
🛠 **Try to complete this yourself, then check the solution below!** 🛠
'''

'''
==================================================
✅ Solution
==================================================
'''

# Import required libraries
import simpy
import random

# Create a SimPy environment
env = simpy.Environment()

# Create a shared resource (check-in counters) with capacity = 2
counter = simpy.Resource(env, capacity=2)

# Define a function to simulate passenger arrivals and check-ins
def arrival(env, name, counter):
    # Simulate the random arrival time of passengers (1-5 minutes apart)
    yield env.timeout(random.randint(1, 5))  # Random arrival time
    print(f'[Time {env.now}] {name} arrives at the airport and waits in line.')

    # Request a check-in counter
    with counter.request() as req:
        yield req  # Wait for an available counter
        print(f'[Time {env.now}] {name} enters the queue.')

        # Simulate the 6-minute check-in process
        yield env.timeout(6)  
        print(f'[Time {env.now}] {name} checks in.')

# Create and process 10 passenger arrivals with random times
for i in range(10):
    env.process(arrival(env, f'Passenger {i+1}', counter))

# Run the simulation
env.run()  # Run the simulation until all passengers are served
