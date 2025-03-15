'''
==================================================
7️⃣ Toll Booth Simulation
==================================================
📌 Scenario:
A highway toll booth serves cars that arrive randomly. 
Each car takes 5 seconds to pass. If the booth is occupied, cars must wait in line.

🔹 **Concepts Used:** 
   - Resource (to represent the toll booth)
   - Timeout (to simulate the time it takes for a car to pass)
   - Process (to simulate the arrival of cars)

🧠 **Think About It!**
Before looking at the solution, try to answer:
1. How do you simulate cars arriving at random intervals?
2. How do you ensure that only one car can pass the toll booth at a time?
3. How do you simulate the time each car takes to pass?

🛠 **Try to complete this yourself, then check the solution below!** 🛠

==================================================
✅ Solution
==================================================
'''

# Import required libraries
import simpy
import random

# Create a SimPy environment
env = simpy.Environment()

# Create a shared resource (the toll booth) with capacity = 1 (only one car can pass at a time)
toll_booth = simpy.Resource(env, capacity=1)

# Define a function to simulate cars passing through the toll booth
def car_pass(name, toll_booth):
    # Simulate arrival at random intervals (1-3 seconds)
    yield env.timeout(random.randint(1, 3))
    print(f'[Time {env.now}] {name} arrives at the toll booth')
    
    # Request the toll booth resource
    with toll_booth.request() as req:
        yield req  # Wait for the toll booth to be available
        print(f'[Time {env.now}] {name} starts passing through the toll booth')
        
        # Simulate the time it takes each car to pass (5 seconds)
        yield env.timeout(5)
        print(f'[Time {env.now}] {name} finishes passing through the toll booth')

# Create and process 5 cars passing through the toll booth
for i in range(1, 6):
    env.process(car_pass(f'Car {i}', toll_booth))

# Run the simulation
env.run()  # Run the simulation until all cars have passed through the toll booth
