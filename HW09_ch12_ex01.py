#!/usr/bin/env python
# HW09_ch12_ex01
# (1) Write a function called most_frequent that takes a string and prints the
#     chars in decreasing order of frequency. (compare and print in lowercase)
# Ex. >>> most_frequent("aaAbcc")
#     a
#     c
#     b
###############################################################################
# Imports


# Body
def create_histogram(s):
  # make a map of letters to number of times they appear in s 
  hist = {}
  for x in s:
    hist[x] = hist.get(x, 0) + 1
  return(hist)

def most_frequent(s):
  #make list all lowercase
  for letter in s:
    letters = s.lower()

  #create a histogram
  hist = create_histogram(letters)

  #for letter + values in histogram, return a list of letters & counts
  t = []
  for letter, count in hist.items():  #.items takes a dict >> tuples
    t.append((count, letter))

  #sort the list, return the letters + counts
  t.sort(reverse = True)
  for count, letter in t:
    print(letter, count)



###############################################################################
def main():   # DO NOT CHANGE BELOW
    print("Example 1:")
    most_frequent("abcdefghijklmnopqrstuvwxyz")
    print("\nExample 2:")
    most_frequent("The quick brown fox jumps over the lazy dog")
    print("\nExample 3:")
    most_frequent("Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
                  "sed do eiusmod tempor incididunt ut labore et dolore magna "
                  "aliqua. Ut enim ad minim veniam, quis nostrud exercitation "
                  "ullamco laboris nisi ut aliquip ex ea commodo consequat. "
                  "uis aute irure dolor in reprehenderit in voluptate velit "
                  "esse cillum dolore eu fugiat nulla pariatur. Excepteur "
                  "sint occaecat cupidatat non proident, sunt in culpa qui "
                  "officia deserunt mollit anim id est laborum.")
    print("\nExample 4:")
    most_frequent("Squdgy fez, blank jimp crwth vox!")

if __name__ == '__main__':
    main()



