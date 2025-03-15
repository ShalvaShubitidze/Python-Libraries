'''
==================================================
3️⃣ Bakery Order System
==================================================
📌 Scenario:
A bakery receives 3 customer orders. Each order takes 4 minutes to prepare. 
The bakery can only handle one order at a time.

🔹 **Concepts Used:** 
   - Resource (to represent the bakery's capacity)
   - Process (to simulate customer orders)
   - Timeout (to simulate time delays)
'''

'''
🧠 **Think About It!**
Before looking at the solution, try to answer:
1. How do you make sure only one customer can order at a time?
2. How do you simulate the order preparation and baking time?
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

# Create a shared resource (bakery) with capacity = 1
# Only one customer can place an order at a time since the bakery's capacity is 1.
bakery = simpy.Resource(env, capacity=1)

# Define a function to simulate customer orders
def customer_order(env, name, bakery):
    # Simulate the customer arrival at random intervals (1-5 minutes)
    yield env.timeout(random.randint(1, 5))  # Random arrival time
    
    print(f'{name} placed an order at time {env.now}')
    
    # Request the bakery resource
    with bakery.request() as req:
        yield req  # Wait for bakery to be available
        print(f'{name} started preparing the order at time {env.now}')
        # Simulate the 4-minute order preparation time
        yield env.timeout(4)  

        print(f'{name} order baked and ready at time {env.now}')

# Create and process 3 customer orders with random arrivals
for i in range(1, 4):
    env.process(customer_order(env, f'Customer {i}', bakery))

# Run the simulation
env.run()  # Run the simulation until all customers are served
