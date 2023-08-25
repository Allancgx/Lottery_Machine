import random


class Lottery_Ticket:
    """#TODO: Need to write a testing module for this class"""

    @staticmethod
    # Static method doesn't need self in the parameter and can be used without initializing an object
    def quick_pick(balls_in_bowl, sample):
        """
        balls_in_bowl: the number of balls we want to put into the bowl
        sample: the number of balls we want to pick without replacemnt from the balls_in_bowl
        Returns a list of picked balls
        """
        bowl = list(
            range(1, balls_in_bowl)
        )  # Generate a list of integers between 1 and population_range, excluding population_range
        picked_balls = random.sample(
            bowl, sample
        )  # Pick the sample number of balls from bowl without replacement
        picked_balls.sort()
        return picked_balls

    def __init__(self, main_numbers=None, powerball=None):
        self.main_numbers = main_numbers or self.quick_pick(
            70, 5
        )  # The left part is calling the setter method instead of accessing the variable directly
        self.powerball = powerball or self.quick_pick(27, 1)[0]

    def __str__(self):
        return f"{self.main_numbers} {self.powerball}"

    @property
    def main_numbers(self):
        return self._main_numbers

    @main_numbers.setter
    def main_numbers(self, new_main_numbers):
        if type(new_main_numbers) is list and len(new_main_numbers) == 5:
            for index, number in enumerate(new_main_numbers):
                if number not in range(1, 70):
                    raise ValueError(
                        f"A element within main_numbers is not valid. Index {index} in the list has value {number}, which is not an integer between 1 and 69!"
                    )
            self._main_numbers = new_main_numbers
        else:
            raise ValueError(
                "main_numbers is not valid. It needs to be a list containing 5 elements."
            )

    @main_numbers.deleter
    def main_numbers(self):
        del self._main_numbers

    @property
    def powerball(self):
        return self._powerball

    @powerball.setter
    def powerball(self, new_powerball):
        try:
            new_powerball = int(new_powerball)
            if new_powerball in range(1, 27):
                self._powerball = new_powerball
            else:
                raise ValueError
        except ValueError:
            raise ValueError(
                "powerball is not valid. Please use an integer between 1 and 26"
            )

    @powerball.deleter
    def powerball(self):
        del self._powerball

    def prize(self, winning_main_numbers, winning_powerball):
        """
        winning_main_numbers: a list of winning main numbers
        winning_powerball: winning powerball
        Returns the total amount of prize payout
        """
        payout = 0
        main_numbers_match = 0
        powerball_match = False
        for ball in self.main_numbers:
            if ball in winning_main_numbers:
                main_numbers_match += 1
        if self.powerball == winning_powerball:
            powerball_match = True

        if main_numbers_match == 0 and powerball_match == True:
            return 4
        elif main_numbers_match == 1 and powerball_match == True:
            return 4
        elif main_numbers_match == 2 and powerball_match == True:
            return 7
        elif main_numbers_match == 3:
            return 7
        elif main_numbers_match == 3 and powerball_match == True:
            return 100
        elif main_numbers_match == 4:
            return 100
        elif main_numbers_match == 4 and powerball_match == True:
            return 50000
        elif main_numbers_match == 5:
            return 1000000
        elif main_numbers_match == 5 and powerball_match == True:
            return "Jackpot"
        else:
            return 0


def main():
    # TODO Ask if they want to QP for each

    while True:
        try:
            tickets = int(
                input("How many lottery tickets would you like to buy with QP?")
            )
            break
        except ValueError:
            print("Please enter an integer")
    winning_main_numbers = Lottery_Ticket.quick_pick(70, 5)
    winning_powerball = Lottery_Ticket.quick_pick(27, 1)[0]
    total_prize = 0
    for index in range(tickets):
        ticket = Lottery_Ticket()
        # print(f"Ticket #{index+1}", ticket.main_numbers, ticket.powerball)
        ticket_prize = ticket.prize(winning_main_numbers, winning_powerball)
        if ticket_prize == "Jackpot":
            total_prize = ticket_prize * (-1)
            print(f"Jackpot! - Ticket #{index+1} won the Jackpot")
        elif ticket_prize != 0:
            total_prize += ticket_prize
            print(f"Won! - Ticket #{index+1} with number {ticket.__str__()} won prize ${ticket_prize}")

    print(
        f"Winning numbers are: {winning_main_numbers} {winning_powerball}. Your total cost is: ${tickets*2}. You won ${total_prize}"
    )
    # Add mechaniisms to automatically check for winning
    return True


if __name__ == "__main__":
    main()
    # test = Lottery_Ticket([1, 2, 3, 4, 70], 10)
    # print(test)
