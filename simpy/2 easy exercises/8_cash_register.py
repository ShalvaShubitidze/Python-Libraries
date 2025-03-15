'''
==================================================
8️⃣ Cash Register in a Store
==================================================
📌 Scenario:
A store has one cash register. Each customer takes 4 minutes to check out. 
There are 5 customers in line. Customers must wait their turn.

🔹 **Concepts Used:** 
   - Resource (to represent the cash register)
   - Timeout (to simulate the checkout time)
   - Process (to simulate each customer taking their turn)

🧠 **Think About It!**
Before looking at the solution, try to answer:
1. How do you simulate customers arriving in line?
2. How do you ensure that only one customer can use the cash register at a time?
3. How do you simulate the checkout time for each customer?

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

# Create a shared resource (the cash register) with capacity = 1 (only one customer can check out at a time)
cash_register = simpy.Resource(env, capacity=1)

# Define a function to simulate customers checking out
def customer_checkout(name, cash_register):
    # Simulate arrival at random intervals (1-3 minutes)
    yield env.timeout(random.randint(1, 3))
    print(f'[Time {env.now}] {name} arrives at the cash register')
    
    # Request the cash register resource
    with cash_register.request() as req:
        yield req  # Wait for the cash register to be available
        print(f'[Time {env.now}] {name} starts checking out')
        
        # Simulate the checkout time for each customer (4 minutes)
        yield env.timeout(4)
        print(f'[Time {env.now}] {name} finishes checking out')

# Create and process 5 customers checking out
for i in range(1, 6):
    env.process(customer_checkout(f'Customer {i}', cash_register))

# Run the simulation
env.run()  # Run the simulation until all customers have checked out
