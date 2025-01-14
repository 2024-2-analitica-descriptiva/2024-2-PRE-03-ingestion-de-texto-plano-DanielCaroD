"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """

    import pandas as pd

    with open("files/input/clusters_report.txt") as file:
      lines = file.readlines()
    lines = [line.strip() for line in lines if line.strip()][3:]
    
    columns = ["cluster", "cantidad_de_palabras_clave", "porcentaje_de_palabras_clave", "principales_palabras_clave"]

    data = []
    row = None

    for line in lines:
       line = line.split()

       if line[0].isdigit():
          if row: 
             data.append(row)
          cluster = int(line[0])
          amount = int(line[1])
          percentage = float(" ".join(line[2:3]).replace(",","."))
          words = " ".join(line[4:]).replace(".", "").strip()
          row = [cluster, amount, percentage, words]

       else:
          row[-1] += " " + " ".join(line).replace(".", "").strip()
          
    data.append(row)

    result = pd.DataFrame(data, columns=columns)
    
    return result

if __name__ == '__main__': 
  print(pregunta_01())