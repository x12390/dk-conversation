from importer import Configured_Questions
from random import shuffle
import os

def start_app():
  cq = Configured_Questions()

  # Auswahlmenue Topic
  while True:
      cnt = 0
      for topic in cq.topics:
          print(f"{cnt}. {topic}")
          cnt += 1
      choice = input("Bitte Topic wählen [1-n] oder q (quit):")

      if choice.isnumeric():
          choice = int(choice)
          topic = cq.topics[choice]
          questions = cq.get_questions_by_topic(topic, './config/questions.ini')
          question_and_answer(questions)
      elif choice == "q":
          quit(0)

def question_and_answer(questions):
    shuffle(questions)  # shuffle questions
    for q in questions:
        os.system('cls')
        print(f"\n====== TOPIC: {q.topic} ======")
        print(f"\nQUESTION: {q.get_first_text()}")
        input("")
        print(f"ANSWER: {q.get_second_text()}")
        input("\nPress Enter to continue...")

    return
if __name__ == '__main__':
    start_app()


