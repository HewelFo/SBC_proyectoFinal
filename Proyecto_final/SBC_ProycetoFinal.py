# Proyecto final de Sistemas basados en concimeotn
# integrantes:
# Dahian Ramirez
# Hewel Ochoa 
# Guillermo Rivas
# Guillermo Hernandez
#

from xml.dom.expatbuilder import ElementInfo

def from_resultados(Resultados):
    print('Despues de la evaluacion los resultados son:')
    for x in Resultados:
        print(x + ': ' + Resultados[x])

if (__name__=='__main__'):
    Resultados = {'turbidez':"", 'Ph':"", 'conductividad':"", 'temperatura':"", 'redox':""}
    valor_de_riesgo = 0
    medida = 0
    conti = 1
    print('vamos a tomar como esto como un ejemplo \n')

    while(conti == 1):
#............................................incia el SBC XD....................................................................
        medida = input('¿Desea saber el riesgo de las plecopteras? -> si or no\n')
        if medida == 'si':
            medida = input('¿Los sensores estan funcionando? -> si or no\n')
            if medida == 'si':

#-----------------------------------------tubidez de la agua------------------------------------------------------------------
                medida = int(input('¿De cuanto es la turbidez del agua?\n'))
                if medida < 5:
                    Resultados['turbidez'] = 'La turbidez es baja, el agua es bastante clara no hay problemas'
#----------------------------------------respuesta peligrosa pregunta 1----------------------------------------------------------------
                else:
                    Resultados['turbidez'] = 'La turbidez del agua es alta y la luz no puede atravezarla muy bien, avisa a las autpridad y los expeertos'
                    valor_de_riesgo = valor_de_riesgo + 30
#-----------------------------------------Ph del agua---------------------------------------------------------------------------------                
                medida = int(input('¿Cual es el Ph del agua?\n'))
                if medida <= 8 and medida >= 6:
                    Resultados['Ph'] = 'El Ph del agua esta en el rango normal'

#----------------------------------------respuestas peligrosas prgunta 2----------------------------------------------------------------
                elif medida >= 9:
                    Resultados['Ph'] = 'El agua es en peligro de ser alcanina'
                    valor_de_riesgo = valor_de_riesgo + 10
                else:
                    Resultados['Ph'] = 'El agua esta en peligro de ser acida'
                    valor_de_riesgo = valor_de_riesgo + 20

#----------------------------------------condiuctividad---------------------------------------------------------------------------------
                medida = int(input('¿Cual es la conductividad del agua?\n'))
                if medida <= 800 and medida >= 400:
                    Resultados['conductividad'] = 'El rango de conductividad es normal'
#-----------------------------------------respuestas peligroos pregunta 3-------------------------------------------------------
                elif medida < 400:
                    Resultados['conductividad'] = 'La conductividad del agua es muy alta, llama a las autoridades'
                    valor_de_riesgo = valor_de_riesgo + 20
                else:
                    Resultados['conductividad'] = 'La conductividad del agua es muy baja, llama a los expertos'
                    valor_de_riesgo = valor_de_riesgo + 10
#-----------------------------------------incia la tercera pregunta--------------------------------------------------------------------
                medida = int(input('¿Cual es al temperatura del agua?\n'))
                if medida <= 30 and medida >= 20:
                    Resultados['temperatura'] = 'La temperatura del agua se encuentra en el rango indicado, todo va bien'
#-------------------------------------------respuestas peligrosas de la pregunta 4-----------------------------------------------------
                elif medida > 30:
                    Resultados['temperatura'] = 'La temperatura del agua es muy alta, avisale a los expertos'
                    valor_de_riesgo = valor_de_riesgo + 10
                else:
                    Resultados['temperatura'] = 'La temperatura del agua es muy baja, llama a las autoridades pudo acurrir un accidente'
                    valor_de_riesgo = valor_de_riesgo + 20
#-------------------------------------------potencial de oxidciono del agua---------------------------------------------------------------
                medida = int(input('¿De cuanto es el potencial de redox del agua?'))
                if medida <= 950 and medida >= 850:
                    Resultados['redox'] = 'La oxidacion del agua es esta en niveles sanos, no hay problemas'
#--------------------------------------------respuesta peligrosas pregutna 5--------------------------------------------------------------
                elif medida < 950:
                    Resultados['redox'] = 'La oxidacion del agua es muy baja, puede haber una disminucion en los nutrientes del agua'
                    valor_de_riesgo = valor_de_riesgo + 20
                else:
                    Resultados['redox'] = 'La oxidacion del agua es muy alta, puedo haber un accidente, avisar a las autorida'
                    valor_de_riesgo = valor_de_riesgo + 20
            else:
                print('El sistema fisico FALLO revicion inmediata')
                break
        if Resultados['redox'] and Resultados['conductividad'] and Resultados['temperatura'] and Resultados['Ph'] and Resultados['turbidez'] != "":
            from_resultados(Resultados)
            print('El valor de riesgo es: ' + str(valor_de_riesgo))


        conti = int(input('para salir 0 | continuar 1\n'))



