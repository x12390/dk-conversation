from card import Card
from configparser import ConfigParser

class Configured_Questions:
    list_of_questions = []
    topics = []

    def __init__(self):
        self.list_of_questions = self.import_questions()

    def import_questions(self):
        questions = []
        parser = ConfigParser()
        candidates = ['./config/questions.ini']
        found = parser.read(candidates, 'utf8')
        missing = set(candidates) - set(found)

        print('Found config files:', sorted(found))
        print('Missing files     :', sorted(missing))

        questions = []
        for ini in found:
            parser.read(ini)
            cnt = 0
            self.topics = parser.sections()
            for section in self.topics:
                cnt += 1
                name = f"{section}_{cnt}"
                for name, value in parser.items(section):
                    if len(name) > 0:
                        firstChar = name[0]
                        if firstChar == "q":
                            question = value
                        elif firstChar == "a":
                            answer = value
                            card = Card(section, question, answer)
                            #print(f"Append new card: {section}, {question}, {answer}")
                            questions.append(card)

        return questions

    def get_questions(self):
        return self.list_of_questions

    def get_questions_by_topic(self, topic, configfile):
        questions = []
        parser = ConfigParser()
        parser.read(configfile, 'utf8')
        topic_section = topic #parser.options(topic)
        for name, value in parser.items(topic_section):
            if len(name) > 0:
                firstChar = name[0]
                if firstChar == "q":
                    question = value
                elif firstChar == "a":
                    answer = value
                    card = Card(topic_section, question, answer)
                    #print(f"Append new card: {topic_section}, {question}, {answer}")
                    questions.append(card)
        return questions


#Test
# obj = Configured_Questions()
# print(obj.topics)
# print(obj.list_of_questions)
# obj.get_questions_by_topic("work", "./config/questions.ini")
