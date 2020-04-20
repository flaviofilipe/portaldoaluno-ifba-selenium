# Automatização do Portal do Aluno IFBA

Projeto criado com fins educativos para demonstrar a utilização da ferramenta Selenium, para automatizar o acesso ao [portal do aluno](https://portaldoaluno.ifba.edu.br/scripts/PortalAluno/index.html) do IFBA. Apenas alunos do instituto poderá inserir suas credenciais para fazer os testes.

## Pré requesito

É necessário fazer a instalação de um WebDriver para executar o Selenium.
Neste projeto foi utilizado o [Gecko](https://github.com/mozilla/geckodriver/releases), WebDriver do firefox.
Para utilizar outros drivers, deverá fazer alterações no arquivo principal **app.py**

## Instalação

- Crie o arquivo .env baseado no arquivo .env.example
- Insira as credenciais de acesso ao portal no arquivo .env
- [Virtualenv](https://virtualenv.pypa.io/en/latest/)
  ```
  virtualenv venv
  Linux: source venv/bin/activate
  Windows: virtualenv\virtual_1\Scripts\activate
  ```
- Requirements
  ```
  pip install -r requirements.txt
  ```
- Run
  ```
  python app.py
  ```
