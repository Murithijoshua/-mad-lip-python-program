# Our Mad Lib
madlib = "On the %s trip to %s, my %s friend and I decided to invent a game. Since this would be a rather %s trip, it would need to be a game with %s and %s. Using our %s to %s, we tried to get the %s next to us to play too, but they just %sed at us and %s away. After a few rounds, we thought the game could use some %s, so we turned on the %s and started %s to the %s that came on. This lasted for %s before I got %s and decided to %s. I'll never %s that trip, it was the %s road trip of my %s."
sourceURL = "http://marcelkupka.cz/wp-content/uploads/2013/03/mad.jpg"
# A list storing the blanks for the Mad Lib
blanks = [
    {"suggestion": "adjective", "ans": ""},
    {"suggestion": "place", "ans": ""},
    {"suggestion": "adjective", "ans": ""},
    {"suggestion": "adjective", "ans": ""},
    {"suggestion": "noun, plural", "ans": ""},
    {"suggestion": "noun, plural", "ans": ""},
    {"suggestion": "noun", "ans": ""},
    {"suggestion": "verb", "ans": ""},
    {"suggestion": "noun", "ans": ""},
    {"suggestion": "verb", "ans": ""},
    {"suggestion": "action verb", "ans": ""},
    {"suggestion": "noun, plural", "ans": ""},
    {"suggestion": "noun", "ans": ""},
    {"suggestion": "verb that ends in ing", "ans": ""},
    {"suggestion": "noun", "ans": ""},
    {"suggestion": "measurement of time", "ans": ""},
    {"suggestion": "adjective", "ans": ""},
    {"suggestion": "action verb", "ans": ""},
    {"suggestion": "verb", "ans": ""},
    {"suggestion": "adjective", "ans": ""},
    {"suggestion": "noun, something you can own", "ans": ""}
]
print("Road Trip Mad Lib\nWhen the program asks you, please enter the appropriate word.")
print("There are %i blanks in this Mad Lib. " % (len(blanks)))
# Ask the user for each one
for blank in blanks:
    ans = input(blank['suggestion'].capitalize() + "> ")
    if len(ans) == 0:
        print("Please don't leave anything blank. It kills the experience.")
        quit()
    blank['ans'] = ans
# The list that stores the format string
fs = []
# Get the answers from the blanks list
for dictionary in blanks:
    fs.append(dictionary['ans'])

# Print the formatted Mad Lib
#ending
print(madlib % tuple(fs))
feedback = input("Pretty funny, right? [y/n] ")
if feedback == "y":
    print("Thanks!")
else:
    print(":( Sorry. I'll try better next time.")
print("\n" + "="*10 + "\nMad Lib sourced from " + sourceURL)
