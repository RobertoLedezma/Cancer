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
  
  def predict_fractal_dimension_worst(data={}):
    """ Predictor for fractal_dimension_worst from model/60a9bfc739339b69d50d71e2

        Predictive model by BigML - Machine Learning Made Easy
    """
    if (data.get('fractal_dimension_mean') is None):
        return 6252.12302
    if (data['fractal_dimension_mean'] > 7305):
        if (data.get('concave_points_mean') is None):
            return 2436.25581
        if (data['concave_points_mean'] > 577):
            if (data.get('perimeter_se') is None):
                return 1758.5641
            if (data['perimeter_se'] > 8619):
                return 9964
            if (data['perimeter_se'] <= 8619):
                if (data.get('concave_points_worst') is None):
                    return 1542.63158
                if (data['concave_points_worst'] > 6089):
                    if (data['fractal_dimension_mean'] > 7879):
                        return 1327
                    if (data['fractal_dimension_mean'] <= 7879):
                        return 9004
                if (data['concave_points_worst'] <= 6089):
                    if (data.get('symmetry_se') is None):
                        return 1116.41176
                    if (data['symmetry_se'] > 5328):
                        return 127
                    if (data['symmetry_se'] <= 5328):
                        if (data.get('symmetry_mean') is None):
                            return 1212.16129
                        if (data['symmetry_mean'] > 218):
                            if (data.get('concavity_worst') is None):
                                return 1183.4
                            if (data['concavity_worst'] > 6278):
                                if (data.get('area_worst') is None):
                                    return 1307
                                if (data['area_worst'] > 5853):
                                    return 1421
                                if (data['area_worst'] <= 5853):
                                    return 1215.8
                            if (data['concavity_worst'] <= 6278):
                                if (data.get('fractal_dimension_se') is None):
                                    return 1130.42857
                                if (data['fractal_dimension_se'] > 1470):
                                    return 1100.47059
                                if (data['fractal_dimension_se'] <= 1470):
                                    return 1257.75
                        if (data['symmetry_mean'] <= 218):
                            return 2075
        if (data['concave_points_mean'] <= 577):
            return 9043.75
    if (data['fractal_dimension_mean'] <= 7305):
        if (data.get('compactness_worst') is None):
            return 6564.06654
        if (data['compactness_worst'] > 3658):
            if (data.get('perimeter_mean') is None):
                return 5362.26812
            if (data['perimeter_mean'] > 8018):
                if (data.get('fractal_dimension_se') is None):
                    return 3021.06452
                if (data['fractal_dimension_se'] > 1841):
                    if (data['compactness_worst'] > 7074):
                        return 6283
                    if (data['compactness_worst'] <= 7074):
                        if (data.get('concave_points_mean') is None):
                            return 1374.38095
                        if (data['concave_points_mean'] > 261):
                            if (data.get('concave_points_worst') is None):
                                return 1077.15
                            if (data['concave_points_worst'] > 3116):
                                return 649.5
                            if (data['concave_points_worst'] <= 3116):
                                if (data['compactness_worst'] > 5067):
                                    return 1236.33333
                                if (data['compactness_worst'] <= 5067):
                                    return 1068.83333
                        if (data['concave_points_mean'] <= 261):
                            return 7319
                if (data['fractal_dimension_se'] <= 1841):
                    if (data.get('concave_points_mean') is None):
                        return 6528.125
                    if (data['concave_points_mean'] > 4835):
                        return 9618
                    if (data['concave_points_mean'] <= 4835):
                        if (data.get('area_se') is None):
                            return 6086.71429
                        if (data['area_se'] > 761):
                            return 6183.83333
                        if (data['area_se'] <= 761):
                            return 5504
            if (data['perimeter_mean'] <= 8018):
                if (data.get('fractal_dimension_se') is None):
                    return 6040.56075
                if (data['fractal_dimension_se'] > 5777):
                    if (data['compactness_worst'] > 5483):
                        if (data.get('radius_se') is None):
                            return 1021
                        if (data['radius_se'] > 1664):
                            if (data.get('texture_se') is None):
                                return 1149.14286
                            if (data['texture_se'] > 1323):
                                return 999.75
                            if (data['texture_se'] <= 1323):
                                return 1348.33333
                        if (data['radius_se'] <= 1664):
                            return 124
                    if (data['compactness_worst'] <= 5483):
                        return 6820.6
                if (data['fractal_dimension_se'] <= 5777):
                    if (data.get('smoothness_worst') is None):
                        return 6426.26596
                    if (data['smoothness_worst'] > 1571):
                        if (data.get('perimeter_se') is None):
                            return 4850.13636
                        if (data['perimeter_se'] > 2910):
                            if (data.get('concave_points_se') is None):
                                return 1680.42857
                            if (data['concave_points_se'] > 5522):
                                return 5871
                            if (data['concave_points_se'] <= 5522):
                                if (data.get('concave_points_mean') is None):
                                    return 982
                                if (data['concave_points_mean'] > 738):
                                    return 1056
                                if (data['concave_points_mean'] <= 738):
                                    return 612
                        if (data['perimeter_se'] <= 2910):
                            if (data['fractal_dimension_mean'] > 2990):
                                if (data['smoothness_worst'] > 5056):
                                    if (data['fractal_dimension_mean'] > 5646):
                                        if (data.get('concave_points_mean') is None):
                                            return 7054.57143
                                        if (data['concave_points_mean'] > 2420):
                                            return 7555.5
                                        if (data['concave_points_mean'] <= 2420):
                                            if (data.get('compactness_se') is None):
                                                return 6854.2
                                            if (data['compactness_se'] > 1112):
                                                return 6734.66667
                                            if (data['compactness_se'] <= 1112):
                                                return 7033.5
                                    if (data['fractal_dimension_mean'] <= 5646):
                                        return 5786
                                if (data['smoothness_worst'] <= 5056):
                                    return 9425
                            if (data['fractal_dimension_mean'] <= 2990):
                                return 3116.66667
                    if (data['smoothness_worst'] <= 1571):
                        if (data.get('concavity_se') is None):
                            return 6907.86111
                        if (data['concavity_se'] > 3938):
                            if (data.get('perimeter_worst') is None):
                                return 8119.54167
                            if (data['perimeter_worst'] > 174):
                                if (data.get('perimeter_se') is None):
                                    return 8428.78261
                                if (data['perimeter_se'] > 2126):
                                    if (data.get('symmetry_se') is None):
                                        return 9029.125
                                    if (data['symmetry_se'] > 1638):
                                        if (data.get('symmetry_mean') is None):
                                            return 9262.16667
                                        if (data['symmetry_mean'] > 1764):
                                            if (data['fractal_dimension_mean'] > 6159):
                                                if (data.get('smoothness_mean') is None):
                                                    return 9758
                                                if (data['smoothness_mean'] > 5407):
                                                    return 9566.5
                                                if (data['smoothness_mean'] <= 5407):
                                                    return 9885.66667
                                            if (data['fractal_dimension_mean'] <= 6159):
                                                return 9015.66667
                                        if (data['symmetry_mean'] <= 1764):
                                            return 8827.25
                                    if (data['symmetry_se'] <= 1638):
                                        return 8330
                                if (data['perimeter_se'] <= 2126):
                                    if (data['fractal_dimension_mean'] > 5444):
                                        if (data.get('concave_points_mean') is None):
                                            return 7218.5
                                        if (data['concave_points_mean'] > 1195):
                                            return 7361.25
                                        if (data['concave_points_mean'] <= 1195):
                                            return 6933
                                    if (data['fractal_dimension_mean'] <= 5444):
                                        return 6085
                            if (data['perimeter_worst'] <= 174):
                                return 1007
                        if (data['concavity_se'] <= 3938):
                            if (data['fractal_dimension_se'] > 3982):
                                if (data['fractal_dimension_mean'] > 6040):
                                    if (data['compactness_worst'] > 4302):
                                        return 979
                                    if (data['compactness_worst'] <= 4302):
                                        return 108
                                if (data['fractal_dimension_mean'] <= 6040):
                                    return 9145
                            if (data['fractal_dimension_se'] <= 3982):
                                if (data.get('radius_se') is None):
                                    return 6980.1
                                if (data['radius_se'] > 489):
                                    if (data['fractal_dimension_mean'] > 327):
                                        if (data.get('radius_worst') is None):
                                            return 7456.13514
                                        if (data['radius_worst'] > 1606):
                                            if (data.get('symmetry_worst') is None):
                                                return 8637.63636
                                            if (data['symmetry_worst'] > 2914):
                                                return 9144.8
                                            if (data['symmetry_worst'] <= 2914):
                                                if (data.get('symmetry_se') is None):
                                                    return 8215
                                                if (data['symmetry_se'] > 1546):
                                                    return 7905.66667
                                                if (data['symmetry_se'] <= 1546):
                                                    return 8524.33333
                                        if (data['radius_worst'] <= 1606):
                                            if (data.get('area_se') is None):
                                                return 6956.26923
                                            if (data['area_se'] > 1266):
                                                if (data['fractal_dimension_se'] > 2261):
                                                    if (data['radius_se'] > 5718):
                                                        return 6336
                                                    if (data['radius_se'] <= 5718):
                                                        if (data['fractal_dimension_se'] > 2711):
                                                            return 7063.5
                                                        if (data['fractal_dimension_se'] <= 2711):
                                                            return 7526.25
                                                if (data['fractal_dimension_se'] <= 2261):
                                                    if (data['fractal_dimension_se'] > 1482):
                                                        if (data.get('concave_points_mean') is None):
                                                            return 6618
                                                        if (data['concave_points_mean'] > 2399):
                                                            return 6446.33333
                                                        if (data['concave_points_mean'] <= 2399):
                                                            if (data['smoothness_worst'] > 1104):
                                                                return 6809
                                                            if (data['smoothness_worst'] <= 1104):
                                                                return 6598.66667
                                                    if (data['fractal_dimension_se'] <= 1482):
                                                        return 6104
                                            if (data['area_se'] <= 1266):
                                                return 7989.5
                                    if (data['fractal_dimension_mean'] <= 327):
                                        return 1023
                                if (data['radius_se'] <= 489):
                                    return 1152
        if (data['compactness_worst'] <= 3658):
            if (data.get('area_mean') is None):
                return 6991.51031
            if (data['area_mean'] > 7349):
                if (data['fractal_dimension_mean'] > 6269):
                    if (data.get('area_se') is None):
                        return 2447.125
                    if (data['area_se'] > 5118):
                        return 8217.5
                    if (data['area_se'] <= 5118):
                        if (data.get('concave_points_worst') is None):
                            return 523.66667
                        if (data['concave_points_worst'] > 1569):
                            return 92
                        if (data['concave_points_worst'] <= 1569):
                            return 955.33333
                if (data['fractal_dimension_mean'] <= 6269):
                    if (data.get('concavity_se') is None):
                        return 6701.76923
                    if (data['concavity_se'] > 787):
                        if (data.get('concave_points_se') is None):
                            return 7232.78261
                        if (data['concave_points_se'] > 9821):
                            return 757
                        if (data['concave_points_se'] <= 9821):
                            if (data.get('concavity_worst') is None):
                                return 7527.13636
                            if (data['concavity_worst'] > 2399):
                                if (data['compactness_worst'] > 3522):
                                    return 9097.5
                                if (data['compactness_worst'] <= 3522):
                                    if (data.get('concave_points_mean') is None):
                                        return 7884.875
                                    if (data['concave_points_mean'] > 5912):
                                        return 8019.8
                                    if (data['concave_points_mean'] <= 5912):
                                        return 7660
                            if (data['concavity_worst'] <= 2399):
                                if (data.get('texture_worst') is None):
                                    return 7026.91667
                                if (data['texture_worst'] > 3241):
                                    return 7999.66667
                                if (data['texture_worst'] <= 3241):
                                    if (data.get('concave_points_mean') is None):
                                        return 6702.66667
                                    if (data['concave_points_mean'] > 5648):
                                        return 7261
                                    if (data['concave_points_mean'] <= 5648):
                                        if (data.get('texture_se') is None):
                                            return 6423.5
                                        if (data['texture_se'] > 1197):
                                            return 6570.5
                                        if (data['texture_se'] <= 1197):
                                            return 6129.5
                    if (data['concavity_se'] <= 787):
                        return 2630.66667
            if (data['area_mean'] <= 7349):
                if (data.get('fractal_dimension_se') is None):
                    return 7115.4887
                if (data['fractal_dimension_se'] > 2937):
                    if (data.get('texture_worst') is None):
                        return 7630.82639
                    if (data['texture_worst'] > 1892):
                        if (data.get('symmetry_se') is None):
                            return 8065.80909
                        if (data['symmetry_se'] > 3974):
                            return 849
                        if (data['symmetry_se'] <= 3974):
                            if (data.get('concave_points_mean') is None):
                                return 8132.01835
                            if (data['concave_points_mean'] > 9571):
                                return 1155
                            if (data['concave_points_mean'] <= 9571):
                                if (data.get('perimeter_mean') is None):
                                    return 8196.62037
                                if (data['perimeter_mean'] > 9814):
                                    return 4807
                                if (data['perimeter_mean'] <= 9814):
                                    if (data.get('smoothness_mean') is None):
                                        return 8260.57547
                                    if (data['smoothness_mean'] > 9942):
                                        return 5520.33333
                                    if (data['smoothness_mean'] <= 9942):
                                        if (data['fractal_dimension_mean'] > 6592):
                                            if (data.get('compactness_se') is None):
                                                return 9071.34615
                                            if (data['compactness_se'] > 3194):
                                                if (data['texture_worst'] > 2004):
                                                    if (data['compactness_se'] > 3409):
                                                        return 9879.6
                                                    if (data['compactness_se'] <= 3409):
                                                        return 9379
                                                if (data['texture_worst'] <= 2004):
                                                    return 8488
                                            if (data['compactness_se'] <= 3194):
                                                if (data.get('perimeter_se') is None):
                                                    return 8813.64706
                                                if (data['perimeter_se'] > 2388):
                                                    if (data['compactness_worst'] > 1731):
                                                        if (data['compactness_worst'] > 2147):
                                                            return 8866
                                                        if (data['compactness_worst'] <= 2147):
                                                            return 8512.5
                                                    if (data['compactness_worst'] <= 1731):
                                                        return 7860.5
                                                if (data['perimeter_se'] <= 2388):
                                                    if (data.get('symmetry_mean') is None):
                                                        return 9032.18182
                                                    if (data['symmetry_mean'] > 697):
                                                        if (data.get('radius_se') is None):
                                                            return 9118.33333
                                                        if (data['radius_se'] > 2755):
                                                            return 8968.75
                                                        if (data['radius_se'] <= 2755):
                                                            return 9238
                                                    if (data['symmetry_mean'] <= 697):
                                                        return 8644.5
                                        if (data['fractal_dimension_mean'] <= 6592):
                                            if (data['fractal_dimension_mean'] > 6572):
                                                return 1118
                                            if (data['fractal_dimension_mean'] <= 6572):
                                                if (data.get('texture_se') is None):
                                                    return 8185.35526
                                                if (data['texture_se'] > 2706):
                                                    if (data['concave_points_mean'] > 218):
                                                        if (data.get('perimeter_worst') is None):
                                                            return 9003.07143
                                                        if (data['perimeter_worst'] > 8823):
                                                            return 9462.66667
                                                        if (data['perimeter_worst'] <= 8823):
                                                            if (data['perimeter_mean'] > 7166):
                                                                if (data['concave_points_mean'] > 2165):
                                                                    return 8770.75
                                                                if (data['concave_points_mean'] <= 2165):
                                                                    return 8451.5
                                                            if (data['perimeter_mean'] <= 7166):
                                                                return 9133.8
                                                    if (data['concave_points_mean'] <= 218):
                                                        return 7738
                                                if (data['texture_se'] <= 2706):
                                                    if (data['area_mean'] > 6743):
                                                        return 9445.75
                                                    if (data['area_mean'] <= 6743):
                                                        if (data.get('smoothness_worst') is None):
                                                            return 7903.91228
                                                        if (data['smoothness_worst'] > 4895):
                                                            if (data.get('texture_mean') is None):
                                                                return 7078.71429
                                                            if (data['texture_mean'] > 2179):
                                                                return 6082
                                                            if (data['texture_mean'] <= 2179):
                                                                if (data['fractal_dimension_se'] > 4340):
                                                                    return 7980
                                                                if (data['fractal_dimension_se'] <= 4340):
                                                                    return 7142.33333
                                                        if (data['smoothness_worst'] <= 4895):
                                                            if (data['compactness_worst'] > 2990):
                                                                if (data.get('compactness_se') is None):
                                                                    return 8492
                                                                if (data['compactness_se'] > 3032):
                                                                    if (data['concave_points_mean'] > 6209):
                                                                        return 8312.33333
                                                                    if (data['concave_points_mean'] <= 6209):
                                                                        return 7851.33333
                                                                if (data['compactness_se'] <= 3032):
                                                                    return 9312.33333
                                                            if (data['compactness_worst'] <= 2990):
                                                                if (data['symmetry_se'] > 2167):
                                                                    if (data['perimeter_mean'] > 7369):
                                                                        return 7014.33333
                                                                    if (data['perimeter_mean'] <= 7369):
                                                                        if (data.get('concave_points_se') is None):
                                                                            return 7811.36364
                                                                        if (data['concave_points_se'] > 1258):
                                                                            if (data.get('texture_mean') is None):
                                                                                return 7676.42857
                                                                            if (data['texture_mean'] > 211):
                                                                                return 7574.6
                                                                            if (data['texture_mean'] <= 211):
                                                                                return 7931
                                                                        if (data['concave_points_se'] <= 1258):
                                                                            return 8047.5
                                                                if (data['symmetry_se'] <= 2167):
                                                                    if (data.get('symmetry_mean') is None):
                                                                        return 8058.37037
                                                                    if (data['symmetry_mean'] > 1509):
                                                                        if (data.get('radius_worst') is None):
                                                                            return 8225.05263
                                                                        if (data['radius_worst'] > 150):
                                                                            if (data.get('radius_mean') is None):
                                                                                return 8291.77778
                                                                            if (data['radius_mean'] > 1254):
                                                                                if (data['perimeter_mean'] > 1131):
                                                                                    if (data['compactness_worst'] > 2247):
                                                                                        return 8329.66667
                                                                                    if (data['compactness_worst'] <= 2247):
                                                                                        return 8561.6
                                                                                if (data['perimeter_mean'] <= 1131):
                                                                                    return 8166.5
                                                                            if (data['radius_mean'] <= 1254):
                                                                                if (data['compactness_worst'] > 2100):
                                                                                    return 7764
                                                                                if (data['compactness_worst'] <= 2100):
                                                                                    return 8194
                                                                        if (data['radius_worst'] <= 150):
                                                                            return 7024
                                                                    if (data['symmetry_mean'] <= 1509):
                                                                        if (data.get('radius_se') is None):
                                                                            return 7662.5
                                                                        if (data['radius_se'] > 3948):
                                                                            return 7235
                                                                        if (data['radius_se'] <= 3948):
                                                                            if (data['smoothness_mean'] > 585):
                                                                                return 7715.8
                                                                            if (data['smoothness_mean'] <= 585):
                                                                                return 8251
                    if (data['texture_worst'] <= 1892):
                        if (data['fractal_dimension_se'] > 4125):
                            if (data['fractal_dimension_mean'] > 7200):
                                return 968
                            if (data['fractal_dimension_mean'] <= 7200):
                                if (data.get('symmetry_worst') is None):
                                    return 7888.57143
                                if (data['symmetry_worst'] > 2439):
                                    if (data['fractal_dimension_mean'] > 6179):
                                        if (data.get('perimeter_worst') is None):
                                            return 9078.28571
                                        if (data['perimeter_worst'] > 7263):
                                            return 9461.25
                                        if (data['perimeter_worst'] <= 7263):
                                            return 8567.66667
                                    if (data['fractal_dimension_mean'] <= 6179):
                                        return 7706.66667
                                if (data['symmetry_worst'] <= 2439):
                                    if (data.get('concave_points_se') is None):
                                        return 7181.09091
                                    if (data['concave_points_se'] > 1475):
                                        if (data.get('concavity_worst') is None):
                                            return 7434.33333
                                        if (data['concavity_worst'] > 1551):
                                            if (data['concave_points_se'] > 2083):
                                                return 7186.33333
                                            if (data['concave_points_se'] <= 2083):
                                                return 7390.33333
                                        if (data['concavity_worst'] <= 1551):
                                            return 7726.33333
                                    if (data['concave_points_se'] <= 1475):
                                        return 6041.5
                        if (data['fractal_dimension_se'] <= 4125):
                            if (data.get('concave_points_se') is None):
                                return 4000.36364
                            if (data['concave_points_se'] > 1273):
                                if (data['compactness_worst'] > 903):
                                    if (data['fractal_dimension_mean'] > 6126):
                                        return 8415
                                    if (data['fractal_dimension_mean'] <= 6126):
                                        return 6517.5
                                if (data['compactness_worst'] <= 903):
                                    return 1020.5
                            if (data['concave_points_se'] <= 1273):
                                if (data['fractal_dimension_mean'] > 6669):
                                    return 1071.5
                                if (data['fractal_dimension_mean'] <= 6669):
                                    return 770
                if (data['fractal_dimension_se'] <= 2937):
                    if (data.get('radius_mean') is None):
                        return 6762.11429
                    if (data['radius_mean'] > 9815):
                        return 793.5
                    if (data['radius_mean'] <= 9815):
                        if (data.get('concave_points_se') is None):
                            return 6819.50481
                        if (data['concave_points_se'] > 8928):
                            if (data.get('smoothness_mean') is None):
                                return 5629.86957
                            if (data['smoothness_mean'] > 1014):
                                if (data.get('texture_worst') is None):
                                    return 6677.47368
                                if (data['texture_worst'] > 3799):
                                    return 722
                                if (data['texture_worst'] <= 3799):
                                    if (data.get('smoothness_worst') is None):
                                        return 7008.33333
                                    if (data['smoothness_worst'] > 1254):
                                        if (data.get('texture_se') is None):
                                            return 7460.125
                                        if (data['texture_se'] > 3639):
                                            return 7907
                                        if (data['texture_se'] <= 3639):
                                            return 7192
                                    if (data['smoothness_worst'] <= 1254):
                                        if (data.get('texture_se') is None):
                                            return 6646.9
                                        if (data['texture_se'] > 1206):
                                            if (data.get('radius_se') is None):
                                                return 6535.125
                                            if (data['radius_se'] > 2067):
                                                return 6390.6
                                            if (data['radius_se'] <= 2067):
                                                return 6776
                                        if (data['texture_se'] <= 1206):
                                            return 7094
                            if (data['smoothness_mean'] <= 1014):
                                return 653.75
                        if (data['concave_points_se'] <= 8928):
                            if (data.get('symmetry_mean') is None):
                                return 6967.4054
                            if (data['symmetry_mean'] > 2177):
                                return 12
                            if (data['symmetry_mean'] <= 2177):
                                if (data.get('symmetry_worst') is None):
                                    return 7005.20652
                                if (data['symmetry_worst'] > 2203):
                                    if (data.get('area_worst') is None):
                                        return 7233.96753
                                    if (data['area_worst'] > 9808):
                                        return 974
                                    if (data['area_worst'] <= 9808):
                                        if (data['area_mean'] > 316):
                                            if (data.get('concavity_se') is None):
                                                return 7315.61184
                                            if (data['concavity_se'] > 92):
                                                if (data.get('compactness_mean') is None):
                                                    return 7364.2
                                                if (data['compactness_mean'] > 8439):
                                                    if (data.get('perimeter_se') is None):
                                                        return 6367.16667
                                                    if (data['perimeter_se'] > 1640):
                                                        if (data['fractal_dimension_se'] > 1847):
                                                            if (data['concave_points_se'] > 8502):
                                                                return 7147
                                                            if (data['concave_points_se'] <= 8502):
                                                                if (data.get('concave_points_mean') is None):
                                                                    return 8090.625
                                                                if (data['concave_points_mean'] > 2532):
                                                                    if (data['fractal_dimension_mean'] > 6139):
                                                                        return 8085
                                                                    if (data['fractal_dimension_mean'] <= 6139):
                                                                        return 8348.66667
                                                                if (data['concave_points_mean'] <= 2532):
                                                                    return 7836.33333
                                                        if (data['fractal_dimension_se'] <= 1847):
                                                            if (data.get('concave_points_mean') is None):
                                                                return 6611
                                                            if (data['concave_points_mean'] > 6770):
                                                                return 6012
                                                            if (data['concave_points_mean'] <= 6770):
                                                                return 7010.33333
                                                    if (data['perimeter_se'] <= 1640):
                                                        return 845
                                                if (data['compactness_mean'] <= 8439):
                                                    if (data['fractal_dimension_mean'] > 6304):
                                                        if (data['compactness_worst'] > 1819):
                                                            if (data.get('smoothness_se') is None):
                                                                return 9001.66667
                                                            if (data['smoothness_se'] > 2562):
                                                                if (data.get('concave_points_mean') is None):
                                                                    return 8739.66667
                                                                if (data['concave_points_mean'] > 323):
                                                                    return 8851
                                                                if (data['concave_points_mean'] <= 323):
                                                                    return 8183
                                                            if (data['smoothness_se'] <= 2562):
                                                                return 9525.66667
                                                        if (data['compactness_worst'] <= 1819):
                                                            if (data['area_worst'] > 3533):
                                                                if (data.get('concave_points_worst') is None):
                                                                    return 8032.11111
                                                                if (data['concave_points_worst'] > 6260):
                                                                    return 7748.75
                                                                if (data['concave_points_worst'] <= 6260):
                                                                    return 8258.8
                                                            if (data['area_worst'] <= 3533):
                                                                return 7338.25
                                                    if (data['fractal_dimension_mean'] <= 6304):
                                                        if (data.get('compactness_se') is None):
                                                            return 7339.67273
                                                        if (data['compactness_se'] > 70):
                                                            if (data.get('smoothness_worst') is None):
                                                                return 7399.6729
                                                            if (data['smoothness_worst'] > 1335):
                                                                if (data.get('concavity_worst') is None):
                                                                    return 7807.97297
                                                                if (data['concavity_worst'] > 1258):
                                                                    if (data['fractal_dimension_se'] > 1058):
                                                                        if (data['concavity_worst'] > 4019):
                                                                            if (data.get('smoothness_mean') is None):
                                                                                return 7210
                                                                            if (data['smoothness_mean'] > 9565):
                                                                                return 7520
                                                                            if (data['smoothness_mean'] <= 9565):
                                                                                return 6900
                                                                        if (data['concavity_worst'] <= 4019):
                                                                            if (data['area_worst'] > 7027):
                                                                                return 7507
                                                                            if (data['area_worst'] <= 7027):
                                                                                if (data['compactness_worst'] > 228):
                                                                                    if (data.get('area_se') is None):
                                                                                        return 8078.52941
                                                                                    if (data['area_se'] > 1251):
                                                                                        if (data.get('smoothness_se') is None):
                                                                                            return 7986.25
                                                                                        if (data['smoothness_se'] > 4797):
                                                                                            if (data['concave_points_se'] > 949):
                                                                                                if (data['fractal_dimension_mean'] > 5742):
                                                                                                    return 7805.4
                                                                                                if (data['fractal_dimension_mean'] <= 5742):
                                                                                                    return 7992.66667
                                                                                            if (data['concave_points_se'] <= 949):
                                                                                                return 8122
                                                                                        if (data['smoothness_se'] <= 4797):
                                                                                            return 8293
                                                                                    if (data['area_se'] <= 1251):
                                                                                        return 8300
                                                                                if (data['compactness_worst'] <= 228):
                                                                                    return 7476.5
                                                                    if (data['fractal_dimension_se'] <= 1058):
                                                                        if (data['compactness_se'] > 1932):
                                                                            return 8315
                                                                        if (data['compactness_se'] <= 1932):
                                                                            return 9351.5
                                                                if (data['concavity_worst'] <= 1258):
                                                                    if (data['fractal_dimension_mean'] > 3059):
                                                                        return 6856.8
                                                                    if (data['fractal_dimension_mean'] <= 3059):
                                                                        return 7814.5
                                                            if (data['smoothness_worst'] <= 1335):
                                                                if (data['fractal_dimension_mean'] > 5543):
                                                                    if (data.get('radius_worst') is None):
                                                                        return 7364.6
                                                                    if (data['radius_worst'] > 2439):
                                                                        return 8757.5
                                                                    if (data['radius_worst'] <= 2439):
                                                                        if (data['fractal_dimension_se'] > 2435):
                                                                            if (data.get('concavity_worst') is None):
                                                                                return 7829.09091
                                                                            if (data['concavity_worst'] > 2295):
                                                                                if (data.get('smoothness_se') is None):
                                                                                    return 7566.33333
                                                                                if (data['smoothness_se'] > 7595):
                                                                                    return 7335.5
                                                                                if (data['smoothness_se'] <= 7595):
                                                                                    return 7681.75
                                                                            if (data['concavity_worst'] <= 2295):
                                                                                return 8144.4
                                                                        if (data['fractal_dimension_se'] <= 2435):
                                                                            if (data.get('concave_points_mean') is None):
                                                                                return 7176.61905
                                                                            if (data['concave_points_mean'] > 2398):
                                                                                if (data['fractal_dimension_se'] > 2278):
                                                                                    return 7632.5
                                                                                if (data['fractal_dimension_se'] <= 2278):
                                                                                    if (data.get('smoothness_mean') is None):
                                                                                        return 6816.61538
                                                                                    if (data['smoothness_mean'] > 9706):
                                                                                        return 7178
                                                                                    if (data['smoothness_mean'] <= 9706):
                                                                                        if (data.get('symmetry_se') is None):
                                                                                            return 6750.90909
                                                                                        if (data['symmetry_se'] > 2936):
                                                                                            return 6435
                                                                                        if (data['symmetry_se'] <= 2936):
                                                                                            return 6782.5
                                                                            if (data['concave_points_mean'] <= 2398):
                                                                                if (data['compactness_worst'] > 1186):
                                                                                    if (data['fractal_dimension_mean'] > 5826):
                                                                                        if (data.get('smoothness_mean') is None):
                                                                                            return 7637.6
                                                                                        if (data['smoothness_mean'] > 8575):
                                                                                            if (data.get('texture_mean') is None):
                                                                                                return 7757.42857
                                                                                            if (data['texture_mean'] > 1577):
                                                                                                return 7688.6
                                                                                            if (data['texture_mean'] <= 1577):
                                                                                                return 7929.5
                                                                                        if (data['smoothness_mean'] <= 8575):
                                                                                            return 7358
                                                                                    if (data['fractal_dimension_mean'] <= 5826):
                                                                                        if (data.get('concavity_worst') is None):
                                                                                            return 7247.44444
                                                                                        if (data['concavity_worst'] > 1718):
                                                                                            return 7056.83333
                                                                                        if (data['concavity_worst'] <= 1718):
                                                                                            return 7628.66667
                                                                                if (data['compactness_worst'] <= 1186):
                                                                                    if (data['concave_points_se'] > 6305):
                                                                                        return 6862.75
                                                                                    if (data['concave_points_se'] <= 6305):
                                                                                        return 7120.75
                                                                if (data['fractal_dimension_mean'] <= 5543):
                                                                    if (data.get('texture_se') is None):
                                                                        return 6521.13333
                                                                    if (data['texture_se'] > 1030):
                                                                        if (data['symmetry_mean'] > 1648):
                                                                            if (data.get('smoothness_se') is None):
                                                                                return 6350.42857
                                                                            if (data['smoothness_se'] > 5882):
                                                                                return 6202.75
                                                                            if (data['smoothness_se'] <= 5882):
                                                                                return 6547.33333
                                                                        if (data['symmetry_mean'] <= 1648):
                                                                            if (data.get('concave_points_mean') is None):
                                                                                return 6960.33333
                                                                            if (data['concave_points_mean'] > 1532):
                                                                                return 6825.75
                                                                            if (data['concave_points_mean'] <= 1532):
                                                                                return 7229.5
                                                                    if (data['texture_se'] <= 1030):
                                                                        return 5801
                                                        if (data['compactness_se'] <= 70):
                                                            return 5199.66667
                                            if (data['concavity_se'] <= 92):
                                                return 3671.5
                                        if (data['area_mean'] <= 316):
                                            return 1084
                                if (data['symmetry_worst'] <= 2203):
                                    if (data['symmetry_worst'] > 324):
                                        if (data.get('concavity_se') is None):
                                            return 3483.63636
                                        if (data['concavity_se'] > 1617):
                                            return 706.6
                                        if (data['concavity_se'] <= 1617):
                                            if (data['concave_points_se'] > 5777):
                                                return 733
                                            if (data['concave_points_se'] <= 5777):
                                                return 6810.8
                                    if (data['symmetry_worst'] <= 324):
                                        if (data.get('texture_mean') is None):
                                            return 7189.84211
                                        if (data['texture_mean'] > 172):
                                            if (data['fractal_dimension_mean'] > 6277):
                                                return 9130
                                            if (data['fractal_dimension_mean'] <= 6277):
                                                if (data['symmetry_mean'] > 1703):
                                                    return 6704.8
                                                if (data['symmetry_mean'] <= 1703):
                                                    if (data['fractal_dimension_mean'] > 5833):
                                                        return 8049.66667
                                                    if (data['fractal_dimension_mean'] <= 5833):
                                                        if (data.get('smoothness_mean') is None):
                                                            return 7270.42857
                                                        if (data['smoothness_mean'] > 8063):
                                                            if (data.get('compactness_se') is None):
                                                                return 7422
                                                            if (data['compactness_se'] > 1220):
                                                                return 7588.33333
                                                            if (data['compactness_se'] <= 1220):
                                                                return 7172.5
                                                        if (data['smoothness_mean'] <= 8063):
                                                            return 6891.5
                                        if (data['texture_mean'] <= 172):
                                            return 651
