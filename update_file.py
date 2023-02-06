#criado por Lucas gabriel
# github : https://github.com/Lucas836-hub/
# instagram : @lucas_git

import os
from datetime import datetime
import urllib
import urllib.request
from bs4 import BeautifulSoup

# check_atualizacao = ver se o github foi atualizado
# passagem do tempo = fazer o calculo de quantos dias se passaram
# atualizar = atualiza a pasta local


# url = repositorio github para ser monitorado ex: https://github.com/Lucas836-hub/repository_up/
def check_atualizacao(url):
    hj=list(url)
    if hj[-1] != "/":
        site = urllib.request.urlopen(url+"/commits/main")
    else:
        site = urllib.request.urlopen(url + "commits/main")
    # Captura a data do ultimo upadate
    soup = BeautifulSoup(site, 'html5lib')
    data_up=soup.find_all('relative-time')

    #filtrar a data do ultimo update
    fgk=list(str(data_up))
    data_ultimo_up=""
    for v in fgk[42:52] : data_ultimo_up+=v

    # listando os diretorios
    pasta =os.getcwd()
    pasta+="/"
    fdpaths=[]
    for fd in os.listdir(pasta): fdpaths.append(fd)
    create_date=[]
    # capturando as datas
    for fdpath in fdpaths:
        statinfo = os.stat(fdpath)
        a=datetime.fromtimestamp(statinfo.st_mtime)
        create_date.append(list(str(a)))

    #organizando as datas
    temp_data_arquivo=""
    all_temp=[]
    for bnm in range(0,len(create_date)):
        temp_data_arquivo = ""
        for uio in create_date[bnm][0:11]:
            temp_data_arquivo+=uio
            all_temp.append(temp_data_arquivo)
    vai_atualiar=False
    for rfv in all_temp:
        if passagem_tempo(temp_data_arquivo, data_ultimo_up):
            vai_atualiar=True

    return vai_atualiar

def passagem_tempo(a, b, c=0):
    # a = data do arquivo
    # b = data da ultima atualizacao do github
    # c = passagem do tempo para a atualizacao por padrao 0 dias
    data = list(str(a))
    data_atual = list(str(b))

    num = [int(data[0] + data[1] + data[2] + data[3]), int(data[5] + data[6] ),int(data[8] + data[9])]
    num2 = [int(data_atual[0] + data_atual[1] + data_atual[2] + data_atual[3]), int(data_atual[5] + data_atual[6] ),int(data_atual[8] + data_atual[9])]
    resp = [num[2] - num2[2], num[1] - num2[1], num[0] - num2[0]]
    if (resp[0] <= c and resp[1] <= 0 or resp[2] < 0 or resp[1] <= 0):
        return True
    else:
        return False

# n_del = lista de arquivos que nao poderam ser excluidos ex: banco de dados , arquivos txt com dados
# url = repositorio github para ser feito o download ex: https://github.com/Lucas836-hub/repository_up/
def atualizar(url,n_del=[]):
    hj = list(url)
    if hj[-1] != "/":
        site = urllib.request.urlopen(url + "/commits/main")
    else:
        site = urllib.request.urlopen(url + "commits/main")
    # Captura a data do ultimo upadate
    soup = BeautifulSoup(site, 'html5lib')
    data_up = str(soup.find_all('a'))

    parametros_a=data_up.replace(">"," ").split("<a")
    nome_do_arquivo_atualizado=[]
    temp_nome_do_arquivo_atualizado=""
    for zaq in parametros_a:
        # procura update ou create para capturar o nome do arquivo que foi atualizado
        if 'Update' in zaq or 'Create' in zaq or "Add files via upload" in zaq:
            try:
                ujm = int(zaq.index("Update"))
            except:
                try:
                    ujm = int(zaq.index("Create"))
                except:
                    ujm = int(zaq.index("Add files via upload"))
            # filtrar o nome do arquivo
            for mnb in zaq[ujm+6:]:
                if mnb == "<":
                    nome_do_arquivo_atualizado.append(temp_nome_do_arquivo_atualizado)
                    temp_nome_do_arquivo_atualizado = ""
                    break
                if mnb != " ":
                    temp_nome_do_arquivo_atualizado += mnb
                    #print(f"texto {mnb}   {temp_nome_do_arquivo_atualizado}")


    # data dos updates
    data_up = soup.find_all('relative-time')

    # filtrar a data do ultimo update
    fgk = str(data_up).split("<relative-time")
    data_ultimo_up = []
    temp_data_ultimo_up=""
    for rfv in range(1,len(fgk)-1):
        for v in fgk[rfv][27:37]:
            temp_data_ultimo_up += v

        if temp_data_ultimo_up != "" or temp_data_ultimo_up != " ":
            data_ultimo_up.append(temp_data_ultimo_up)
        temp_data_ultimo_up = ""

    git_final=[] # nome do arquivo + data do up
    for g in range(0,len(nome_do_arquivo_atualizado)):
        try:
            git_final.append([nome_do_arquivo_atualizado[g],data_ultimo_up[g]])
        except:
            pass


    # pegar o n_del copiar para uma pasta / apagar diretorio / instalar o novo / inserir o n_del /substituir semelhantes
    pasta = list(str(os.getcwd()))
    past=[]
    var_tem=""
    for gh in pasta:
        if gh != "/" :
            var_tem+=gh
        else:
            if var_tem != "":
                past.append("/"+var_tem)
                var_tem=""
    # ver quais precisam atualizar
    path = str(os.getcwd())
    arquivos_datas_local=[] # recebe o nome dos arquivos e a data do local
    fdpaths = [path + "/" + fd for fd in os.listdir(path)]
    for fdpath in fdpaths:
        statinfo = os.stat(fdpath)
        create_date = datetime.fromtimestamp(statinfo.st_ctime)
        mju=[]
        mju=fdpath.split("/")# pega o nome do arquivo
        nhy=str(create_date).split()[0:9]# pega a data
        arquivos_datas_local.append([mju[-1],nhy[0]])

    desatualizados=[]
    atualizadso=[]
    for mnbv in arquivos_datas_local:
        # VER SE A DATA DOS ARQUIVOS COINCIDEM
        for zxcv in git_final:
            if mnbv[0] == zxcv[0]:
                if passagem_tempo(zxcv[1],mnbv[1]) :
                    desatualizados.append(zxcv[0])
                    print("\033[92mATUALIZACAO DETECTADA\033[m")
                else:
                    atualizadso.append(zxcv[0])
                    print("\033[91mATUALIZACAO  NAO  DETECTADA\033[m")
                break
    if desatualizados != []:
        for trew in desatualizados:
            if trew in n_del:
                pass
            else:
                os.system(f"rm -f {trew}")
                try :
                    os.system(f"wget {url+'/blob/main/'+trew}")
                except:
                    os.system(f"wget {url + '/tree/main/' + trew}")
