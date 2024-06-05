from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
import webbrowser

# Configuração do Selenium
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#########################################################################################################################
def get_news_from_tradingview_news():
    url = 'https://www.tradingview.com/news/'
    driver.get(url)

    # Captura o conteúdo HTML após o carregamento das notícias
    page_source = driver.page_source
    # Usa BeautifulSoup para analisar o HTML
    soup = BeautifulSoup(page_source, 'html.parser')
    # Encontra todas as tags <a> dentro da div com classe 'list-iTt_Zp4a'
    noticias = soup.find_all('a')
    
    verificadas = 0
    news_dict = {}
    for noticia in noticias:
        # Condição 1: A notícia deve estar dentro de uma tag <a>
        if noticia.article:
            # Condição 2: A notícia deve ter uma tag <article> dentro dela
            article = noticia.article
            # Condição 3: A notícia deve conter uma <div> com a classe 'apply-overflow-tooltip'
            div = article.find('div', class_='apply-overflow-tooltip')
            if div:
                title = div.text.strip() # Obtém o título da notícia
                link = noticia.get('href') # Obtém o link da notícia
                title_lower = title.lower()
                verificadas += 1
                if ('iron ' in title_lower) or ('china' in title_lower) :  # Verifica se é uma noticia interessante
                    news_dict[title] = link
    return news_dict, verificadas
news1, verificadas1 = get_news_from_tradingview_news()

print()
print(f"{verificadas1} Notícias verificadas em 'tradingview/news'.")
print()
for title, link in news1.items():
    # Corrigir o link para o site TradingView
    if link.startswith('/'):
        link = 'https://www.tradingview.com' + link
    print(f"Título: {title}\nLink: {link}\n")
print(f"{len(news1)} Notícias relevantes localizadas.")
#########################################################################################################################
def get_news_from_ft():
    url = 'https://www.ft.com/chinese-business-finance'
    driver.get(url)

    # Captura o conteúdo HTML após o carregamento das notícias
    page_source = driver.page_source
    # Usa BeautifulSoup para analisar o HTML
    soup = BeautifulSoup(page_source, 'html.parser')
    # Encontra todas as tags <a> dentro da div com classe 'js-teaser-heading-link'
    noticias = soup.find_all('a', class_='js-teaser-heading-link')

    verificadas = 0
    news_dict = {}
    for noticia in noticias:
        # Verifica se o elemento <a> possui o atributo 'href'
        link = noticia.get('href')    # Obtém o link da notícia
        if link:
            title = noticia.text.strip()  # Obtém o título da notícia
            title_lower = title.lower()
            verificadas += 1
            if ('iron ' in title_lower) or ('china' in title_lower) :    # Verifica se é uma notícia interessante
                news_dict[title] = link
    return news_dict, verificadas
news2, verificadas2 = get_news_from_ft()

print()
print(f"{verificadas2} Notícias verificadas em 'ft'.")
print()
for title, link in news2.items():
    # Verifica se o link é relativo e adiciona o domínio se necessário
    if link.startswith('/'):
        link = 'https://www.ft.com' + link
    print(f"Título: {title}\nLink: {link}\n")
print(f"{len(news2)} Notícias relevantes localizadas.")
#########################################################################################################################
def get_news_from_mining():
    url = 'https://www.mining.com/'
    driver.get(url)

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    noticias = soup.find_all('a')

    verificadas = 0
    news_dict = {}
    for noticia in noticias:
        link = noticia.get('href')
        if link:
            title = noticia.text.strip()
            title_lower = title.lower()
            verificadas += 1
            if ('iron ' in title_lower) or ('china' in title_lower) :
                news_dict[title] = link
    return news_dict, verificadas
news3, verificadas3 = get_news_from_mining()

print()
print(f"{verificadas3} Notícias verificadas em 'mining'.")
print()
for title, link in news3.items():
    print(f"Título: {title}\nLink: {link}\n")
print(f"{len(news3)} Notícias relevantes localizadas.")
#########################################################################################################################
def get_news_from_tradingview_market():
    url = 'https://www.tradingview.com/news/markets/?category=futures'
    driver.get(url)

    # Aguarda até que o botão esteja presente na página
    button_xpath = '/html/body/div[3]/div[4]/div/div/div/div[2]/div/div[2]/div[3]/button'
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, button_xpath)))
    # Localiza o botão e clica nele
    button = driver.find_element(By.XPATH, button_xpath)
    button.click()

    import time
    time.sleep(3)

    # Captura o conteúdo HTML após o carregamento das notícias
    page_source = driver.page_source
    # Usa BeautifulSoup para analisar o HTML
    soup = BeautifulSoup(page_source, 'html.parser')
    # Encontra todas as tags <a> dentro da div com classe 'list-iTt_Zp4a'
    noticias = soup.find('div', class_='list-iTt_Zp4a').find_all('a')

    verificadas = 0
    news_dict = {}
    for noticia in noticias:
        # Condição 1: A notícia deve estar dentro de uma tag <a>
        if noticia.article:
            # Condição 2: A notícia deve ter uma tag <article> dentro dela
            article = noticia.article
            # Condição 3: A notícia deve conter uma <div> com a classe 'apply-overflow-tooltip'
            div = article.find('div', class_='apply-overflow-tooltip')
            if div:
                title = div.text.strip() # Obtém o título da notícia
                link = noticia.get('href') # Obtém o link da notícia
                title_lower = title.lower()
                verificadas += 1
                if ('iron ' in title_lower) or ('china' in title_lower) :  # Verifica se é uma noticia interessante
                    news_dict[title] = link
    return news_dict, verificadas
news4, verificadas4 = get_news_from_tradingview_market()

print()
print(f"{verificadas4} Notícias verificadas em 'tradingview/market'.")  # Imprime o número de notícias localizadas
print()
for title, link in news4.items():
    # Corrigir o link para o site TradingView
    if link.startswith('/'):
        link = 'https://www.tradingview.com' + link
    print(f"Título: {title}\nLink: {link}\n")
print(f"{len(news4)} Notícias relevantes localizadas.")
#########################################################################################################################
def get_news_from_infomoney():
    url = 'https://www.infomoney.com.br/ultimas-noticias/'
    driver.get(url)
    import time

    try:
        # Procure o primeiro elemento '//*[@id="fechar"]' por 5 segundos
        close_button = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, '//*[@id="fechar"]')))
        close_button.click()
        print("Botão 'fechar' encontrado e clicado.")
    except TimeoutException:
        print("Botão 'fechar' não encontrado, iniciando o loop para carregar mais notícias.")
        while True:
            try:
                # Procure o segundo elemento '//*[@id="infinite-handle"]' por 5 segundos
                WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, '//*[@id="infinite-handle"]')))
                button_xpath = '//*[@id="infinite-handle"]/span/button'
                button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
                button.click()
                print("Botão 'carregar mais notícias' encontrado e clicado.")
            except TimeoutException:
                print("Botão 'carregar mais notícias' não encontrado, encerrando o loop.")
                break
            except ElementClickInterceptedException:
                print("Não foi possível clicar no botão, tentando novamente.")
                driver.execute_script("arguments[0].scrollIntoView(true);", button)
                time.sleep(1)
                button.click()
    print("Processo concluído.")

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    noticias = soup.find_all('a')

    verificadas = 0
    news_dict = {}
    for noticia in noticias:
        link = noticia.get('href')
        if link:
            title = noticia.text.strip()
            title_lower = title.lower()
            verificadas += 1
            if ('ferro ' in title_lower) or ('china' in title_lower) :
                news_dict[title] = link
    return news_dict, verificadas
news5, verificadas5 = get_news_from_infomoney()

print()
print(f"{verificadas5} Notícias verificadas em 'infomoney/ultimas-noticias")
print()
for title, link in news5.items():
    print(f"Título: {title}\nLink: {link}\n")
print(f"{len(news5)} Notícias relevantes localizadas.")
#########################################################################################################################

# Escrever os resultados em um arquivo HTML
with open('news.html', 'w') as f:
    f.write('<html><head><title>Buscador de Notícias</title></head><body>')

    f.write(f'<h1>{verificadas1} Notícias verificadas em "tradingview/news".</h1>')
    for title, link in news1.items():
        # Corrigir o link para o site TradingView
        if link.startswith('/'):
            link = 'https://www.tradingview.com' + link
        f.write(f'<p><strong>{title}</strong><br><a href="{link}">{link}</a></p>')

    f.write(f'<h1>{verificadas2} Notícias verificadas em "ft".</h1>')
    for title, link in news2.items():
        # Verifica se o link é relativo e adiciona o domínio se necessário
        if link.startswith('/'):
            link = 'https://www.ft.com' + link
        f.write(f'<p><strong>{title}</strong><br><a href="{link}">{link}</a></p>')

    f.write(f'<h1>{verificadas3} Notícias verificadas em "mining".</h1>')
    for title, link in news3.items():
        f.write(f'<p><strong>{title}</strong><br><a href="{link}">{link}</a></p>')

    f.write(f'<h1>{verificadas4} Notícias verificadas em "tradingview/market".</h1>')
    for title, link in news4.items():
        # Corrigir o link para o site TradingView
        if link.startswith('/'):
            link = 'https://www.tradingview.com' + link
        f.write(f'<p><strong>{title}</strong><br><a href="{link}">{link}</a></p>')

    f.write(f'<h1>{verificadas5} Notícias verificadas em "infomoney/ultimas-noticias".</h1>')
    for title, link in news5.items():
        f.write(f'<p><strong>{title}</strong><br><a href="{link}">{link}</a></p>')

    f.write('</body></html>')

# Abrir o arquivo HTML no navegador padrão
webbrowser.open('news.html')

# Fechar o navegador
driver.quit()