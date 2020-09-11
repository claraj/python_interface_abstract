from response_listener import ResponseListener
from data_collector import PoliteDataCollector, RudeDataCollector


class WeatherSurvey(ResponseListener): 

    def survey(self):
        polite_data_collector = PoliteDataCollector(self)
        polite_data_collector.collect_data('What is the weather today?')

    def response_collected(self, response):
        print(f'Your response has been recorded. The weather is: {response}')


if __name__ == '__main__':
    survey = WeatherSurvey()
    survey.survey()


