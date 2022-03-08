import pyfiglet
import whois
import time
import sys

def colour(r,g,b,text,font):
    return print("\033[{};{};{}m {}".format(r,g,b,pyfiglet.figlet_format(text,font="{}".format(font))))
    
def exit(reason):
    sys.exit(reason)

def whois_lookup():
    colour(1,33,40,"Target(domain/ip) : ","small")
    target=input("\t\t")
    print(f"\n\n{whois.whois(target).text}")

def menu():
    
    colour(1,31,40,"1. Whois lookup\n0. Exit\n\noption:","digital")
    
    try:
        opt = int(input("\t\t"))
    except ValueError:
        exit("Kindly enter a valid option...")
    except:
        exit("Unknown error occured. kindly report in https://github.com/linux-bee")

    if opt == 1:
        whois_lookup()
        
    if opt == 0:
        exit("User termination successfull")


def welcome():
    colour(1,36,40,"W H O I S","letters")
    menu()

welcome()

    

