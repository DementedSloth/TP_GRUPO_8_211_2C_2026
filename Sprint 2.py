print("\n------ EVALUACIÓN DE INVENTARIO ------\n")

cantidad_consultas = 0
suma_scores = 0
score_maximo = 0
score_minimo = 0
contador_urgente = 0
contador_alta = 0
contador_media = 0
contador_baja = 0
contador_demanda_alta = 0

seguir = True

while seguir:
    cantidad_consultas += 1
    print(f"\n--- Consulta N° {cantidad_consultas} ---")
    print("-INGRESO DE DATOS DEL PRODUCTO")

    nombre = input("Ingrese el nombre del producto: ")

    # Validaciones
    valido = False
    while not valido:
        stock = int(input("Ingrese el stock actual: "))
        if stock >= 0:
            valido = True
        else:
            print("Error: el stock no puede ser negativo.")

    valido = False
    while not valido:
        stock_minimo = int(input("Ingrese el stock minimo: "))
        if stock_minimo > 0:
            valido = True
        else:
            print("Error: el stock mínimo debe ser mayor a 0.")

    valido = False
    while not valido:
        demanda = input("Ingrese la demanda (Baja, Media, Alta): ")
        if demanda == "Baja" or demanda == "Media" or demanda == "Alta":
            valido = True
        else:
            print("Error: ingrese exactamente Baja, Media o Alta. (Respetar mayúsculas).")

    valido = False
    while not valido:
        vencimiento = input("Ingrese el vencimiento (Proximo, No_proximo): ")
        if vencimiento == "Proximo" or vencimiento == "No_proximo":
            valido = True
        else:
            print("Error: ingrese exactamente Proximo o No_proximo.")

    
    
    relacion_stock = f"({stock}/{stock_minimo})"
    cobertura = stock / stock_minimo



    score = 0
    recomendaciones = ""

    # Reglas
    if stock == 0 and demanda == "Alta":
        score += 50
        recomendaciones += "- Reposición de emergencia inmediata.\n"

    if stock < stock_minimo and demanda == "Alta" and vencimiento == "No_proximo":
        score += 40
        recomendaciones += "- Generar orden de compra prioritaria con proveedor.\n"

    if stock < stock_minimo and demanda == "Alta":
        score += 20
        recomendaciones += "- Priorizar reposición en góndola.\n"

    if stock < stock_minimo and demanda == "Media":
        score += 15
        recomendaciones += "- Programar pedido en el lote de la semana.\n"

    if stock < stock_minimo and demanda == "Baja":
        score += 10
        recomendaciones += "- Evaluar si es necesario reponer a corto plazo.\n"

    if stock == stock_minimo and demanda == "Alta":
        score += 10
        recomendaciones += "- Monitorear stock frecuentemente por alta rotación.\n"

    if vencimiento == "Proximo" and stock >= stock_minimo and demanda != "Alta":
        score += 15
        recomendaciones += "- Aplicar descuento o promoción por vencimiento cercano.\n"

    if cobertura > 2 and demanda == "Baja" and vencimiento == "No_proximo":
        score -= 10
        recomendaciones += "- Pausar compras y reevaluar espacio disponible en depósito.\n"

    if stock >= stock_minimo and demanda == "Baja" and vencimiento == "No_proximo":
        recomendaciones += "- Estado estable. No requiere intervención inmediata.\n"

    if recomendaciones == "":
        recomendaciones = "- Sin recomendaciones.\n"



    # Resultado
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
    if vencimiento == "Proximo" and stock == 0:
        oferta = "No hay oferta, sin stock"
    elif vencimiento == "Proximo" and demanda == "Alta":
        oferta = "No, la alta demanda debería agotar el stock antes del vencimiento"
    elif vencimiento == "Proximo" and cobertura > 2:
        oferta = "Sí, oferta muy grande por exceso de stock y vencimiento próximo"
    elif vencimiento == "Proximo" and stock >= stock_minimo:
        oferta = "Sí, hacer oferta por vencimiento próximo"
    elif vencimiento == "Proximo" and stock < stock_minimo and demanda == "Media":
        oferta = "Sí, descuento moderado para liquidar antes del vencimiento"
    elif vencimiento == "Proximo" and stock < stock_minimo and demanda == "Baja":
        oferta = "Sí, descuento grande para liquidar antes del vencimiento"
    elif vencimiento == "No_proximo" and cobertura > 2 and demanda == "Baja":
        oferta = "Sí, promoción para liberar espacio en depósito (sin urgencia de vencimiento)"


    
    print(f"\n-EVALUACIÓN DE INVENTARIO\n"
          f"Producto: {nombre}\n"
          f"Stock: {relacion_stock}\n"
          f"Demanda: {demanda}\n"
          f"Vencimiento: {vencimiento}\n"
          f"Score acumulado: {score}\n"
          f"Resultado General: {resultado_general}\n"
          f"Aviso de Oferta: {oferta}\n"
          f"Recomendaciones generadas:\n{recomendaciones}")
    


    # Actualizar estadísticas
    suma_scores += score

    if cantidad_consultas == 1:
        score_maximo = score
        score_minimo = score
    else:
        if score > score_maximo:
            score_maximo = score
        if score < score_minimo:
            score_minimo = score

    if demanda == "Alta":
        contador_demanda_alta += 1

    if resultado_general == "Reposición urgente":
        contador_urgente += 1
    elif resultado_general == "Prioridad alta":
        contador_alta += 1
    elif resultado_general == "Prioridad media":
        contador_media += 1
    else:
        contador_baja += 1

    # Preguntar si continúa
    repetir = input("\n¿Desea evaluar otro producto? (S/N): ")
    if repetir == "S":
        seguir = True
    else:
        seguir = False



# Estadísticas finales
print("\n------ ESTADÍSTICAS FINALES ------")
print(f"Cantidad de consultas realizadas: {cantidad_consultas}")

promedio_score = suma_scores / cantidad_consultas
print(f"Score promedio: {promedio_score}")
print(f"Score máximo: {score_maximo}")
print(f"Score mínimo: {score_minimo}")

porcentaje_urgente = (contador_urgente / cantidad_consultas) * 100
porcentaje_demanda_alta = (contador_demanda_alta / cantidad_consultas) * 100
print(f"Porcentaje de consultas con Reposición urgente: {porcentaje_urgente}%")
print(f"Porcentaje de consultas con demanda Alta: {porcentaje_demanda_alta}%")



# Gráfico
print("\n--- Gráfico: Resultados por consulta ---")
print(f"Reposición urgente  | {'*' * contador_urgente}")
print(f"Prioridad alta      | {'*' * contador_alta}")
print(f"Prioridad media     | {'*' * contador_media}")
print(f"Prioridad baja      | {'*' * contador_baja}")
