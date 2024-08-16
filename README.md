# Python Password Game

#### Video Demo: [Watch here](https://youtu.be/tSSAurEApgI)

## Description

In this program, the user is required to create a strong password, but not just any simple one! The user must enter a password that meets the criteria of the rules of the game.

### Rules of the Game:
1. **Rule 1**: The password must be at least 5 characters long.
2. **Rule 2**: The password must contain a number.
3. **Rule 3**: The password must contain an uppercase letter.
4. **Rule 4**: The password must include a special character.
5. **Rule 5**: The digits in your password must add up to 10.
6. **Rule 6**: Your password must include the current month.
7. **Rule 7**: Your password must include the name of a UEFA Champions League final goal scorer between the years 2015 - 2024.
8. **Rule 8**: A sacrifice must be made. Pick two letters that you will no longer be able to use.
9. **Rule 9**: Your password must include the length of your password.
10. **Rule 10**: The length of your password must be a prime number.
11. **Rule 11**: Your password must include this captcha code.

#
#


```
When I was first developing the program, I needed it to be a clean terminal based game so the user does not get confused with what's going on the screen. After countless tries of trying to clear the screen every time the user provides an input, I found a module called curses which made my life so much easier. The curses module let me add specific sentences in specific parts of the terminal window and also edit how they looked. It was especially needed while displaying the rules as when the condition for the rule is not met, the text is highlighted in red and green when it is.

I had debated including 30 rules at first but then later came to 11 since it would be unnecessarily long and difficult. I also had to change many rules, especially those including emojis since the curses module did not allow the user to enter emojis by copy pasting. Another change I made was instead of copying and pasting the users input in the input window every time they get it wrong, there would be a separate line mentioning the previous input the user had entered because the rules can cause the user to completely change the entire password from the beginning.

While designing the program, I had originally defined separate functions for each rule which returned a boolean value so that the program would execute it again if it returned false. But then that would make the code very long and difficult to read as well so I ended up storing the functions and their corresponding error messages in a list of tuples and then looping over them until all of the conditions are satisfied. Also I removed the functions which could be stored in just one line so that the lines of code would be smaller. I also debated whether or not to use the re function as it would help in several instances but then later decided not to because there were far simpler ways because some of the rules needed dates and values that change every time the program is run.

The test_project.py part of the project includes all the testing in the program of the different functions. This was relatively easy to implement as these short functions returned true only if certain characters were contained in the parameter.

The captcha.png in the program includes the captcha that will be displayed at the end of the game. I only have 2 characters displaying currently to make it easier while testing the program.

During testing of the program, I ran into many problems. The curses module was very new to me and required some getting used to. I looked up many tutorials online for having the contents of the screen remain the same with only the user input being erased. At the very first I almost wrote the entire program in one loop containing branching conditions for each rule which I regretted very quickly and started over. Definitely the hardest part of the program was designing the terminal. I also created a test.py file which I later deleted to test smaller parts of the program for some rough ideas.

In the end of the program I wanted the user to get a victory screen as well so I cleared the screen and highlighted the message in green with a side note with the length of the password as the score.

This was my very first program that I ever created in python so it does have a lot of issues that needs to be fixed.

```
