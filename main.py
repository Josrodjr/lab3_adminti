#Helmuth Nistal
#Jose Perez
#Javier Ramos
import numpy
import math

# duracion del proyecto 20 dias
PROJECT_DURATION = 20
# iteracinoes
ITERATIONS = 1000000

tiempos = {
    'd_interfaz':    {'optimista': 1, 'probable': 2, 'pesimista': 3},
    'd_nivel':       {'optimista': 1, 'probable': 2, 'pesimista': 3},
    'd_mecanicas':   {'optimista': 4, 'probable': 6, 'pesimista': 9},
    'd_historia':    {'optimista': 0, 'probable': 1, 'pesimista': 2},
    'p_unitarias':   {'optimista': 2, 'probable': 3, 'pesimista': 6},
    'p_integracion': {'optimista': 2, 'probable': 3, 'pesimista': 6},
    'p_usuario':     {'optimista': 2, 'probable': 3, 'pesimista': 4},
    'e_especiales':  {'optimista': 1, 'probable': 2, 'pesimista': 3},
    'tutorial':      {'optimista': 1, 'probable': 2, 'pesimista': 3}
}

# triangular distrubution
print(math.floor(numpy.random.triangular(1, 5, 10)))

# suffering from success DJ KALED
success = 0

for i in range(ITERATIONS):
    # no elapsed time
    elapsed_time = 0
    # throw a random for each value on the dictionary
    for tarea in tiempos:
        duracion = math.floor(numpy.random.triangular(tiempos[tarea]['optimista'], tiempos[tarea]['probable'], tiempos[tarea]['pesimista']))
        elapsed_time += duracion
    
    # revisamos si se supero el tiempo
    if elapsed_time <= PROJECT_DURATION:
        success += 1

print(success/ITERATIONS)