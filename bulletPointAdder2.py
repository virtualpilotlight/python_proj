import pyperclip
text = pyperclip.paste()
text = text.split("\n")
for i in text:
    print( "* " + i)
