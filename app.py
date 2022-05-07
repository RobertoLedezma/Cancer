import streamlit as st
st.title('Cáncer💉🩸')
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
