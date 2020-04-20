import os
from selenium import webdriver
from PortalDoAluno import PortalDoAluno
from selenium.webdriver.firefox.options import Options
from dotenv import load_dotenv

# Carregamento das ariáveis de ambiente
load_dotenv()

# Dados de acesso do aluno
matricula = os.getenv('matricula')
password = os.getenv('password')


# Opção para não exibir o Browser
# Remover durante os testes para acompanhar todo o fluxo
options = Options()
options.add_argument("--headless")

# driver do firefox
driver = webdriver.Firefox(firefox_options=options)

portalDoAluno = PortalDoAluno(driver, matricula, password)
portalDoAluno.main()

# Finaliza o browser
driver.quit()
