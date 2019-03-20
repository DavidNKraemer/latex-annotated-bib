# latex-annotated-bib
A small project for managing annotated bibliographies in LaTeX

# Dependencies:

* Python
  * `bibtexparser`
* system
  * `latexmk`

# Example usage:

```
$ python annbib.py database targets
```

This takes every `.tex` and `.bib` file with the same name and merges them into one bibliography entry, compiles, and renders them into a single PDF.
