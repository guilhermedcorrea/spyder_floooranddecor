from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
import pandas as pd


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("https://www.flooranddecor.com/")


def scroll() -> None:
    driver.implicitly_wait(1)
    lenOfPage = driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match = False
    while not match:
        lastCount = lenOfPage
        lenOfPage = driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        if lastCount == lenOfPage:
            match = True



def get_urlsget_categorias_produtos():
    lista_categorias = []
  

    for lista in lista_categorias:
        yield lista
        
        
        
def get_url_produtos():
    lista_produtos = []
    try:
        produtos = get_urlsget_categorias_produtos()
        while True:
            driver.implicitly_wait(3)
            driver.get(next(produtos))
            scroll()
            
            urls = driver.find_elements(By.XPATH,'/html/body/div[5]/div[9]/div/main/div/section[3]/div/main/div/article/div/div/figure/a')
            for url in urls:
                urls_produtos = url.get_attribute('href')
                print(urls_produtos)
                lista_produtos.append(urls_produtos)
    except:
        pass
    
    return lista_produtos

lista_produtos = []
produtos = get_url_produtos()
for produto in produtos:
    dict_item = {}
    driver.get(produto)
    dict_item['urlprodutos'] = produto
    try:
        nome = driver.find_elements(By.XPATH,"/html/body/main/div[1]/section/div[1]/form/div/article[2]/div/div/h1")[0].text
        dict_item['nome'] = nome
    except:
        pass
    
    
    try:
        preco = driver.find_elements(By.XPATH,'/html/body/main/div[1]/section/div[1]/form/div/article[3]/div/div/span[1]')[0].text
        dict_item['precos'] = preco
    except:
        pass
        

    try:
        dimensao = driver.find_elements(
                        By.XPATH,'/html/body/main/div[1]/section/div[1]/form/div/article[4]/div/div/div[2]')[0].text
        dict_item['dimensao'] = dimensao
    except:
        pass
    
    try:
        sku = driver.find_elements(
                        By.XPATH,'/html/body/main/div[1]/section/div[1]/form/div/article[4]/div/div/div[1]/div')[0].text
        dict_item['sku'] = str(sku).split(":")[-1].strip()
    except:
        pass
    
    try:
        dimensao = driver.find_elements(
                        By.XPATH,'/html/body/main/div[1]/section/div[1]/form/div/article[4]/div/div/div[2]')[0].text
        dict_item['dimensao'] = dimensao
    except:
        pass
    
                    
    categorias = driver.find_elements(By.XPATH,'/html/body/main/div/div/div')
    cont = 0
    for categoria in categorias:
        dict_item['Categoria'+str(cont)] =  categoria.text
        cont+=1
      
    imagens = driver.find_elements(By.XPATH,"//img[contains(@class, 'b-pdp_thumbnail-figure_img')]")
    cont = 0
    for imagem in imagens:
        dict_item['imagem'+str(cont)] = imagem.get_attribute("src")
        cont+=1 
       
    script = """
            var elementos = document.querySelectorAll("section.b-pdp_specifications-container article span.b-pdp_specifications-name, section.b-pdp_specifications-container article span.b-pdp_specifications-number");
            var dados = {};
            for (var i = 0; i < elementos.length; i += 2) {
                var referencia = elementos[i].textContent.trim();
                var valor = elementos[i + 1].textContent.trim();
                dados[referencia] = valor;
            }
            return dados;
            """

    informacoes = driver.execute_script(script)

    dict_item.update(informacoes)


    try:
        product_details = driver.find_elements(By.XPATH,'/html/body/main/div[1]/section/div[1]/div/section[2]/div[2]/div/div/div/p[1]')[0].text
        dict_item["ProductDetails"] = product_details
    except:
        pass
    
   
    try:
        installation = driver.find_element(By.XPATH, "//figure[@class='b-products_install-figure']/img")
        dict_item["installation"] = installation.get_attribute("src")
    except NoSuchElementException:
        print("Elemento 'installation' não encontrado")
        
    try:
        cair_maintence = driver.find_element(By.XPATH, "//a[@class='b-products_install-title' and text()='Care & Maintenance']")
        dict_item['CairMaintence'] = cair_maintence.get_attribute("href")
    except NoSuchElementException:
                print("Elemento 'CairMaintence' não encontrado")

    try:
        user_guide = driver.find_element(By.XPATH, "//figure[@class='b-products_install-figure']/img")
        dict_item["UserGuide"] = user_guide.get_attribute("src")
    except NoSuchElementException:
        print("Elemento 'UserGuide' não encontrado")

    print(dict_item)
    lista_produtos.append(dict_item)
    
    
dados = pd.DataFrame(lista_produtos)
dados.to_excel("pisos.xlsx", index=False)