from class_property import Class_Property as prop

class Card:
    topic = ""
    first_text = ""
    second_text = ""

    def __init__(self, topic, first_text="", second_text=""):
        self.set_topic(topic)
        self.set_first_text(first_text)
        self.set_second_text(second_text)

    def set_topic(self, text):
        self.topic = text

    def get_topic(self):
        return self.topic

    def set_first_text(self, text):
        self.first_text = text

    def get_first_text(self):
        return self.first_text

    def set_second_text(self, text):
        self.second_text = text

    def get_second_text(self):
        return self.second_text