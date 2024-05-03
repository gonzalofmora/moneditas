import requests
from bs4 import BeautifulSoup

# Funciones
#################################################################################################################
def my_soup(url):
    """Esta función es para traer directamente la Soup de BeautifulSoup de una página web
    :param url: el link con el que se va a crear la soup
    :return soup: la soup de la página web
    """
    page =  requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    return soup

def precio_carrefour(url):
    """Extrae el precio del producto de la página de Carrefour
    :param url: el link del producto de Carrefour a controlar
    :return precio_lindo: el precio del producto en formato float
    """
    soup = my_soup(url)
    precio_feo = soup.find_all("span", class_="valtech-carrefourar-product-price-0-x-currencyContainer")[0].text
    limpieza_de_caracteres = str.maketrans({'.':'', ',':'.', '$':'','\xa0':''})
    precio_lindo = float(precio_feo.translate(limpieza_de_caracteres))
    
    return precio_lindo
#################################################################################################################


#Links de los productos
protein_url           = "https://www.carrefour.com.ar/leche-descremada-la-serenisima-uat-proteinas-1-l/p"
prebioticos_url       = "https://www.carrefour.com.ar/leche-la-serenisima-con-prebioticos-1-lt-705547/p"
cero_lactosa_url      = "https://www.carrefour.com.ar/leche-descremada-larga-vida-la-serenisima-cero-lactosa-1-l/p"
nesquik_menos_az_300g = "https://www.carrefour.com.ar/nesquik-original-cacao-en-polvo-menos-azucar-300-g-719361/p"

#Nombres de los productos
productos_carrefour = {
    "Serenísima Protein:        $" : protein_url,
    "Serenísima Prebióticos:    $" : prebioticos_url,
    "Serenísima Cero Lactosa:   $" : cero_lactosa_url,
    "Nesquik menos azúcar 300g: $" : nesquik_menos_az_300g
}

# Precios de los productos
#for producto, link in productos_carrefour.items():
#    print(producto, precio_carrefour(link))

#Esto es una prueba