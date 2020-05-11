import multiprocessing

def get_mass_and_temp():
    """
    Gets single instance of mass and temp from user
       with validation of values.
    :return: dictionary entry of mass & temp
    """
    while True:
        try:
            mass = float(input(" Please enter the mass: "))
            temp = float(input(" Please enter the temp change: "))
        except ValueError:
            print("You must enter a numeric value")
            continue
        return {"mass": mass, "temp": temp}

def check_energy(measurements):
    """ Calculates the energy needed (in Joules) based on mass & temp change
        Then prints it (used for map - could use a lambdas this is so simple)
        :param: measurements = dictionary with mass & temp as keys (from water list)
    """
    print(f"The energy was {4.186 * measurements['mass'] * measurements['temp']}")


if __name__ == "__main__":
    water = []
    exit_flag = True

    while exit_flag:
        water.append(get_mass_and_temp())

        user_ans = input("Do you have more information on water & mass? (Y or N)")
        if user_ans[0] == 'n':
            exit_flag = False

    # See ppt on Pool vs. Process (we are using Pool not to break things)
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    # map is basically the same as any functional use of map: map elements to given function
    result = pool.map(check_energy, water)

    # Always close your processes (and typically you join them back too)
    pool.close()
    pool.join()
