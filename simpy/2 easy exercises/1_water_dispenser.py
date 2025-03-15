'''
==================================================
1️⃣ Water Dispenser Simulation
==================================================
📌 Scenario:
Simulate a **water dispenser** that takes **2 seconds** to fill a cup. 
There are **5 people** waiting in line. Each person **waits** until the dispenser is available.

🔹 **Concepts Used:** 
   - Resource (to represent the dispenser)
   - Timeout (to simulate time delays)
   - Process (to represent customers)
'''

'''
🧠 **Think About It!**
Before looking at the solution, try to answer:
1. How do you create a **shared resource** that only **one person** can use at a time?
2. How do you make customers arrive at different times?
3. How can you simulate the **time delay** for filling the cup?
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

# Create a shared resource (water dispenser) with capacity = 1
dispenser = simpy.Resource(env, capacity=1)

# Define a function to simulate a customer using the dispenser
def customer(env, name, dispenser):
    print(f'[Time {env.now}] {name} arrives at the water dispenser')

    # Request access to the dispenser
    with dispenser.request() as req:
        yield req  # Wait for the dispenser to be available
        print(f'[Time {env.now}] {name} starts filling the cup')

        # Simulate the 2-second filling process
        yield env.timeout(2)  
        print(f'[Time {env.now}] {name} leaves with a full cup')

# Function to generate customers with random arrival times
def generate_customers(env, num_customers):
    for i in range(1, num_customers + 1):
        yield env.timeout(random.randint(1, 3))  # Stagger arrival by 1-3 seconds
        env.process(customer(env, f'Customer {i}', dispenser))

# Start generating 5 customers with random arrival times
env.process(generate_customers(env, 5))

# Run the simulation for 20 time units
env.run(until=20)

