This lab just consisted of one file called lab6.py and a couple other files for the dataset and the
stop-word-list and explicit terms file. The dataset used is called billboard_lyrics_1964-2015.csv. It
is rather large so I don't recommend opening it since it caused atom to crash a couple times when i did. The
stop-word-list.txt is a file of the meaningless words I filtered out of the Term frequency calculations.
Terms-to-Block.csv is the list of explicit words I used for explicit lyric analysis over time for the
songs in the dataset.

All of the code I used for graphs and visualization purposes
is commented out to allow the program to run completely through. All of the output is
in the command line and meaningful graphs and text analysis are described in the report.

The packages used in the program were:
    import numpy as np
    import csv
    from collections import Counter
    import operator
    import matplotlib.pyplot as plt
    import math as math

I didn't end up using nltk so I just commented it out.

You can simply run the file after making sure the dataset, stop-word-list, and Terms-to-Block
are in the same directory as lab6.py. just do:

        python lab6.py and the file will run all the way through and output into the terminal.
