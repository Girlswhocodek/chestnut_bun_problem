
"""
Problema del Dorayaki (栗まんじゅう問題) - Crecimiento exponencial
Basado en el episodio de Doraemon con la "Baibain" que duplica objetos cada 5 minutos
"""

import math
import matplotlib.pyplot as plt

# Constantes y volúmenes de referencia (en metros cúbicos)
VOLUMEN_DORAYAKI = 0.00015  # Aprox. 150 cm³ por dorayaki (5cm x 5cm x 6cm)
VOLUMEN_SISTEMA_SOLAR = 3.69e38  # Volumen aproximado del Sistema Solar
VOLUMEN_TOKYO_DOME = 1.24e6  # 1,240,000 m³
VOLUMEN_CANICA = 0.0000001  # Aprox. 1 cm³ para una canica pequeña
VOLUMEN_PELOTA_FUTBOL = 0.0056  # Aprox. 5600 cm³ para pelota estándar

# Tiempo de duplicación de la Baibain (5 minutos en segundos)
TIEMPO_DUPLICACION = 5 * 60  # 300 segundos

def calcular_tiempo_para_volumen(volumen_objetivo, volumen_inicial, tiempo_duplicacion=TIEMPO_DUPLICACION):
    """
    Calcula el tiempo necesario para que un objeto duplicándose alcance un volumen objetivo.
    
    Parameters:
    volumen_objetivo (float): Volumen objetivo en m³
    volumen_inicial (float): Volumen inicial en m³
    tiempo_duplicacion (int): Tiempo entre duplicaciones en segundos
    
    Returns:
    tuple: (minutos_total, duplicaciones_necesarias, datos_evolucion)
    """
    if volumen_inicial <= 0 or volumen_objetivo <= volumen_inicial:
        return 0, 0, []
    
    # Calcular número de duplicaciones necesarias: volumen_objetivo = volumen_inicial * 2^n
    duplicaciones_necesarias = math.ceil(math.log2(volumen_objetivo / volumen_inicial))
    tiempo_total_segundos = duplicaciones_necesarias * tiempo_duplicacion
    tiempo_total_minutos = tiempo_total_segundos / 60
    tiempo_total_horas = tiempo_total_minutos / 60
    tiempo_total_dias = tiempo_total_horas / 24
    
    # Generar datos de evolución para gráficos
    datos_evolucion = []
    for n in range(duplicaciones_necesarias + 1):
        tiempo_actual = n * tiempo_duplicacion
        volumen_actual = volumen_inicial * (2 ** n)
        datos_evolucion.append((tiempo_actual / 60, volumen_actual, n))  # Tiempo en minutos
    
    return tiempo_total_minutos, duplicaciones_necesarias, datos_evolucion

def problema_dorayaki_sistema_solar():
    """Resuelve el problema principal: dorayaki cubriendo el Sistema Solar"""
    print("=" * 70)
    print("PROBLEMA DEL DORAYAKI: ¿CUÁNTO PARA CUBRIR EL SISTEMA SOLAR?")
    print("=" * 70)
    
    tiempo_minutos, duplicaciones, datos = calcular_tiempo_para_volumen(
        VOLUMEN_SISTEMA_SOLAR, VOLUMEN_DORAYAKI
    )
    
    tiempo_horas = tiempo_minutos / 60
    tiempo_dias = tiempo_horas / 24
    
    print(f"🍙 VOLÚMENES DE REFERENCIA:")
    print(f"• 1 Dorayaki: {VOLUMEN_DORAYAKI:.2e} m³")
    print(f"• Sistema Solar: {VOLUMEN_SISTEMA_SOLAR:.2e} m³")
    print(f"• Relación: {VOLUMEN_SISTEMA_SOLAR/VOLUMEN_DORAYAKI:.2e} veces mayor")
    
    print(f"\n⏰ RESULTADOS:")
    print(f"• Duplicaciones necesarias: {duplicaciones}")
    print(f"• Tiempo total: {tiempo_minutos:,.0f} minutos")
    print(f"• Tiempo total: {tiempo_horas:,.1f} horas")
    print(f"• Tiempo total: {tiempo_dias:,.1f} días")
    
    # Puntos intermedios interesantes
    puntos_interes = [
        ("Canica", VOLUMEN_CANICA),
        ("Pelota de fútbol", VOLUMEN_PELOTA_FUTBOL),
        ("Tokyo Dome", VOLUMEN_TOKYO_DOME),
        ("Tierra", 1.08321e21),  # Volumen de la Tierra
        ("Sol", 1.41e27),        # Volumen del Sol
    ]
    
    print(f"\n📊 PUNTOS INTERMEDIOS:")
    for nombre, volumen in puntos_interes:
        if volumen > VOLUMEN_DORAYAKI:
            tiempo, dup, _ = calcular_tiempo_para_volumen(volumen, VOLUMEN_DORAYAKI)
            print(f"• {nombre}: {tiempo:,.0f} min ({dup} duplicaciones)")
    
    return tiempo_minutos, duplicaciones, datos

def problema_tokyo_dome_pelota():
    """Ejemplo adicional: pelota de fútbol llenando el Tokyo Dome"""
    print("\n" + "=" * 70)
    print("PROBLEMA ADICIONAL: PELOTA DE FÚTBOL EN TOKYO DOME")
    print("=" * 70)
    
    tiempo_minutos, duplicaciones, datos = calcular_tiempo_para_volumen(
        VOLUMEN_TOKYO_DOME, VOLUMEN_PELOTA_FUTBOL
    )
    
    print(f"⚽ VOLÚMENES:")
    print(f"• Pelota de fútbol: {VOLUMEN_PELOTA_FUTBOL:.2e} m³")
    print(f"• Tokyo Dome: {VOLUMEN_TOKYO_DOME:.2e} m³")
    
    print(f"\n⏰ RESULTADOS:")
    print(f"• Duplicaciones necesarias: {duplicaciones}")
    print(f"• Tiempo total: {tiempo_minutos:,.0f} minutos")
    print(f"• Tiempo total: {tiempo_minutos/60:,.1f} horas")
    
    return tiempo_minutos, duplicaciones, datos

def problema_generico(objeto_nombre, volumen_objetivo, volumen_inicial):
    """Función genérica para cualquier objeto y volumen objetivo"""
    print("\n" + "=" * 70)
    print(f"PROBLEMA GENÉRICO: {objeto_nombre.upper()}")
    print("=" * 70)
    
    tiempo_minutos, duplicaciones, datos = calcular_tiempo_para_volumen(
        volumen_objetivo, volumen_inicial
    )
    
    tiempo_horas = tiempo_minutos / 60
    
    print(f"📦 VOLÚMENES:")
    print(f"• Objeto inicial: {volumen_inicial:.2e} m³")
    print(f"• Volumen objetivo: {volumen_objetivo:.2e} m³")
    
    print(f"\n⏰ RESULTADOS:")
    print(f"• Duplicaciones necesarias: {duplicaciones}")
    print(f"• Tiempo total: {tiempo_minutos:,.1f} minutos")
    print(f"• Tiempo total: {tiempo_horas:,.1f} horas")
    
    return tiempo_minutos, duplicaciones, datos

def visualizar_crecimiento_exponencial(datos_dorayaki, datos_pelota, datos_genericos=[]):
    """Visualiza el crecimiento exponencial en gráficos"""
    print("\n" + "=" * 70)
    print("VISUALIZACIÓN DEL CRECIMIENTO EXPONENCIAL")
    print("=" * 70)
    
    # Configuración para CodeSpaces
    plt.switch_backend('Agg')
    
    # Crear figura con múltiples subgráficos
    plt.figure(figsize=(15, 10))
    
    # Gráfico 1: Crecimiento del dorayaki (escala lineal)
    if datos_dorayaki:
        tiempos = [d[0] for d in datos_dorayaki]  # Minutos
        volumenes = [d[1] for d in datos_dorayaki]  # m³
        
        plt.subplot(2, 2, 1)
        plt.plot(tiempos, volumenes, 'r-', linewidth=2, marker='o', markersize=3)
        plt.axhline(y=VOLUMEN_SISTEMA_SOLAR, color='orange', linestyle='--', 
                   label='Volumen Sistema Solar')
        plt.title('Crecimiento del Dorayaki - Escala Lineal', fontweight='bold')
        plt.xlabel('Tiempo (minutos)')
        plt.ylabel('Volumen (m³)')
        plt.yscale('log')  # Usar escala log para mejor visualización
        plt.grid(True, alpha=0.3)
        plt.legend()
    
    # Gráfico 2: Crecimiento comparativo (escala logarítmica)
    plt.subplot(2, 2, 2)
    
    # Dorayaki
    if datos_dorayaki:
        tiempos_d = [d[0] for d in datos_dorayaki]
        volumenes_d = [d[1] for d in datos_dorayaki]
        plt.plot(tiempos_d, volumenes_d, 'r-', linewidth=2, label='Dorayaki → Sistema Solar')
    
    # Pelota de fútbol
    if datos_pelota:
        tiempos_p = [d[0] for d in datos_pelota]
        volumenes_p = [d[1] for d in datos_pelota]
        plt.plot(tiempos_p, volumenes_p, 'b-', linewidth=2, label='Pelota → Tokyo Dome')
    
    plt.axhline(y=VOLUMEN_SISTEMA_SOLAR, color='orange', linestyle='--', alpha=0.7)
    plt.axhline(y=VOLUMEN_TOKYO_DOME, color='green', linestyle='--', alpha=0.7)
    
    plt.title('Comparación de Crecimiento Exponencial', fontweight='bold')
    plt.xlabel('Tiempo (minutos)')
    plt.ylabel('Volumen (m³) - Escala Log')
    plt.yscale('log')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    # Gráfico 3: Número de duplicaciones vs volumen
    plt.subplot(2, 2, 3)
    duplicaciones = list(range(0, 101, 10))  # 0 a 100 en pasos de 10
    factores_crecimiento = [2 ** n for n in duplicaciones]
    
    plt.plot(duplicaciones, factores_crecimiento, 'purple', linewidth=2)
    plt.title('Crecimiento por Número de Duplicaciones', fontweight='bold')
    plt.xlabel('Número de Duplicaciones')
    plt.ylabel('Factor de Crecimiento (2^n)')
    plt.yscale('log')
    plt.grid(True, alpha=0.3)
    
    # Gráfico 4: Tiempos para diferentes objetivos
    plt.subplot(2, 2, 4)
    objetivos = [
        ('Canica\n(1cm³)', VOLUMEN_CANICA),
        ('Dorayaki', VOLUMEN_DORAYAKI),
        ('Pelota', VOLUMEN_PELOTA_FUTBOL),
        ('Tokyo Dome', VOLUMEN_TOKYO_DOME),
        ('Tierra', 1.08321e21),
        ('Sistema Solar', VOLUMEN_SISTEMA_SOLAR)
    ]
    
    tiempos_objetivos = []
    nombres = []
    
    for nombre, volumen in objetivos:
        if volumen > VOLUMEN_DORAYAKI:
            tiempo, _, _ = calcular_tiempo_para_volumen(volumen, VOLUMEN_DORAYAKI)
            tiempos_objetivos.append(tiempo)
            nombres.append(nombre)
    
    plt.bar(nombres, tiempos_objetivos, color=['blue', 'green', 'red', 'orange', 'purple', 'brown'])
    plt.title('Tiempo para Alcanzar Diferentes Objetivos', fontweight='bold')
    plt.ylabel('Minutos Requeridos')
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    
    # Añadir valores en las barras
    for i, v in enumerate(tiempos_objetivos):
        plt.text(i, v + max(tiempos_objetivos)*0.01, f'{v:,.0f}', 
                ha='center', va='bottom', fontsize=8)
    
    plt.tight_layout()
    plt.savefig('crecimiento_exponencial_dorayaki.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    print("✅ Gráfico guardado como 'crecimiento_exponencial_dorayaki.png'")

def main():
    """Función principal del programa"""
    print("🍙 PROBLEMA DEL DORAYAKI - CRECIMIENTO EXPONENCIAL")
    print("Basado en el episodio de Doraemon con la 'Baibain'")
    print("=" * 70)
    
    try:
        # Resolver problemas principales
        tiempo_dorayaki, dup_dorayaki, datos_dorayaki = problema_dorayaki_sistema_solar()
        tiempo_pelota, dup_pelota, datos_pelota = problema_tokyo_dome_pelota()
        
        # Ejemplo genérico adicional
        tiempo_canica, dup_canica, datos_canica = problema_generico(
            "Canica llenando una piscina", 
            100,  # 100 m³ (piscina pequeña)
            VOLUMEN_CANICA
        )
        
        # Visualización
        visualizar_crecimiento_exponencial(datos_dorayaki, datos_pelota)
        
        # Resumen ejecutivo
        print("\n" + "=" * 70)
        print("RESUMEN EJECUTIVO - LECCIONES APRENDIDAS")
        print("=" * 70)
        
        print(f"🎯 TIEMPOS CLAVE:")
        print(f"• Dorayaki → Sistema Solar: {tiempo_dorayaki/60:,.0f} horas")
        print(f"• Pelota → Tokyo Dome: {tiempo_pelota:,.0f} minutos")
        print(f"• Canica → Piscina: {tiempo_canica:,.0f} minutos")
        
        print(f"\n💡 LECCIONES SOBRE CRECIMIENTO EXPONENCIAL:")
        print(f"• Comienza lentamente, luego acelera dramáticamente")
        print(f"• 10 duplicaciones: ×1,024")
        print(f"• 20 duplicaciones: ×1,048,576") 
        print(f"• 30 duplicaciones: ×1,073,741,824")
        
        print(f"\n⚠️  APLICACIONES EN LA VIDA REAL:")
        print(f"• Crecimiento de poblaciones bacterianas")
        print(f"• Propagación de virus y epidemias")
        print(f"• Interés compuesto en finanzas")
        print(f"• Crecimiento de datos digitales")
        
        print(f"\n🔍 DATOS CURIOSOS DE DORAEMON:")
        print(f"• En el episodio original, terminan lanzando los dorayakis al espacio")
        print(f"• La Baibain duplica objetos cada 5 minutos")
        print(f"• Es una metáfora del crecimiento exponencial incontrolado")
        
    except Exception as e:
        print(f"❌ Error durante la ejecución: {e}")

# Ejecutar el programa
if __name__ == "__main__":
    main()
