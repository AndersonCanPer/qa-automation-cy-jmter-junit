# Mercado Libre Automation Test

## Descripción
Automatización de búsqueda de productos en Mercado Libre usando Python, Selenium y Pytest usando el modelo de diseño POM.
Se realiza:

- Selección de país (México)
- Búsqueda de "playstation 5"
- Filtro por condición "Nuevo"
- Filtro por ubicación "CDMX"
- Ordenamiento por "Mayor a menor precio"
- Impresión de los primeros 5 resultados (nombre + precio)

## Instalación

pip install -r requirements.txt

## Ejecución

Para correr la prueba automatizada, abre tu terminal en la raíz del proyecto y ejecuta el comando:

pytest -v -s test_execute.py --html=ReporteHTML.html