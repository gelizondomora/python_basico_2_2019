#

# Misc classes
class misc:
    def __repr__(self):  # cada vez que la clase se le haga print va a retornar self.__class__.__name__
        # return the clase name
        return self.__class__.__name__

    def __str__(self): #cada vez que la clase se le haga str() va a retornar self.__class__.__name__
        # return the clase name
        return self.__class__.__name__

