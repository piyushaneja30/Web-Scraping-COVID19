from tkinter import *
import requests
import bs4

def details():
    url='https://www.mygov.in/covid-19/'
    html_data=requests.get(url)
    clean_data=bs4.BeautifulSoup(html_data.text,'html.parser')
    span=clean_data.findAll('span',class_='icount')

    headings=['Active','Total Cases','Discharged','Deaths']
    i=0
    all_details=''
    for data in span:
        all_details=all_details+headings[i]+' '+data.get_text()+'\n\n'
        i+=1

    return all_details


def refresh():
    new_data=details()
    dataLabel.config(text=new_data)



root=Tk()
root.title('Covid 19 Details Of India')
root.iconbitmap('icon.ico')

root.geometry('550x550+225+50')
root.config(bg='red')

logoimage=PhotoImage(file='icon.png')

logoLabel=Label(root,image=logoimage,bg='yellow')
logoLabel.pack()

dataLabel=Label(root,bg='red',text=details(),font=('poppins',20,'bold'),fg='white')
dataLabel.pack()

refreshButton=Button(root,text='REFRESH',font=('poppins',18,'bold'),command=refresh)
refreshButton.pack()


root.mainloop()
