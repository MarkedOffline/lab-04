
#
# CS 101 Lab
# Program #4
# Gabe Gonzalez
# gggxgq@umsystem.edu
#
# PROBLEM : Describe the problem
#
# ALGORITHM :
#      1. Write out the algorithm
#
# ERROR HANDLING:
#      Any Special Error handling to be noted.  Wager not less than 0. etc
#
# OTHER COMMENTS:
#      Any special comments
#


# import modules needed
import random


def play_again() -> bool:
    play_yes = ['y', 'yes', 'YES', 'Y','YeS','yEs','YEs','yeS''Yes','yES']
    play_no = ['no','NO''n','N','No','nO']
    play = input('Do you want to play again? ==>')
    while (play not in play_no and play not in play_yes):
        print('You must enter Y/YES/N/NO to continue. Please try again')
        play = input('Do you want to play again? ==>')
        if play in play_yes:
            return True
        elif play in play_no:
            return False
    return True


def get_wager(bank: int) -> int:
    wager = int(input('How many chips would you like to wager? ==> '))
    while wager < 0 or wager > bank:
        if wager < 0:
            print('Too low a value, you can only choose 1 - 100 chips')
        elif wager > bank:
            print('Too high a value, you can only choose 1 - 100 chips')
            wager = int(input('How many chips would you like to wager? ==> '))

    return wager


def get_slot_results() -> tuple:
    r1, r2, r3 = random.randrange(1, 11), random.randrange(1, 11), random.randrange(1, 11)
    return r1, r2, r3


def get_matches(reela, reelb, reelc) -> int:
    if (reela == reelb == reelc):
        return 3
    elif (reela == reelb) or (reela == reelc) or (reelb == reelc):
        return 2
    else:
        return 0


def get_bank() -> int:
    bank = int(input('How many chips do you want to start with? ==> '))
    while bank < 0 or bank > 100:
        if bank < 0:
            print('Too low a value, you can only choose 1 - 100 chips')
        elif bank > 100:
            print('Too high a value, you can only choose 1 - 100 chips')
        bank = int(input('How many chips do you want to start with? ==> '))

    return bank


def get_payout(wager, matches):
    if matches == 3:
        return wager * 10
    elif matches == 2:
        return wager * 3
    else:
        return wager * -1


if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()

        while (bank > 0):

            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()

        print("You lost all", 0, "in", 0, "spins")
        print("The most chips you had was", 0)
        playing = play_again()