'''
==================================================
9️⃣ Bank Loan Processing
==================================================
📌 Scenario:
Customers apply for loans. If they have high priority, their request is processed faster. 
Otherwise, they wait. Simulate loan approvals for different customers.

🔹 **Concepts Used:** 
   - PriorityResource (to handle priority processing)
   - Timeout (to simulate the loan processing time)
   - Process (to simulate each customer's loan request)
   - Queue (to simulate the waiting line for lower priority customers)

🧠 **Think About It!**
Before looking at the solution, try to answer:
1. How do you handle different priority levels for customers?
2. How do you ensure that higher priority customers are processed first?
3. How do you simulate the time it takes to process each loan?

🛠 **Try to complete this yourself, then check the solution below!** 🛠

==================================================
✅ Solution
==================================================
'''

# Import required libraries
import simpy
import random

# Create the simulation environment
env = simpy.Environment()
# PriorityResource is used to manage which customer gets processed first
priority_resource = simpy.PriorityResource(env, capacity=1)

# Bank loan processing function
def process_loan(env, customer_id, priority_level, priority_resource):
    # Show when a customer arrives and with what priority
    print(f"[time: {env.now}] Customer {customer_id} arrives with priority {priority_level}")

    # Request loan with the given priority
    with priority_resource.request(priority=priority_level) as request:
        yield request  # Wait for the turn to be processed
        print(f"[time: {env.now}] Customer {customer_id} is being processed")

        # Simulate loan processing time
        processing_time = random.randint(1, 5)  # Random processing time between 1 and 5 minutes
        yield env.timeout(processing_time)

        # Once processed, show the result
        print(f"[time: {env.now}] Customer {customer_id} is approved. Processed in {processing_time} minutes.")

# Random arrival function
def random_arrival(env, priority_resource):
    customer_id = 1
    while True:
        arrival_time = random.randint(1, 3)  # Random arrival every 1-3 time units
        yield env.timeout(arrival_time)  # Wait for the arrival time
        priority_level = random.randint(1, 5)  # Random priority between 1 and 5 (1- highest priority ; 5 - lowest priority)
        env.process(process_loan(env, customer_id, priority_level, priority_resource))  # Start processing the loan
        customer_id += 1



# Start the random arrival process
env.process(random_arrival(env, priority_resource))
# Run the simulation for 20 time units
env.run(until=20)
