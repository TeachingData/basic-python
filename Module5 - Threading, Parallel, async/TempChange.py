import threading
import time

def check_energy():
    """ Gets the mass and change information from list (version 2 will use other process)
        Then calculates the energy needed (in Joules) & displays
        Finally checks if user is finished, if not re-run after 1 seconds
        WE ARE USING: A count of 24 with a wait of 1 second to mimic 24 hours & once an hour

        :return: False = sets flag allowing program to exit
    """
    for i in range(24):
        water_mass = 46.1 - i
        temp_change = i + .25

        energy = 4.186 * water_mass * temp_change
        print(f"The energy was {energy}")

        time.sleep(1)

"""
Calculates the energy used when changing temp of water
   - waits 1 seconds then repeats operation 24 times (mimicing an every hour check & log)
     - Feel free to try a longer process when you get this working
   - This is basically our Module 2 program as a thread
Note, if using Windows (and not a VM or subsystem of Linux) this may have a slight delay (10+ sec),
Then print all at once or when you open a different program.

I will talk about the workaround in class but its not required or included here.
"""

print("Starting new daily Temp Log")
threading.Thread(target=check_energy).start()
