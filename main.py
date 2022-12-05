import PySimpleGUI as sg
import requests
sg.theme('DarkAmber')

#requests

API_key = "781b368c4fc219abb0baf459b4ab9eac"
lon = ""
lat = ""
cidade = "são paulo"
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_key}&lang=pt_br"

requisisao = requests.get(link)
requisisao_dic = requisisao.json()

descricao = requisisao_dic['weather'][0]['description']

temperatua = requisisao_dic['main']['temp'] - 273.15
clima_var = f"{descricao}"

#pysimple gui

layout = [
    [sg.Text(f"Clima atual do seu estado.")],
    [sg.Text(f"estado: {cidade}", key="cidade")],
    [sg.Text(f"Clima: {clima_var}.", key="clima")],
    [sg.Text(f"Temperatura: {temperatua} °C", key="temperatura")],
    [sg.Text("Nome do estado: "), sg.InputText(" ", key="input", size=(15,3)), sg.Button("Mudar a cidade.")]

]
def Mudar():
    global cidade, requisisao, requisisao_dic, descricao, temperatua, clima_var, link, API_key
    API_key = "781b368c4fc219abb0baf459b4ab9eac"
    cidade = values["input"]
    link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_key}&lang=pt_br"

    requisisao = requests.get(link)
    requisisao_dic = requisisao.json()

    descricao = requisisao_dic['weather'][0]['description']

    temperatua = requisisao_dic['main']['temp'] - 273.15
    clima_var = f"{descricao}"


janela = sg.Window("Clima", layout)

while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

    if event == "Mudar a cidade.":
        Mudar()
        janela["cidade"].update(value=f"estado: {cidade}")
        janela["clima"].update(value=f"Clima: {clima_var}.")
        janela["temperatura"].update(value=f"Temperatura: {temperatua} °C")

janela.close()