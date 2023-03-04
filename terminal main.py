#  MEU DINHEIRO 0.0.4
# modo terminal

#criado por Lucas gabriel
# github : https://github.com/Lucas836-hub/
# instagram : @lucas_git

import sqlite3
import os
from datetime import datetime
from random import *
import update_file # CHAMANDO O ATUALIZADOR
class main():
	def __init__(self):
		try:
			# VERIFICANDO ATUALIZACOES
			if update_file.check_atualizacao("https://github.com/Lucas836-hub/administrador_de_dinheiro"):
				self.titulo("ATUALIZANDO")
				# ATUALIZANDO O SCRIPT LOCAL
				update_file.atualizar("https://github.com/Lucas836-hub/administrador_de_dinheiro")
		except:
			pass

		self.banco = sqlite3.connect("data_pront.db")
		self.cursor = self.banco.cursor()
		
		try:
			self.cursor.execute("CREATE TABLE saldo(total real, reseva real,disponivel real)")
			self.cursor.execute("INSERT INTO saldo(total, reseva,disponivel) VALUES(0,0,0)")
			self.cursor.execute(f"CREATE TABLE gastos(data char, descricao char,valor real )")
			
			data_e_hora_atuais = datetime.now()
			data_atual =data_e_hora_atuais.strftime("%d/%m/%Y")
			M_A=data_e_hora_atuais.strftime("%m/%Y")
			A=data_e_hora_atuais.strftime("%Y")
			
			self.cursor.execute("CREATE TABLE receb_anual(ano char,valor real)")
			self.cursor.execute("INSERT INTO receb_anual(ano, valor) VALUES(?,0)",(A,))
			
			self.cursor.execute("CREATE TABLE receb_mes(mes char,valor real)")
			self.cursor.execute("INSERT INTO receb_mes(mes, valor) VALUES(?,0)",(M_A,))
			
			self.cursor.execute("CREATE TABLE receb_sem(dia char,mes char,valor real)")
			
			self.banco.commit()
			#self.cursor.execute("CREATE TABLE devedores(devendo int,cliente char,data char,descricao char , valor real)")
		except:
			pass
		
		self.menu()
	
	
	def stats(self):
		self.cursor.execute("SELECT * FROM saldo")	
		sd=self.cursor.fetchall()
		print(f"\033[94mValor Total R$ : {self.numb_valor(sd[0][0])}\n      Reseva R$ : {self.numb_valor(sd[0][1])}\n      Disponivel R$ : {self.numb_valor(sd[0][2])}\033[m\n")
		
		
	def menu(self):
		self.limpar()
		self.titulo("MENU PRINCIPAL")
		self.stats()
		op=["adicionar pagamento",'adicionar um gasto','historico de recebimento','sair']
		print(f'Digite 1 para {op[0].title()}')
		for c in range(1,len(op)):
			print(f"       {c+1} para {op[c].title()}")
			
		resp=self.imput(len(op))			
		
		if resp == 0 :
			self.menu_pg()
		if resp == 1:
			self.gastos()
		if (resp == 2):
			self.hist_receb()
		if resp == 3:
			#  "EM DESENVOLVIMENTO ..."
			self.banco.close()
			print('\033[36mPrograma salvo e finalizado =)\033[m')
			exit()
			#self.devedores()
		if(resp == len(op)-1):
			self.banco.close()
			print('\033[36mPrograma salvo e finalizado =)\033[m')
			exit()
	
	
	def imput(self,qt=0):
		while True:
			try:
				k=int(input('Digite sua escolha >>> \033[92m'))
			except ValueError:
				print('\033[91mERRO : caractere invalido !\033[m')
			else:
				if(k<1 or k >qt):
					print('\033[91mERRO : opção invalida !\033[m')
				else:
					print("\033[m")
					return k-1
					
					
	def limpar(self):
		os.system("clear")
		
	def titulo(self,text=''):
		print('\033[96m_'*50)
		print()
		print(text.center(50))
		print('\033[96m_\033[m'*50)
		print()
	
	def quitar(self):
		pass
		
	def devedores(self):
			self.limpar()
			self.titulo("DEVEDORES")
			self.stats()
			
			try:
				self.cursor.execute("CREATE TABLE devendo(id char,nome char,devendo char,valor real,data char, descricao char)")
				self.cursor.execute("CREATE TABLE hist_receb(id char,descricao char)")
				self.cursor.execute("CREATE TABLE hist_add_divi(id char,descricao char)")
			except:
				pass
				
			# DB
			# id , nome , devendo , valor , data , descricao
			print("Digite 1 para Ver todos clientes\n       2 para Adicionar um cliente\n       3 para Quitar um cliente\n       4 para voltar ao menu\n")
			resp=self.imput(4)
			if(resp == 3):
				self.limpar()
				self.menu()
				
			if(resp == 0):
				self.limpar()
				self.titulo("TODOS OS CLIENTES")
				self.stats()
				self.cursor.execute("SELECT * FROM devendo")
				cl=self.cursor.fetchall()
				if len(cl) == 0:
					print("AINDA NAO HA NADA !")
					input("Digite algo para voltar >>> ")
					self.devedores()
				else:
					for k in range(0,len(cl)):
						print(f"{k+1} - {cl[k][1].title()}")
						print(f"{len(cl)+1} - Voltar")
					print("\nDigite o numero para selecionar o cliente")
					resl=self.imput(len(cl)+1)
					if(resl == len(cl)):
						self.devedores()
					else:
						self.limpar()
						self.titulo("DADOS DO CLIENTE")
						print(f"Nome : {cl[resl][1]}\nDevendo R$ : {cl[resl][3]}")
						print("\nDigite 1 para Renomea-lo\n       2 para Adicionar uma divida\n       3 para quitar uma dividal\n       4 para voltar ao menu\n")
						resp=self.imput(4)
						if(resp == 3):
							self.devedores()
							
						if(resp == 2):
							self.quitar()
							
						if(resp == 1):
							self.limpar()
						self.titulo("ADICIONAR DIVIDA")
						print(f"Nome : {cl[resl][1]}\nDevendo R$ : {cl[resl][3]}")
						data_e_hora_atuais = datetime.now()
						data_atual =data_e_hora_atuais.strftime("%d/%m/%Y")
						print(f"\033[92mA data de hoje é : {data_atual}\033[m")
						print("O formato da infomacao deve ser :\n        1 - Data\n        2 - Descrição\n        3 - Valor\n")
						dt=input("Data : \033[92m")
						desc=input("\033[mDescrição : \033[92m")
						print("\033[m")
						while True:
							j=input("\nDigite o valor R$ : \033[92m")
							print("\033[m")
							if(self.num(j)[1] == "false"):
								print('\033[91mERRO : caractere invalido !\033[m')
							else:
								# ADICONAR A DIVIDA SEM RETIRAR A ANTERIOR
								pass
						
						if(resp == 0):
							nome=input("Digite o nome do cliente ou break para cancelar >>> ")
							if nome == 'break':
								self.devedores()
							else:
								try:
									self.cursor.execute("UPDATE devendo SET nome = ? WHERE id =?",(nome,cl[resl][0],))
									self.banco.commit()
								except:
									print('\033[91mOCORREU UM ERRO\033[m')
								else:
									print('\033[92mALTERACAO FEITA COM SUCESSO\033[m')
								input("Digite algo para continuar >>> ")
								self.devedores()
						
				
			if(resp == 2):
				self.limpar()
				self.titulo("DEVENDO")
				self.stats()
				self.cursor.execute("SELECT * FROM devendo WHERE devendo == 'true' ")
				cl=self.cursor.fetchall()
				if len(cl) == 0:
					print("AINDA NAO HA NADA !")
					input("Digite algo para voltar >>> ")
					self.devedores()
				else:
					for k in range(0,len(cl)):
						print(f"{k} - {cl[k][1]}")
				
		
			if(resp == 1):
				self.limpar()
				self.titulo("ADICIONAR CLIENTE")
				# id , nome , devendo , valor , data , descricao
				nome=input("Digite o nome do cliente ou break para cancelar >>> ")
				if nome == 'break':
					self.devedores()
				else:
					id=f"{choice('abcdefghijklmnopqrstuvwxyz')}{randint(0,999)}{choice('abcdefghijklmnopqrstuvwxyz')}{choice('abcdefghijklmnopqrstuvwxyz')}{randint(0,999)}"
					try:
						self.cursor.execute("INSERT INTO devendo(id,nome,devendo,valor,data, descricao) VALUES(?,?,?,?,?,?)",(id,nome,'false',0,'','',))
					except:
						print("\033[91mERRO : OCORREU UM ERRO\033[m")
					else:
						print("\033[96mNOVO CLIENTE SALVO\033[m")
						self.banco.commit()
					input("Digite algo para voltar >>> ")
					self.devedores()
				
	
	def menu_pg(self):
			self.limpar()
			self.titulo("ADICIONAR PAGAMENTO")
			self.stats()
			print("Digite 1 para Adicionar valor para disponivel\n       2 para mover de disponivel para a reserva\n       3 para mover da reserva para disponivel\n       4 para voltar ao menu\n")
			resp=self.imput(4)
			if(resp == 3):
				self.limpar()
				self.menu()
			if(resp == 0):
				self.limpar()
				self.titulo("ADICIONAR VALOR")
				self.stats()
				while True:
					j=input("\nDigite 'break' para cancelar ou o valor R$ : \033[92m")
					print("\033[m")
					if(j == "break"):
						self.menu_pg()
						break
					if(self.num(j)[1] == "false"):
						print('\033[91mERRO : caractere invalido !\033[m')
					else:
						gh=self.num(j)[0]
						data_e_hora_atuais = datetime.now()
						data_atual =data_e_hora_atuais.strftime("%d/%m/%Y")
						M_A=data_e_hora_atuais.strftime("%m/%Y")
						A=data_e_hora_atuais.strftime("%Y")
	
						self.cursor.execute('SELECT * FROM saldo')
						td=self.cursor.fetchall()
						
						if(td[0][0] < 0):
							tot=td[0][0]+gh
							dis=td[0][0]+gh
							res=0
							
						else:
							tot=td[0][0]+gh
							res=td[0][1]
							dis=td[0][2]+gh
							
						self.cursor.execute("UPDATE saldo SET total = ?,reseva =?,disponivel = ?",(tot,res,dis,))
						self.banco.commit()
						
						self.cursor.execute("SELECT * FROM receb_anual")
						ano=self.cursor.fetchall()
						self.cursor.execute("SELECT * FROM receb_mes")
						mes=self.cursor.fetchall()
						self.cursor.execute("SELECT * FROM receb_sem")
						semana=self.cursor.fetchall()
						print(ano)
						
						fgrtd=gh+ano[-1][1]
						if A == ano[-1][0] :
							self.cursor.execute("UPDATE receb_anual SET valor = ?",(fgrtd,))
						else:
							self.cursor.execute("INSERT INTO receb_anual(ano,valor) VALUES(?,?)",(A,gh,))
						
						fgrtd=gh+mes[-1][1]	
						if M_A == mes[-1][0] :
							self.cursor.execute("UPDATE receb_mes SET valor = ? WHERE mes == ?",(fgrtd,M_A,))
						else:
							self.cursor.execute("INSERT INTO receb_mes(mes,valor) VALUES(?,?)",(M_A,gh,))
						
						try:
							if(semana[-1][0] == data_atual):
								dtg=gh+semana[-1][2]
								self.cursor.execute("UPDATE receb_sem SET valor = ?,mes = ? WHERE dia == ?",(dtg,M_A,data_atual,))
							else:
								self.cursor.execute("INSERT INTO receb_sem(dia,mes,valor) VALUES(?,?,?)",(data_atual,M_A,gh,))
						
						except IndexError:
							self.cursor.execute("INSERT INTO receb_sem(dia,mes,valor) VALUES(?,?,?)",(data_atual,M_A,gh,))
						
						
							
						self.banco.commit()	
						self.menu_pg()
						
									
			
#			self.cursor.execute("CREATE TABLE receb_mes(mes char,valor real)")
#			self.cursor.execute("CREATE TABLE receb_sem(dia char,valor real)")
						
			if(resp == 1):
				self.limpar()
				self.stats()
				while True:
					j=input("\nDigite 'break' para cancelar ou o valor para mover para reserva R$ : \033[92m")
					print("\033[m")
					if(j == "break"):
						self.menu_pg()
						break
					if(self.num(j)[1] == "false"):
						print('\033[91mERRO : caractere invalido !\033[m')
					else:
						gh=self.num(j)[0]
						self.cursor.execute('SELECT * FROM saldo')
						td=self.cursor.fetchall()
						if(td[0][2] <gh):
							print("\n\033[91mERRO : esta operacao nao e possivel\033[m\n")
						else:
							tot=td[0][1]+gh
							dis=td[0][2]-gh
							self.cursor.execute("UPDATE saldo SET reseva = ?,disponivel = ?",(tot,dis,))
							self.banco.commit()
							self.menu_pg()
						
			if(resp == 2):
				self.limpar()
				self.stats()
				while True:
					j=input("\nDigite 'break' para cancelar ou o valor para mover para disponivel R$ : \033[92m")
					print("\033[m")
					if(j == "break"):
						self.menu_pg()
						break
					if(self.num(j)[1] == "false"):
						print('\033[91mERRO : caractere invalido !\033[m')
					else:
						gh=self.num(j)[0]
						self.cursor.execute('SELECT * FROM saldo')
						td=self.cursor.fetchall()
						if(td[0][1] <gh):
							print("\n\033[91mERRO : esta operacao nao e possivel\033[m\n")
						else:
							tot=td[0][1]-gh
							dis=td[0][2]+gh
							self.cursor.execute("UPDATE saldo SET reseva = ?,disponivel = ?",(tot,dis,))
							self.banco.commit()
							self.menu_pg()
						
						
	def hist_receb(self):
			self.limpar()
			self.titulo("Historico De Recebimento")
			self.stats()
			
			self.cursor.execute("SELECT * FROM receb_anual")
			ano=self.cursor.fetchall()
			self.cursor.execute("SELECT * FROM receb_mes")
			mes=self.cursor.fetchall()
			self.cursor.execute("SELECT * FROM receb_sem")
			semana=self.cursor.fetchall()
			
			fygyyu=0
			for b in range(0,len(mes)):
				fygyyu+=mes[b][1]
				
			ghyd=0
			for x in range(0,len(semana)):
				ghyd+=semana[x][2]
			
			try :	
				print(f"Media de recebimento mensal R$ : {self.numb_valor(fygyyu/len(mes))}\nMedia de recebimento semanal R$ : {self.numb_valor(ghyd/len(semana))}")
				for kske in range(0,len(ano)):
					print(f"Recebimento do Ano de {ano[kske][0]} foi de R$ : {self.numb_valor(ano[kske][1])}\n")
				print("Digite 1 Ver  Detalhado\n       2 Voltar ao Menu\n")
				resp=self.imput(2)
			#	print(len(semana))
	#			print('\033[33m',len(mes),'\033[m')
		#		print('\033[34m',mes[0][0],'\033[m')
				
				if(resp == 0):
					for tesmes in range(0,len(mes)):
						self.titulo(f"TOTAL DO MES {mes[tesmes][0]} FOI R$ : {self.numb_valor(mes[tesmes][1])}")
						for c in range(0,len(semana)):
							
							if(semana[c][1] == mes[tesmes][0]):
								print(f"{semana[c][0]} R$ : {self.numb_valor(semana[c][2])}")								
					
				print("\nDigite 1 Voltar ao Menu\n")
				resp=self.imput(1)
				if(resp == 0):
					self.limpar()
					self.menu()
					
			except :
				self.titulo("Não há nada ainda")
				print("\nDigite 1 Voltar ao Menu\n")
				resp=self.imput(1)
				if(resp == 0):
					self.limpar()
					self.menu()
					
			if(resp == 1):
				self.limpar()
				self.menu()
		
								
	def gastos(self):
			self.limpar()
			self.titulo("ADICIONAR GASTO")
			self.stats()
			print("Digite 1 para continuar\n       2 para voltar ao menu\n       3 para ver historico de gastos\n")
			resp=self.imput(3)
			if(resp == 1):
				self.limpar()
				self.menu()
				
			if(resp == 2):
				self.cursor.execute('SELECT * FROM gastos')
				gst=self.cursor.fetchall()
				
				if( gst == []):
					self.titulo("Não há nada ainda")
				
				data_run_tratam='pg'
				mes_run=0
				for l in range(0,len(gst)):
					data_run=''				
					for menm in list(gst[l][0])[3:]:
						data_run+=menm
					data_run_2=list(gst[l][0])[3:]
					
					if data_run_tratam != data_run :						
						for lp in range(0,len(gst)):
							if(list(gst[lp][0])[3:]  == data_run_2):
								mes_run+=gst[lp][2]
						self.titulo(f"O GASTO TOTAL DO MES {data_run} FOI R$ : {self.numb_valor(mes_run)}")
						mes_run=0
						data_run_tratam=data_run
						for hrjei in range(0,len(gst)):
							if(list(gst[hrjei][0])[3:] == data_run_2):
								print("\033[92m",gst[hrjei][0]," | ",gst[hrjei][1]," | R$ : ",self.numb_valor(gst[hrjei][2]))
							
					
				input("\n\033[mDigite algo para volta ao menu >>> ")
				self.menu()
				
			if(resp == 0):
				data_e_hora_atuais = datetime.now()
				data_atual =data_e_hora_atuais.strftime("%d/%m/%Y")
				print(f"\033[92mA data de hoje é : {data_atual}\033[m")
				print("O formato da infomacao deve ser :\n        1 - Data\n        2 - Descrição\n        3 - Valor\n")
				dt=input("Data : \033[92m")
				desc=input("\033[mDescrição : \033[92m")
				print("\033[m")
				while True:
					j=input("\nDigite o valor R$ : \033[92m")
					print("\033[m")
					if(self.num(j)[1] == "false"):
						print('\033[91mERRO : caractere invalido !\033[m')
					else:
						gh=self.num(j)[0]
						self.cursor.execute('SELECT * FROM saldo')
						td=self.cursor.fetchall()
						#total, reseva,disponivel
						total=td[0][0]-gh
						if(td[0][2]-gh < 0 ):
							disponivel=0
							reseva=(td[0][2]+td[0][1])-gh
						else:		
							disponivel=td[0][2]-gh
							reseva=td[0][1]
						
						self.cursor.execute("UPDATE saldo SET total = ? ,reseva = ?,disponivel = ?",(total,reseva,disponivel,))
						self.banco.commit()
						
						self.cursor.execute("INSERT INTO gastos(data, descricao,valor) VALUES(?,?,?) ",(dt,desc,gh,))
						self.banco.commit()
						
						self.menu()
							

	def numb_valor(self,g):
		g=f"{float(g):.2f}"
		g=str(g).replace(".",",").strip()
		g.replace(" ","").replace("  ","")
		if(g ==""):
			return 0
		else:
			if(len(g)-1 - g.find(",") <2):
				g+="0"
		
			m=0		
			if(len(g)-3 > 3):
				m=len(g)-3
				l=list(g)
				while (m > 2):
					m-=3
					l.insert(m," ")
				r=""
				for kl in range(0,len(l)):
					r+=str(l[kl])
				g=r
			return g
		

	def num(self,o):
	        t=[]
	        i=str(o).replace(",",".")
	        kl=list(i)
	        i=""
	        for c in range(0,len(kl)):
	        	if(kl[c] != " "):
	        		i+=kl[c] 
	        try:
	        	p=float(i)
	        except:
	        	t.append(i)
	        	t.append("false")
	        	return t
	        else:
	        	i=float(f'{float(i):.2f}')
	        	t.append(float(i))
	        	t.append("true")
	        	return t
	        	
	        															
																				
main()
