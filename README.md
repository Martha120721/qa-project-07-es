# Proyecto 7
- Martha Veronica Sanchez Marquez
- Cohort 07
# Pruebas de comprobacion de funcionalidad de aplicacion Urban Routes[]
- Para estas pruebas se utilizarán Python, pytest, Selenium y Chrome.
- Necesitas tener instalado el paquete "selenium web driver (version 4.18.1)"para ejecutar las pruebas.
- - Instalar pytest:
- 1-Abre la terminal o consola.
- 2-Ingresa el comando "pip install pytest".
- Instalar drivers Selenium
- 1-Descargar los drivers deacuerdo a tu navegador.
- 2-Descomprime el archivo. Crea una carpeta llamada WebDriver/bin y guarda el archivo allí.
- 3-Agrega la ruta a bin a la variable de entorno PATH. El algoritmo depende del sistema operativo.
- Instalacion de Selenium Web Driver
- 1- Abrir la Consola o Terminal Terminal desde las aplicaciones o usando el buscador de aplicaciones.
- 2-Escribe el siguiente comando para instalar el paquete de Selenium "pip install selenium".
- 3-Una vez que la instalación esté completa, es una buena práctica verificar que el paquete se haya instalado correctamente.
- 4-Ahora abre un proyecto en PyCharm. 
- Importa el paquete Selenium WebDriver: "from selenium import webdriver"
- 5-Ahora podemos asegurarnos de que Selenium está conectado.
- Para hacerlo, necesitas ejecutar un código. 
- 6-Busca el archivo connect_selenium_in_pycharm.py y ábrelo en PyCharm.
- 7-Ejecuta todas las pruebas con el comando pytest folder/de/proyecto.
- 
- En este proyecto se realizarán pruebas automatizadas para combrobar la funcionalidad de la aplicación: Urban Routes.
- Se utilizará la aplicacion Urban Routes para cubrir el proceso completo al solicitar un taxi.
- Las pruebas de confirmacion que se realizarán son las siguientes:
- 1- Configurar la dirección.
- 2- Seleccionar la tarifa Comfort.
- 3- Rellenar el número de teléfono.
- 4- Agregar una tarjeta de crédito. (Consejo: el botón 'link' (enlace) no se activa hasta que el campo CVV de la tarjeta en el modal 'Agregar una tarjeta', id="code" class="card-input", pierde el enfoque. Para cambiar el enfoque, puedes simular que el usuario o usuaria presiona TAB o hace clic en otro lugar de la pantalla). El repositorio tiene preparada la función retrieve_phone_code() que intercepta el código de confirmación requerido para agregar una tarjeta.
- 5- Escribir un mensaje para el controlador.
- 6- Pedir una manta y pañuelos.
- 7- Pedir 2 helados.
- 8- Aparece el modal para buscar un taxi.

- 