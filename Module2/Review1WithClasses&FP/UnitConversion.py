class UnitConversion:
    """ There is no true private or protected in Python (unlike C++ or Java)
        However, by convention we use "_" to mean protected & "__" to mean private
            * the reason for was a design decision within the Python development
            * More later but want you to have an idea of a Library Class in Python
        References: https://docs.python.org/3/tutorial/classes.html
    """

    __UNITS = {
        "feet": 12,
        "yards": 36,
        "miles": 63360,
        "centimeters": 2.54
    }

    ''' Depending on the application I sometimes set this as a dict 
        that just points to the functions (or has a lambdas that just converts it)
        Overkill and too much overhead in this instance (probably more reads then writes)
        But something to remember for more analytic conversion (ones based on stats)
    '''
    __inches = 0.0
    __feet = 0.0
    __yards = 0.0
    __miles = 0.0
    __centimeters = 0.0

    def __init__(self, feet=0.0, inches=0.0):
        """This is a constructor so someone could call this with the user_feet & inches
           self = this for those with Java & C++ background
                Note how it is being passed by reference
           Using the 0.0 with the two parameters sets a default value & : float the type
           :param feet: The number of feet as a floating point number
           :param inches: The number of inches as a floating point number
        """
        self.__inches = inches + feet * 12

    """Now for our setters: 
        - no set inches because that should be done on instance
        - Also this is not the Pythonic way to do this but I want an intro here
          - The Pythonic way (with decorators & properties) will be covered later
          - Also the Pythonic way to give type hints will be covered then
          - Its also in this directory so feel free to look at it early if you wish
        - It would also likely be made into a Base Class for our Abstracts by Unit (later)
    """
    def _set_feet(self):
        self.__feet = self.__inches / self.__UNITS["feet"]

    def _set_yards(self):
        self.__yards = self.__inches / self.__UNITS["yards"]

    def _set_miles(self):
        self.__miles = self.__inches / self.__UNITS["miles"]

    def _set_centimeters(self):
        self.__centimeters = self.__inches / self.__UNITS["centimeters"]

    # One special setter that just calls and sets all the values at once
    # And yes, I'm going to make it public

    def set_all(self):
        self._set_feet()
        self._set_miles()
        self._set_yards()
        self._set_centimeters()

    #And the getters (which will all be public)

    def get_inches(self):
        return self.__inches

    def get_feet(self):
        return self.__feet

    def get_yards(self):
        return self.__yards

    def get_miles(self):
        return self.__miles

    def get_centimeters(self):
        return self.__centimeters

    # Note: here is another "do I want a dict or properties?" i.e: you could just return the dict

    def get_all(self):
        """
          Returns all the values (from inches to centimeters) as a list grouped by system
            Ordered by Value
          :return: List of all conversions (inches, feet, yards, miles, centimeters)
        """
        return [self.__inches, self.__feet, self.__yards, self.__miles, self.__centimeters]

    def __str__(self):
        """ With this type of library I typically just need the getters as "prints"...
            technically I just make the functions in a library and call them
            (functions are first-class citizens)....but for the sake of completion:
            this is the Python equivalent of ".toString"
            Again - another reason for a dict
              (but again I would typically just use the getters)

            :return String: A formatted string of units & conversions
        """
        return "Inches = {}, Feet = {:.2f}, Yards = {:.4f}, Miles = {:.8f}, CM = {:.6f}".format(
            self.__inches, self.__feet, self.__yards, self.__miles, self.__centimeters)
