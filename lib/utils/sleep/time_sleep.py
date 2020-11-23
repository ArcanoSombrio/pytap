import gc
import sys
import time


# Função que realiza uma pausa na execução do código nos segundos passados
def time_sleep(seconds):
    gc.garbage.append(sys.stdout)
    sys.stdout.flush()
    time.sleep(seconds)
