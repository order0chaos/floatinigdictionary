from tkinter import *
from tkinter import simpledialog
from bs4 import BeautifulSoup
import requests

def getme():
    s = simpledialog.askstring("dictionary", 'enter the word')
    wind = Tk()
    wind.eval('tk::PlaceWindow %s center' % wind.winfo_toplevel())
    wind.title('search result')
    source = requests.get('https://www.google.com/search?q='+ s +'+meaning').text
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
    
    for definition in soup.find_all('div', class_="BNeawe s3v9rd AP7Wnd"):
        if not c==0:
            # continue
            Label(wind, text = "  "+ str(c)+ " : "+ definition.text).pack()
        c+=1
        if c > 4:
            break


win = Tk()
win.geometry('250x100')
# height of a button is 25
# win.withdraw()

Button(win, text= 'google', command=getme).pack()
# Button(win, text = 'dictionary.com').pack()
Button(win, text='dictionary.com', command=getme).pack()
# button2.pack()

win.mainloop()