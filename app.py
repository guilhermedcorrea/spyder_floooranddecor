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
    lista_categorias = [
    'https://www.flooranddecor.com/explore-bathrooms?tab=icon-filter-tabs-1',
    'https://www.flooranddecor.com/explore-showers?tab=icon-filter-tabs-1',
    'https://www.flooranddecor.com/explore-backsplashes?tab=icon-filter-tabs-1',
    'https://www.flooranddecor.com/explore-kitchens?tab=icon-filter-tabs-1',
    'https://www.flooranddecor.com/finishing-pieces-tile',
    'https://www.flooranddecor.com/explore-outdoors?tab=icon-filter-tabs-1',
    'https://www.flooranddecor.com/explore-pools?prefn1=color&prefv1=Blue&prefn2=poolSafeIndicator&prefv2=Pool+Interiors&tab=icon-filter-tabs-2',
    'https://www.flooranddecor.com/wall-tile',
    'https://www.flooranddecor.com/garage-flooring',
    'https://www.flooranddecor.com/large-format-tile-tile',
    'https://www.flooranddecor.com/dramatic-stone-look-tile',
    'https://www.flooranddecor.com/porcelain-tile',
    'https://www.flooranddecor.com/ceramic-tile',
    'https://www.flooranddecor.com/glass-tile',
    'https://www.flooranddecor.com/wood-look-plank-tile',
    'https://www.flooranddecor.com/marble-look-tile',
    'https://www.flooranddecor.com/subway-decoratives',
    'https://www.flooranddecor.com/stone-look-tile',
    'https://www.flooranddecor.com/patterned-floors',
    'https://www.flooranddecor.com/polished-high-gloss-look-tile',
    'https://www.flooranddecor.com/vinyl',
    'https://www.flooranddecor.com/tile',
    'https://www.flooranddecor.com/marble-stone',
    'https://www.flooranddecor.com/ledgers-stone',
    'https://www.flooranddecor.com/brick-stone?tab=icon-filter-tabs-1',
    'https://www.flooranddecor.com/travertine-stone',
    'https://www.flooranddecor.com/slate-stone',
    'https://www.flooranddecor.com/granite-stone',
    'https://www.flooranddecor.com/limestone-basalt-stone',
    'https://www.flooranddecor.com/large-format-stone',
    'https://www.flooranddecor.com/textured-stone',
    'https://www.flooranddecor.com/dramatic-stone-looks',
    'https://www.flooranddecor.com/dark-stone-tile',
    'https://www.flooranddecor.com/bathroom-stone',
    'https://www.flooranddecor.com/backsplashes-stone',
    'https://www.flooranddecor.com/kitchen-stone',
    'https://www.flooranddecor.com/explore-outdoors?tab=icon-filter-tabs-1',
    'https://www.flooranddecor.com/explore-pools?prefn1=poolDeckSafe&prefv1=Pool+Decks&srule=predictive+sort+v3&tab=icon-filter-tabs-1',
    'https://www.flooranddecor.com/wall-stone',
    'https://www.flooranddecor.com/explore-showers?tab=icon-filter-tabs-1',
    'https://www.flooranddecor.com/mosaic-stone',
    'https://www.flooranddecor.com/finishing-pieces-stone',
    'https://www.flooranddecor.com/stone-countertops.html',
    'https://www.flooranddecor.com/pavers',
    'https://www.flooranddecor.com/engineered-hardwood-wood',
    'https://www.flooranddecor.com/solid-hardwood-wood',
    'https://www.flooranddecor.com/bamboo',
    'https://www.flooranddecor.com/cork',
    'https://www.flooranddecor.com/unfinished-wood',
    'https://www.flooranddecor.com/wood-butcher-block-countertops',
    'https://www.flooranddecor.com/moldings.html',
    'https://www.flooranddecor.com/stair-parts?tab=icon-filter-tabs-1',
    'https://www.flooranddecor.com/oak-wood',
    'https://www.flooranddecor.com/hickory-wood',
    'https://www.flooranddecor.com/maple-wood',
    'https://www.flooranddecor.com/birch-wood',
    'https://www.flooranddecor.com/water-resistant-flooring',
    'https://www.flooranddecor.com/bruce-wood?prefn1=brand&prefv1=Dogwood%20by%20Bruce',
    'https://www.flooranddecor.com/aquaguard-wood',
    'https://www.flooranddecor.com/aquaguard-bamboo',
    'https://www.flooranddecor.com/bruce-wood',
    'https://www.flooranddecor.com/eco-forest',
    'https://www.flooranddecor.com/wood',
    'https://www.flooranddecor.com/acacia-wood',
    'https://www.flooranddecor.com/aquaguard-performance',
    'https://www.flooranddecor.com/water-resistant-laminate',
    'https://www.flooranddecor.com/laminate-flooring',
    'https://www.flooranddecor.com/pet-friendly-laminate',
    'https://www.flooranddecor.com/attached-pad-laminate',
    'https://www.flooranddecor.com/extra-long-laminate',
    'https://www.flooranddecor.com/authentic-texture-laminate',
    'https://www.flooranddecor.com/aquaguard-performance',
    'https://www.flooranddecor.com/hydroshield-laminate',
    'https://www.flooranddecor.com/hampstead-premium-laminate',
    'https://www.flooranddecor.com/explore-backsplashes?tab=icon-filter-tabs-1',
    'https://www.flooranddecor.com/explore-bathrooms?tab=icon-filter-tabs-1',
    'https://www.flooranddecor.com/explore-showers?tab=icon-filter-tabs-1',
    'https://www.flooranddecor.com/accent-wall-tile',
    'https://www.flooranddecor.com/explore-pools?prefn1=color&prefv1=Blue&prefn2=poolSafeIndicator&prefv2=Pool+Interiors&tab=icon-filter-tabs-2',
    'https://www.flooranddecor.com/marble-decoratives',
    'https://www.flooranddecor.com/porcelain-ceramic-decoratives',
    'https://www.flooranddecor.com/glass-decoratives',
    'https://www.flooranddecor.com/stone-decoratives',
    'https://www.flooranddecor.com/pebble-stone-decoratives',
    'https://www.flooranddecor.com/blue-decoratives',
    'https://www.flooranddecor.com/black-decoratives',
    'https://www.flooranddecor.com/waterjet-decoratives',
    'https://www.flooranddecor.com/mother-of-pearl-decoratives',
    'https://www.flooranddecor.com/search?cgid=subway-size-decoratives',
    'https://www.flooranddecor.com/florals-decoratives',
    'https://www.flooranddecor.com/hot-glass-decoratives',
    'https://www.flooranddecor.com/vinyl'
]

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
