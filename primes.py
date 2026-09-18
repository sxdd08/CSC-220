'''
Name: Siddiqi Komou
Email: siddiqikomou08@gmail.com
Date: 9/15/2026
Course Number: CSC-220
Course Name: Data Sturctures and Algorithms
Problem Number:
Problem Description:
'''

'''
Academic Honor Code Goes Here:
I certify that this code is my own work and was
not generate by AI or copied form any unauthroized
source. I understand that while AI or tools like 
ChatGPT may assist with my learning, the code
I submit must  reflect my personal understanding.
Relying on external sources without comprehension
undermines my learning and may result in a lower
grade. If there are any concerns about my submission,
I am willing to meet during lab within two weeks of 
grading to demonstrate my understanding.
'''

#
# DO NOT REMOVE THE COMMENTS MADE IN THIS TEMPLATE!
#

# **********************************************
# imports here
from library import get_integer, confirm_input, count_primes, count_gaps, determine_largest_prime_gap

# **********************************************
# Define as many constants you need here

TITLE = "CSC-220 Prime Patterns in Range V1.0: Siddiqi Komou"
CONTINUE_PROMPT = "Do this again? [y/N] "


# **********************************************
# Define as many functions or classes you need here
" Set all of my function definitions with constraints in library.py"


# **********************************************
# Start your logic coding in the process function
def process():
    start = get_integer("Enter start: ")
    end = get_integer("Enter end: ")

    if not confirm_input(start, end):
        return

    prime_count = count_primes(start, end)
    gap_count = count_gaps(start, end)
    largest_gap, first_prime, second_prime = determine_largest_prime_gap(start, end)

    print(f"Count of primes: {prime_count}")

    if gap_count > 0:
        print(f"Largest gap: {largest_gap} (between {first_prime} and {second_prime})")
    else:
        print("Largest gap: 0")

    


# **********************************************
# Do not change the main function
def main():
    def do_this_again(prompt):
        do_over = input(prompt).strip()
        return do_over.lower() == 'y'
    print(f"Welcome to {TITLE}")
    while True:
        process()
        if not do_this_again(CONTINUE_PROMPT):
            break
    print(f"Thank you for using {TITLE}")


if __name__ == "__main__":
    main()
