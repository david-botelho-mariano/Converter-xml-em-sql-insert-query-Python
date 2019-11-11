# -*- coding: utf-8 -*-

import os
import xmltodict

def ler_diretorios_e_subdiretorios():
	path = os.getcwd()
	#define o diretorio raiz

	lista_arquivos_desejados = []
	#lista de caminho absolutos para os arquivos

	#percorre todos pastas e subpastas em busca de arquivos .xml
	for lista_nome_diretorios, lista_nome_pastas, lista_nome_arquivos in os.walk(path):
		for arquivo in lista_nome_arquivos:
			if '.xml' in arquivo:
				lista_arquivos_desejados.append(os.path.join(lista_nome_diretorios, arquivo))

	#para cada arquivo XML encontrado, sera feito a analise do arquivo
	for arquivo in lista_arquivos_desejados:
		analisarXML(arquivo)
		

def remover_ultimos_caracteres(palavra, quant_caract_excluir):
	string_formatada = palavra[:-quant_caract_excluir]
	return string_formatada

def gerar_query_insert(db_nome, dados_dict):
	#primeiro parametro recebe o nome da tabela, e no segundo parametro o path para aquela informacao

	colunas_concat = ""
	linhas_concat = ""

	for chave, valor in dados_dict.items():
		#percorre cada valor e chave da lista inserida

		colunas_concat +=  chave + ', '

		try:
			#verica se eh string ou int e concatena com a string de fora do laco
			valor_sem_ponto = valor.replace('.', '').replace(",", "")
			if(int(valor_sem_ponto) == True):
				linhas_concat +=  valor + ', '
			else:
				linhas_concat +=  valor + ', '

		except Exception as e:
			linhas_concat += "'" + valor + "', "


	colunas_concat = remover_ultimos_caracteres(colunas_concat, 2)
	linhas_concat = remover_ultimos_caracteres(linhas_concat, 2)
	#formatacao da string

	insert_query = 'INSERT INTO ' + db_nome + ' (' + colunas_concat + ') VALUES ('+ linhas_concat +');'
	print(insert_query)
	#criacao da query insert

	f = open("insert-query.sql", "a")
	f.write(insert_query + "\n")
	f.close()
	#salvar em um arquivo	

def analisarXML(arquivo): 
	with open(arquivo, 'r') as f:
		dados_xml = f.read()	
		dados_dict = xmltodict.parse(dados_xml)
	#le o arquivo XMl e converte em dict (semelhante ao json)

	gerar_query_insert('xml_info', dados_dict['note'])
	#gera a query insert
      
if __name__ == "__main__": 
    ler_diretorios_e_subdiretorios()
    #inicializacao do script
