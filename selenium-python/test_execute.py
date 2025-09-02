from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import pytest
import time
from utils import global_funciones

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    url="https://www.mercadolibre.com/"
    driver.get(url)
    yield driver
    driver.quit()

def test_NavegacionyBusqueda (driver):
    assert "Mercado Libre" in driver.title, "El titulo de la página no corresponde al esperado: 'Mercado Libre'"
    print(f"El titulo de la página corresponde: {driver.title}")
    funciones=global_funciones(driver)
    funciones.seleccion_pais(driver, "MX")
    driver.save_screenshot("screenshots/01_seleccion_pais.png")
    funciones.cookies_mensaje(driver,"Aceptar cookies")
    driver.save_screenshot("screenshots/02_cookies.png")
    funciones.buscar_producto(driver, "Playstation 5")
    driver.save_screenshot("screenshots/03_busqueda.png")
    funciones.filtrar_productos(driver,"Nuevo")
    driver.save_screenshot("screenshots/04_filtro_condicion.png")
    funciones.filtrar_productos(driver, "Distrito Federal")
    driver.save_screenshot("screenshots/05_filtro_ubicacion.png")
    funciones.ordenar_resultados(driver, "Mayor precio")
    driver.save_screenshot("screenshots/06_ordenado.png")

    time.sleep(3)
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='poly-card__content']")))

    productos = driver.find_elements(By.XPATH, "//div[@class='poly-card__content']")
    for i in range(5):
        try:
            producto = productos[i]
            driver.execute_script("arguments[0].scrollIntoView(true);", producto)
            time.sleep(1)
            driver.save_screenshot(f"screenshots/07_producto_{i+1}.png")

            nombre = producto.find_element(By.XPATH, ".//a[@class='poly-component__title']").text
            precio = producto.find_element(By.XPATH, ".//div[@class='poly-component__price']").text
            print(f"{i+1}. {nombre} : {precio}")
        except Exception as e:
            print(f"Error producto {i+1}: {e}")