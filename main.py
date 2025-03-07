from datetime import datetime

# Listas de palabras clave para el análisis
PALABRAS_POSITIVAS = [
    "excelente",
    "muy buena",
    "fantástica",
    "increíble",
    "destacado",
    "sobresaliente",
    "ideal",
    "perfecta",
]
PALABRAS_NEGATIVAS = [
    "malo",
    "deficiente",
    "decepcionante",
    "pésimo",
    "terrible",
    "insuficiente",
]
PALABRAS_NEUTRALES = ["normal", "ok", "regular", "común"]


def obtener_rating(comentario: str) -> int:
    # Desarrollar
    #definimos variables
    palabra_positiva = 0
    palabra_negativa = 0
    palabra_neutra = 0
    #colocamos los comentarios en minuscula, eliminamos los simbolos de putuacion y se separa en cada espacio en blanco " "
    comentario = comentario.lower().replace(",","").replace(".","").split(" ")
    for palabra in comentario:
        if palabra in PALABRAS_POSITIVAS:
            palabra_positiva += 1
        elif palabra in PALABRAS_NEGATIVAS:
            palabra_negativa += 1
        elif palabra in PALABRAS_NEUTRALES:
            palabra_neutra += 1
    if palabra_positiva > palabra_negativa and palabra_positiva > palabra_neutra:
        rating = 3
    elif palabra_negativa > palabra_positiva and palabra_negativa > palabra_neutra:
        rating = 1
    else:
        rating = 2
    return rating



def procesar_linea(linea: str) -> dict:
    # Desarrollar
    datos = linea.strip().split(";")
    review_id_str, nombre, email, producto, fecha, comentario = datos
    #se verifica que el id se pueda convertir a entero y si es positivo
    try:
        review_id = int(review_id_str)
        if review_id <= 0:
            raise ValueError ("Valor de id menor a 0")
    except ValueError:
        raise ValueError ("El id debe ser un número entero")
    #se verifica que el nombre del cliente no esté en blanco
    if nombre == "":
        raise ValueError ("Escriba su nombre completo")
    #se verifica que en el email haya un "@"
    if "@" not in email:
        raise ValueError (f"Email no válido: {email}")
    #se verifica que el nombre del producto no esté en blanco
    if producto == "":
        raise ValueError ("El nombre del producto no puede estar en blanco")
    #se verifica que el formato de la fecha sea DD-MM-YYYY
    try:
        datetime.strptime(fecha, "%d-%m-%Y")
    except Exception:
        raise ValueError (f"Formato de fecha inválido: {fecha} no corresponde a DD-MM-YYYY")
    #se verifica que se haya escrito un comentario sobre el producto
    if comentario == "":
        raise ValueError ("Debe agregar un comentario sobre el producto")
        
            
    #Si todos los datos son válidos se agregan a un diccionario
    reseña = {"review_id": review_id,
                "nombre": nombre,
                "email": email,
                "producto": producto,
                "fecha": fecha,
                "comentario": comentario,
                "rating": obtener_rating(comentario)
        }
    return reseña
    


def leer_reseñas(ruta_archivo: str) -> list:
    # Desarrollar
    linea_procesada = 0
    reseñas = []
    try:
        with open("customer_reviews.txt", "r", encoding="utf-8") as archivo:
            #se lee cada linea del archivo, se registra la lectura y si es procesada sin errores se agrega a "reseñas"
            for linea in archivo:
                linea_procesada += 1
                try:
                    reseñas.append(procesar_linea(linea))
                except ValueError as e:
                    print(f"Error en línea {linea_procesada}: {e}")
                    #se imprime el error que evitó el registro de la reseña
    except FileNotFoundError:
        print("Archivo no encontrado")
    return reseñas



def agrupar_por_producto(reseñas: list) -> dict:
    # Desarrollar
    total_reseñas_sx = 0
    total_reseñas_lb = 0
    total_reseñas_lp = 0
    suma_rating_sx = 0
    suma_rating_lb = 0
    suma_rating_lp = 0
    rating_1_sx = 0
    rating_2_sx = 0
    rating_3_sx = 0
    rating_1_lb = 0
    rating_2_lb = 0
    rating_3_lb = 0
    rating_1_lp = 0
    rating_2_lp = 0
    rating_3_lp = 0
    #para cada reseña se verifica de qué producto se trata 
    for reseña in reseñas:
        if reseña["producto"] == "Smartphone X":
            #se incrementa el numero de reseñas hechas para el producto
            total_reseñas_sx += 1
            #sumatoria de los ratings 
            suma_rating_sx += reseña["rating"]
            #cálculo del promedio del rating del producto
            promedio_rating = float(suma_rating_sx/total_reseñas_sx)
            if reseña["rating"] == 1:
                rating_1_sx += 1
            elif reseña["rating"] == 2:
                rating_2_sx += 1
            else:
                rating_3_sx += 1
            #se almacena en un diccionario la información obtenida del producto
            smartphone_x = {"total_reseñas": total_reseñas_sx,
                            "promedio_rating": round(promedio_rating,2),
                            "rating_1": rating_1_sx,
                            "rating_2": rating_2_sx,
                            "rating_3": rating_3_sx}
        elif reseña["producto"] == "Laptop Basic":
            total_reseñas_lb += 1
            suma_rating_lb += reseña["rating"]
            promedio_rating = float(suma_rating_lb/total_reseñas_lb)
            if reseña["rating"] == 1:
                rating_1_lb += 1
            elif reseña["rating"] == 2:
                rating_2_lb += 1
            else:
                rating_3_lb += 1
            laptop_basic = {"total_reseñas": total_reseñas_lb,
                            "promedio_rating": round(promedio_rating,2),
                            "rating_1": rating_1_lb,
                            "rating_2": rating_2_lb,
                            "rating_3": rating_3_lb}
        elif reseña["producto"] == "Laptop Pro":
            total_reseñas_lp += 1
            suma_rating_lp += reseña["rating"]
            promedio_rating = float(suma_rating_lp/total_reseñas_lp)
            if reseña["rating"] == 1:
                rating_1_lp += 1
            elif reseña["rating"] == 2:
                rating_2_lp += 1
            else:
                rating_3_lp += 1
            laptop_pro = {"total_reseñas": total_reseñas_lp,
                            "promedio_rating": round(promedio_rating,2),
                            "rating_1": rating_1_lp,
                            "rating_2": rating_2_lp,
                            "rating_3": rating_3_lp}
    datos_producto ={"Smartphone X": smartphone_x,
            "Laptop Basic": laptop_basic,
            "Laptop Pro": laptop_pro
            }
    return datos_producto


def generar_lista_seguimiento(reseñas: list) -> list:
    # Desarrollar
    lista_seguimiento = []
    for reseña in reseñas:
        if reseña["rating"] == 1:
            lista_seguimiento.append(reseña)
    return lista_seguimiento



def escribir_reporte_integral(datos: dict, ruta_salida: str):
    # Desarrollar
    try:
        with open("reporte_integral.txt", "w", encoding="utf-8") as reporte_integral:
            for producto in datos.keys():
                info_producto = datos.get(producto)
                reporte_integral.write(f"\nProducto: {producto}\n Total de reseñas: {info_producto.get("total_reseñas")}\n Promedio de Rating: {info_producto.get("promedio_rating")}\n Reseñas con Rating 1: {info_producto.get("rating_1")}\n Reseñas con Rating 2: {info_producto.get("rating_2")}\n Reseñas con Rating 3: {info_producto.get("rating_3")}\n")
            return reporte_integral
    except FileNotFoundError:
        print("Error: el archivo 'reporte_integral.txt 'no se encontró")


def escribir_reporte_seguimiento(lista: list, ruta_salida: str):
    # Desarrollar
    smartphone_x = []
    laptop_basic = []
    laptop_pro = []
    for reseña in lista:
        if reseña.get("producto") == "Smartphone X":
            smartphone_x.append(reseña)
        if reseña.get("producto") == "Laptop Basic":
            laptop_basic.append(reseña)
        if reseña.get("producto") == "Laptop Pro":
            laptop_pro.append(reseña)
    try:
        with open("reporte_seguimiento.txt", "w", encoding="utf-8") as reporte_seguimiento:
            reporte_seguimiento.write("\nProducto: Smartphone X\n") 
            for rsña_sx in smartphone_x:
                reporte_seguimiento.write(f"Cliente: {rsña_sx.get("nombre")}, Email: {rsña_sx.get("email")}, Fecha: {rsña_sx.get("fecha")}, Comentario: {rsña_sx.get("comentario")}\n")
            reporte_seguimiento.write("\nProducto: Laptop Basic\n")
            for rsña_lb in laptop_basic:
                reporte_seguimiento.write(f"Cliente: {rsña_lb.get("nombre")}, Email: {rsña_lb.get("email")}, Fecha: {rsña_lb.get("fecha")}, Comentario: {rsña_lb.get("comentario")}\n")
            reporte_seguimiento.write("\nProducto: Laptop Pro\n")
            for rsña_lp in laptop_pro:
                reporte_seguimiento.write(f"Cliente: {rsña_lp.get("nombre")}, Email: {rsña_lp.get("email")}, Fecha: {rsña_lp.get("fecha")}, Comentario: {rsña_lp.get("comentario")}\n")
            #print(reporte_seguimiento)
            return reporte_seguimiento
    except FileNotFoundError:
        print("Error: el archivo 'reporte_seguimiento.txt' no se encontró")




def main():
    ruta_archivo = "customer_reviews.txt"
    reseñas = leer_reseñas(ruta_archivo)
    if not reseñas:
        print("No se han leído reseñas válidas.")
        return

    datos_producto = agrupar_por_producto(reseñas)
    lista_seguimiento = generar_lista_seguimiento(reseñas)

    escribir_reporte_integral(datos_producto, "reporte_integral.txt")
    escribir_reporte_seguimiento(lista_seguimiento, "reporte_seguimiento.txt")

    print(
        "Procesamiento completado. Se han generado 'reporte_integral.txt' y 'reporte_seguimiento.txt'."
    )


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Ocurrió un error durante el procesamiento: {e}")
