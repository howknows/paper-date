# paper-date

ever wonder what the research date was on a paper? me too. 

this extracts PDF creation time from metadata and converts it to huma-readable for a possible approximate research time.

requirements:
pdfminer:
git clone https://github.com/euske/pdfminer.git

usage: python paper-date [pdf file]

example:

python paper-date.py wei-apan-v10.pdf 

output:
Research for wei-apan-v10.pdf was probably conducted around 2008-07-01 18:45:10 according to PDF creation time.


