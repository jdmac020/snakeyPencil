class Sheet:

    def __innit__(self):
	    self.__content = None

    def get_content(self):
	    return self.__content
		
    def write_down(self, inputString):
	    self.__content = inputString