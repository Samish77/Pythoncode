text=input("Enter the text \n")
if("Make a lot of money" in text):
    spam=True
elif("buy now"in text):
    spam=True
elif("subscribe this" in text):
    spam=True
else:
    spam=False  

if(spam):
    print("text is spam")
else:
    print("text is not a spam")      