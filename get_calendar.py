import requests;
import log

def download(url, path):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        with open(path, 'wb') as calendar_file:
             calendar_file.write(response.content)


    except requests.exceptions.ConnectionError as error:
        log.e(f'Erro {error} No Request')

    except requests.exceptions.HTTPError as error:
        log.e(f'Erro {error} Na URL')

    except FileNotFoundError:
        log.e('Não Foi Possivel Encontrar o Path')

    except PermissionError:
        log.e('Permissão de Gravação Negada')

    else:
        log.s('Arquivo Baixado Com Sucesso')
        return True

        

