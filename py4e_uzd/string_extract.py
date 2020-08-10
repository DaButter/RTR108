text = "X-DSPAM-Confidence:    0.8475";

#Extract 0.8475 from text, convert to floating point number, print it out

a=text.find('0.8475') # atrod kur sakas mekletais teksts
b=(text[a:])
print(float(b)) # koverte str uz float un izprinte

