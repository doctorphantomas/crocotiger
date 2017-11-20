
# coding: utf-8

# In[18]:


import math
altura=float(input('Introduce tu altura en metros: '))
peso=float(input('Introduce tu peso en kg: '))   
cintura=float(input('Introduce la medida de la circunferencia de tu cintura en cm: '))
cuello=float(input('Introduce la medida de la circunferencia de tu cuello en cm: '))
cadera=float(input('Introduce la medida de la circunferencia de tu cadera en cm: '))
sexo=input('Introduce tu sexo: Hombre o Mujer: ')
#función del imc
def imc(peso,altura):
    imc=peso/(altura*altura)
    if imc<=18.5:
        print ('Tu IMC es: ',imc ,'Estás demasiado delgado')
    elif imc>18.5 and imc<=25:
        print ('Tu IMC es: ',imc ,'Tu peso es normal')    
    elif imc>25 and imc<=30:
        print ('Tu IMC es: ',imc ,'Tienes sobrepeso') 
    elif imc>30 and imc<40:
        print ('Tu IMC es: ',imc ,'Tienes obesidad')
    elif imc>=40:
        print ('Tu IMC es: ',imc ,'Tienes obesidad mórbida')   
    else:
        print ('Introduce datos validos')
    return imc    
    

#función del indice cintura/altura
def ica(cintura,altura):
    sexo2=sexo.lower()
    ica=cintura/(altura*100)
    if sexo2=="mujer":
        if ica<=0.34:
            print ('Tu ICA es: ',ica ,'Estás demasiado delgada')
        elif ica>0.34 and ica<=0.41:
            print ('Tu ICA es: ',ica ,'Estás delgada,pero en un margen sano') 
        elif ica>0.41 and ica<=0.48:
            print ('Tu ICA es: ',ica ,'Estás en un peso normal') 
        elif ica>0.48 and ica<=0.53:
            print ('Tu ICA es: ',ica ,'Tienes sobrepeso')    
        elif ica>0.53 and ica<=0.57:
            print ('Tu ICA es: ',ica ,'Tienes sobrepeso elevado,estás obesa')
        elif ica>0.58:
            print ('Tu ICA es: ',ica ,'Tienes obesidad mórbida')
        else:
            print('Introduce unos datos validos')  
        return ica    
    if sexo2=="hombre":
        if ica<=0.34:
            print ('Tu ICA es: ',ica ,'Estás demasiado delgado')
        elif ica>0.34 and ica<=0.42:
            print ('Tu ICA es: ',ica ,'Estás delgada,pero en un margen sano') 
        elif ica>0.42 and ica<=0.52:
            print ('Tu ICA es: ',ica ,'Estás en un peso normal') 
        elif ica>0.53 and ica<=0.57:
            print ('Tu ICA es: ',ica ,'Tienes sobrepeso')    
        elif ica>0.58 and ica<=0.62:
            print ('Tu ICA es: ',ica ,'Tienes sobrepeso elevado,estás obeso')
        elif ica>0.62:
            print ('Tu ICA es: ',ica ,'Tienes obesidad mórbida')   
        else:
            print('Introduce unos datos validos')
        return ica 
#función para calcular porcentaje de grasa
def grasa_porcentaje(cintura,cuello,altura,cadera):
    sexo2=sexo.lower()
    if sexo2=="mujer":
        grasa_porcentaje=495/(1.29579-0.35004*(math.log10(cintura+cadera-cuello))+0.22100*(math.log10(altura*100)))-450
        if grasa_porcentaje<=13:
            print ('Tu porcentaje de grasa corporal es: ',grasa_porcentaje ,'Tienes la grasa esencial para vivir.')
        elif grasa_porcentaje>13 and grasa_porcentaje<=20:
            print ('Tu porcentaje de grasa corporal es: ',grasa_porcentaje ,'Tienes un nivel de grasa propio de un atleta.')
        elif grasa_porcentaje>=21 and grasa_porcentaje<=24:
            print ('Tu porcentaje de grasa corporal es: ',grasa_porcentaje ,'Tienes un nivel de grasa bajo,cuerpo fitness')
        elif grasa_porcentaje>=25 and grasa_porcentaje<=31:
            print ('Tu porcentaje de grasa corporal es: ',grasa_porcentaje ,'Tienes un nivel de grasa aceptable')
        elif grasa_porcentaje>=32:
            print ('Tu porcentaje de grasa corporal es: ',grasa_porcentaje ,'Tienes un nivel de grasa alto')
        else:
            print('Introduce unos datos validos')
            
        return grasa_porcentaje    
            
            
            
    if sexo2=="hombre":
        grasa_porcentaje=495/(1.0324-0.19077*(math.log10(cintura-cuello))+0.15456*(math.log10(altura*100)))-450
        if grasa_porcentaje<=5:
            print ('Tu porcentaje de grasa corporal es: ',grasa_porcentaje ,'Tienes la grasa esencial para vivir.')
        elif grasa_porcentaje>=6 and grasa_porcentaje<=3:
            print ('Tu porcentaje de grasa corporal es: ',grasa_porcentaje ,'Tienes un nivel de grasa propio de un atleta.')
        elif grasa_porcentaje>=14 and grasa_porcentaje<=17:
            print ('Tu porcentaje de grasa corporal es: ',grasa_porcentaje ,'Tienes un nivel de grasa bajo,cuerpo fitness')
        elif grasa_porcentaje>=18 and grasa_porcentaje<=25:
            print ('Tu porcentaje de grasa corporal es: ',grasa_porcentaje ,'Tienes un nivel de grasa aceptable')
        elif grasa_porcentaje>=26:
            print ('Tu porcentaje de grasa corporal es: ',grasa_porcentaje ,'Tienes un nivel de grasa alto')
        else:
            print('Introduce unos datos validos')
            
        return grasa_porcentaje
    
    
    
    
    
imc(peso,altura)
ica(cintura,altura) 
grasa_porcentaje(cintura,cuello,altura,cadera)

