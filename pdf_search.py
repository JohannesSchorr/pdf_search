from pathlib import Path
import re
from pdfminer.high_level import extract_text

"""
PDF-Search
==========
Determine if given search-text is in one or a number of pdf's that is 
given within a given search path

Usage from Console
------------------
Introduction
############
From the console two ways of using the script are possible. 
1. by passing arguments to the function within the console
2. passing **no arguments** to the module within the console

With arguments
##############
Passing this file to the console with arguments as follows searches the 
pdfs in the given directory ``path\\to\\directory`` for the given ``search-text``::
   
   > python pdf_search.py 'search-text' 'path\\to\\directory'

Without arguments
#################
Passing this file without arguments to the console starts a file-dialog as follows::
   
   > python pdf_search.py
   Please insert text to search for in pdfs: 'search-text'
   Please insert the directory to search in (Default: current directory): 'path\\to\\directory'


Usage via python
----------------

.. code-block:: python
   
>>> from pdf_search import check_pdfs
>>> check_pdfs(search_text='search-text', directory='path\\to\\directory')
"""


def is_pdf(file_name: str) -> bool:
    """check if file is pdf using the ending

    Parameters
    ----------
    file_name : str
        name of the file that is to be checked

    Returns
    -------
    bool
      - True in case a pdf-file
      - False in case not a pdf-file
    """
    if re.search(pattern="^.*?\.pdf$", string=file_name) is not None:
        return True
    else:
        return False


def is_text_in(pdf_text: str, search_text: str) -> bool:
    """check if ``search_text`` is in ``pdf_text`` using Regular Expressions

    Parameters
    ----------
    pdf_text : str
        text of the pdf
    search_text : str
        text to look for in the pdf

    Returns
    -------
    bool
        ``True`` if ``search_text`` is found, otherwise ``False``
    """
    if re.search(pattern=search_text, string=pdf_text, flags=re.IGNORECASE) is not None:
        return True
    else:
        return False


def check_pdfs(directory: str, search_text: str):
    """
    check bunch of pdf's in a given directory for specifc search_text

    Prints out relevant pdfs.
    Sub-directories will not be searched.

    Parameters
    ----------
    directory : str
        directory with a number of pdf's to search for
    search_text : str
        text to search pdf's for
    """
    path = Path(directory)
    if not path.exists():
        raise ValueError(f"Path {directory} does not exists.")
    pdf_names = []
    print(f"\nStart searching in directory '{path.absolute().__str__()}'")
    for file in path.iterdir():
        if is_pdf(file.__str__()):
            print(f'\tsearch file "{file.name}"')
            pdf_text = extract_text(file.absolute().__str__())
            if is_text_in(pdf_text, search_text):
                print(f"\t\t{search_text=} found in pdf '{file.name}'.")
                pdf_names.append(file)

    if len(pdf_names) == 0:
        print(f"\n\tNo pdf in {directory=} found.")
    else:
        print(f"\n\tPdf's with {search_text=} inside:")
        for name in pdf_names:
            print(f"\t\t- {name.name}")


def dialog() -> None:
    """dialog to user"""
    text = input("Please insert text to search for in pdfs: ")
    directory = input(
        "Please insert the directory to search in (Default: current directory): "
    )
    if directory == "":
        directory = "."
    check_pdfs(directory=directory, search_text=text)


def main():
    """run if module is called from the command-line"""
    from argparse import ArgumentParser

    parser = ArgumentParser(
        description="Prints the name of the pdf's where the given search-text is included."
    )
    parser.add_argument(
        "-t", "--text", help="text to search for in pdf's", default="", type=str
    )
    parser.add_argument(
        "-d",
        "--directoryname",
        help="name of the directory where pdf's are located. Defaults to the current directory.",
        default=".",
        type=str,
    )
    args = parser.parse_args()
    if args.text == "":
        dialog()
    else:
        check_pdfs(directory=args.directoryname, search_text=args.text)


if __name__ == "__main__":
    main()
