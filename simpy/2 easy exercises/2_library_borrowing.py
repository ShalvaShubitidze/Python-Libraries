'''
==================================================
2️⃣ Library Borrowing System
==================================================
📌 Scenario:
Simulate a **library** with **3 copies** of a popular book. 
Students come to borrow and return books. If all copies are taken, the student waits until a copy is returned.

🔹 **Concepts Used:** 
   - Resource (to represent the books)
   - Timeout (to simulate time delays)
'''

'''
🧠 **Think About It!**
Before looking at the solution, try to answer:
1. How do you create a **shared resource** that only **one person** can use at a time?
2. How do you make customers arrive at different times?
3. How can you simulate the **time delay** for borrowing and returning the book?
'''

'''
🛠 **Try to complete this yourself, then check the solution below!**
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

# Create a shared resource (books) with 3 copies available
books = simpy.Resource(env, capacity=3)

# Define a function to simulate borrowing a book
def borrow_book(env, name, books):
    print(f'time: {env.now} === customer: {name} arrived')

    # Request a book from the library
    with books.request() as req:
        yield req  # Wait for an available book
        print(f'time: {env.now} === customer: {name} borrowed a book.')
        
        # Simulate the time spent reading the book (1-5 seconds)
        yield env.timeout(random.randint(1, 5))
        print(f'time: {env.now} === customer: {name} returned the book.')
        # print how many books are left at the library
        available = check_available_resources(books)
        print(f'[Time {env.now}] Available resources: {available}')


# Generate customers with staggered start times
def generate_customers():
    count = 1
    while count <= 10:  # 10 customers in total
        yield env.timeout(random.randint(1, 2))  # Add a small random delay between customer arrivals
        env.process(borrow_book(env, f'Customer {count}', books))
        count += 1




# Function to check available resources (for better visibility not required)
def check_available_resources(books):
    used_resources = len(books.users)  # Count how many resources are currently used
    available_resources = books.capacity - used_resources  # Calculate available resources
    return available_resources



# Start the customer generation process
env.process(generate_customers())

# Run the simulation for 20 time units
env.run(until=20)




'''
you can also improve this code by adding a simple queue,
that shows how many costumers are waiting in line
'''