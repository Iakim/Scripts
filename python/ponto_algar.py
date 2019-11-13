# -*- coding: utf-8 -*-
###########################################################################
# NOME: Script para enviar submits para web com campos preenchidos
# AUTOR: Isaac de Moraes
############################################################################
## Passo 1: Instalar python 2.7.X
## Passo 2: Fazer download do GeckoDriver https://github.com/mozilla/geckodriver/releases
## Passo 3: Extrair o arquivo geckodriver (linux) geckodriver.exe (windowns)
## Passo 4: Executar o comando "python ponto_algar.py /path/to/geckodriver usuario senha"
## ee: Adicione na cron ou no agendador de tarefas a execução de tempos em tempos
############################################################################
from selenium import webdriver
import sys
import time
if len(sys.argv) == 4:
    iakim = webdriver.Firefox(executable_path=(sys.argv[1]))
    iakim.get("https://portalth.algarnet.com.br/Algar/Produtos/SAAA/Principal2.aspx?amb_selecionado=0&abrir_nova_janela=N&eh_mdesigner=N&nome_portal=634C3649335370516551633D")
    iakim.find_element_by_id("txtLogin").clear()
    iakim.find_element_by_id("txtLogin").send_keys((sys.argv[2]))
    iakim.find_element_by_id("txtSenha").send_keys((sys.argv[3]))
    iakim.find_element_by_css_selector(".botao").click()
    iakim.get("https://portalth.algarnet.com.br/Algar/Produtos/NorberMyWay2010/NorberRedirecionamento.aspx?paginaAsp=just_user/IncluirMarcacaoOnLine.asp")
    time.sleep(5)
    main_page = iakim.current_window_handle 
    for handle in iakim.window_handles: 
        if handle != main_page: 
            login_page = handle
    time.sleep(5)
    iakim.switch_to.window(login_page)
    iakim.find_element_by_id("Button1").click()
else:
    print("Use: python ponto_algar.py /path/to/geckodriver usuario senha")
