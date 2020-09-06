import random


class RockPaperScissors:
    def __init__(self, ratings_file='rating.txt'):
        self.ratings_file = ratings_file
        self.scores = {}
        self.load_all_scores()

    def rules(self):
        lose_comb = {}

        shapes = [shape for shape in input().split(",")]
        if shapes == [""]:
            shapes = ['rock', 'paper', 'scissors']
        doubled_shapes = shapes * 2
        n_comb = len(shapes) // 2
        for idx in range(0, len(shapes)):
            lose_comb[shapes[idx]] = doubled_shapes[idx + 1:idx + 1 + n_comb]
        print("Okay, let's start")
        return shapes, lose_comb

    def play(self):
        self.load_all_scores()
        name = self.greeting()
        if name not in self.scores:
            self.scores[name] = 0
        options_, lose_combinations = self.rules()

        while True:
            user_choice = input()

            if user_choice in options_:
                com_choice = random.choice(options_)

                if user_choice == com_choice:
                    self.scores[name] += 50
                    print(f'There is a draw ({com_choice})')

                elif com_choice in lose_combinations[user_choice]:
                    print(f'Sorry, but the computer chose {com_choice}')

                else:
                    self.scores[name] += 100
                    print(f'Well done. The computer chose {com_choice} and failed')

            elif user_choice == "!exit":
                self.through_rating()
                print("Bye!")
                break

            elif user_choice == "!rating":
                print("Your rating: " + str(self.rating(name)))

            else:
                print("Invalid input")

    def greeting(self):
        name = input("Enter your name: ")
        print(f'Hello, {name}')
        return name

    def load_all_scores(self):
        with open("rating.txt", 'r') as file:
            for line in file:
                name_user, score = line.split()
                self.scores[name_user] = int(score)

    def rating(self, name):
        return self.scores[name] if name in self.scores else 0

    def through_rating(self):
        with open("rating.txt", 'w') as file:
            for name, score in self.scores.items():
                print(name, score, sep=" ", file=file, flush=True)


sulifa = RockPaperScissors()
sulifa.play()
