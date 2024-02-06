import pickle

class ProgramState:
    def __init__(self):
        self.variable1 = 0
        self.variable2 = "Hola"

    def display_state(self):
        print(f"Variable1: {self.variable1}, Variable2: {self.variable2}")

def save_checkpoint(state, filename="checkpoint.pkl"):
    with open(filename, "wb") as file:
        pickle.dump(state, file)

def load_checkpoint(filename="checkpoint.pkl"):
    with open(filename, "rb") as file:
        return pickle.load(file)

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una instancia del estado del programa
    current_state = ProgramState()
    current_state.display_state()

    # Guardar un checkpoint
    save_checkpoint(current_state, "initial_checkpoint.pkl")

    # Modificar el estado del programa
    current_state.variable1 = 42
    current_state.variable2 = "Mundo"
    current_state.display_state()

    # Guardar otro checkpoint después de la modificación
    save_checkpoint(current_state, "modified_checkpoint.pkl")

    # Restaurar desde el primer checkpoint
    restored_state = load_checkpoint("initial_checkpoint.pkl")
    print("\nRestaurado desde el primer checkpoint:")
    restored_state.display_state()

    # Restaurar desde el segundo checkpoint
    restored_state = load_checkpoint("modified_checkpoint.pkl")
    print("\nRestaurado desde el segundo checkpoint:")
    restored_state.display_state()
