# 1.- Carga de Datos:

ventas = [
    {"fecha": "2024-01-01", "producto": "Camisa", "cantidad": 3, "precio": 19.99},
    {"fecha": "2024-01-02", "producto": "Pantalón", "cantidad": 2, "precio": 34.50},
    {"fecha": "2024-01-03", "producto": "Zapatos", "cantidad": 1, "precio": 59.99},
    {"fecha": "2024-01-01", "producto": "Sombrero", "cantidad": 5, "precio": 12.00},
    {"fecha": "2024-01-01", "producto": "Bufanda", "cantidad": 4, "precio": 15.75},
    {"fecha": "2024-01-02", "producto": "Camisa", "cantidad": 2, "precio": 19.99},
    {"fecha": "2024-01-01", "producto": "Zapatos", "cantidad": 1, "precio": 59.99},
    {"fecha": "2024-01-03", "producto": "Sombrero", "cantidad": 3, "precio": 12.00},
    {"fecha": "2024-01-03", "producto": "Bufanda", "cantidad": 2, "precio": 15.75},
    {"fecha": "2024-01-02", "producto": "Pantalón", "cantidad": 1, "precio": 34.50}
]

# 2.- Cálculo de Ingresos Totales:

ingresos_totales = 0.0

for venta in ventas:
    ingresos_venta = venta["cantidad"] * venta["precio"]
    ingresos_totales += ingresos_venta

print(f"Ingresos totales por ventas: ${ingresos_totales:.2f}")

# 3.- Análisis del Producto Más Vendido:
# a)
ventas_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    
    if producto in ventas_por_producto:
        ventas_por_producto[producto] += cantidad
    else:
        ventas_por_producto[producto] = cantidad

for producto, cantidad_total in ventas_por_producto.items():
    print(f"{producto}: {cantidad_total}")

# b)
producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)
cantidad_mas_vendido = ventas_por_producto[producto_mas_vendido]

print(f"El producto con la mayor cantidad total vendida es: {producto_mas_vendido} con {cantidad_mas_vendido} unidades.")

# 4.- Promedio de Precio por Producto
# a)
precios_por_producto = {}

for venta in ventas:
    producto = venta["producto"]
    monto_total = venta["cantidad"] * venta["precio"]
    cantidad = venta["cantidad"]
    
    if producto in precios_por_producto:
        suma_precios, suma_cantidades = precios_por_producto[producto]
        precios_por_producto[producto] = (suma_precios + monto_total, suma_cantidades + cantidad)
    else:
        precios_por_producto[producto] = (monto_total, cantidad)

for producto, datos in precios_por_producto.items():
    print(f"{producto}: Monto total = {datos[0]:.2f}, Cantidad total = {datos[1]}")

# b)
precio_promedio_por_producto = {}
for producto, (suma_precios, suma_cantidades) in precios_por_producto.items():
    precio_promedio = suma_precios / suma_cantidades
    precio_promedio_por_producto[producto] = precio_promedio

for producto, precio_promedio in precio_promedio_por_producto.items():
    print(f"El precio promedio de venta para {producto} es: ${precio_promedio:.2f}")

# 5.- Ventas por Día:
# a)
ingresos_por_dia = {}
for venta in ventas:
    fecha = venta["fecha"]
    ingreso = venta["cantidad"] * venta["precio"]
    
    if fecha in ingresos_por_dia:
        ingresos_por_dia[fecha] += ingreso
    else:
        ingresos_por_dia[fecha] = ingreso

for fecha, ingreso_total in ingresos_por_dia.items():
    print(f"{fecha}: ${ingreso_total:.2f}")


# 6.- Representación de Datos:
resumen_ventas = {}
for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    ingresos = cantidad * venta["precio"]
    
    if producto not in resumen_ventas:
        resumen_ventas[producto] = {
            "cantidad_total": 0,
            "ingresos_totales": 0.0,
            "precio_promedio": 0.0
        }
    
    resumen_ventas[producto]["cantidad_total"] += cantidad
    resumen_ventas[producto]["ingresos_totales"] += ingresos

for producto, datos in resumen_ventas.items():
    datos["precio_promedio"] = datos["ingresos_totales"] / datos["cantidad_total"]

for producto, datos in resumen_ventas.items():
    print(f"{producto}:")
    print(f"  Cantidad total: {datos['cantidad_total']}")
    print(f"  Ingresos totales: ${datos['ingresos_totales']:.2f}")
    print(f"  Precio promedio: ${datos['precio_promedio']:.2f}\n")