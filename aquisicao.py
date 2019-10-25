# -*- coding: UTF-8 -*-

import xml.etree.ElementTree as ET
import requests

arq = open('dados.txt', 'w')

deputados = [204534, 204464, 160672, 92346, 160976]
periodos = [["2015-01-01", "2015-06-30"],
            ["2015-07-01", "2015-12-31"],
            ["2016-01-01", "2016-06-30"],
            ["2016-07-01", "2016-12-31"],
            ["2017-01-01", "2017-06-30"],
            ["2017-07-01", "2017-12-31"],
            ["2018-01-01", "2018-06-30"],
            ["2018-07-01", "2018-12-31"],
            ["2019-01-01", "2019-06-30"],
            ["2019-07-01", "2019-12-31"],]

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

    #print perfil
    for periodo in periodos:
        url = "https://dadosabertos.camara.leg.br/api/v2/deputados/"+str(deputado)+"/discursos?dataInicio="+str(periodo[0])+"&dataFim="+str(periodo[1])+"&ordenarPor=dataHoraInicio&ordem=ASC"
        header = { 'Accept': 'application/xml' }
        r = requests.get(url, headers=header)

        tree =  ET.ElementTree(ET.fromstring(r.content))

        #arquivo = "discursos?dataInicio=2015-01-01.xml"
        #tree =  ET.parse(arquivo)

        root = tree.getroot()

        filtro = "*"
        discurso = []
        for child in root.iter(filtro):
            #print(child.tag, child.text)
            for tipoDiscurso in child.findall("tipoDiscurso"):
                #print(tipoDiscurso.text)
                discurso.append(tipoDiscurso.text)
            for transcricao in child.findall("transcricao"):
                discurso.append(transcricao.text)
                #print(discurso.text)
                #print("\n")
        if len(discurso) == 2:
            arq.write(perfil[0]+";"+perfil[1]+";"+perfil[2]+";"+perfil[3]+";"+perfil[4]+";"+perfil[5]+";"+discurso[0]+";"+discurso[1])
        print perfil,discurso
arq.close()
