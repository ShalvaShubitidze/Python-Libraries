'''
==================================================
5️⃣ Printer Queue Simulation
==================================================
📌 Scenario:
Three users are waiting for a shared printer. 
Each print job takes between 3-6 minutes to complete. 
If the printer is busy, the user must wait.

🔹 **Concepts Used:** 
   - Resource (to represent the shared printer)
   - Timeout (to simulate waiting time and printing duration)
   - Randomization (to simulate varying print job durations)
'''

'''
🧠 **Think About It!**
Before looking at the solution, try to answer:
1. How can we ensure users wait for the printer if it's already in use?
2. How do we simulate random print job durations?
3. What will happen if two or more users try to access the printer at the same time?
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

# Create a shared resource (printer) with capacity = 1 (only one user can print at a time)
printer = simpy.Resource(env, capacity=1)

# Define a function to simulate print jobs
def print_job(name, printer):
    # Simulate a random arrival time (1-3 minutes)
    yield env.timeout(random.randint(1, 3))  
    print(f'[Time {env.now}] {name} arrives at the printer')
    
    # Request the printer resource
    with printer.request() as req:
        yield req  # Wait for the printer to be available
        print(f'[Time {env.now}] {name} starts printing')
        
        # Simulate the printing process (3-6 minutes)
        print_duration = random.randint(3, 6)
        yield env.timeout(print_duration)  
        print(f'[Time {env.now}] {name} finishes printing')

# Create and process 3 user print jobs with random arrival times and print durations
for i in range(1, 4):
    env.process(print_job(f'User {i}', printer))

# Run the simulation
env.run()  # Run the simulation until all users have finished printing
