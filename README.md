# Aprendizaje de máquina II - CEIA 
## Trabajo práctico

En el siguiente repositorio encontrará los archivos necesarios para replicar la arquitectura de solución propuesta (mostrada en clases). Podrá acceder a las slides, mediante el siguiente [enlace](https://github.com/ldidone/aprendizaje_de_maquina_II_CEIA_TP/blob/main/slides/Presentaci%C3%B3n%20ML%202%20_%20Cardozo%20-%20Didone.pdf).

***
### Arquitectura propuesta:

![Acoustic extinguiher fire arquitecture](https://user-images.githubusercontent.com/26725551/185769836-a4b32a22-c5eb-40e0-a2d9-9c82199134d8.png)

#### Archivos necesarios para replicar la DB:
- En la siguiente [capeta](https://github.com/ldidone/aprendizaje_de_maquina_II_CEIA_TP/tree/main/DB) encontrará los archivos necesarios para crear la tabla utilizada para entrenar el modelo y también para popularla.

#### Archivos necesarios para replicar la VM:
- En la siguiente [carpeta](https://github.com/ldidone/aprendizaje_de_maquina_II_CEIA_TP/tree/main/VM) encontrará los archivos necesarios para entrenar el modelo ([train.sh](https://github.com/ldidone/aprendizaje_de_maquina_II_CEIA_TP/blob/main/VM/train/train.sh)) y para servirlo ([serve.sh](https://github.com/ldidone/aprendizaje_de_maquina_II_CEIA_TP/blob/main/VM/inference/serve.sh)).
- Pasos para crear el entorno virtual e instalar las dependencias (previamente debe tener instalado virtualenv en su VM):
```bash
python3 -m venv ./venv
source ./venv/bin/activate
pip install -r ./requirements.txt
```

#### Archivos necesarios para implementar la Cloud Function:
- En la siguiente [carpeta](https://github.com/ldidone/aprendizaje_de_maquina_II_CEIA_TP/tree/main/cloud_function) encontrará el código que deberá implementar en la lambda function junto al archivo de dependencias (requirements.txt).
*** 
### Invocar la función lambda desde internet:
- Podrá invocar la cloud function implementada mediante el siguiente cURL:
```bash
curl -m 15 -X POST https://us-central1-gothic-state-355815.cloudfunctions.net/inferences \
-H "Content-Type:application/json" \
-d '{"data": [[1, "gasoline", 10, 96, 0.0, 75]]}'
```

*** 
### Trabajo previo: Machine Learning 1
- Podrá acceder al trabajo previo realizado en la cátedra Aprendizaje de Máquina 1, mediante el siguiente [enlace](https://github.com/ldidone/aprendizaje_de_maquina_I_CEIA_TP).

----------------------------------------------------------------------------------------------
> Alumnos:
> - Emmanuel Cardozo
> - Lucas Didone

-------------------------------------------------------------------------------------------
> ### Citation
> Yavuz Selim TASPINAR, Murat KOKLU and Mustafa ALTIN CV:https://www.muratkoklu.com/en/publications/ DATASET: https://www.muratkoklu.com/datasets/ Citation Request : 1: KOKLU M., TASPINAR Y.S., (2021). Determining the Extinguishing Status of Fuel Flames With Sound Wave by Machine Learning Methods. IEEE Access, 9, pp.86207-86216, Doi: 10.1109/ACCESS.2021.3088612 Link: https://ieeexplore.ieee.org/document/9452168 (Open Access) https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9452168

> 2: TASPINAR Y.S., KOKLU M., ALTIN M., (2021). Classification of Flame Extinction Based on Acoustic Oscillations using Artificial Intelligence Methods. Case Studies in Thermal Engineering, 28, 101561, Doi: 10.1016/j.csite.2021.101561 Link: https://www.sciencedirect.com/science/article/pii/S2214157X21007243 (Open Access) https://www.sciencedirect.com/sdfe/reader/pii/S2214157X21007243/pdf

> 3: TASPINAR Y.S., KOKLU M., ALTIN M., (2022). Acoustic-Driven Airflow Flame Extinguishing System Design and Analysis of Capabilities of Low Frequency in Different Fuels. Fire Technology, Doi: 10.1007/s10694-021-01208-9 Link: https://link.springer.com/content/pdf/10.1007/s10694-021-01208-9.pdf
