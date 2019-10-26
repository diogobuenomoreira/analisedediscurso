# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import xml.etree.ElementTree as ET
import requests
import codecs

arquivo = "psol2019" + ".data"

with codecs.open(arquivo, 'w', 'utf-8') as arq:
    PSOL = [204509, 205548, 134812, 204407, 152605, 73531, 74784, 76874, 204535, 204464]
    NOVO = [204532, 204519, 204461, 156190, 204523, 204365, 204528, 204516]
    #deputados = [204534, 204464, 160672, 92346, 160976]
    vetor20152019 = [["2015-01-01", "2015-06-30"],
                ["2015-07-01", "2015-12-31"],
                ["2016-01-01", "2016-06-30"],
                ["2016-07-01", "2016-12-31"],
                ["2017-01-01", "2017-06-30"],
                ["2017-07-01", "2017-12-31"],
                ["2018-01-01", "2018-06-30"],
                ["2018-07-01", "2018-12-31"],
                ["2019-01-01", "2019-06-30"],
                ["2019-07-01", "2019-12-31"]]

    vetor2019 = [["2019-01-01", "2019-01-31"],
                ["2019-02-01", "2019-02-28"],
                ["2019-03-01", "2019-03-31"],
                ["2019-04-01", "2019-04-30"],
                ["2017-05-01", "2017-05-31"],
                ["2017-06-01", "2017-06-30"],
                ["2018-07-01", "2018-07-31"],
                ["2018-08-01", "2018-08-31"],
                ["2019-09-01", "2019-09-30"],
                ["2019-10-01", "2019-10-31"]]

    deputados = PSOL
    periodos = vetor2019
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
                perfil.append(id.text)
            for nomeEleitoral in child.findall("nomeEleitoral"):
                perfil.append(nomeEleitoral.text)
            for sexo in child.findall("sexo"):
                perfil.append(sexo.text)
            for escolaridade in child.findall("escolaridade"):
                perfil.append(escolaridade.text)
            for siglaUf in child.findall("siglaUf"):
                perfil.append(siglaUf.text)
            for siglaPartido in child.findall("siglaPartido"):
                perfil.append(siglaPartido.text)

        for periodo in periodos:
            url = "https://dadosabertos.camara.leg.br/api/v2/deputados/"+str(deputado)+"/discursos?dataInicio="+str(periodo[0])+"&dataFim="+str(periodo[1])+"&ordenarPor=dataHoraInicio&ordem=ASC"
            header = { 'Accept': 'application/xml' }
            r = requests.get(url, headers=header)

            tree =  ET.ElementTree(ET.fromstring(r.content))

            root = tree.getroot()

            filtro = "*"
            discurso = []
            tipodiscurso = []
            for child in root.iter(filtro):
                for tipo in child.findall("tipoDiscurso"):
                    tipodiscurso.append(tipo.text)
                for transcricao in child.findall("transcricao"):
                    discurso.append(transcricao.text)
            for d in range(len(discurso)):
                arq.write(str(perfil[0])+";"+str(perfil[1])+";"+str(perfil[2])+";"+str(perfil[3])+";"+str(perfil[4])+";"+str(perfil[5])+";"+str(tipodiscurso[d])+";"+str(discurso[d])+"*\n")
print "RESULTADOS GRAVADOS EM " + arquivo
