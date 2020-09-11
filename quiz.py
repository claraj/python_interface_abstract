from response_listener import ResponseListener
from data_collector import RudeDataCollector

# Quiz question

class TechnologyQuiz(ResponseListener): 

    def start_quiz(self):
        polite_data_collector = RudeDataCollector(self)
        polite_data_collector.collect_data('What number system do computers use?')

    def response_collected(self, response):
        if response.strip().upper() == 'BINARY':
            print('Correct!')
        else:
            print('Sorry, the answer is "Binary"')


if __name__ == '__main__':
    quiz = TechnologyQuiz()
    quiz.start_quiz()




