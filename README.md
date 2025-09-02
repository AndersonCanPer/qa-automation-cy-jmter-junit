# QA Automation con Cypress, JMeter y JUnit

Este proyecto contiene pruebas automatizadas usando diferentes tecnologías:
- **Cypress** → pruebas E2E de interfaz gráfica.
- **JMeter** → pruebas de rendimiento.
- **JUnit** → pruebas unitarias en Java con Maven.
- **Selenium (Python)** → pruebas de UI automatizadas
  
## Requisitos previos

- [Node.js](https://nodejs.org/) y npm  
- [Java 17+](https://adoptium.net/)  
- [Apache Maven](https://maven.apache.org/)  
- [JMeter](https://jmeter.apache.org/) (opcional si quieres ejecutar pruebas de carga localmente)

## Ejecución de pruebas

# Cypress (pruebas E2E)

Instalar dependencias
npm install

Ejecutar pruebas en consola
npx cypress run

(Opcional) Abrir interfaz gráfica de Cypress
npx cypress open

# JUnit (pruebas unitarias con Maven)
Asegúrate de tener Java 17+ y Maven instalados.

Ejecutar pruebas unitarias:
mvn clean test

# JMeter (pruebas de rendimiento)

Abre JMeter y carga el archivo:
./jmeter/mi-prueba.jmx

Para ejecutarlo en modo consola:
jmeter -n -t ./jmeter/mi-prueba.jmx -l ./reportes/resultados.jtl

# Selenium (pruebas UI)
pip install -r requirements.txt

Para correr la prueba automatizada, abre tu terminal en la raíz del proyecto y ejecuta el comando:
pytest -v -s test_execute.py --html=ReporteHTML.html

## Integración Continua (CI)

Este proyecto usa GitHub Actions para ejecutar pruebas automáticamente en cada push.
Mira los workflows en .github/workflows/.

## Autores

Anderson Cancelada Pérez
