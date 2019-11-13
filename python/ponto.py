###########################################################################
# NOME: Script para enviar submits para web com campos preenchidos
# AUTOR: Isaac de Moraes
############################################################################
## Passo 1: Instalar python 2.7.X
## Passo 2: Fazer download do GeckoDriver https://github.com/mozilla/geckodriver/releases
## Passo 3: Extrair o arquivo geckodriver (linux) geckodriver.exe (windowns)
## Passo 4: Em inspecionar elemento verifique o Id do campo do usuario e subistua os campos "substituirloginpasso4" pelo Id.
## Passo 5: Em inspecionar elemento verifique o Id do campo de senha e subistua o campo "substituirsenhapasso5" pelo Id.
## Passo 6: Em inspecionar elemento verifique o Id do campo de submit e subistua o campo "substituirsubmitpasso6" pelo Id.
## Passo 7: Executar o comando "python ponto.py /path/to/geckodriver http://iakim.url.com/login/page username password"
## ee: Adicione na cron ou no agendador de tarefas a execução de tempos em tempos
############################################################################

from selenium import webdriver
import sys
if len(sys.argv) == 4:
    print len(sys.argv)
    iakim = webdriver.Firefox(executable_path=(sys.argv[1]))
    iakim.get((sys.argv[2]))
    iakim.find_element_by_id("substituirloginpasso4").clear()
    iakim.find_element_by_id("substituirloginpasso4").send_keys((sys.argv[3]))
    iakim.find_element_by_id ("substituirsenhapasso5").send_keys((sys.argv[4]))
    iakim.find_element_by_css_selector(".substituirsubmitpasso6").click()
else:
    print("Use: python ponto.py /path/to/geckodriver http://iakim.url.com/login/page username password")
