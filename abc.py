from pdfminer.high_level import extract_text
text = extract_text('5.3.3.pdf')
with open('./Commitee/Highlights.txt', 'w') as f:
    f.write(text)