class UnitConversion:
    """ This is a full library file, similar to what I would make (if using a class - typically sub)
        The point is to show the Pythonic way of class creation which varies greatly from Java/C++

        Convert inches and/or feet to inches, feet, yards, miles, and centimeters
        :TODO: Create a list of references to docs (I think sopython room has the old list) & Logging
    """

    __UNITS = {
        "feet": 12,
        "yards": 36,
        "miles": 63360,
        "centimeters": 2.54
    }

    '''Using type annotation to give hints throughout the library'''
    __inches: float = 0.0
    __feet: float = 0.0
    __yards: float = 0.0
    __miles: float = 0.0
    __centimeters: float = 0.0

    def __init__(self, feet: float = 0.0, inches: float = 0.0):
        """Python doesn't allow for overloading (its dynamically typed so this makes sense)
            So this is the pythonic way to have multiple constructors (i.e. what I use with Python)
           :param feet: The number of feet as a floating point number
           :param inches: The number of inches as a floating point number
        """
        try:
            self.__inches = inches + feet * 12
        except (ValueError, UnitConversion) as e:
            # didn't pass something which could convert to a float
            self.__inches = 0.0
        self.convert_all()

    @classmethod
    def from_inches(cls, inches: float = 0.0):
        """ Honestly, I would remove this and just add a setinches call in Main but
            To show overloading: we use class reference, fix the values, and pass as "new" init
            :param cls: The class reference (think self)
            :param inches: The inches to be used in calculations
        """
        try:
            feet = inches // 12
        except (ValueError, UnitConversion) as e:
            # didn't pass something which could convert to a float
            return cls(0.0, 0.0)
        return cls(feet, inches - feet * 12)

    '''Now using properties in a pythonic fashion for getters & setters (to encapsulate)
        to encapsulate but allow usage as properties over "methods" (functions)
        - For students: Why should or shouldn't I alter the setters (besides inches)?
    '''

    @property
    def inches(self):
        return self.__inches

    @inches.setter
    def inches(self, inches: float = 0.0):
        try:
            self.__inches = inches
        except (ValueError, UnitConversion) as e:
            self.inches = 0.0
        self.convert_all()

    @property
    def feet(self):
        return self.__feet

    def _set_feet(self):
        self.__feet = self.__inches / self.__UNITS["feet"]

    @property
    def yards(self):
        return self.__yards

    def _set_yards(self):
        self.__yards = self.__inches / self.__UNITS["yards"]

    @property
    def miles(self):
        return self.__miles

    def _set_miles(self):
        self.__miles = self.__inches / self.__UNITS["miles"]

    @property
    def centimeters(self):
        return self.__centimeters

    def _set_centimeters(self):
        self.__centimeters = self.__inches / self.__UNITS["centimeters"]

    def convert_all(self):
        """Converts the current inches value to all possible measurements"""
        self._set_feet()
        self._set_miles()
        self._set_yards()
        self._set_centimeters()

    def get_all(self):
        """
          Returns all the values (from inches to centimeters) as a list grouped by system
            Ordered by Value
          :return: List of all conversions (inches, feet, yards, miles, centimeters)
        """
        return [self.__inches, self.__feet, self.__yards, self.__miles, self.__centimeters]

    def __str__(self):
        """ :return String: A formatted string of units & conversions """
        return "Inches = {}, Feet = {:.2f}, Yards = {:.4f}, Miles = {:.8f}, CM = {:.6f}".format(
            self.__inches, self.__feet, self.__yards, self.__miles, self.__centimeters)
