# Ejercicio_2_LV
Ejercicio de APIS 

# Solución 
Se usa Python especificamente la librería requests que permite interactuar con metodos HTTP.

# Lo que hace
Interactua con los metodos GET de la API y se responden las preguntas cin fitros sobre un diccionario de Python.

Se configura un archivo de logs y reporte de resultados.

# Instrucciones para montar ambiente
La versión de Python tiene que ser mayor o igual a 3.10

La libreria requests es de versión 2.32.5

Se debe clonar el repositorio y con CMD abrir la ruta local donde se descargó el proyecto.

        cd C:\Users\USUARIO\Documents\ruta_local\

Para armar un ambiente virtual de python se puede correr los siguientes comandos en un CMD:

        python -m venv venv

        .\venv\Scripts\activate

Para instalar dependencias se corre en CMD:

        pip install -r requirements.txt

Para ejecutarlo se corre el script main.py

        python main.py

# Parametros

Al incio del script dse configura la url base de la API y un diccionario con las claves a filtrar.

También un variable con el límite de registros para visualizar.

# Ejemplo resultado 

    --------------PREGUNTA 1--------------
    20 productos encontrados
    2 productos encontrados con rate = 4.8
    No existe producto con estas caracteristicas: 
        rate = 4.8
        id = 10
        categoria = electronics
        nombre = Silicon Power 256GB SSD 3D NAND A55 SLC Cache performance Boost SATA III 2.5
    --------------PREGUNTA 2--------------
    20 productos encontrados
    6 productos encontrados con categoria = electronics
    1 productos encontrados con categoria = electronics y id 10
    --------------PREGUNTA 3--------------
    3 productos maximo a mostrar
    Producto 1:
        id = 9
        titulo = WD 2TB Elements Portable External Hard Drive - USB 3.0 
        precio = 64
        descripcion = USB 3.0 and USB 2.0 Compatibility Fast data transfers Improve PC Performance High Capacity; Compatibility Formatted NTFS for Windows 10, Windows 8.1, Windows 7; Reformatting may be required for other operating systems; Compatibility may vary depending on user’s hardware configuration and operating system
        categoria = electronics
        imagen = https://fakestoreapi.com/img/61IBBVJvSDL._AC_SY879_t.png
        rating = {'rate': 3.3, 'count': 203}
    Producto 2:
        id = 10
        titulo = SanDisk SSD PLUS 1TB Internal SSD - SATA III 6 Gb/s
        precio = 109
        descripcion = Easy upgrade for faster boot up, shutdown, application load and response (As compared to 5400 RPM SATA 2.5” hard drive; Based on published specifications and internal benchmarking tests using PCMark vantage scores) Boosts burst write performance, making it ideal for typical PC workloads The perfect balance of performance and reliability Read/write speeds of up to 535MB/s/450MB/s (Based on internal testing; Performance may vary depending upon drive capacity, host device, OS and application.)
        categoria = electronics
        imagen = https://fakestoreapi.com/img/61U7T1koQqL._AC_SX679_t.png
        rating = {'rate': 2.9, 'count': 470}
    Producto 3:
        id = 11
        titulo = Silicon Power 256GB SSD 3D NAND A55 SLC Cache Performance Boost SATA III 2.5
        precio = 109
        descripcion = 3D NAND flash are applied to deliver high transfer speeds Remarkable transfer speeds that enable faster bootup and improved overall system performance. The advanced SLC Cache Technology allows performance boost and longer lifespan 7mm slim design suitable for Ultrabooks and Ultra-slim notebooks. Supports TRIM command, Garbage Collection technology, RAID, and ECC (Error Checking & Correction) to provide the optimized performance and enhanced reliability.
        categoria = electronics
        imagen = https://fakestoreapi.com/img/71kWymZ+c+L._AC_SX679_t.png
        rating = {'rate': 4.8, 'count': 319}
