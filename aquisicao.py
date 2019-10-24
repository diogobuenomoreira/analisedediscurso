# -*- coding: UTF-8 -*-

import xml.etree.ElementTree as ET
import requests

deputados = [204534, 204464, 160672, 92346, 160976]

for deputado in deputados:
    url = "https://dadosabertos.camara.leg.br/api/v2/deputados/" + str(deputado)
    header = { 'Accept': 'application/xml' }
    r = requests.get(url, headers=header)
    tree =  ET.ElementTree(ET.fromstring(r.content))
    root = tree.getroot()
    filtro = "*"

    perfil = []
    for child in root.iter(filtro):
        for id in child.findall("id"):
            #print(id.tag, id.text)
            perfil.append(id.text)
        for nomeEleitoral in child.findall("nomeEleitoral"):
            #print(nomeEleitoral.tag, nomeEleitoral.text)
            perfil.append(nomeEleitoral.text)
        for sexo in child.findall("sexo"):
            #print(sexo.tag, sexo.text)
            perfil.append(sexo.text)
        for escolaridade in child.findall("escolaridade"):
            #print(escolaridade.tag, escolaridade.text)
            perfil.append(escolaridade.text)
        for siglaUf in child.findall("siglaUf"):
            #print(siglaUf.tag, siglaUf.text)
            perfil.append(siglaUf.text)
        for siglaPartido in child.findall("siglaPartido"):
            #print(siglaPartido.tag, siglaPartido.text)
            perfil.append(siglaPartido.text)

    print perfil
    continue
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
