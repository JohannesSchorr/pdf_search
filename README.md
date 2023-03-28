# PDF-Search

Determine if a given search-text is in one or a number of pdf's that is 
given within a given search path

## Usage from Console

### Introduction

From the console two ways of using the script are possible. 
1. by passing arguments to the function within the console
2. passing **no arguments** to the module within the console

### With arguments

Passing this file to the console with arguments as follows searches the 
pdfs in the given directory ``path\\to\\directory`` for the given ``search-text``:
```
>>> python pdf_search.py 'search-text' 'path\\to\\directory'
```
### Without arguments

Passing this file without arguments to the console starts a file-dialog as follows::

```
> python pdf_search.py
Please insert text to search for in pdfs: 'search-text'
Please insert the directory to search in (Default: current directory): 'path\\to\\directory'
```

## Usage in python

```python
from pdf_search import check_pdfs
check_pdfs(search_text='search-text', directory='path\\to\\directory')
```