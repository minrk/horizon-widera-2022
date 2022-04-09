#!/usr/bin/env python3
"""
Check final.pdf is not too long. Raise ValueError if it is too long.

"""

import subprocess


def check_page_length(document="final.pdf", max_allowed_pages=40):
    # establish current number of pages, store output in pdftk-output.txt
    subprocess.check_call(
        f"pdftk {document} dump_data_annots output pdftk-data-annots-output.txt".split()
    )

    # retrieve length
    for line in open("pdftk-data-annots-output.txt", "rt"):
        if line.startswith("NumberOfPages:"):
            pages = int(line.split("NumberOfPages:")[1])
            # we ignore everything else in the output file
            break

    msg = f"{document} has {pages} pages (out of a maximum of {max_allowed_pages})."
    print(msg, end=" ")
    if pages > max_allowed_pages:
        msg2 = f"That is {pages-max_allowed_pages} pages too many."
        print(msg2)
        raise ValueError(msg + " " + msg2)
    elif pages == max_allowed_pages:
        pass
    else:
        print(f"{max_allowed_pages-pages} additional pages are allowed.")


if __name__ == "__main__":
    check_page_length()
