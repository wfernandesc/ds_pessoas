import requests
import json


def buscaFuncionarios(chapa):

    url = f"http://corporativorm.ecad.org.br:8051/rmsrestdataserver/rest/FopFuncData?filter=[\"CHAPA LIKE '{chapa}%'\"]"
 
    payload = "{\r\n    \"CODIGOTOMADORTEMP\": \"1\"\r\n}"
    headers = {
      'Authorization': 'Basic V0NVTkhBOm1lbmdv',
      'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    data = response.json()['data']

    return data


    '''
    obj = response.json()

    funcionarios = []
    i = 0

    for funcionario in obj["data"] :
        funcionario['chapa'] = obj['data'][i]['CHAPA']
        funcionario['nome'] = obj['data'][i]['NOME']
        
        funcionarios.append(funcionario)
        i += 1  

    print(f'Total de funcionários {len(funcionarios)}')

    print(f"Funcionário: {funcionarios[1]['chapa']} - {funcionarios[1]['nome']}")
    '''