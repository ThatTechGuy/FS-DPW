class DataCompiler(object):
    #Initiate class with auth_key, pages, and operation all set to false
    def __init__(self):
        self.__auth_key = False
        self.__pages = False
        self.__operation = False

    #Set pages in current instance with data given from controller
    def config(self, data):
        self.__pages = data

    #Sets operation details and clears auth_key while doing addl functions
    def collate(self, data):
        self.__operation = data
        local = data['local'].lower()
        image = "image/" + local + ".png"
        self.__operation['image'] = image
        self.__auth_key = True

    #GETTER for releasing either pages or operation based on authentication
    @property
    def store(self):
        if self.__auth_key:
            result = self.__operation
        else:
            result = self.__pages
        return result
