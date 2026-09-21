print("\n------ EVALUACIÓN DE INVENTARIO ------\n")

# ENTRADA DE DATOS
print("-INGRESO DE DATOS DEL PRODUCTO")

nombre = input("Ingrese el nombre del producto: ")
stock = int(input("Ingrese el stock actual: "))
stock_minimo = int(input("Ingrese el stock minimo: "))
demanda = input("Ingrese la demanda (Baja, Media, Alta): ")
vencimiento = input("Ingrese el vencimiento (Proximo, No_proximo): ")

# RELACIÓN STOCK 
relacion_stock = f"({stock}/{stock_minimo})"


# VARIABLES
score = 0
recomendaciones = ""


# REGLAS

# 1: Demanda alta y vencimiento próximo
if stock == 0 and demanda == "Alta" and vencimiento == "Proximo":
    score += 50
    recomendaciones += "-Reposición de emergencia inmediata y liquidar por vencimiento.\n"

# 3: Stock menor al mínimo y demanda alta
if stock < stock_minimo and demanda == "Alta":
    score += 20
    recomendaciones += "-Priorizar reposición en góndola.\n"

# 4: Stock bajo el mínimo y demanda media
if stock < stock_minimo and demanda == "Media":
    score += 15
    recomendaciones += "-Programar pedido en el lote de la semana.\n"

# 5: Stock bajo el mínimo y demanda baja
if stock < stock_minimo and demanda == "Baja":
    score += 10
    recomendaciones += "-Programar pedido en el lote de la semana.\n"

# 6: Stock suficiente pero demanda alta
if stock >= stock_minimo and demanda == "Alta":
    score += 10
    recomendaciones += "-Monitorear stock frecuentemente por alta demanda.\n"

# 7: Vencimiento próximo con stock suficiente
if vencimiento == "Proximo" and stock >= stock_minimo and demanda != "Alta":
    score += 15
    recomendaciones += "-Aplicar descuento o promoción por vencimiento cercano.\n"

# 8: Demasiado stock (el doble del stock mínimo) y demanda baja
if stock > (stock_minimo * 2) and demanda == "Baja" and vencimiento == "No_proximo":
    score -= 10
    recomendaciones += "-Pausar compras y evaluar espacio disponible en depósito.\n"

# 9: Situación estable
if stock >= stock_minimo and demanda == "Baja" and vencimiento == "No_proximo":
    recomendaciones += "-Estado estable. No requiere intervención inmediata.\\n"


# SCORE FINAL
if score >= 70:
    resultado_general = "Reposición urgente"
elif score >= 40:
    resultado_general = "Prioridad alta"
elif score >= 20:
    resultado_general = "Prioridad media"
else:
    resultado_general = "Prioridad baja"


# EVALUACIÓN DE OFERTA
oferta = "No"
if vencimiento == "Proximo":
    oferta = "Sí, hacer oferta por vencimiento próximo"


# RESULTADOS
if recomendaciones == "":
    recomendaciones += "- Sin recomendaciones específicas."
print(f"\n-EVALUACIÓN DE INVENTARIO\n"
    f"Producto: {nombre}\n"
    f"Stock: {relacion_stock}\n"
    f"Demanda: {demanda}\n"
    f"Vencimiento: {vencimiento}\n"
    f"Score acumulado: {score}\n"
    f"Resultado General: {resultado_general}\n"
    f"Aviso de Oferta: {oferta}\n"
    f"Recomendaciones generadas: {recomendaciones}\n")

