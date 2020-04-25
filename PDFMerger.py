from PyPDF2 import PdfFileMerger
import tkinter
from tkinter import filedialog

root = tkinter.Tk()
filespdf = filedialog.askopenfilenames(parent=root,title='Escolha os arquivos para mesclar',filetypes = (("pdf files","*.pdf"),))
pdfs = (root.tk.splitlist(filespdf))

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

create_pdf = tkinter.Tk()
create_pdf.withdraw()
create_pdf.filename = filedialog.asksaveasfilename(title = "Salvar como excel como",filetypes = (("pdf file","*.pdf"),))

merger.write(create_pdf.filename+'.pdf')