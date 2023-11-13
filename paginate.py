from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import time

def scroll(start=0, step=500, sz=528):
    url = f"https://www.flooranddecor.com/porcelain-tile?start={start}&sz={sz}"
    driver.get(url)
    time.sleep(1)
    lenOfPage = driver.execute_script(f"window.scrollTo(0, {start});var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match = False
    while not match:
        lastCount = lenOfPage
        lenOfPage = driver.execute_script(f"window.scrollBy(0, {step});var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        if lastCount == lenOfPage:
            match = True

def get_urls_categorias_produtos():
    lista_categorias = []
    lista_categorias.append("https://www.flooranddecor.com/porcelain-tile")
    for categoria in lista_categorias:
        yield categoria

def get_url_produtos():
    lista_produtos = []
    try:
        categorias = get_urls_categorias_produtos()
        for categoria in categorias:
            for start in range(0, 500, 100): 
                scroll(start=start)
                elementos_produtos = driver.find_elements(By.CSS_SELECTOR, 'a.b-product_tile-figure_link')
                for elemento in elementos_produtos:
                    url_produto = elemento.get_attribute('href')
                    print(url_produto)
                    lista_produtos.append(url_produto)
                    if len(lista_produtos) >= 500:  
                        return lista_produtos
    except Exception as e:
        print(f"Erro ao obter URLs de produtos: {e}")
    return lista_produtos

def obter_detalhes_produto(url_produto):
    dict_item = {"urlprodutos": url_produto}
    driver.get(url_produto)
    
    print(dict_item)
    return dict_item


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

lista_produtos = []
produtos = get_url_produtos()

for produto in produtos:
    dict_item = obter_detalhes_produto(produto)
    lista_produtos.append(dict_item)

dados = pd.DataFrame(lista_produtos)
dados.to_csv("urlsprodutos_floordecor_01.csv", index=False)


driver.quit()
