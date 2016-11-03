Does _Pirates of the Caribbean: Dead Man's Chest_ pass the Bechdel Test? A Digital Humanities lesson for undergraduates: 

# Current Status: CODE BORKEN; DONUT USE

## Where I need help.

Pythonistas and data scientists: I'm struggling with pandas and pattern-matching in text. I'm trying to write a lesson where we see whether a terrible movie passes the Bechdel test. NLTK's webtext corpus has _Pirates of the Caribbean: Dead Man's Chest_, so we're using that. But I think [I'm doing regular expressions and pandas wrong](https://github.com/ComputationalModeling/text-processing-and-the-bechdel-test/blob/c725a04bdb2ff0b324f574e265203125186376b8/bechdel.py).

What I think I want: to read a script line-by-line, check whether a given line is a line of dialogue (by pattern matching against a regex), and if that line is dialogue I want to extract the character name and the speech.

I've been getting by with the `re` module, but I end up writing contorted code with multiple calls to re.match and all sorts of conditional checks (make sure it matches, make sure the match has a `goupdict` attribute before I try to access it, and so on.) Is there a better/simpler way to be doing this?
