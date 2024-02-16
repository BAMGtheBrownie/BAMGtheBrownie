import threading
import multiprocessing
import concurrent.futures

# Función para calcular la suma de los cuadrados de los primeros N números naturales
def calcular_suma_cuadrados(N):
    suma = 0
    for i in range(1, N + 1):
        suma += i ** 2
    print(f"La suma de los cuadrados de los primeros {N} números es: {suma}")

# Función que se ejecutará en un hilo
def ejecutar_hilo(N):
    threading.current_thread().name = f"Hilo - N={N}"
    calcular_suma_cuadrados(N)

# Función que se ejecutará en un proceso
def ejecutar_proceso(N):
    multiprocessing.current_process().name = f"Proceso - N={N}"
    calcular_suma_cuadrados(N)

# Función que se ejecutará en concurrencia
def ejecutar_concurrencia(N):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for i in range(N):
            executor.submit(calcular_suma_cuadrados, i + 1)

if __name__ == "__main__":
    N = 5  # Número de iteraciones para calcular la suma de los cuadrados

    # Ejecución en un hilo
    hilo = threading.Thread(target=ejecutar_hilo, args=(N,))
    hilo.start()
    hilo.join()

    # Ejecución en un proceso
    proceso = multiprocessing.Process(target=ejecutar_proceso, args=(N,))
    proceso.start()
    proceso.join()

    # Ejecución en concurrencia
    ejecutar_concurrencia(N)
