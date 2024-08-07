import sys
import PyPDF2

def merge_pdfs(pdf_list, output_path):
    pdf_merger = PyPDF2.PdfMerger()

    for pdf in pdf_list:
        pdf_merger.append(pdf)

    with open(output_path, 'wb') as output_pdf:
        pdf_merger.write(output_pdf)


def main():
    output_pdf = 'merged_output.pdf'
    pdf_files=[]

    if len(sys.argv) < 2:
        print("No args??")
        sys.exit(1)

    # Access command-line arguments
    for arg in sys.argv[1:]:
        pdf_files.append(arg)

    merge_pdfs(pdf_files, output_pdf)
    print(f'Merged PDF saved as {output_pdf}')

if __name__=='__main__':
    main()