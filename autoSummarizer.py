""" Author - Aryamaan Parikh
Python 2.7 



"""


from gensim.summarization import summarize
import pdf2txt
import re
def particularRangeSearch(textlist, frompage,topage):
    summarized = []
    print("Summarized Text is :" + "\n")
    for t in range(frompage,topage+1):
        # print(type(textlist[t]))
        print("Page" + str(t) + "\n")
        summ = summarize(textlist[t], split=False)
        summ = re.sub(" +"," ",summ)
        summarized.append(summ)
        #CHECK TUNING OPTIONS
        print(str(summ) + "\n")
    return summarized

def dataCleaner(textlist):
    cleanText = []
    for t in textlist:
        t = re.sub("[^a-zA-Z0-9.]"," ",t)
        cleanText.append(t)
    return cleanText

def sectionSearcher(textlist, keywords):
    ##LATER
    pass #Take keywords, and go to index section, then find page numbers
    #And then call particularRangeSearch

if __name__ == "__main__":

    pgnoStart = input("Enter the starting page number which you want to convert.")
    pgnoEnd = input("Enter the last page number (included)")
    pdfpath = "sample.pdf"  # Enter path of your pdf file here
    if(pdf2txt.validator(pdfpath)):
        extractedText = pdf2txt.convertWithPdfMiner("sample.pdf")
    else:
        vecPath = pdf2txt.scan2vec(pdfpath)
        extractedText = pdf2txt.convertWithPdfMiner(vecPath)

    cleanExtractedText = dataCleaner(extractedText)
    summarized_text = particularRangeSearch(cleanExtractedText,pgnoStart,pgnoEnd)
