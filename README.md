# PDF-Search

Determine if a given search-text is in one or a number of pdf's that is 
given within a given search path

## Dependencies

For accessing the text of the pdf's the [pdfminer](https://pdfminersix.readthedocs.io/en/latest/)-package is needed, that must [be installed](https://pdfminersix.readthedocs.io/en/latest/tutorial/install.html) beforehand.

Furthermore, ``pdf_search`` depends on [pathlib](https://docs.python.org/3/library/pathlib.html) and [re](https://docs.python.org/3/library/re.html) that are both given in the [Standard-Library](https://docs.python.org/3/) of Python 3.

## Usage

### Usage from Console

#### Introduction

From the console two ways of using the script are possible. 
1. by passing arguments to the function within the console
2. passing **no arguments** to the module within the console

#### With arguments

Passing this file to the console with arguments as follows searches the 
pdfs in the given directory ``path\\to\\directory`` for the given ``search-text``:
```
>>> python pdf_search.py 'search-text' 'path\\to\\directory'
```
#### Without arguments

Passing this file without arguments to the console starts a file-dialog as follows::

```
> python pdf_search.py
Please insert text to search for in pdfs: 'search-text'
Please insert the directory to search in (Default: current directory): 'path\\to\\directory'
```

### Usage in python

```python
from pdf_search import check_pdfs
check_pdfs(search_text='search-text', directory='path\\to\\directory')
```

## Use cases

Imagine you have a number of papers, e.g. from a conference. 
And you want to filter those papers writen by a specific author, but the naming of the pdfs gives no evidence who has written the paper.

Now, you could open every paper and look for the specific name until you find the desired one. 
This is a tedious task and by the way very time-consuming and boooooooring.
Here, ``pdf_search`` comes into play and will do that task for you while you may - for example - drink a cup of coffee.