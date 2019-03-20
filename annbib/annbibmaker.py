import os
import bibtexparser

class AnnotatedBibliographyMaker:
    def __init__(self, database, target):
        self.database = database
        self.target_dir = target
        self.bibliography_db = bibtexparser.bibdatabase.BibDatabase()

    def make_bibliography(self):
        bibfile = open(f"{self.target_dir}/main.bib", "w")
        mainfile = open(f"{self.target_dir}/main.tex", "w")

        self.add_frontmatter(mainfile)

        for i, (dirpath, dirnames, filenames)  in enumerate(os.walk(self.database)):
            print(f"Parsing through directory {dirpath}...")
            for entry in filenames:
                if entry.endswith(".bib"):
                    self.add_entry(bibfile, entry[:-4])

        self.add_backmatter(mainfile)

        self.add_bibliography(bibfile)

        bibfile.close()
        mainfile.close()

    def add_frontmatter(self, mainfilename):
        preamble = "\n".join([
        r"\documentclass{article}",
        r"",
        r"\usepackage{annotated-bib}",
        r"",
        r"\title{Annotated Bibliography}",
        r"\author{ }",
        r"\date{\today}",
        r"",
        ])
        mainfilename.write(preamble)

        frontmatter = "\n".join([
        r"\begin{document}",
        r"",
        r"\nocite{*}",
        r"\bibliographystyle{annotate}",
        r"\bibliography{main.bib}",
        r"",
        r""
        ])
        mainfilename.write(frontmatter)

    def add_backmatter(self, mainfilename):
        backmatter = "\n".join([
        r"\end{document}"
        ])

        mainfilename.write(backmatter)

    def add_entry(self, bibfilename, entry):
        entry_bib = open(f"{self.database}{entry}.bib", "r")
        entry_tex = open(f"{self.database}{entry}.tex", "r")

        new_entry = bibtexparser.load(entry_bib).entries[0]
        annotation = entry_tex.read()
        new_entry["annotate"] = annotation

        self.bibliography_db.entries.append(new_entry)

        entry_bib.close()
        entry_tex.close()

    def add_bibliography(self, bibfilename):
        bibtexparser.dump(self.bibliography_db, bibfilename)
