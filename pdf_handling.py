from PyPDF2 import PdfFileReader, PdfFileWriter

def merge_pdf(infnList, outfn):
    
    pdf_output = PdfFileWriter()
    
    for infn in infnList:
        pdf_input = PdfFileReader(open(infn, 'rb'))
        
        page_count = pdf_input.getNumPages()
        
        for i in range(page_count):
            pdf_output.addPage(pdf_input.getPage(i))
            
    pdf_output.write(open(outfn, 'wb'))


def split_pdf(input_pdf, out_num, split_site):

    for i in range(out_num):
        with open(input_pdf, 'rb') as open_pdf, open(str(i)+'.pdf', 'wb') as write_pdf:
            pdfReader = PdfFileReader(open_pdf)
            pdfWriter = PdfFileWriter()
            for j in range(i*split_site, (i+1)*split_site):
                page = pdfReader.getPage(j)
                pdfWriter.addPage(page)
            pdfWriter.write(write_pdf)
