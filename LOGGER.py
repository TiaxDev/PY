import mechanize
from bs4 import *
import re
from easygui import passwordbox
br=mechanize.Browser()
br.set_handle_robots(False)
def menu():
    print("============================================================")
    print("BENVENUTO NEL PROGRAMMA DI GESTIONE DEL REGISTRO ELETTRONICO\n(ITIS G.GALILEI-CREMA):")
    print("============================================================\n")
    scelta=raw_input("Che sezione vuoi visionare? (Voti, Assenze, Argomenti[BETA], Agenda): ")
    if scelta=="voti" or scelta=="Voti" or scelta=="VOTI":
        login()
        getvoti()
        menu2()
    elif scelta=="assenze" or scelta=="Assenze" or scelta=="ASSENZA":
        login()
        getass()
        menu2()
    elif scelta=="argomenti" or scelta=="Argomenti" or scelta=="ARGOMENTI":
        login()
        getargo()
        menu2()
    elif scelta=="agenda" or scelta=="Agenda" or scelta=="AGENDA":
        login()
        getagenda()
        menu2()
    else:
        print("Errore. La categoria '%s' non esiste!\n" %(scelta))
        return menu()
def login():
        nome=raw_input("INSERISCI IL NOME UTENTE: ")
        passw=passwordbox("INSERISCI LA PASSWORD: ",title="PASSWORD")
        r=br.open("https://galilei-cr-sito.registroelettronico.com/votes")
        br.select_form(nr=0)
        br.form["username"]=nome
        br.form["password"]=passw
        r=br.submit()
        insuccess=re.search("Nome utente e/o password errati.",r.read())
        if insuccess is None:
            br.open("https://galilei-cr-sito.registroelettronico.com/votes")
            scrivo=open("MainHTML.html","w")
            scrivo.write(br.response().read())
            scrivo.close()
            scrivo=open("MainHTML.html","r")
            html_doc=(scrivo)
            soup=BeautifulSoup(html_doc)
            for node in soup.findAll('h2',{'id':'student_name'}):
                nome_studente=''.join(node.findAll(text=True))
                print("\nBenvenuto, %s!\n") %(nome_studente)
        else:
            print("\nErrore. Nome utente e/o password errati.\n")
            return login()
def menu2():
    while True:
        scelta=raw_input("Che sezione vuoi visionare? (Voti, Assenze, Argomenti[BETA], Agenda): ")
        if scelta=="voti" or scelta=="Voti" or scelta=="VOTI":
            getvoti()
        elif scelta=="assenze" or scelta=="Assenze" or scelta=="ASSENZA":
            getass()
        elif scelta=="argomenti" or scelta=="Argomenti" or scelta=="ARGOMENTI":
            getargo()
        elif scelta=="agenda" or scelta=="Agenda" or scelta=="AGENDA":
            getagenda()
        else:
            print("Errore. La categoria '%s' non esiste!\n" %(scelta))
            return menu2()
def getvoti():
    br.open("https://galilei-cr-sito.registroelettronico.com/votes")
    scrivo=open("VotiHTML.html","w")
    scrivo.write(br.response().read())
    scrivo.close()
    scrivo=open("VotiHTML.html","r")
    html_doc=(scrivo)
    soup=BeautifulSoup(html_doc)
    print("\nLISTA VOTI AGGIORNATA:")
    print("(Ordine per data)\n\n")
    print("===================================================")
    for node in soup.findAll('p',{'class':'day_description'}):
        print ''.join(node.findAll(text=True))
    print("====================================================")
    scrivo.close()
def getass():
    br.open("https://galilei-cr-sito.registroelettronico.com/absences")
    scrivo=open("AssenzeHTML.html","w")
    scrivo.write(br.response().read())
    scrivo.close()
    scrivo=open("AssenzeHTML.html","r")
    html_doc=(scrivo)
    soup=BeautifulSoup(html_doc)
    print("\nLISTA ASSENZE AGGIORNATA:")
    print("(Ordine per data)\n\n")
    print("====================================================")
    for node in soup.findAll('p',{'class':'day_description'}):
        print ''.join(node.findAll(text=True))
    print("====================================================")
    scrivo.close()
def getargo():
    br.open("https://galilei-cr-sito.registroelettronico.com/topics")
    scrivo=open("ArgomentiHTML.html","w")
    scrivo.write(br.response().read())
    scrivo.close()
    scrivo=open("ArgomentiHTML.html","r")
    html_doc=(scrivo)
    soup=BeautifulSoup(html_doc)
    print("\nLISTA ARGOMENTI AGGIORNATA:")
    print("(Ordine per data)\n\n")
    print("====================================================")
    for node in soup.findAll('p',{'class':'day_description'}):
        print ''.join(node.findAll(text=True))
    print("====================================================")
    scrivo.close()
def getagenda():
    br.open("https://galilei-cr-sito.registroelettronico.com/agenda")
    scrivo=open("AgendaHTML.html","w")
    scrivo.write(br.response().read())
    scrivo.close()
    scrivo=open("AgendaHTML.html","r")
    html_doc=(scrivo)
    soup=BeautifulSoup(html_doc)
    print("\nAGENDA AGGIORNATA:")
    print("(Ordine per data)\n\n")
    print("====================================================")
    for node in soup.findAll('p',{'class':'day_description'}):
        print ''.join(node.findAll(text=True))
    print("====================================================")
    scrivo.close()
menu()
