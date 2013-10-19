# Bingo Square Generator
# n! / (n - r)!; 24! = 620,448,401,733,239,439,360,000 = 6.2 x 10^23

import random
import sys

try:
    filename = sys.argv[1]
    sheets = sys.argv[2]
    title = sys.argv[3:]
except IndexError:
    print "Parameters for bingo.py: filename, number of sheets to create, title."
    sys.exit(1)

try:
    with open(filename) as bingo_squares_file:
        bingo_squares = bingo_squares_file.read().split("\n")
        if len(bingo_squares) < 24:
            print "Include at least 24 items in your file to create a full bingo sheet!"
            sys.exit(1)
except IOError:
    print "Failed to open {0}".format(filename)
    sys.exit(1)

try:
    sheets = int(sheets)
except Exception:
    sheets = 1

title = ' '.join(title)

# Removing illegal filename characters from title so it can be used to create a file
title = title.replace("\\","").replace("/","").replace(":","").replace("*","").replace("?","").replace('"',"").replace("<","").replace(">","").replace("|","")

for sheet_num in xrange(sheets):

    with open("{0}{1}.html".format(title, sheet_num), "a") as bingo_square_output:

        bingo_square_output.write("<html><b>{0} Sheet #{1}</b><br><table border=1 cellpadding=10 width=850>\r\n".format(title, sheet_num))

        square_num = 1

        random.shuffle(bingo_squares)

        for squares in bingo_squares:

            if (square_num in (1,6,11,15,20)):
                bingo_square_output.write("<tr>\r\n")

            if (square_num == 13):
                bingo_square_output.write('<td style="height:150px; width: 20%; text-align: center; vertical-align: text-center;"><b>Free space</b></td>\r\n<td style="height:150px; width: 20%; text-align: center; vertical-align: text-center;">{0}</td>\r\n'.format(squares))
            else:
                bingo_square_output.write('<td style="height:150px; width: 20%; text-align: center; vertical-align: text-center;">{0}</td>\r\n'.format(squares))

            if (square_num in (5,10,14,19,24)):
                bingo_square_output.write("</tr>\r\n")

            square_num += 1

            if square_num >= 25:
                break

        bingo_square_output.write("</table></html>")

print "Finished creating {0} {1} bingo sheets".format(sheets, title)
