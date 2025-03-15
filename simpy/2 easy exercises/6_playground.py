'''
==================================================
6️⃣ Playground Slide Simulation
==================================================
📌 Scenario:
A playground has 1 slide, and 5 kids take turns using it. 
Each slide takes 2 seconds. Kids can only slide when it’s their turn.

🔹 **Concepts Used:** 
   - Resource (to represent the slide)
   - Timeout (to simulate slide time)
   - Process (to simulate each kid taking their turn)
'''

'''
🧠 **Think About It!**
Before looking at the solution, try to answer:
1. How do you simulate the kids arriving at random intervals?
2. How do you make sure only one kid uses the slide at a time?
3. How do you simulate the time each kid spends on the slide?
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

# Create a shared resource (the slide) with capacity = 1 (only one kid can slide at a time)
slide = simpy.Resource(env, capacity=1)

# Define a function to simulate kids using the slide
def kid_slide(name, slide):
    # Simulate arrival at random intervals (1-3 seconds)
    yield env.timeout(random.randint(1, 3))
    print(f'[Time {env.now}] {name} arrives at the slide')
    
    # Request the slide resource
    with slide.request() as req:
        yield req  # Wait for the slide to be available
        print(f'[Time {env.now}] {name} starts sliding')
        
        # Simulate the time each kid spends on the slide (2 seconds)
        yield env.timeout(2)
        print(f'[Time {env.now}] {name} finishes sliding')

# Create and process 5 kids using the slide
for i in range(1, 6):
    env.process(kid_slide(f'Kid {i}', slide))

# Run the simulation
env.run()  # Run the simulation until all kids have finished sliding
