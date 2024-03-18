from prefect import Flow, task
import requests

@task
def descargar_valor_dolar():
    try:
        # Realizar una solicitud GET a una API que proporcione información sobre el valor del dólar
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        response.raise_for_status()  # Lanza una excepción si la solicitud no es exitosa (código de estado no es 200)
        data = response.json()  # Convertir la respuesta a formato JSON
        return data["rates"]["COP"]  # Devolver el valor del dólar en pesos colombianos
    except Exception as e:
        print("Error al descargar el valor del dólar:", e)
        return None

@task
def analizar_valor_dolar(valor_dolar):
    # Realizar cualquier análisis necesario sobre el valor del dólar
    print("El valor actual del dólar es:", valor_dolar)

with Flow("Monitoreo del valor del dólar") as flujo:
    valor_dolar = descargar_valor_dolar()
    analizar_valor_dolar(valor_dolar)

# Ejecutar el flujo de trabajo
if __name__ == "__main__":
    flujo.run()
