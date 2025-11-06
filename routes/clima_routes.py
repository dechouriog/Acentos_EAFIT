from fastapi import APIRouter, Request, Query
import requests

router = APIRouter(prefix="/clima", tags=["Clima"])


@router.get("/")
def obtener_clima(
    request: Request,
    lat: float = Query(6.2442, description="Latitud, por defecto Medellín"),
    lon: float = Query(-75.5812, description="Longitud, por defecto Medellín"),
):
    """
    Consulta la API pública de Open-Meteo y devuelve el clima actual
    para la latitud y longitud indicadas.
    """
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
    }

    try:
        respuesta = requests.get(url, params=params, timeout=5)
        respuesta.raise_for_status()
        data = respuesta.json()
        return {
            "ubicacion": {"latitud": lat, "longitud": lon},
            "clima_actual": data.get("current_weather", {}),
        }
    except requests.RequestException as e:
        return {"error": f"No se pudo obtener el clima: {str(e)}"}
