from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai.chat_models import ChatOpenAI
import os

load_dotenv()


def main():
    print("Hello from langchain-course!")
    print(os.environ.get("OPENAI_AI_KEY"))

    information = """
        Linus Benedict Torvalds (Helsinki, 28 dicembre 1969) è un informatico e blogger finlandese, conosciuto soprattutto per essere stato l'autore e programmatore della prima versione del kernel Linux nonché il coordinatore del progetto di sviluppo dello stesso[1], oltre ad aver ideato nel 2005 il software Git.
Linus Torvalds nel 2002
Biografia

Nato a Helsinki da una famiglia appartenente alla minoranza finlandese di lingua svedese, ha studiato all'Università di Helsinki tra il 1988 e il 1996, conseguendo la laurea in informatica con una tesi intitolata Linux: A Portable Operating System.[2]
Sviluppo del kernel Linux

Linus Torvalds è stato l'iniziatore dello sviluppo del kernel Linux, di cui è pure ispiratore del nome. Il sistema operativo completo GNU/Linux, ottenuto unendo il kernel Linux con il sistema operativo GNU, creato da Richard Matthew Stallman a fine anni 1980, è entrato nella storia dell'informatica come valida alternativa ai sistemi operativi non liberi (come ad esempio Microsoft Windows, MacOS, Unix); a differenza di questi ultimi sistemi, infatti, il kernel Linux è software libero coperto dalla licenza GNU GPLv2.[3]

La popolarità di Torvalds ebbe inizio a seguito di una disputa di carattere tecnico in un newsgroup Usenet con il professor Andrew Tanenbaum, della Vrije Universiteit di Amsterdam. Il professor Andrew Tanenbaum aveva infatti realizzato per scopi didattici MINIX, un sistema operativo simile a Unix, che poteva essere eseguito su di un comune personal computer. Tale sistema operativo veniva distribuito con il codice sorgente, ma la sua licenza di distribuzione vietava di apportare modifiche al codice senza l'autorizzazione dell'autore.

Altre divergenze tra Andrew Tanenbaum e Torvalds portarono quest'ultimo a riflettere sulla possibilità di creare una sorta di Unix per PC, ispirato a Minix, ma con una licenza d'uso che consentisse a chiunque la libera modifica del codice. Fu questa scelta a dare il via al progetto che, data la licenza di software libero adottata, nel giro di pochi anni ha coalizzato centinaia di programmatori che, per lavoro o per hobby, sono impegnati ad aggiornare il codice del kernel Linux.
    """

    summary_template = """
    given the information {information} about a person I want to create: 
    1. A short summary
    2. Two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model="gpt-5")
    chain = summary_prompt_template | llm

    response = chain.invoke(input={"information": information})
    print(response)

if __name__ == "__main__":
    main()
