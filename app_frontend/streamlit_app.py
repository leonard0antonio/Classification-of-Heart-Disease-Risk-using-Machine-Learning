#ALGUNS DADOS QUE DEVEM EXISTIR NO INPUT DO USUARIO:

#   age: int, #idade
#   sex: Literal[0, 1] #sexo -> recebe apenas [0 ou 1]
#   cp: #chest pain type (são 4 valores, de 0 a 4) -> recebe apenas [0, 1, 2 ou 4]
#  trestbps:  int,  #resting blood pressure (pressão arterial em repouso) 
#  chol:  int, #serum cholestoral in mg/dl (colesterol sérico em mg/dl)
#  fbs: #fasting blood sugar > 120 mg/dl (fasting blood sugar > 120 mg/dl) -> recebe apenas [0, 1]
# restecg: #resting electrocardiographic results (values 0,1,2) (resultados do eletrocardiograma em repouso) -> recebe apenas [0, 1 ou 2]
#  thalach: int,  #maximum heart rate achieved (frequência cardíaca máxima atingida)
#  exang:  #exercise induced angina (angina induzida por exercício) -> recebe apenas [0, 1]
# oldpeak: float , #ST depression induced by exercise relative to rest (depressão do segmento ST induzida pelo exercício em relação ao repouso)
# slope: the slope of the peak exercise ST segment (inclinação do segmento ST no pico do exercício) -> recebe apenas [0, 1 ou 2]
# ca: number of major vessels (0-3) colored by flourosopy (número de vasos principais (0–3) coloridos por fluoroscopia) -> recebe apenas [0, 1, 2 ou 3]
#  thal: thal: 0 = normal; 1 = fixed defect; 2 = reversable defect (thal: 0 = normal; 1 = defeito fixo; 2 = defeito reversível) -> recebe apenas [0, 1, 2 ou 3]
#
#TODOS OS DADOS ACIMA FORAM RETIRADOS DO CSV DO NOSSO MODELO, SÃO ESSES OS DADOS Q A I.A ESPERA NO INPUT
#CASO DUVIDAS SOBRE OS DADOS ACIMA, CONSULTEM EM: https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset?resource=download
#OU https://colab.research.google.com/drive/1Yq_Cbc8-KGwZbna0ByTsFqSQiTOK3oxG?usp=sharing (vai precisar configurar primeiro)