print("Hello Wlord")
# as you can see, I made a typo in line 1 on the word World. The program will still run without error
# because my typo was inside parenthesis. If my typo was in print, then there would have been an error

# problem 2 - after doing import this into a python terminal session a message appears. It starts
# with the Zen of Python, by Tim Peters. Then the text reads beautiful is better than ugly, explicit
# is better than implicit, then continues.

# the stuff below is for problem 3
message_1 = "Hello world!"
print(message_1)


# problem 4
# 8-1
# the first part, defining the function
def display_message():
    """Displays a message about what I'm Learning"""
    print("I'm learning how to define a function!"
          "The line above this is called a"
          "docstring, it describes what the function "
          "does.")


# calling the function
# left two blank lines after defining function
display_message()

# 8-2
# defining the function

# defining variable for function to call
book_1 = "harry potter"

# defining the function
# .title() makes title of the book caps


def favorite_book():
    """MY favorite book"""
    print(f"My favorite book is {book_1.title()}!")


# calling the function
favorite_book()



