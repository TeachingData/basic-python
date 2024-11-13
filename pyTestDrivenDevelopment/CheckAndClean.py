class CheckAndClean:
    """ This is meant to show how to use unit testing with Python.
        It is not a serious project but meant for education.
    """

    # Sting to use to check for "special" characters
    __SPECIALS = "$!'\"\\=-+*&^%$#@~`.?:;,<>,{}[]()"

    # Honestly need to change this to use apptype to set some options
    def __init__(self, apptype: str = "SQL"):
        self.__apptype = apptype

    # Setup getters and setters for apptype
    @property
    def apptype(self):
        return self.__apptype

    @apptype.setter
    def apptype(self, apptype: str="SQL"):
        self.__apptype = apptype

    """ This takes a string and checks if any character are in SpECIALS.
        If they are, it appends them with backslash to escape
        If not, it just appends them.
        
        :param toclean The string to sanitize
        :return A new string that has escaped all special chars
    """
    def sanitize(self, toclean: str):
        """ Two options here: make a list and add to it each time then return that joined
                              use a list comprehension to make an anon list and return that joined
        #Here is the written out form

        toreturn = []
        for char in toclean:
            if char in self.__SPECIALS:
                toreturn.append("\\"+char)
            else:
                toreturn.append(char)
        return "".join(toreturn)
        """

        # I'm going to use the list comprehension because that's what I usually use
        return "".join(["\\"+char if char in self.__SPECIALS else char for char in toclean])