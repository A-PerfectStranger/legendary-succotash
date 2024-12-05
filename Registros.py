import csv
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

ciudades = ['Quito', 'Riobamba', 'Cuenca', 'Loja']
representantes = ['Sofía Morales', 'Camila Rojas', 'Alejandro Vargas', 'Sebastián Méndez', 'Andrea Castillo']
marcas = ['Toyota', 'Honda', 'Ford', 'Nissan', 'Chevrolet', 'BMW']
categorias = ['Automovil', 'SUV', 'Camioneta']
valor_min = 12800
valor_max = 42500

def generar_fecha_aleatoria(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)


start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)


registros = []
for _ in range(100):
    fecha_venta = generar_fecha_aleatoria(start_date, end_date).strftime('%Y-%m-%d')
    
    ciudad = random.choice(ciudades)
    
    representante = random.choice(representantes)
    
    marca = random.choice(marcas)
    
    categoria = random.choice(categorias)
    
    valor_vehiculo = round(random.uniform(valor_min, valor_max), 2)
    
    registros.append([fecha_venta, ciudad, representante, marca, categoria, valor_vehiculo])



with open('transacciones_vehiculos.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Fecha_Venta', 'Ciudad', 'Representante', 'Marca', 'Categoria', 'Valor_Vehiculo'])
    writer.writerows(registros)

print("Archivo 'transacciones_vehiculos.csv' generado exitosamente.")
