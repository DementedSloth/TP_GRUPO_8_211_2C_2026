print("\n------ EVALUACIÓN DE INVENTARIO ------\n")

# Input
print("-INGRESO DE DATOS DEL PRODUCTO")

nombre = input("Ingrese el nombre del producto: ")
stock = int(input("Ingrese el stock actual: "))
stock_minimo = int(input("Ingrese el stock minimo: "))
demanda = input("Ingrese la demanda (Baja, Media, Alta): ")
vencimiento = input("Ingrese el vencimiento (Proximo, No_proximo): ")
#
relacion_stock = f"({stock}/{stock_minimo})"
#
score = 0
recomendaciones = ""

# Reglas

# Sin stock, demanda alta, vence pronto
if stock == 0 and demanda == "Alta" and vencimiento == "Proximo":
    score += 50
    recomendaciones += "- Reposición de emergencia inmediata y liquidar saldo por vencimiento.\\n"
# Falta stock, demanda alta, vencimiento largo
if stock < stock_minimo and demanda == "Alta" and vencimiento == "No_proximo":
    score += 40
    recomendaciones += "- Generar orden de compra prioritaria con proveedor.\n"
# Falta stock con demanda alta
if stock < stock_minimo and demanda == "Alta":
    score += 20
    recomendaciones += "- Priorizar reposición en góndola.\n"
# Falta stock con demanda media
if stock < stock_minimo and demanda == "Media":
    score += 15
    recomendaciones += "- Programar pedido en el lote de la semana.\n"
# Falta stock con demanda baja
if stock < stock_minimo and demanda == "Baja":
    score += 10
    recomendaciones += "- Evaluar si es necesario reponer a corto plazo.\n"
# Hay stock pero mucha demanda (para estar atentos)
if stock = stock_minimo and demanda == "Alta":
score += 10 recomendaciones += "- Monitorear stock frecuentemente por alta rotación.\n"
# Vence pronto pero hay stock
if vencimiento == "Proximo" and stock >= stock_minimo and demanda != "Alta":
    score += 15 recomendaciones += "- Aplicar descuento o promoción por vencimiento cercano.\n"
# Demasiado stock (2 veces el mínimo) y poca demanda
if stock > (stock_minimo \* 2) and demanda == "Baja" and vencimiento == "No_proximo":
    score -= 10 recomendaciones += "- Pausar compras y reevaluar espacio disponible en depósito.\n"
# Hay stock, demanda baja y vencimiento largo
if stock >= stock_minimo and demanda == "Baja" and vencimiento == "No_proximo":
recomendaciones += "- Estado estable. No requiere intervención inmediata.\n"


# Score
if score >= 70:
    resultado_general = "Reposición urgente"
elif score >= 40:
    resultado_general = "Prioridad alta"
elif score >= 20:
    resultado_general = "Prioridad media"
else:
    resultado_general = "Prioridad baja"


# Oferta
oferta = "No"
if vencimiento == "Proximo":
    oferta = "Sí, hacer oferta por vencimiento próximo"


# Resultados
if recomendaciones == "":
    recomendaciones += "- Sin recomendaciones."
print(f"\n-EVALUACIÓN DE INVENTARIO\n"
    f"Producto: {nombre}\n"
    f"Stock: {relacion_stock}\n"
    f"Demanda: {demanda}\n"
    f"Vencimiento: {vencimiento}\n"
    f"Score acumulado: {score}\n"
    f"Resultado General: {resultado_general}\n"
    f"Aviso de Oferta: {oferta}\n"
    f"Recomendaciones generadas: {recomendaciones}\n")

