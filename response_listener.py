import abc 

class ResponseListener(abc.ABC):
    @abc.abstractmethod 
    def response_collected(self, response):
        pass