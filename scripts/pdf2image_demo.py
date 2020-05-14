from pdf2image import convert_from_path
import matplotlib.pyplot as plt
img_page = convert_from_path(PDF_PATH, first_page=0, last_page=0)[0]
print(img_page)
plt.imshow(img_page)
