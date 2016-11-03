import math
import pandas as pd
import nltk
import re # regular expressions for pattern matching
from nltk.corpus import webtext # contains the pirates of the caribbean movie script. You may need to download this corpus using nltk.download()

def load_pirates_movie_script():
    return pd.DataFrame(
        data=webtext.raw('pirates.txt').splitlines(),
        columns=["line_of_script"])

pirates_of_the_caribbean = load_pirates_movie_script()
pirates_of_the_caribbean.head()

def create_dialogue_element(line):
    # Now we're going to make a pattern that describes what a line of dialogue
    #   looks like in this movie script
    #
    # Visualize this regular expression at https://www.debuggex.com/r/Gpqh5VW146QH4acn
    dialogue_pattern = r'''(?x)
          (?P<character_name>  # Create a capturing group called `character_name`
              [A-Z,\s]+)       #   Where movie character names contain either ALL CAPS letters or spaces
          :                    # followed by a colon,
          \s*                  # followed by some whitespace,
          (?P<what_they_say>   # Then create a capturing group for what the movie character actually says
              .*               #   Where what they actually say can be any characters 0 or more,
              $)               #   followed by the end of the line
    '''
    possible_match = re.match(line, dialogue_pattern)
    if possible_match and hasattr(possible_match, groupdict):
        return possible_match.groupdict()
    else:
        return None

# error: multiple repeat at position 39
pirates_of_the_caribbean["line_of_script"].apply(create_dialogue_element)
