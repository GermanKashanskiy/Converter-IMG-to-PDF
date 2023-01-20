from PIL import Image
import docx2pdf
import re

# This is where you enter the location of the file
image_input = input("Enter the location of the file ")


# Here the input is filtered to determine the file type
def file_convert(file_name):
    match_jpg = re.search(r'\.(jpe?g)$', file_name, re.IGNORECASE)
    match_png = re.search(r'\.(png)$', file_name, re.IGNORECASE)
    match_webp = re.search(r'\.(webp)$', file_name, re.IGNORECASE)
    match_docx = re.search(r'\.(docx)$', file_name, re.IGNORECASE)

    # Here is the converting of files to pdf
    if match_jpg:
        image = Image.open(file_name)
        image.save("output-jpg.pdf", "PDF", resolution=100.0)
    elif match_png:
        image = Image.open(file_name)
        image = image.convert("RGB")
        image.save("output-png.pdf", "PDF", resolution=100.0)
    elif match_webp:
        image = Image.open(file_name)
        image.save("output-webp.pdf", "PDF", resolution=100.0)
    elif match_docx:
        docx2pdf.convert(file_name, "output-docx.pdf")
    else:
        print("You need to enter location of file with type of file. For example C:/../../image.png, "
              "C:/../../image.webp \n")

    print("END")


file_convert(image_input)
