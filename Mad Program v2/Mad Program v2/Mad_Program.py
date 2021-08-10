#!/usr/local/bin/python3
from tkinter import *;
import tkinter as tk;
import os;

x=650
y=600

xStr=str(x)
yStr=str(y)

def main():
    #Jeg laver første et vindue der hedder "Window" med titlen Madprogram
    exit = False;
    window = tk.Tk();
    window.title("Madprogram");
    window.geometry(xStr+'x'+yStr)




    #Her ler jeg en funktion til at lukke programmet, hvis man ønsker det
    def lukProgrammet():
        global exit;
        window.destroy();
        exit = True;

    #Her er knappen til funktionen "lukProgrammet" til at lukke programmet
    exitBtn = tk.Button(window, text="X", command = lukProgrammet,bg="red",width=3);
    exitBtn.grid(row=0,column=3,sticky="NE");
    

    def dessertBut():
        window.destroy();
        bagning();
    def retterBut():
        window.destroy();
        retter();
    def bagningBut():
        window.destroy();
        desserter();

   
    #Her er knappen til funktionen "lukProgrammet" til at lukke programmet
    bagBtn = tk.Button(window, text="Bagning", command = dessertBut);
    bagBtn.grid(row=1,column=0,padx=115,sticky="W",pady=120);
    #Her er knappen til funktionen "lukProgrammet" til at lukke programmet
    retBtn = tk.Button(window, text="Retter", command = retterBut);
    retBtn.grid(row=1,column=1,sticky="N", pady=120);
    #Her er knappen til funktionen "lukProgrammet" til at lukke programmet
    desBtn = tk.Button(window, text="Desserter", command = bagningBut);
    desBtn.grid(row=1,column=2,padx=115,sticky="E");



    def enter(event):
        rigtigLogin();
    def close(event):
        lukProgrammet();
    window.bind('<Return>', enter);
    window.bind('<Escape>', close);
    window.mainloop();

    

def desserter():
    window = tk.Tk();
    window.title("Dessert");

    window.geometry(xStr+'x'+yStr);

    def home():
        window.destroy();
        main();
    
    

    #Her er knappen til funktionen "lukProgrammet" til at lukke programmet
    homeBtn = tk.Button(window, text="Tilbage", command = home);
    homeBtn.pack();

    #Defining option list
    strPath=os.path.abspath(os.getcwd()+"/Retter/Desserter"+"/")
    OptionList = [ item for item in os.listdir(strPath) if os.path.isdir(os.path.join(strPath, item)) ]
    #print (OptionList)
    w=Scrollbar(window,orient="vertical");
    variable = tk.StringVar(window);
    variable.set(OptionList[0]);
    opt = tk.OptionMenu(window, variable, *OptionList);
    opt.config(width=30, font=('Helvetica', 12));
    opt.pack(side="top");
    #Labels
    ingredienserTekst = tk.Text(window, height=50,font=('Helvetica', 12));
    ingredienserTekst.pack(side="top");

    #Function
    def callback(*args):
        ingredienserTekst.configure(state="normal")
        ingredienserTekst.delete('1.0',END)        
        ingredienser=open(strPath+"/"+"{}".format(variable.get())+"/"+"ingredienser.txt",encoding="utf-8");
        fremstilling=open(strPath+"/"+"{}".format(variable.get())+"/"+"fremstilling.txt",encoding="utf-8");
        ingredienserTekst.insert(END,ingredienser.read()+"\n\nFremstilling:\n\n"+fremstilling.read());
        ingredienser.close();
        fremstilling.close();
        ingredienserTekst.configure(state="disabled")
    variable.trace("w", callback);
    scrollbar = tk.Scrollbar(window,orient='vertical',command=ingredienserTekst.yview);
    scrollbar.pack(side="right")

    ingredienserTekst['yscrollcommand'] = scrollbar.set

    
    window.mainloop();

def retter():
    window = tk.Tk();
    window.title("Retter");
    window.geometry(xStr+'x'+yStr)

    def home():
        window.destroy();
        main();


    #Her er knappen til funktionen "lukProgrammet" til at lukke programmet
    homeBtn = tk.Button(window, text="Tilbage", command = home);
    homeBtn.pack();

    #Defining option list
    strPath=os.path.abspath(os.getcwd()+"/Retter/Aftensmad"+"/")
    OptionList = [ item for item in os.listdir(strPath) if os.path.isdir(os.path.join(strPath, item)) ]

    w=Scrollbar(window,orient="vertical");
    variable = tk.StringVar(window);
    variable.set(OptionList[0]);
    opt = tk.OptionMenu(window, variable, *OptionList);
    opt.config(width=30, font=('Helvetica', 12));
    opt.pack(side="top");
    #Labels
    ingredienserTekst = tk.Text(window, font=('Helvetica', 12));
    ingredienserTekst.pack(side="top");

    #Function
    def callback(*args):
        ingredienserTekst.configure(state="normal")
        ingredienserTekst.delete('1.0',END)        
        ingredienser=open(strPath+"/"+"{}".format(variable.get())+"/"+"ingredienser.txt",encoding="utf-8");
        fremstilling=open(strPath+"/"+"{}".format(variable.get())+"/"+"fremstilling.txt",encoding="utf-8");
        ingredienserTekst.insert(END,ingredienser.read()+"\n\nFremstilling:\n\n"+fremstilling.read());
        ingredienser.close();
        fremstilling.close();
        ingredienserTekst.configure(state="disabled")
    variable.trace("w", callback);
    scrollbar = tk.Scrollbar(window,orient='vertical',command=ingredienserTekst.yview);
    scrollbar.pack(side="right")

    ingredienserTekst['yscrollcommand'] = scrollbar.set



    
    window.mainloop();
    
def bagning():
    window = tk.Tk();
    window.title("Bagning");
    window.geometry(xStr+'x'+yStr)

    def home():
        window.destroy();
        main();


    #Her er knappen til funktionen "lukProgrammet" til at lukke programmet
    homeBtn = tk.Button(window, text="Tilbage", command = home);
    homeBtn.pack();

    #Defining option list
    strPath=os.path.abspath(os.getcwd()+"/Retter/Bagning"+"/")
    OptionList = [ item for item in os.listdir(strPath) if os.path.isdir(os.path.join(strPath, item)) ]
    
    
    w=Scrollbar(window,orient="vertical");
    variable = tk.StringVar(window);
    variable.set(OptionList[0]);
    opt = tk.OptionMenu(window, variable, *OptionList);
    opt.config(width=30, font=('Helvetica', 12));
    opt.pack(side="top");
    #Labels
    ingredienserTekst = tk.Text(window, font=('Helvetica', 12));
    ingredienserTekst.pack(side="top");

    #Function
    def callback(*args):
        ingredienserTekst.configure(state="normal")
        ingredienserTekst.delete('1.0',END)        
        ingredienser=open(strPath+"/"+"{}".format(variable.get())+"/"+"ingredienser.txt",encoding="utf-8");
        fremstilling=open(strPath+"/"+"{}".format(variable.get())+"/"+"fremstilling.txt",encoding="utf-8");
        ingredienserTekst.insert(END,ingredienser.read()+"\n\nFremstilling:\n\n"+fremstilling.read());
        ingredienser.close();
        fremstilling.close();
        ingredienserTekst.configure(state="disabled")
    variable.trace("w", callback);
    scrollbar = tk.Scrollbar(window,orient='vertical',command=ingredienserTekst.yview);
    scrollbar.pack(side="right")

    ingredienserTekst['yscrollcommand'] = scrollbar.set



    
    window.mainloop();

if  __name__ =='__main__' :main();

