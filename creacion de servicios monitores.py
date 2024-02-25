import os # Importamos módulo os para funciones de sistema operativo
import time # Importamos módulo time para hacer delays
import psutil # Importamos psutil para obtenr información de procesos

NOMBRE_APP = "emu8086.exe" # Creamos constante con el nombre de la aplicación objetivo en este caso la aplicacion de emu8086

while True:
    def check_app_status(): # Definimos la función de monitoreo
        
        for proc in psutil.process_iter(): # Iteramos sobre procesos ejecutándose
        
            if proc.name() == NOMBRE_APP: # Comparamos nombre de proceso
                    
                    app_pid = proc.pid # Obtenemos ID de Proceso 
                    app_proc = psutil.Process(app_pid) # Objeto psutil.Process 

                    cpu_uso = app_proc.cpu_percent(interval=1) # Porcentaje de uso de CPU
                    mem_uso = app_proc.memory_percent() # Porcentaje de uso de RAM
                    
                    # Mostramos información del estado  
                    print(f"{NOMBRE_APP} corriendo. PID: {app_pid}. CPU: {cpu_uso}%. MEM: {mem_uso}%")
                    
                    return True # Retornamos True porque la encontramos
                
        print(f"{NOMBRE_APP} no se está ejecutando") # No se encontró el proceso
        return False # Se retorna False 
                

    if __name__ == "__main__": # Punto de entrada como programa principal 
        
        while True:
            check_app_status() # Ejecutamos la monitorización
            time.sleep(5) # Pausa de 5 segundos