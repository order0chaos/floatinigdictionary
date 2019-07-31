from tkinter import *
from bs4 import BeautifulSoup
import requests

def funct():
    Word = ment.get()
    source = requests.get('https://www.google.com/search?q='+ Word+'+meaning').text
    soup = BeautifulSoup(source, 'lxml')
    search = soup.find('div', class_='BNeawe deIvCb AP7Wnd')
    Label(wind, text = search.text).pack()
    # Label(wind, text = '').pack()
    # print(search.text)
    pronounce = soup.find('div', class_="BNeawe tAd8D AP7Wnd")
    Label(wind, text = pronounce.text).pack()
    Label(wind, text = '').pack()
    # print(pronounce.text)
    grammar = soup.find('div', class_="BNeawe s3v9rd AP7Wnd").span
    Label(wind, text = grammar.text).pack()
    Label(wind, text = '').pack()
    # print(grammar.text)

    c = 0
    
    for definition in soup.find('div', class_="BNeawe s3v9rd AP7Wnd"):
        if not c==0:
            # continue
            Label(wind, text = "  "+ str(c)+ " : "+ definition.text).pack()
        c+=1

# def getme():
    # opens second dialogue box
wind = Tk()
wind.eval('tk::PlaceWindow %s center' % wind.winfo_toplevel())
wind.title('search')


label = Label(wind, text = "GOOGLE SEARCH")
label.pack()
ment = StringVar()
entry = Entry(wind, textvariable = ment)
entry.pack()
Button(wind, text = 'search', command = funct).pack()
# button.pack()

wind.mainloop()

wind.deiconify()
wind.destroy()
wind.quit()
    

# win = Tk()
# win.geometry('250x40')
# win.title('search')

# #google button
# b_google = Button(win, text='google', command=getme)
# b_google.pack()

# win.mainloop()
