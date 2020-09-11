import abc

class DataCollector(abc.ABC):
    @abc.abstractmethod
    def collect_data(self, question):
        pass 


class PoliteDataCollector(DataCollector):

    def __init__(self, response_listener):
        self.response_listener = response_listener

    def collect_data(self, question):
        print('Hello! Please answer the following question. Thanks in advance!')
        response = input(f'{question}: ')
        print('Thanks very much! I\'ll send this response to be processed ASAP.')
        self.response_listener.response_collected(response)
        

class RudeDataCollector(DataCollector):

    def __init__(self, response_listener):
        self.response_listener = response_listener

    def collect_data(self, question):
        print('Answer the question.')
        response = response = input(f'{question}: ')
        print('Time for something else to deal with whatever you typed.')
        self.response_listener.response_collected(response)
        
