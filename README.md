# textSummarizer
Tool to help with academic study/research work for condensing the meaning of large bodies of text into summarized text

For now, it is page numbers that the user will be inputting, but in a while, I'm going to augment this with search too.
So in the future, you'll be inputting a topic, and the code will go through MULTIPLE e_books and return a condensed 
output which is much more easily readable.

Great uses in note making for academic purposes + literature reviews and tedious manual work in researching.

For now,
this code takes in from_page and to_page integers, and points to just one pdf -> sample.pdf (Which is Jurafsky Martin's Speech and Text Recognition pdf)

It uses pdfminer to extract text from the pdf, and it takes a LONG time.
For some reason (probably versioning), PyPDF2 does not work. It is an EXTREMELY fast solution, but until I resolve it,
I'm going to use pdfminer.

So it extracts the text, and cleans it for non Alnum + full stop characters.
We finally use gensim's summarizer to summarize the text. I am yet to tune this summarizer, but the default settings give
a pretty good output.

You get a pagewise summary of an output, which is good.

Note : pdfminer can possibly be the result of data loss, i.e, it reads only 70-80% of the page. This is an OCR problem and I
really can't tweak the algo for that, but PyPDF2 offers a cleaner output for English docs.

So until I get that working, pdfminer will have to be placeholder

Looking forward to making this better !
