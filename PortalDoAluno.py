from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from bs4 import BeautifulSoup as bs


class PortalDoAluno:
    def __init__(self, driver: webdriver, matricula: str, password: str):
        self.matricula = matricula
        self.password = password
        self.driver = driver

        self.url = "https://portaldoaluno.ifba.edu.br/scripts/PortalAluno/index.html"
        self.input_username = 'login_username'  # name
        self.input_password = 'secretkey'  # name
        self.btn_ok = 'ok'  # name

    def _get_username(self) -> webdriver:
        """
        Input do usuário no formulário de login
        """
        return self.driver.find_element_by_name(self.input_username)

    def _get_password(self) -> webdriver:
        """
        Input da senha no formulário de login
        """
        return self.driver.find_element_by_name(self.input_password)

    def _get_btn_ok(self) -> webdriver:
        """
        Botão de login
        """
        return self.driver.find_element_by_name(self.btn_ok)

    def _login(self) -> bs:
        """
        Faz o login no portal
        """
        self._get_username().send_keys(self.matricula)
        self._get_password().send_keys(self.password)

        try:
            self._get_btn_ok().click()
        except WebDriverException as e:
            raise Exception('Erro ao fazer o login, tente novamente!')
        return bs(self.driver.page_source, 'html.parser')

    def navigate(self):
        """
        Acessa o site do portal do aluno
        """
        self.driver.get(self.url)

    def index_data(self, page: bs) -> list:
        """
        Informações da primeira página, após fazer o login no portal
        """
        title = page.title.string
        tables = page.find_all('table')
        user_infor = self._fix_user_infor(tables[0].find_all('p')[-1].text)

        data = [title, user_infor]
        return data

    def _fix_user_infor(self, user: str) -> dict:
        """
        Tratamento dos dados do aluno
        :param user: str Informações do usuários vindas do portal
        :returns: Dicionário com os dados pessoais do usuário
        :rtype dict
        """
        user = user.replace('\n', '').replace('\t', '')
        fields = [
            'Nome: ',
            'Matricula: ',
            'Curso: ',
            'Coeficiente de Rendimento : ',
            'Coeficiente de Aproveitamento : '
        ]
        items = {}
        for field in fields:
            position = user.find(field)
            user = user.replace(field, '')
            items[field.lower().replace(':', '').strip()] = position

        data = {
            'nome': user[items['nome']:items['matricula']].rstrip(),
            'matricula': user[items['matricula']:items['curso']].rstrip(),
            'curso': user[items['curso']:items['coeficiente de rendimento']].rstrip(),
            'rendimento': user[items['coeficiente de rendimento']:items['coeficiente de aproveitamento']].rstrip(),
            'aproveitamento': user[items['coeficiente de aproveitamento']:-1].rstrip(),
        }

        return data

    def main(self):
        """
        Método principal
        """
        self.navigate()
        login_page = self._login()
        index = self.index_data(login_page)
        print(index)
