#!/usr/bin/env python3
"""
Check final.pdf is not too long. Raise ValueError if it is too long.

"""

MB = 1e6  # 1 MegaByte: use 1e6 not 2^20 to get more conservative estimate

import os
import subprocess


def check_page_length(document="final.pdf", max_allowed_pages=45):
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


def check_file_size(document="final.pdf", limit=10 * MB):
    filesize = os.stat(document).st_size  # in bytes
    msg = f"{document} has a size of {filesize/MB} MB  (limit: {limit/MB} MB)"
    print(msg)
    if filesize >= limit:
        msg2 = f"File is too large."
        print(msg2)
        raise ValueError(msg + " " + msg2)


if __name__ == "__main__":
    check_page_length()
    check_file_size()
