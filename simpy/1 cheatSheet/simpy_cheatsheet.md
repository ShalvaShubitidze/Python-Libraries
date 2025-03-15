# SimPy Detailed Cheatsheet

This **SimPy cheatsheet** provides an in-depth overview of the essential concepts and functions in **SimPy**, a process-based discrete-event simulation framework for Python. It covers initialization, creating processes, handling events, managing resources, time management, random variables, and more advanced features like monitoring, statistics, and custom events.

---

## 1️⃣ Initializing SimPy

Before using any SimPy features, you must import and initialize the library.

### Import SimPy:
- **`import simpy`**: Imports the SimPy library to your script.
    ```python
    import simpy
    ```

---

## 2️⃣ Creating an Environment

In SimPy, all simulations occur within an environment. The environment controls the simulation's time and event processing.

### Functions:
- **`simpy.Environment()`**: Creates the simulation environment that manages processes and events.
    ```python
    env = simpy.Environment()
    ```

- **`env.run(until)`**: Starts the simulation and runs until the specified time or until no more events remain.
    ```python
    env.run(until=10)  # Run the simulation until time 10
    ```

- **`env.now`**: Retrieves the current simulation time.
    ```python
    print(f"Current simulation time: {env.now}")
    ```

---

## 3️⃣ Creating Processes

SimPy processes are the core components of the simulation. They are Python functions that yield events during their execution.

### Functions:
- **`env.process(process_name())`**: Adds a new process to the environment.
    ```python
    def my_process(env):
        yield env.timeout(5)  # Simulates a delay of 5 units of time

    env.process(my_process(env))  # Adds the process to the environment
    ```

- **`yield env.timeout(time)`**: Creates a timeout event, causing the process to "pause" for a specified amount of time.
    ```python
    yield env.timeout(10)  # Process pauses for 10 time units
    ```

- **`yield env.event()`**: Creates a generic event, useful for synchronizing processes.
    ```python
    event = env.event()
    yield event  # Waits for the event to be triggered
    ```

---

## 4️⃣ Handling Resources

Resources like machines, workers, or vehicles are shared among processes in SimPy. These resources can be controlled using SimPy's resource management system.

### Functions:
- **`simpy.Resource(env, capacity)`**: Creates a resource with a specified capacity (number of units).
    ```python
    resource = simpy.Resource(env, capacity=3)  # Resource with 3 units
    ```

- **`resource.request()`**: Requests a unit of the resource.
    ```python
    request = resource.request()  # Request a unit of the resource
    yield request  # Wait for the resource to become available
    ```

- **`resource.release(request)`**: Releases a previously acquired unit of the resource.
    ```python
    resource.release(request)  # Releases the resource
    ```

- **`resource.count`**: Returns the number of resources currently in use.
    ```python
    print(resource.count)  # Number of resources currently in use
    ```

- **`resource.release()`**: Releases a request.
    ```python
    resource.release(request)
    ```

- **`resource.capacity`**: Returns the total number of available resources.
    ```python
    print(resource.capacity)  # Total number of resources available
    ```

---

## 5️⃣ Using Events and Conditions

SimPy processes interact with events to synchronize their execution. Events can be triggered when certain conditions are met.

### Functions:
- **`env.timeout(time)`**: Creates a timeout event that causes a delay for a specified amount of time.
    ```python
    yield env.timeout(10)  # Simulate a delay of 10 units
    ```

- **`env.event()`**: Creates a simple event that can be triggered manually.
    ```python
    event = env.event()
    ```

- **`event.succeed()`**: Marks the event as succeeded, allowing other processes waiting for it to proceed.
    ```python
    event.succeed()  # Trigger the event and allow waiting processes to continue
    ```

- **`event.fail()`**: Marks the event as failed, causing any waiting processes to raise an exception.
    ```python
    event.fail()  # Mark the event as failed
    ```

- **`env.exit()`**: Terminates the simulation by raising an exception.
    ```python
    env.exit('Simulation complete')  # Ends the simulation
    ```

---

## 6️⃣ Time Management

SimPy uses a discrete event system to model the flow of time. You can simulate time advances and control the simulation’s progression.

### Functions:
- **`env.timeout(time)`**: Waits for the specified amount of time.
    ```python
    yield env.timeout(5)  # Waits for 5 units of time
    ```

- **`env.now`**: Retrieves the current simulation time.
    ```python
    print(f"Current simulation time: {env.now}")
    ```

- **`env.run(until)`**: Runs the simulation until the specified time.
    ```python
    env.run(until=10)  # Run the simulation for 10 units of time
    ```

- **`env.process()`**: A generator function that starts a process at the given time in the environment.
    ```python
    env.process(my_process(env))
    ```

---

## 7️⃣ Monitoring Processes

SimPy includes tools for monitoring the progress of processes, events, and resources during the simulation.

### Functions:
- **`simpy.Store()`**: A queue-like container for managing items that need to be processed.
    ```python
    store = simpy.Store(env)
    store.put('item')  # Put an item into the store
    item = yield store.get()  # Get an item from the store
    ```

- **`simpy.PriorityResource()`**: A resource where requests can have priority levels.
    ```python
    pr_resource = simpy.PriorityResource(env, capacity=1)
    ```

- **`simpy.Container()`**: Allows you to model fluid or item levels that can be added or removed from a container.
    ```python
    container = simpy.Container(env, capacity=10, init=5)  # Container with initial value 5
    yield container.put(3)  # Add 3 units to the container
    yield container.get(2)  # Remove 2 units from the container
    ```

---

## 8️⃣ Using Random Variables

SimPy supports random variables, which are essential for simulating real-world randomness in your processes.

### Functions:
- **`random.randint(a, b)`**: Generates a random integer between a and b.
    ```python
    import random
    random_number = random.randint(1, 10)
    ```

- **`random.uniform(a, b)`**: Generates a random floating-point number between a and b.
    ```python
    random_float = random.uniform(1.0, 5.0)
    ```

- **`random.expovariate(lambd)`**: Generates a random number based on an exponential distribution.
    ```python
    inter_arrival_time = random.expovariate(1/5)  # Average inter-arrival time of 5 units
    ```

- **`random.gauss(mu, sigma)`**: Generates a random number based on a normal distribution.
    ```python
    gaussian_value = random.gauss(0, 1)  # Random value from a normal distribution with mean 0 and standard deviation 1
    ```

---

## 9️⃣ Example Simulation: Bank Queue

Here's a simple example of a simulation for a bank queue with customers arriving and waiting for a teller.

```python
import simpy
import random

# Bank simulation process
def customer(env, name, bank):
    print(f'{name} arrives at the bank at {env.now}')
    with bank.request() as request:
        yield request
        print(f'{name} starts being served at {env.now}')
        service_time = random.expovariate(1/3)
        yield env.timeout(service_time)
        print(f'{name} leaves the bank at {env.now}')

# Setting up the environment and resources
env = simpy.Environment()
bank = simpy.Resource(env, capacity=1)  # Only one teller available

# Creating customer processes
for i in range(5):
    env.process(customer(env, f'Customer {i+1}', bank))

# Running the simulation
env.run()
```


---

## 🔚 Conclusion

SimPy is a powerful and flexible library for building **discrete-event simulations** in Python. By understanding and utilizing the core concepts such as processes, resources, events, and time management, you can create a wide variety of simulations. 

With the functions and tools discussed here, you can simulate systems like **queues**, **manufacturing processes**, **logistics**, and **service models**. The library allows for easy integration of **randomness** to mimic real-world uncertainties, such as arrival times or service durations, making it highly applicable for both simple and complex models.

By leveraging SimPy’s built-in **monitoring** tools and **resource management**, you can track your system's performance, optimize workflows, and analyze behaviors. Its simplicity in defining processes and events makes it easy to use, even for those new to simulation modeling.

SimPy also integrates well with Python’s powerful libraries, allowing you to build **custom models**, experiment with **random variables**, and analyze simulation results. The flexibility of defining complex interactions between multiple processes in an **event-driven** framework ensures that your simulations can be tailored to a wide range of real-world applications.

In conclusion, whether you’re modeling a simple bank queue, a complex factory system, or testing a new logistics process, SimPy provides an excellent platform to explore, build, and analyze your models. By mastering the concepts and functions outlined in this cheatsheet, you'll be well-equipped to simulate and optimize processes in many domains. 

---

Feel free to refer to this cheatsheet as you experiment with SimPy and explore the vast possibilities of discrete-event simulation. If you have any further questions or need assistance with any part of SimPy, don't hesitate to reach out.
