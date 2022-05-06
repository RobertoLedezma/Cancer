import streamlit as st
from cancer import predict_fractal_dimension_worst
st.title('Cáncer')
st.sidebar.image('logofcq.png', width = 100)
st.sidebar.write(''' Team Robert's
''')
st.sidebar.write(''' Integrantes:
''')
st.sidebar.write('''Camila Alejandra Flores Ramos 349240
''')
st.sidebar.write('''Roberto Ledezma Ruiz 348978
''')
st.sidebar.write('''Anahí Neri Hermosillo 349200
''')
st.sidebar.write('''Cynthia Rebeca Porras Rubio 349184
''')
st.sidebar.write('Grupo: 4°D')
st.write('El cáncer es una de las enfermedades más comunes en el mundo, causante de muchas muertes diarias y esto se debe a que sus síntomas son atendidos rara vez a tiempo por el paciente.')
st.subheader('¿Cuál es el tipo de cáncer que más se presenta?:microscope:')
#st.image('https://upload.wikimedia.org/wikipedia/commons/8/80/Breast_DCIS_histopathology_%281%29.jpg')
#st.image('https://www.cancerquest.org/sites/default/files/Latest%20Pics%202017/SkinCancer.jpg')
#st.image('https://d7lju56vlbdri.cloudfront.net/var/ezwebin_site/storage/images/_aliases/img_1col/noticias/las-celulas-madre-del-higado-intervienen-en-el-desarrollo-de-tumores/5971960-2-esl-MX/Las-celulas-madre-del-higado-intervienen-en-el-desarrollo-de-tumores.jpg')
#st.image('https://static3.abc.es/media/salud/2018/01/15/prostatecancer-kXfG--620x349@abc.jpg')
#st.image('https://d7lju56vlbdri.cloudfront.net/var/ezwebin_site/storage/images/_aliases/img_1col/noticias/el-cancer-cervical-es-mas-agresivo-cuando-no-hay-virus-del-papiloma-humano/6478113-1-esl-MX/El-cancer-cervical-es-mas-agresivo-cuando-no-hay-virus-del-papiloma-humano.jpg')
#st.image('https://upload.wikimedia.org/wikipedia/commons/5/54/Lung_small_cell_carcinoma_%281%29_by_core_needle_biopsy.jpg')
#st.image('https://elmedicointeractivo.com/wp-content/uploads/2016/10/2016101913381476238.jpg')
cancer = st.selectbox('Elige un tipo de cáncer',['Piel','Mama','Hígado','Próstata','Cuello_uterino','Pulmón','Leucemia'])
if cancer =='Piel':
  st.write('Piel')
  st.image('https://www.cancerquest.org/sites/default/files/Latest%20Pics%202017/SkinCancer.jpg')
  st.info('Incorrecto')
if cancer =='Hígado':
  st.write('Hígado')
  st.image('https://d7lju56vlbdri.cloudfront.net/var/ezwebin_site/storage/images/_aliases/img_1col/noticias/las-celulas-madre-del-higado-intervienen-en-el-desarrollo-de-tumores/5971960-2-esl-MX/Las-celulas-madre-del-higado-intervienen-en-el-desarrollo-de-tumores.jpg')
  st.info('Incorrecto')  
if cancer =='Próstata':
  st.write('Próstata')
  st.image('https://static3.abc.es/media/salud/2018/01/15/prostatecancer-kXfG--620x349@abc.jpg')
  st.info('Incorrecto') 
if cancer =='Cuello_uterino':
  st.write('Cuello_uterino')
  st.image('https://d7lju56vlbdri.cloudfront.net/var/ezwebin_site/storage/images/_aliases/img_1col/noticias/el-cancer-cervical-es-mas-agresivo-cuando-no-hay-virus-del-papiloma-humano/6478113-1-esl-MX/El-cancer-cervical-es-mas-agresivo-cuando-no-hay-virus-del-papiloma-humano.jpg')
  st.info('Incorrecto')    
if cancer =='Pulmón':
  st.write('Pulmón')
  st.image('https://upload.wikimedia.org/wikipedia/commons/5/54/Lung_small_cell_carcinoma_%281%29_by_core_needle_biopsy.jpg')
  st.info('Incorrecto') 
if cancer =='Leucemia':
  st.write('Leucemia')
  st.image('https://elmedicointeractivo.com/wp-content/uploads/2016/10/2016101913381476238.jpg')
  st.info('Incorrecto') 
if cancer =='Mama':
  st.write('🌸Mama🌸')
  st.image('https://upload.wikimedia.org/wikipedia/commons/8/80/Breast_DCIS_histopathology_%281%29.jpg')
  st.write('Tumor maligno')
  st.info('Correcto:heavy_check_mark:')
  Informacion = st.button('Ver información👁️')
  if Informacion:
    st.write('''CÁNCER DE MAMA:

    Para regiones subdesarrolladas 324.000 personas padencen la enfermedad lo cual representa un 14.3%

    Para regiones desarrolladas 198.000 padecen esta enfermedad, que representa el 15.4%

    ''')
    st.write('''Causas:
    Los médicos saben que el cáncer de mama ocurre cuando algunas células mamarias comienzan a crecer de manera anormal. Estas células se dividen más rápido que las células saludables y continúan acumulándose, formando un bulto o masa. Las células pueden diseminarse (hacer metástasis) por la mama hasta los ganglios linfáticos o a otras partes del cuerpo.
    El cáncer de mama suele comenzar en las células en los conductos que producen leche (carcinoma ductal invasivo). El cáncer de mama también puede comenzar en el tejido glandular denominado lóbulo (carcinoma lobular invasivo) o en otras células o tejido dentro de la mama.
    ''')
    st.write('''Los investigadores han identificado factores relacionados con las hormonas, el estilo de vida y el entorno que pueden aumentar tu riesgo de desarrollar cáncer. Sin embargo, no se sabe con exactitud por qué algunas personas que no presentan ningún factor de riesgo desarrollan cáncer y otras personas con factores de riesgo nunca lo desarrollan. Es posible que el cáncer de mama se produzca por una interacción compleja entre tu composición genética y tu entorno.
    ''')
    st.write('''Síntomas:
    Entre los signos y síntomas del cáncer de mama se pueden incluir los siguientes:
    ''')
    st.write('''-Un bulto o engrosamiento en la mama que se siente diferente del tejido que la rodea.
    -Cambio de tamaño, forma o aspecto de una mama.
    ''')
    st.write('''-Cambios en la piel que se encuentra sobre la mama, como formación de hoyuelos.
    ''')
    st.write('''-La inversión reciente del pezón
    ''')
    st.write('''-Descamación, desprendimiento de la piel, formación de costras y pelado del área pigmentada de la piel que rodea el pezón (areola) o la piel de la mama
    ''')
    st.write('''-Enrojecimiento o pequeños orificios en la piel que se encuentra sobre tu mama, como la piel de una naranja.
    ''')
  Extras = st.button('Extra')
  if Extras:
   import pandas as pd
   import numpy as np
   import seaborn as sns 
   import matplotlib.pyplot as plt
   st.subheader('Base de Datos "Breast-cancer-Wisconsin"')
   df1 = pd.read_csv("https://raw.githubusercontent.com/Muhd-Shahid/Breast-Cancer-Wisconsin/master/data_breast-cancer-wiscons.csv")
   df1.head(7)
   st.write(df1)
   df1.shape
   st.subheader('Tabla de diagnóstico')
   df1['diagnosis'].value_counts()
   sns.countplot(df1['diagnosis'],label= 'count')
   st.write(df1.describe())
   df1.isnull().sum()
   df1 = df1.dropna(axis=1)
   df1.shape
   st.subheader('Tipo de diagnóstico')
   df1.dtypes
   st.subheader('Evaluación de tumor')
   from sklearn.preprocessing import LabelEncoder
   labelencoder_Y = LabelEncoder()
   df1.iloc[:,1]=labelencoder_Y.fit_transform(df1.iloc[:,1].values)
   df1.iloc[:,1]
   st.subheader('Diagnóstico de primeros cinco pacientes')
   st.write(df1.head(5))
   sns.pairplot(df1.iloc[:,1:5], hue='diagnosis')
   df1.iloc[:,1:12].corr()
   st.subheader('Tabla de correlación')
   st.write(df1.iloc[:,1:12].corr())
   plt.figure(figsize=(10,10))
   sns.heatmap(df1.iloc[:,1:12].corr(), annot=True ,fmt='.0%')
   X = df1.iloc[:,2:31].values
   Y = df1.iloc[:,1].values
   st.subheader('Escala estándar')
   from sklearn.model_selection import train_test_split
   x_train,x_test,y_train,y_test= train_test_split(X,Y, test_size = 0.25 , random_state = 0)
   from sklearn.preprocessing import StandardScaler
   sc = StandardScaler()
   x_train = sc.fit_transform(x_train)
   x_test = sc.fit_transform(x_test)
   x_train
   def models(x_train,y_train):
     from sklearn.linear_model import LogisticRegression
     log = LogisticRegression(random_state=0)
     log.fit(x_train,y_train)

     from sklearn.tree import DecisionTreeClassifier
     tree = DecisionTreeClassifier(criterion = 'entropy' ,random_state=0)
     tree.fit(x_train,y_train)

     from sklearn.ensemble import RandomForestClassifier
     forest = RandomForestClassifier(n_estimators = 10 ,criterion = 'entropy' ,random_state = 0)
     forest.fit(x_train,y_train)
     
     st.write('[0] Logistics Regression training accuracy:' , log.score(x_train,y_train))
     st.write('[1] Decision Tree Classifier training accuracy:' , tree.score(x_train,y_train))
     st.write('[2] Random Forest Classifier training accuracy:' , forest.score(x_train,y_train))
     return log,tree,forest
   model = models(x_train, y_train)
   from sklearn.metrics import confusion_matrix
   for i in range ( len (model)):
     st.write('Model', i)
     cm = confusion_matrix(y_test,model[1].predict(x_test))

     TP = cm[0][0]
     TN = cm[1][1]
     FN = cm[1][0]
     FP = cm[0][1]
     st.write(cm)
     st.write('testing accuracy =', (TP + TN)/ (TP + TN + FN + FP))
   st.subheader('Predicción de tumores del modelo 1 y 2')
   pred = model[2].predict(x_test)
   st.write(pred)
   st.write()
   st.write(y_test)
   

   st.subheader('Selecciona el valor 1 o 0 para conocer si el tumor es benigno o maligno')
   diagnosis = st.selectbox('Valores',[0,1])
   if diagnosis == 0:
     st.write('Benigno✅')
   if diagnosis == 1:
     st.write('Maligno:no_entry:')
   
   st.subheader('Ingresa al siguiente link para saber más sobre el cáncer de mama')
   st.write('Video')
   st.write('https://www.youtube.com/watch?v=RjHLU9oLPyw')
   st.balloons()
