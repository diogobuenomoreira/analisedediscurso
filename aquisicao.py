import xml.etree.ElementTree as ET
import requests

url = "https://dadosabertos.camara.leg.br/api/v2/deputados/92346/"
header = { 'Accept': 'application/xml' }
r = requests.get(url, headers=header)

tree =  ET.ElementTree(ET.fromstring(r.content))
root = tree.getroot()
filtro = "*"
for child in root.iter(filtro):
    for id in child.findall("id"):
        print(id.tag, id.text)
    for nomeEleitoral in child.findall("nomeEleitoral"):
        print(nomeEleitoral.tag, nomeEleitoral.text)
    for sexo in child.findall("sexo"):
        print(sexo.tag, sexo.text)
    for escolaridade in child.findall("escolaridade"):
        print(escolaridade.tag, escolaridade.text)
    for siglaUf in child.findall("siglaUf"):
        print(siglaUf.tag, siglaUf.text)
    for siglaPartido in child.findall("siglaPartido"):
        print(siglaPartido.tag, siglaPartido.text)


url = "https://dadosabertos.camara.leg.br/api/v2/deputados/92346/discursos?dataInicio=2015-01-01&dataFim=2015-12-31&ordenarPor=dataHoraInicio&ordem=ASC"
header = { 'Accept': 'application/xml' }
r = requests.get(url, headers=header)

tree =  ET.ElementTree(ET.fromstring(r.content))

#arquivo = "discursos?dataInicio=2015-01-01.xml"
#tree =  ET.parse(arquivo)

root = tree.getroot()

filtro = "*"
for child in root.iter(filtro):
    #print(child.tag, child.text)
    for sumario in child.findall("tipoDiscurso"):
        print(sumario.text)
    for discurso in child.findall("transcricao"):
        print(discurso.text)
        print("\n")
