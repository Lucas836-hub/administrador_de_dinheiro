#criado por Lucas gabriel
# github : https://github.com/Lucas836-hub/
# instagram : @lucas_git

# se auto atualizar ok
# ver a defazagem de tempo do github = pegar localizaco , ver o deley do pais
# barra de progresso e tamanho do arquivo
# VERIFICAR PASTAS NO GITHUB    

import os
from datetime import datetime
import urllib
import urllib.request
from bs4 import BeautifulSoup


# url = repositorio github para ser monitorado ex: https://github.com/Lucas836-hub/repository_up/
def check_atualizacao(url):
    pasta_up("C")
    hj=list(url)
    if hj[-1] != "/":
        site = urllib.request.urlopen(url+"/commits/main")
    else:
        site = urllib.request.urlopen(url + "commits/main")
    # Captura a data do ultimo upadate
    soup = BeautifulSoup(site, 'html5lib')
    data_up=soup.find_all('relative-time')

    #filtrar a data do ultimo update do github
    fgk=list(str(data_up))
    #print(data_up)
    #print(fgk)
    data_ultimo_up=""
    for v in fgk[42:52] : data_ultimo_up+=v

    # filtrar a hora do ultimo update do github
    hora_ultima_atualizacao_git=[]
    hora_str=""
    for azdev in fgk[53:61]:
        hora_str += azdev
    hora_ultima_atualizacao_git=hora_str.split(":")

    #print(hora_ultima_atualizacao_git)
    #print(data_ultimo_up)
    data_ultimo_up=data_ultimo_up.split(":")
    # ultimo up local
    vai_atualizar = False
    #print(f"pasta V {pasta_up('V')}")
    dados_pasta = pasta_up("V")

    #print(f"\033[96mpasta : {dados_pasta}  |  github : hora {hora_ultima_atualizacao_git} data {data_ultimo_up}\033[m")

    if dados_pasta == [] :
        vai_atualizar = True
        #print("PASTA VAZIA")

    else:
        if  passagem_tempo(dados_pasta[0], data_ultimo_up) and passagem_hora(hora_ultima_atualizacao_git,dados_pasta[1]):
            #print(f"\033[34mdados encontrados {passagem_tempo(dados_pasta[0], data_ultimo_up) and passagem_hora(hora_ultima_atualizacao_git,dados_pasta[1])}\033[m")
            vai_atualizar = True
        #else:
            #print(f"\033[31mnao deu {passagem_tempo(dados_pasta[0], data_ultimo_up) and passagem_hora(hora_ultima_atualizacao_git, dados_pasta[1])}\033[m")

    #pasta_up("UP")
    return vai_atualizar

def passagem_hora(h1,h2):
    # h1 = hora do ultimo up do github
    # h2 = hora do ultimo up dos arquivos locais
    #print("github ",h1)
    #print("arquivo ",h2)
    if int(int(h1[0])-int(h2[0])) > 0 or int(int(h1[1])- int(h2[1])) > 0 and int(int(h1[0])-int(h2[0])) >= 0 or int(int(h1[1])- int(h2[1])) >= 0 and int(int(h1[0])-int(h2[0])) >= 0 and int(int(h1[2])-int(h2[2])) > 0 :
        #print(f"passagem hora  {int(h1[0])-int(h2[0])} {int(int(h1[1])-int(h2[1]))} {int(int(h1[2])-int(h2[2]))} True")
        return True
    else:
        #print(f"passagem hora  {int(h1[0]) - int(h2[0])} {int(int(h1[1]) - int(h2[1]))} {int(int(h1[2]) - int(h2[2]))} False")
        return False

def pasta_up(comand):
    # criar = C  / atualiza = UP / valores = V <- retorna uma matriz 2x3 com data e hora OBS DATA EM STRING NORMAL
    dh = datetime.now()
    data_hora = dh.strftime("%Y-%m-%d %H:%M:%S")

    if comand == "C":
        if not os.path.exists(".ultima_atualizacao.txt"):
            arquivo = open(".ultima_atualizacao.txt", "a")
            arquivo.write(data_hora)
            arquivo.close()
            #print(f"C {data_hora}")

    if comand == "UP":
        arquivo = open(".ultima_atualizacao.txt", "w")
        arquivo.write(data_hora)
        arquivo.close()
        #print(f"UP {data_hora}")

    if comand == "V":
        arquivo = open(".ultima_atualizacao.txt", "r")
        ler=arquivo.read()
        gh=str(ler).split(" ")
        bjk=[gh[0],gh[1].split(":")]
        #print(f"\033[92mV {data_hora} bjk {bjk} gh {gh} arquivo {arquivo} ler {ler}\033[m")
        return bjk


def passagem_tempo(a, b, c=0):
    # a = data do arquivo
    # b = data da ultima atualizacao do github
    # c = passagem do tempo para a atualizacao por padrao 0 dias
    data = list(str(a).replace("[","").replace("]","").replace("'",""))
    data_atual = list(str(b).replace("[","").replace("]","").replace("'",""))

    #print(f"\033[31mdata 1 {data}  data 2 {data_atual}")

    num = [int(data[0] + data[1] + data[2] + data[3]), int(data[5] + data[6] ),int(data[8] + data[9])]
    num2 = [int(data_atual[0] + data_atual[1] + data_atual[2] + data_atual[3]), int(data_atual[5] + data_atual[6] ),int(data_atual[8] + data_atual[9])]
    resp = [num[2] - num2[2], num[1] - num2[1], num[0] - num2[0]]
    if (resp[0] < c and resp[1] <= 0 or resp[2] < 0 or resp[1] < 0 and resp[2] <= 0):
        print(f"passagem tempo arquivo {a} github {b} = {resp[0]} {resp[1]} {resp[2]}")
        return True
    else:
        print(f"passagem tempo arquivo {a} github {b} = {resp[0]} {resp[1]} {resp[2]} False")
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
        entrat=True
        try:
            for ent in range(0,len(git_final)):
                #print(f"g  = {nome_do_arquivo_atualizado[g]}   git = {git_final[ent][0]}  ")
                if nome_do_arquivo_atualizado[g] in git_final[ent][0]:
                    entrat=False
            if entrat:
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

    #print(f"\033[93m github {git_final}\033[m")
    # print(f"\033[94m arquivo {arquivos_datas_local}\033[m")

    for mnbv in arquivos_datas_local:
        # VER SE A DATA DOS ARQUIVOS COINCIDEM
        for zxcv in git_final:
            #print(f"\033[95mnbv {mnbv[0]} zxcv {zxcv[0]}\033[m")

            if mnbv[0] == zxcv[0]  :
                if passagem_tempo(mnbv[1],zxcv[1]) :
                    desatualizados.append(zxcv[0])
                    #print("\033[92mATUALIZACAO DETECTADA\033[m")

                else:
                    atualizadso.append(zxcv[0])
                    #print("\033[91mATUALIZACAO  NAO  DETECTADA\033[m")
                break

    for efj in range(0,len(git_final)):
        entrou=True
        for mnbvfg in range(0,len(arquivos_datas_local)):
            if git_final[efj][0]  in arquivos_datas_local[mnbvfg][0]:
                entrou=False
        if entrou and git_final[efj][0] != "lesviaupload":
            desatualizados.append(git_final[efj][0])

    if desatualizados != []:

        oav=""
        afl = url.split("/")
        for xoe in afl[3:]:oav+="/"+xoe

        for trew in desatualizados:
            #print(f"\033[93mdesatualizados {desatualizados}\033[m")
            #print(f"\033[94matualizados {atualizadso}\033[m")
            if trew in n_del:
                pass
            else:
                if os.path.exists(trew) :
                    os.system(f"rm -r {trew}")
                if os.path.isdir(trew):
                    os.rmdir(trew)
                try :
                    urllib.request.urlopen(f"https://raw.githubusercontent.com{oav + '/main/' + trew}")
                    site = f"https://raw.githubusercontent.com{oav + '/main/' + trew}"
                except:
                    urllib.request.urlopen(f"https://raw.githubusercontent.com{oav + '/master/' + trew}")
                    site = f"https://raw.githubusercontent.com{oav + '/master/' + trew}"


                os.system(f"wget {site}")
        pasta_up("UP")

try:
    atualizar("https://github.com/Lucas836-hub/repository_up",["README.md","requirements.txt"])
except:
    pass