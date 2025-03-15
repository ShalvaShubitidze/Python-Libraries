'''
==================================================
9️⃣ Cinema Ticket Counter
==================================================
📌 Scenario:
A cinema has 1 ticket counter. Customers arrive every 2 minutes, and each transaction takes 3 minutes. 
If the counter is busy, customers must wait.

🔹 **Concepts Used:** 
   - Resource (to simulate the ticket counter)
   - Timeout (to simulate the transaction time)
   - Process (to simulate each customer's arrival and transaction)

🧠 **Think About It!**
Before looking at the solution, try to answer:
1. How do you handle multiple customers when the ticket counter is busy?
2. How do you simulate the time it takes for each customer to buy a ticket?
3. How do you ensure customers wait their turn?

🛠 **Try to complete this yourself, then check the solution below!** 🛠

==================================================
✅ Solution
==================================================
'''

import simpy


# Create the simulation environment
env = simpy.Environment()
# The ticket counter is a resource with capacity 1 (only 1 customer can be served at a time)
ticket_counter = simpy.Resource(env, capacity=1)

# Function to simulate the customer process
def customer(env, customer_id, ticket_counter):
    # When the customer arrives
    print(f"[time: {env.now}] Customer {customer_id} arrives and starts waiting for the ticket counter.")
    
    # Request the ticket counter (it can only serve one customer at a time)
    with ticket_counter.request() as request:
        yield request  # Wait for the ticket counter to be available
        print(f"[time: {env.now}] Customer {customer_id} is being served.")
        
        # Simulate the transaction time (3 minutes)
        transaction_time = 3
        yield env.timeout(transaction_time)
        print(f"[time: {env.now}] Customer {customer_id} has bought the ticket. Transaction took {transaction_time} minutes.")

# Function to simulate customer arrivals
def customer_arrival(env, ticket_counter):
    customer_id = 1
    while True:
        yield env.timeout(2)  # Customers arrive every 2 minutes
        env.process(customer(env, customer_id, ticket_counter))  # Start the process for the arriving customer
        customer_id += 1


# Start the customer arrival process
env.process(customer_arrival(env, ticket_counter))
# Run the simulation for 20 time units
env.run(until=20)