import json

print('Witam, zapraszam do wzięcia udziału w "Quiz-ie".')

points = 0


def show_question(question):
    global points
    print()
    print(question["pytanie"])
    print("a:", question["a"])
    print("b:", question["b"])
    print("c:", question["c"])
    print("d:", question["d"])
    print()

    answer = input("Którą odpowiedź wybierasz? ")

    if answer == question["prawidlowa_odpowiedz"]:
        points += 1
        print("Dobra odpowiedź, Brawo! Liczba punktów:", points)
    else:
        print("Niestety to zła odpowiedź. Prawidłowa odpowiedź to:", question["prawidlowa_odpowiedz"], ".")


with open("quiz.json") as json_file:
    questions = json.load(json_file)

    for i in range(0, len(questions)):
        show_question(questions[i])

print()
print("Koniec gry. Liczba zdobytych punktów to:", points, "na 5 możliwych do zdobycia.")
