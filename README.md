Bingo Sheets

Generates a number of Bingo Sheets in a simple HTML format.

First, create a list of at least 24 items to use and save it as a text file, one item per line.

Next, at the command line, run: python bingo.py <text file of your items> <number of sheets to create> <title of your sheets - if your title has spaces, wrap it in quotes>

Example:  python bingo.py fruits.txt 10 "Yummy Fruits"

Bingo.py will then generate 10 random bingo sheets based on fruits.txt and save them in the working directory as <title>-<sheet number>.html