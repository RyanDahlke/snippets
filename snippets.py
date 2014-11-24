#!/usr/bin/env python

import logging
import csv
import argparse
import sys

# Set the log output file, and the log level
logging.basicConfig(filename="output.log", level=logging.DEBUG)

def put(name, snippet, filename):
    """ Store a snippet with an associated name in the CSV file """
    logging.info("Writing {!r}:{!r} to {!r}".format(name, snippet, filename))
    logging.debug("Opening file")
    with open(filename, "a") as f:
        writer = csv.writer(f)
        logging.debug("Writing snippet to file")
        writer.writerow([name, snippet])
    logging.debug("Write sucessful")
    return name, snippet

# Store an iteam using a fully qualifed names
python snippets.py --type "put" --name "spam" --snippet "eggs" --filename "snippets.csv"

# Store an item using abbreviations.
python snippets.py -t "put" -n "spam" -s "eggs" -f "snippets.csv"

# Have a default argument for filename, so we can leave it empty.
python snippets.py -t "put" -n "spam" -s "eggs"

#Use positonal rather than optional arguments
python snippets.py put spam eggs snippets.csv

#As above, but with a default arugment for filename.
python snippets.py put spam eggs

def make_parser():
    """ Construct the command line parser"""
    logging.info("Constructing parser")
    description = "Store and retrieve snippets of text"
    parser = argparse.ArgumentParser(description = description)

    return parser

def main():
    """ Main Function"""
    logging.info("Starting snippets")
    parser = make_parser()
    arguments = parser.parse_args(sys.argv[1:])

if __name__ == "__main__":
    main()