import pyperclip

text=pyperclip.paste()

listItems=text.split('\n')
for i in range(len(listItems)):
    listItems[i]="* "+listItems[i]

text="\n".join(listItems)

pyperclip.copy(text)
print(text)
