import curses
from curses import wrapper
import sys
import datetime
import operator as op
import random
from PIL import Image
from captcha.image import ImageCaptcha
import string

#the list of champions league final goal scorers of the last 10 years
cl_scorers = ['rodri', 'carvajal', 'vinicius', 'ronaldo', 'neymar', 'rakitic', 'morata', 'suarez',
              'ramos', 'carrasco', 'mane', 'bale', 'salah', 'casemiro', 'ascensio', 'coman', 'havertz']

def main(stdscr):
    # Initialize curses colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK )

    # Color pairs
    green = curses.color_pair(1)
    red = curses.color_pair(2)
    cyan = curses.color_pair(3)

    stdscr.clear()
    stdscr.addstr(0, 0, "THE PASSWORD GAME", curses.A_BOLD | curses.A_UNDERLINE)
    stdscr.addstr(1,0, "Type 'quit' if you want to exit the program", cyan)
    stdscr.addstr(2, 0, "Enter Password: ")
    stdscr.refresh()

    # Define rules and their corresponding error messages
    rules = [
        #Rule 1: the password must be at least 5 characters
        (lambda pwd: len(pwd) >= 5, "Rule 1: Your password must be at least 5 characters"),
        #Rule 1: the password must be at least 5 characters
        (lambda pwd: any(char.isdigit() for char in pwd), "Rule 2: Your password must contain a number"),
        #Rule 3: the password must contain an uppercase letter
        (lambda pwd: any(char.isupper() for char in pwd), "Rule 3: Your password must contain an uppercase letter"),
        #Rule 4: Your password must include a special character
        (lambda pwd: any(not char.isalnum() for char in pwd), "Rule 4: Your password must include a special character"),
        #Rule 5: The digits in your password must add up to 10
        (rule_5, "Rule 5: The digits in your password must add up to 20" ),
        #Rule 6: Your password must include the current month
        (rule_6, "Rule 6: Your password must include the current month"),
        #Rule 7 : Your password must include the name of a UEFA Champions League final goal scorer between the years 2015 - 2024
        (rule_7 , "Rule 7 : Your password must include the name of a UEFA Champions League final goal scorer between the years 2015 - 2024"),
        #Rule 8 : A sacrifice must be made. Pick two letters that you will no longer be able to use
        (lambda pwd: rule_8(stdscr, pwd), "Rule 8 – A sacrifice must be made. Pick two letters that you will no longer be able to use"),
        #Rule 9 : Your password must include the length of your password
        (lambda pwd: str(len(pwd)) in pwd, "Rule 9 : Your password must include the length of your password"),
        #Rule 10 : The length of your password must be a prime number
        (rule_10, "Rule 10: The length of your password must be a prime number"),
        #Rule 11 :Your password must include this captcha code
        (rule_11, "Rule 11: Your password must include this captcha code (The image is in the folder)")
    ]

    while True:
        #Get Input
        curses.echo()
        password = stdscr.getstr(2, 17).decode("utf-8")

        if password == "quit":
            sys.exit()

        valid_password = True
        # Check all rules
        for i, (rule, error_message) in enumerate(rules):
            stdscr.addstr(3,0, " " * 100)
            stdscr.addstr(3, 0, f"Previous Try: {password}")
            if not rule(password):
                stdscr.addstr(5 + i, 0, error_message, red)
                stdscr.refresh()
                valid_password = False
                break
            else:
                stdscr.addstr(5 + i, 0, error_message, green)
                stdscr.refresh()

        #Password is valid
        if valid_password:
            stdscr.clear()
            stdscr.addstr(1, 0, "You Created a Strong Password!", green)
            stdscr.addstr(2, 0, f"The length of your Password was {len(password)}", cyan)
            stdscr.getch()
            return True

        # Clear input line for new input
        stdscr.addstr(2, 17, " " * 20)
        stdscr.move(2, 17)
        stdscr.refresh()

def rule_5(password):
    total = sum(int(i) for i in password if i.isdigit())
    return total == 20

def rule_6(password):
    todays_date = datetime.datetime.now()
    todays_month = todays_date.strftime('%B')
    return todays_month.lower() in password.lower()

def rule_7(password):
    for i in cl_scorers:
        if op.contains(password.lower(), i):
            return True
    return False

has_executed = False
no_letters = ""
def rule_8(stdscr, password):
    global has_executed, no_letters
    if not has_executed:
        stdscr.addstr(4, 0, "Pick two letters that you will no longer be able to use: ")
        stdscr.refresh()
        no_letters = stdscr.getstr(4, 57).decode("utf-8")
        has_executed = True
    for char in no_letters:
        if char in password:
            return False
    return True

def rule_10(password):
    length = len(password)
    if length < 2:
        return False
    for i in range(2, length):
        if length%i == 0:
            return False
    return True

runned = False
captcha_text = ""

def rule_11(password):
    global runned, captcha_text
    if not runned:
        captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 2))
        image = ImageCaptcha()
        captcha_image = image.generate_image(captcha_text)
        captcha_image.save("captcha.png")
        img = Image.open("captcha.png")
        img.show
        runned = True
    return captcha_text in password

def valid__password(stdscr, pwd):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK )

    # Color pairs
    green = curses.color_pair(1)
    red = curses.color_pair(2)
    cyan = curses.color_pair(3)

    stdscr.clear()
    stdscr.addstr(1, 0, "You Created a Strong Password!", green)
    stdscr.addstr(2, 0, f"The length of your Password was {len(pwd)}", cyan)
    stdscr.getch()
    return True

if __name__ == "__main__":
    wrapper(main)
