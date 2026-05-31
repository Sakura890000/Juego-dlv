import json
import os
from datetime import datetime

ARCHIVO_PARTIDA = "partida_guardada.json"

def guardar_partida(P1, P2, turno_actual, posiciones, casillas_juego, casillas_trampa, casillas_lucky):
    """Guarda el estado completo del juego"""
    datos = {
        "timestamp": datetime.now().isoformat(),
        "puntos": {
            "P1": P1,
            "P2": P2
        },
        "turno_actual": turno_actual,
        "posiciones": {
            "J1": {
                "casilla_actual": posiciones["J1"]["casilla_actual"],
                "pierde_turno": posiciones["J1"]["pierde_turno"]
            },
            "J2": {
                "casilla_actual": posiciones["J2"]["casilla_actual"],
                "pierde_turno": posiciones["J2"]["pierde_turno"]
            }
        },
        "tablero": {
            "casillas_juego": list(casillas_juego),
            "casillas_trampa": list(casillas_trampa),
            "casillas_lucky": list(casillas_lucky)
        }
    }
    
    with open(ARCHIVO_PARTIDA, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)
    
    print(f"✓ Partida guardada en '{ARCHIVO_PARTIDA}'")
    return datos

def cargar_partida():
    """Carga el estado completo del juego"""
    if not os.path.exists(ARCHIVO_PARTIDA):
        print(f"⚠ No hay partida guardada (archivo no encontrado)")
        return None
    
    try:
        with open(ARCHIVO_PARTIDA, "r", encoding="utf-8") as f:
            datos = json.load(f)
        
        # Convertir listas back a sets para casillas
        datos["tablero"]["casillas_juego"] = set(map(tuple, datos["tablero"]["casillas_juego"]))
        datos["tablero"]["casillas_trampa"] = set(map(tuple, datos["tablero"]["casillas_trampa"]))
        datos["tablero"]["casillas_lucky"] = set(map(tuple, datos["tablero"]["casillas_lucky"]))
        
        print(f"✓ Partida cargada desde '{ARCHIVO_PARTIDA}'")
        print(f"  Fecha: {datos['timestamp']}")
        print(f"  Turno: {datos['turno_actual']}")
        return datos
    
    except Exception as e:
        print(f"✗ Error al cargar partida: {e}")
        return None

def listar_partidas_guardadas():
    """Muestra si existe una partida guardada"""
    if os.path.exists(ARCHIVO_PARTIDA):
        try:
            with open(ARCHIVO_PARTIDA, "r", encoding="utf-8") as f:
                datos = json.load(f)
            return f"Última partida: {datos['timestamp']}"
        except:
            return "Partida corrupta"
    return "No hay partida guardada"

def eliminar_partida():
    """Borra la partida guardada"""
    if os.path.exists(ARCHIVO_PARTIDA):
        os.remove(ARCHIVO_PARTIDA)
        print(f"✓ Partida eliminada")
    else:
        print("⚠ No hay partida guardada")
