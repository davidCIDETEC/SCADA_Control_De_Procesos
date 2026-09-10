import subprocess
import time

procesos = {}

"""
def invocacion():
        subprocess.Popen(["python3", "/app/C_1.py"])
        subprocess.Popen(["python3", "/app/C_2.py"])
        subprocess.Popen(["python3", "/app/C_3.py"])
        subprocess.Popen(["python3", "/app/C_4.py"])
        subprocess.Popen(["python3", "/app/C_5.py"])
        subprocess.Popen(["python3", "/app/C_6.py"])
        subprocess.Popen(["python3", "/app/C_7.py"])
        subprocess.Popen(["python3", "/app/C_8.py"])
"""
def invocacion():
    scripts = [f"/app/C_{i}.py" for i in range(1, 9)]
    procesos = [subprocess.Popen(["python3", s]) for s in scripts]

    # Espera a que TODOS terminen antes de que el script principal salga
    for p in procesos:
        p.wait()

print("En ejecucion")

invocacion()

