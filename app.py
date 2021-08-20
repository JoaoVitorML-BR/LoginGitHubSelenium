from selenium import webdriver
from time import sleep

# Funções para acessar site, sair, logar etc...

class ChromeAuto:
    def __init__(self):
        self.driver_path = 'chromedriver' # < caminho para acessar o chromedriver na pasta.
        self.options = webdriver.ChromeOptions() #salva o perfil da seção dentro daqui do projeto
        self.options.add_argument(r'user-data-dir=C:\Users\jvmli\AppData\Local\Google\Chrome\User Data\Default') #pasta onde ele ira salvar o perfil dentro do projeto
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        ) # abre o chorme

    def clica_sign_in(self):
        try: #ele tenta clicar no botão 'Sign in'
            btn_sign_in = self.chrome.find_element_by_link_text('Sign in') # ele procura o elemento sign in
            btn_sign_in.click() # clica se achou
        except Exception as e:
            print('Erro ao clicar em Sign in:', e)

    def acessa(self, site): # pega a url do site que quero acessar (github)
        self.chrome.get(site)

    def sair(self): # aqui ele sai do site
        self.chrome.quit() #func que faz sair do site quit()

    def clica_perfil(self):
        try:
            perfil = self.chrome.find_element_by_css_selector(
                'body>div.position-relative.js-header-wrapper>header>div.Header-item.position-relative.mr-0.d-none.d-md-flex>details>summary')
            perfil.click()
        except Exception as e:
            print('Erro ao clicar no perfil:', e)

    def faz_logout(self):
        try:
            perfil = self.chrome.find_element_by_css_selector(
                'body>div.position-relative.js-header-wrapper>header>div.Header-item.position-relative.mr-0.d-none.d-md-flex>details>details-menu>form>button') # copy selector
            perfil.click()
        except Exception as e:
            print('Erro fazer logout:', e)

    def faz_login(self):
        try:
            input_login = self.chrome.find_element_by_id('login_field')
            input_password = self.chrome.find_element_by_id('password')
            btn_login = self.chrome.find_element_by_name('commit')

            input_login.send_keys('email@gmail.com') # coloque seu email
            input_password.send_keys('senha') # coloque sua senha
            sleep(3)
            btn_login.click()

        except Exception as e:
            print('Erro ao fazer login:', e)


# chamando as funções na ordem correta de executção

if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessa('https://github.com/')
    chrome.clica_sign_in()
    chrome.faz_login()

    chrome.clica_perfil()

    sleep(5)
    chrome.faz_logout()

    sleep(5)
    chrome.sair()
