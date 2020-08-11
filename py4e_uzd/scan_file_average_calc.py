# Use the file name mbox-short.txt as the file name
count = 0
total = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    if line.startswith("X-DSPAM-Confidence:") :
        count=count+1 #sakrit ar faila izvadito rindu skaitu
    a=line.find('0.')
    b=float((line[a:])) # izvada visus skaitlus no rindas float formaa
    total = total + b # visu sk summa
print('Average spam confidence:',total/count) # izvada videejo vertibu
