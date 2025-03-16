'''
==================================================================================
2️⃣ Hospital Emergency Room
==================================================================================
📌 Scenario:
A hospital emergency room has 3 doctors and 2 nurses. Patients arrive at random intervals, 
and each treatment requires both a doctor and a nurse. Treatment times vary depending on the severity of the condition. 
If no doctor or nurse is available, patients must wait.

🔹 **Concepts Used:**
   - Multiple resources
   - Randomization
   - Timeout

🧠 **Think About It!**
Before looking at the solution, try to answer:
1. How do you manage the availability of doctors and nurses simultaneously?
2. How do you simulate random patient arrivals and treatment times?
3. How do you ensure patients wait for both a doctor and a nurse?

🛠 **Try to complete this yourself, then check the solution below!** 🛠

==================================================================================
✅ Solution
==================================================================================
'''

import random
import simpy
from colorama import Fore, Style, init  # for more appealing outputs

# Initialize colorama
init(autoreset=True)

# Create the simulation environment
env = simpy.Environment()

# Create resources (3 doctors and 2 nurses)
doctors = simpy.Resource(env, capacity=3)
nurses = simpy.Resource(env, capacity=2)

# Global variable to track the number of patients waiting in line
waiting_patients = 0

# Patient generator (random patient arrivals)
def patient_generator(env, doctors, nurses):
    id = 1
    while True:
        yield env.timeout(random.randint(1, 5))  # Random arrival time between 1 and 5
        env.process(treatment(env, random.randint(3, 7), id, doctors, nurses))  # Random severity between 3 and 7
        id += 1

# Treatment process (doctor and nurse needed for treatment)
def treatment(env, severity, id, doctors, nurses):
    global waiting_patients
    arrival_time = env.now
    print(f'{Fore.CYAN}[{arrival_time:3}] -- Patient[{id}] arrived')

    # Increment the waiting patients count
    waiting_patients += 1
    print(f'{Fore.YELLOW}[{env.now:3}] -- Patient[{id}] is waiting')
    print(f'{Fore.WHITE}Patients in line -- {waiting_patients}')

    # Request both a doctor and a nurse
    with doctors.request() as doctor_req, nurses.request() as nurse_req:
        # Wait until both a doctor and a nurse are available
        yield doctor_req & nurse_req

        # Start treatment
        treatment_time = severity * 2  # Treatment time depends on severity
        print(f'{Fore.GREEN}[{env.now:3}] -- Patient[{id}] started treatment (finishes in {treatment_time})')
        waiting_patients -= 1
        print(f'{Fore.WHITE}Patients in line -- {waiting_patients}')

        # Simulate the treatment time
        yield env.timeout(treatment_time)

        # Finish treatment
        print(f'{Fore.MAGENTA}[{env.now:3}] -- Patient[{id}] finished treatment')

# Start the patient generator process
env.process(patient_generator(env, doctors, nurses))

# Run the simulation for 120 time units
print(f'{Fore.WHITE}{Style.BRIGHT}=== Hospital Emergency Room Simulation ===')
env.run(until=120)
