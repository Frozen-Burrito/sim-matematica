from enum import Enum


class EstadoTorniquete(Enum):
    """El estado de un torniquete."""
    BLOQUEADO = 1
    DESBLOQUEADO = 2


class EntradaTorniquete(Enum):
    """Una acción sobre un torniquete."""
    MONEDA = 1
    EMPUJAR = 2


class Torniquete:
    """Representa un torniquete usando una máquina de estados finitos.
    
    Atributos
    ---------
    estado : EstadoTorniquete
        el estado actual del torniquete.

    Métodos
    -------
    procesar_entrada(entrada)
        Procesa una entrada y vuelve a evaluar el estado del torniquete.
    """

    def __init__(self, estado_inicial = EstadoTorniquete.BLOQUEADO):
        """
        Parámetros
        ----------
        estado_inicial : EstadoTorniquete, opcional
            El estado inicial del torniquete (BLOQUEADO por defecto).
        """

        self.estado = estado_inicial


    def procesar_entrada(self, entrada):
        """
        Parámetros
        ----------
        entrada : EntradaTorniquete
            La acción sobre el torniquete.
        """
        # Asegurar que `entrada` sea un valor de `EntradaTorniquete`.
        assert type(entrada) == EntradaTorniquete
        assert entrada in [EntradaTorniquete.MONEDA, EntradaTorniquete.EMPUJAR]

        if self.estado == EstadoTorniquete.BLOQUEADO and entrada == EntradaTorniquete.MONEDA:
            # La moneda desbloquea el torniquete.
            self.estado = EstadoTorniquete.DESBLOQUEADO
        elif self.estado == EstadoTorniquete.DESBLOQUEADO and entrada == EntradaTorniquete.EMPUJAR:
            # El torniquete vuelve a quedar bloqueado despues de empujarlo.
            self.estado = EstadoTorniquete.BLOQUEADO


class PruebaTorniquete:
    """Prueba un `Torniquete` usando entradas y salidas en consola.
    
    Atributos
    ---------
    torniquete : Torniquete
        el torniquete que está probando.

    Métodos
    -------
    ejecutar()
        Inicia un ciclo de ejecución para enviar acciones al torniquete y observar los 
        cambios de estado.
    """

    def __init__(self, torniquete):
        """
        Parámetros
        ----------
        torniquete : Torniquete
            La instancia de `Torniquete` a probar.
        """
        self.torniquete = torniquete


    def ejecutar(self):
        # Registrar el número de iteración actual.
        self.num_iteracion = 1

        while True:
            print(f"\n= Iteración: {self.num_iteracion}")
            print(f"= Estado del torniquete: {self.torniquete.estado.name}")

            try:
                # Recibir la acción que escriba el usuario.
                print("- Elige una acción: 1 para echar una moneda, 2 para empujar")
                entrada_str = input(">")
                entrada = EntradaTorniquete(int(entrada_str))

                # Ejecutar la acción sobre el torniquete.
                estado_anterior = self.torniquete.estado
                self.torniquete.procesar_entrada(entrada)

                # Comparar el estado anterior y el actual, mostrar el cambio para claridad.
                if entrada == EntradaTorniquete.MONEDA:
                    if estado_anterior != self.torniquete.estado:
                        print("- Desbloqueaste el torniquete")
                    else:
                        print("! El torniquete ya está desbloqueado")
                elif entrada == EntradaTorniquete.EMPUJAR:
                    if estado_anterior != self.torniquete.estado:
                        print("- Empujaste el torniquete")
                    else:
                        print("! El torniquete está bloqueado")

            except ValueError:
                # La entrada del usuario no es un entero válido, o no es un valor de `EntradasTorniquete`.
                print(f"! El torniquete no acepta la acción \"{entrada_str}\", intenta otra vez")

            self.num_iteracion += 1


if __name__ == "__main__":
    # Punto de entrada principal del script.
    prueba_torniquete = PruebaTorniquete(Torniquete())
    prueba_torniquete.ejecutar()