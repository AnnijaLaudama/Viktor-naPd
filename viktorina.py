from multiprocessing import Value
from typing import ValuesView
import PySimpleGUI as el

layout=[
    [el.T("atbildi uz viktorīnas jautājumiem")],
    [el.T("1. Kāds ir lielākais okeāns uz Zemes?")],
    [el.Radio("klusais okeāns","Radio1", default=False, key="-par1-"), el.Radio("Atlantijas okeāns", "radio2", default=False, key="-nepareizi-")],
    [el.T("2. cik krāsas varvīksnē")],
    [el.T("a)"), el.Checkbox('5', default=False, key="-nepareizi2-"), el.T("  b)"), el.Checkbox('8', default=False, key="-nepareizi3-"),el.T("  c)"), el.Checkbox('6', default=False, key="-6-")],
    [el.T("3. cik cilvēka rokai ir pirksti?")],
    [el.Radio("5","Radio1", default=False, key="-5-"), el.Radio("6", "radio2", default=False, key="-nepareizi4-")],
    [el.T("4. Kāds ir spāres mūžs?")],
    [el.T("a)   "), el.Checkbox('24 stundas', default=False, key="-24h-"),el.T("b)   "), el.Checkbox('3 gadi', default=False, key="-nepareizi5-"),el.T("c)   "), el.Checkbox('5 mēneši', default=False, key="-nepareizi6-")],
    [el.T("5. Kāds ir sudraba ķīmiskais simbols?")],
    [el.T("a)   "), el.Checkbox('Cu', default=False, key="-nepareizi7-"),el.T("b)   "), el.Checkbox('Ag', default=False, key="-p-"),el.T("c)   "), el.Checkbox('H', default=False, key="-nepareizi8-")],
    [el.T("6. kuru no šīm dziesmām ir sarakstījis Ludoviko Einaudi?")],
    [el.T("a)   "), el.Checkbox('Mamma mia', default=False, key="-nepareizi9-"),el.T("b)   "), el.Checkbox('Primawera', default=False, key="-klus-"),el.T("c)   "), el.Checkbox('Melanholiskais valsis', default=False, key="-nepareizi10-")],
    [el.T("7. paties vai aplams: Maikls bija astotais no desmit bērniem?")],
    [el.Radio("Pareizi","Radio1", default=False, key="-par-"), el.Radio("Nepeareizi", "radio2", default=False, key="-nepareizi11-")],
    [el.T("8. paties vai aplams: Maikls ieguva 1984. gada Grammy balvu kā gada ieraksts par dziesmu 'Beat It'?")],
    [el.Radio("Pareizi","Radio1", default=False, key="-par2-"), el.Radio("Nepeareizi", "radio2", default=False, key="-nepareizi12-")],
    [el.Button('iziet')],
    [el.Button('pabeigt')],
    [el.Text('', key='-vieta-')],
    [el.Text('', key='-vieta2-')]  
]

logs=el.Window("boom", layout, size=(700,850))
while True:
    event, Values = logs.read()

    if event == el.WINDOW_CLOSED or event == 'iziet':
        break
    elif event =='pabeigt':
        klusais=Value['-par1-']
        Atlantijas=Value['-nepareizi-']
        pieci=Value['-nepareizi2-']
        astoni=Value['-nepareizi3-']
        sesi=Value['-6-']

        izvele=[]
        if klusais:
            izvele.append('Klusais okeāns ir pareizā atbilde')
        if Atlantijas:
            izvele.append('Atlantijas okeāns ir nepareizā atbilde')

        izvele2=[]
        if pieci:
            izvele2.append('5 ir nepareizā atbilde')
        if astoni:
            izvele2.append('8 ir nepareizā atbilde')
        if sesi:
            izvele2.append('6 ir pareizā atbilde')

    logs['-vieta-'].update(f'jūs izvēlējāties: {", ".join(izvele)}.')
    logs['-vieta2-'].update(f'jūs izvēlējāties: {", ".join(izvele2)}.')