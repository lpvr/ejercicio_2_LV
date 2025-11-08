import requests
import logging

url = "https://fakestoreapi.com/products/"
patron_busqueda = {
    'rate' : 4.8,
    'id': 10,
    'categoria': 'electronics',
    'nombre': 'Silicon Power 256GB SSD 3D NAND A55 SLC Cache performance Boost SATA III 2.5'
}
limite_visualizacion = 3

# Función para logs
def configurar_logs():
    logging.basicConfig(
        filename='reporte_novedades.txt',
        filemode='a',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

def print_log_info(valor):
    logging.info(valor)
    print(valor)

def print_log_error(valor):
    logging.error(valor)
    print(valor)

def validacion_uno():
    '''
    Obtener todos los productos de su tienda y validar que uno de sus productos
    estrellas con un rate de 4.8, tenga el id 10, su categoria corresponda con
    electronics y que su título coincida con
    “Silicon Power 256GB SSD 3D NAND A55 SLC Cache performance Boost SATA III 2.5
    '''

    configurar_logs()
    print_log_info(f'--------------PREGUNTA 1--------------')
    resp = requests.get(url)
    if resp.status_code == 200:
        productos = resp.json()
        print_log_info(f'{len(productos)} productos encontrados')
    else:
        print_log_info(f'Metodo API no responde')

    # Parametros de busqueda
    rate = patron_busqueda['rate']
    id = patron_busqueda['id']
    categoria = patron_busqueda['categoria']
    nombre = patron_busqueda['nombre']
    filtrados = [p for p in productos if p['rating']['rate'] == rate]
    if len(filtrados) > 0:
        print_log_info(f'{len(filtrados)} productos encontrados con rate = {rate}')
        filtrados = [p for p in filtrados if p['id'] == id]
        if len(filtrados) > 0:
            print_log_info(f'{len(filtrados)} productos encontrados con rate = {rate} y id = {id}')
            filtrados = [p for p in filtrados if p['category'] == categoria]
            if len(filtrados) > 0:
                print_log_info(f'{len(filtrados)} productos encontrados con rate = {rate}, id = {id} y categoria = {categoria}')
                filtrados = [p for p in filtrados if p['title'].lower() == nombre.lower()]
                if len(filtrados) > 0:
                    print_log_info(
                        f'Si existe el producto con rate = {rate}, id = {id}, categoria = {categoria} y nombre = {nombre}')
                else:
                    print_log_info(
                        f'No existe producto con estas caracteristicas: \n\trate = {rate}\n\tid = {id}\n\tcategoria = {categoria}\n\tnombre = {nombre}')
            else:
                print_log_info(
                    f'No existe producto con estas caracteristicas: \n\trate = {rate}\n\tid = {id}\n\tcategoria = {categoria}\n\tnombre = {nombre}')
        else:
            print_log_info(
                f'No existe producto con estas caracteristicas: \n\trate = {rate}\n\tid = {id}\n\tcategoria = {categoria}\n\tnombre = {nombre}')
    else:
        print_log_info(f'No existe producto con estas caracteristicas: \n\trate = {rate}\n\tid = {id}\n\tcategoria = {categoria}\n\tnombre = {nombre}')


def validacion_dos():
    '''
    Luego necesita validar que en el catalogo de productos, cuantos busca
    por categoría electronics, venga 6 productos en total y que este el producto con id 10
    '''

    configurar_logs()
    print_log_info(f'--------------PREGUNTA 2--------------')
    resp = requests.get(url)
    if resp.status_code == 200:
        productos = resp.json()
        print_log_info(f'{len(productos)} productos encontrados')
    else:
        print_log_info(f'Metodo API no responde')

    # Parametros de busqueda
    categoria = patron_busqueda['categoria']
    id = patron_busqueda['id']
    filtrados = [p for p in productos if p['category'] == categoria]
    if len(filtrados) == 6:
        print_log_info(f'{len(filtrados)} productos encontrados con categoria = {categoria}')
        filtrados = [p for p in productos if p['id'] == id]
        if len(filtrados) > 0:
            print_log_info(f'{len(filtrados)} productos encontrados con categoria = {categoria} y id {id}')
        else:
            print_log_info(
                f'No existe producto de categoria = {categoria} & id = {id}')

    else:
        print_log_info(
            f'No existen 6 productos de categoria = {categoria}')



def validacion_tres():
    '''
    Visualizar los productos  por catagoría electronics,
    pero que solo pueda ver en la busqueda hasta 3 resultados cómo límite
    '''

    configurar_logs()
    print_log_info(f'--------------PREGUNTA 3--------------')
    resp = requests.get(url + 'category/electronics?limit=3')
    if resp.status_code == 200:
        productos = resp.json()
        print_log_info(f'{len(productos)} productos maximo a mostrar')
        for i, p in enumerate(productos):
            print_log_info(f'Producto {i + 1}:')
            print_log_info(f'\tid = {p["id"]}\n\ttitulo = {p["title"]}\n\tprecio = {p["price"]}\n\tdescripcion = {p["description"]}\n\tcategoria = {p["category"]}\n\timagen = {p["image"]}\n\trating = {p["rating"]}')

    else:
        print_log_info(f'Metodo API no responde')

def main():
    validacion_uno()
    validacion_dos()
    validacion_tres()

if __name__ == "__main__":
    app = main()