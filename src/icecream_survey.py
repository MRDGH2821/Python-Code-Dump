"""Icecream Survey.

Takes a survey of icecream flavors & displays selected flavor.
"""

import sys

from easygui import ccbox, choicebox, msgbox

while True:
    msgbox("Hello, world!")
    msg = "What is your favorite flavor?"
    title = "Ice Cream Survey"
    choices = ["Vanilla", "Chocolate", "Strawberry", "Rocky Road"]
    choice = choicebox(msg, title, choices)
    # note that we convert choice to string, in case
    # the user cancelled the choice, and we got None.
    msgbox("You chose: " + str(choice), "Survey Result")
    msg = "Do you want to continue?"
    title = "Please Confirm"
    if ccbox(msg, title):  # show a Continue / Cancel dialog
        pass  # user chose Continue
    else:
        sys.exit(0)
