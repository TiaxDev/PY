#!/usr/bin/env python

#Mattia Tanzini, 2013

import mechanize
from bs4 import *
import getpass
import re
import sys

br = mechanize.Browser()
br.set_handle_robots(False)

def menu(isLoggedIn):

    if(isLoggedIn == False):
        login();
    isLoggedIn = True
    
    scelta = raw_input("Che sezione vuoi visionare? (1)Voti, (2)Assenze, (3)Argomenti[BETA], (4)Agenda, (5)Uscita: ")

    if scelta == "1":
        get("https://galilei-cr-sito.registroelettronico.com/votes/", "votes")
        return menu(isLoggedIn)
    elif scelta == "2":
        get("https://galilei-cr-sito.registroelettronico.com/absences/", "absences")
        return menu(isLoggedIn)
    elif scelta == "3":
        get("https://galilei-cr-sito.registroelettronico.com/topics/", "topics")
        return menu(isLoggedIn)
    elif scelta == "4":
        get("https://galilei-cr-sito.registroelettronico.com/agenda/", "agenda")
        return menu(isLoggedIn)
    elif scelta == "5":
        print("Exit...")
        sys.exit(0)
    else:
        print("Errore. La categoria '%s' non esiste!\n" %(scelta))
        return menu(isLoggedIn)
    
def login():
        nome = raw_input("INSERISCI IL NOME UTENTE: ")
        passw = raw_input("INSERISCI PASSWORD (watch your back!): ");
        print "Connessione..."
        r = br.open("https://galilei-cr-sito.registroelettronico.com/votes")
        print "Autenticazione..."
        br.select_form(nr=0)
        br.form["username"] = nome
        br.form["password"] = passw
        r = br.submit()
        insuccess = re.search("Nome utente e/o password errati.", r.read())
        if insuccess is None:
            br.open("https://galilei-cr-sito.registroelettronico.com/votes")
            scrivo = open("mainTemp.html", "w")
            scrivo.write(br.response().read())
            scrivo.close()
            scrivo = open("mainTemp.html", "r")
            html_doc = (scrivo)
            soup = BeautifulSoup(html_doc)
            for node in soup.findAll('h2',{'id':'student_name'}):
                nome_studente = ''.join(node.findAll(text=True))
                print("\nBenvenuto, %s!\n") %(nome_studente)
        else:
            print("\nErrore. Nome utente e/o password errati.\n")
            return login()
        
def get(URL, fileName):
    br.open(URL)
    scrivo = open("temp" + fileName + ".html", "w")
    scrivo.write(br.response().read())
    scrivo.close()
    scrivo = open("temp" + fileName + ".html", "r")
    html_doc = (scrivo)
    soup = BeautifulSoup(html_doc)
    print "\n(Lista aggiornata)\n"
    print("===================================================")
    for node in soup.findAll('p',{'class':'day_description'}):
        print ''.join(node.findAll(text=True))
    print("====================================================\n")
    scrivo.close()

#Main

print("===============================================")
print("PROGRAMMA DI GESTIONE DEL REGISTRO ELETTRONICO\n(ITIS G.GALILEI-CREMA):")
print("Author: Mattia Tanzini \nInfo: @TiaxDev (https://github.com/TiaxDev)")
print("===============================================\n") 
menu(False)
