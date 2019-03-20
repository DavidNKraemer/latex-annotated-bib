import argparse
import os
import subprocess
from annbib import AnnotatedBibliographyMaker

parser = argparse.ArgumentParser()

parser.add_argument(
        "database", 
        type=str,
        help="directory of .tex and .bib files"
        )

parser.add_argument(
        "target",
        type=str,
        help="directory of all of the stuff getting created"
        )

args = parser.parse_args()

annotated_bibmaker = AnnotatedBibliographyMaker(args.database, args.target)
annotated_bibmaker.make_bibliography()

wd = os.getcwd()
os.chdir(f"{args.target}")
subprocess.run(["latexmk", "-c"])
subprocess.run(["latexmk", "-pdf"])
subprocess.run(["latexmk", "-c"])
os.chdir(wd)

