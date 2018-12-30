class Sheet:

    __content = None

    def get_content(self):
        return self.__content
        
    def write_down(self, inputString):
        
        if self.__content is None:
            self.__content = inputString
        else:
            self.__content += inputString