from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pytest
from selenium.webdriver.common.action_chains import ActionChains

class global_funciones():

    def __init__(self,driver):
        self.driver=driver
    
    def seleccion_pais(self, driver, ID):
        try:
            busca_pais=WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, ID)))
            driver.execute_script("arguments[0].scrollIntoView(true);", busca_pais)
            busca_pais.click()
        except TimeoutException:
            print("No se encontró el país según el ID ingresado: ", ID)

    def validaURL(self, driver):
        urlactual=driver.current_url
        print("Usted está navegando en: ", urlactual)
    
    def buscar_producto(self, driver, nombre_producto):

        try:
            mensaje_ubicacion=WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='andes-button__content' and contains(text(), 'Más tarde')]")))
            driver.execute_script("arguments[0].scrollIntoView(true);", mensaje_ubicacion)
            mensaje_ubicacion.click()
        except TimeoutException:
            print("No se logra localizar el mensaje emergente de ubicación")
        try:    
            campo_busqueda=WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "cb1-edit")))
            driver.execute_script("arguments[0].scrollIntoView(true);", campo_busqueda)
            campo_busqueda.click()
            campo_busqueda.send_keys(nombre_producto)
        except:
            print("No se halló el campo de busqueda a tiempo")

        try:
            clic_buscar=WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[@role='img' and @aria-label='Buscar']")))
            driver.execute_script("arguments[0].scrollIntoView(true);", clic_buscar)
            clic_buscar.click()
        except TimeoutException:
            print("No se halló el botón de busqueda a tiempo")

        try:
            resultado_busqueda=WebDriverWait(driver,5).until(EC.visibility_of_all_elements_located((By.XPATH, f"//a[contains(text(), '{nombre_producto}')]")))
            print(f"Se encontraron coincidencias para: {nombre_producto}")
        except TimeoutException:
            print(f"No se encontraron coindidencias para: {nombre_producto}")
    
    def filtrar_productos (self, driver, nombre_filtro):
        try:
            filtro=WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, f"//span[@class='ui-search-filter-name' and text()='{nombre_filtro}']")))
            driver.execute_script("arguments[0].scrollIntoView(true);", filtro)
            filtro.click()
        except TimeoutException:
            print(f"No se halló el filtro: {nombre_filtro}")
        
        try:
            valida_filtroAplicado=WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH, f"//div[@class='andes-tag__label' and text()='{nombre_filtro}']")))
            print(f"Se visualiza aplicado el filtro {nombre_filtro}")
        except TimeoutException:
            print(f"No se logró aplicar el filtro: {nombre_filtro}")

    def ordenar_resultados(self, driver,opcion_ordenar):
        try:
            selector_orden=WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='andes-dropdown__standalone-arrow']")))
            acciones=ActionChains(driver)
            acciones.move_to_element(selector_orden).perform()
            selector_orden.click()
        except TimeoutException:
            print("No se logró encontrar el filtro de 'Ordenar por'")
        try:
            seleccion_opcion=WebDriverWait(driver,8).until(EC.visibility_of_element_located((By.XPATH, f"//ul[contains(@class, 'andes-list')]//li//span[contains(text(), '{opcion_ordenar}')]")))
            driver.execute_script("arguments[0].scrollIntoView(true);", seleccion_opcion)
            print(f"Se filtran los productos por la opción de Ordenar por: {opcion_ordenar}")
            seleccion_opcion.click()
        except TimeoutException:
            print(f"No se logra encontrar el elemento {opcion_ordenar}")
    
    def cookies_mensaje (self, driver,opcion_cookies):
        try:
            WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='cookie-consent-banner-opt-out__actions']")))
            try:
                cerrar_mensaje=WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH, f"//button[@data-testid='action:understood-button' and contains(text(), '{opcion_cookies}')]")))
                cerrar_mensaje.click()
                WebDriverWait(driver, 5).until_not(EC.presence_of_element_located((By.XPATH, "//div[@class='cookie-consent-banner-opt-out__actions']")))
            except TimeoutException:
                print(f"No se encuentra el boton: {opcion_cookies}")
        except TimeoutException:
            print("No se visualiza mensaje de cookies en la pagina")