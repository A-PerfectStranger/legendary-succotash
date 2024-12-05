import csv
import random
from faker import Faker
from datetime import datetime, timedelta

# Inicializar el generador de datos falsos
fake = Faker()

# Listas de datos posibles
ciudades = ['Quito', 'Riobamba', 'Cuenca', 'Loja']
representantes = ['Quito_Rep_1', 'Quito_Rep_2', 'Riobamba_Rep', 'Cuenca_Rep', 'Loja_Rep']
marcas = ['Toyota', 'Honda', 'Ford', 'Nissan', 'Chevrolet', 'BMW']
categorias = ['Automovil', 'SUV', 'Camioneta']
valor_min = 12800
valor_max = 42500

# Función para generar fecha aleatoria
def generar_fecha_aleatoria(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

# Fechas de inicio y fin (formato datetime)
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

# Generar 100 registros de transacciones
registros = []
for _ in range(100):
    # Fecha aleatoria entre el 1 de enero de 2023 y el 31 de diciembre de 2023
    fecha_venta = generar_fecha_aleatoria(start_date, end_date).strftime('%Y-%m-%d')
    
    # Ciudad aleatoria
    ciudad = random.choice(ciudades)
    
    # Representante de ventas aleatorio
    representante = random.choice(representantes)
    
    # Marca de vehículo aleatoria
    marca = random.choice(marcas)
    
    # Categoría de vehículo aleatoria
    categoria = random.choice(categorias)
    
    # Valor aleatorio del vehículo entre 12,800 y 42,500 USD
    valor_vehiculo = round(random.uniform(valor_min, valor_max), 2)
    
    # Agregar el registro a la lista
    registros.append([fecha_venta, ciudad, representante, marca, categoria, valor_vehiculo])

# Escribir los registros en un archivo CSV
with open('transacciones_vehiculos.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Escribir los encabezados
    writer.writerow(['Fecha_Venta', 'Ciudad', 'Representante', 'Marca', 'Categoria', 'Valor_Vehiculo'])
    # Escribir los datos
    writer.writerows(registros)

print("Archivo 'transacciones_vehiculos.csv' generado exitosamente.")
