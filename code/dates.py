def fecha_es_tupla(fecha):
    return type(fecha) is tuple and len(fecha) == 3


def fecha_es_vailida(fecha):
    if fecha_es_tupla(fecha):
        anno = fecha[0]
        mes = fecha[1]
        dia = fecha[2]

        if dia > 0 and 0 < mes <= 12:
            if anno > 1582:
                if mes == 2:
                    if bisiesto(fecha):
                        if dia <= 29:
                            return True
                        else:
                            return False
                    else:
                        if dia <= 28:
                            return True
                        else:
                            return False
                elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
                    if dia <= 30:
                        return True
                    else:
                        return False
                else:
                    if dia <= 31:
                        return True
            elif anno == 1582:
                if mes > 10:
                    if mes == 11:
                        if dia <= 30:
                            return True
                        else:
                            return False
                    else:
                        if dia <= 31:
                            return True
                elif mes == 10:
                    if 15 <= dia <= 31:
                        return True

    return False


def bisiesto(fecha):
    if fecha_es_tupla(fecha):
        anno = fecha[0]
        if (anno % 400 == 0) or (anno % 100 != 0) and (anno % 4 == 0):
            return True
        else:
            return False
    else:
        return None


def dia_siguiente(fecha):
    if fecha_es_vailida(fecha):
        anno = fecha[0]
        mes = fecha[1]
        dia = fecha[2]

        if mes == 2:
            if bisiesto(fecha):
                if dia == 29:
                    annoNuevo = anno
                    mesNuevo = mes + 1
                    diaNuevo = 1
                else:
                    annoNuevo = anno
                    mesNuevo = mes
                    diaNuevo = dia + 1
            else:
                if dia == 28:
                    annoNuevo = anno
                    mesNuevo = mes + 1
                    diaNuevo = 1
                else:
                    annoNuevo = anno
                    mesNuevo = mes
                    diaNuevo = dia + 1
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            if dia == 30:
                annoNuevo = anno
                mesNuevo = mes + 1
                diaNuevo = 1
            else:
                annoNuevo = anno
                mesNuevo = mes
                diaNuevo = dia + 1
        elif mes == 12 and dia == 31:
            annoNuevo = anno + 1
            mesNuevo = 1
            diaNuevo = 1
        else:
            if dia == 31:
                annoNuevo = anno
                mesNuevo = mes + 1
                diaNuevo = 1
            else:
                annoNuevo = anno
                mesNuevo = mes
                diaNuevo = dia + 1
    else:
        return None

    return (annoNuevo, mesNuevo, diaNuevo)


def ordinal_dia(fecha):
    if fecha_es_vailida(fecha):
        anno = fecha[0]
        mes = fecha[1]
        dia = fecha[2]

        count = 0
        i = 1  # Empieza en uno
        while i < mes:
            if i == 2:
                # Calcula si el febrero de ese año es bisiesto
                if bisiesto((anno, i, dia)):
                    count += 29
                else:
                    count += 28
            elif i == 4 or i == 6 or i == 9 or i == 11:
                count += 30
            else:
                count += 31
            i += 1

        i = 1
        while i < dia:
            i += 1

        count += i
        return count
    else:
        return None

def imprimir_mes(dias):
    diaSemana=1
    semana=''
    salida=[]
    for i in range (1,dias+1):
        if diaSemana == 7:
            semana = semana + str(i)
            salida.append(semana)
            semana = ''
            #print(str(i)+'  ', end="")
            # print(space.rjust(0, ' '), end ='')
            diaSemana=1     
        else:
            if i<10:
                semana= semana+str(i)+'  '
##                print(str(i)+'  ', end="") 
                diaSemana += 1
                
            else:
                semana = semana + str(i)+' '
                diaSemana += 1
                
    salida.append(semana)
    return salida 


def imprimir_3x4(anno):
    meses ={1:'Enero', 2:'Febrero', 3:'Marzo',  
        4:'Abril', 5:'Mayo', 6:'Junio', 7:'Julio', 
        8:'Agosto', 9:'Setiembre', 10:'Octubre', 
        11:'Noviembre', 12:'Diciembre'}
    diaSemana='D '+ " " +'L '+ " " + 'K ' + " " + 'M ' + " " + 'J ' + " " + 'V ' + " " + 'S'
    if anno > 1582:
        print('Calendario del año ' + str(anno) + ' D.C'+'\n')
        mesActual = 1
        while mesActual <= 12:
            print('\n''{:^30}{:^2}{:^30}{:^2}{:^30}{:^2}{:^30}'.format(meses[mesActual],'|',meses[mesActual+1],'|',meses[mesActual+2],'|',meses[mesActual+3]))
            print('{:^30}{:^2}{:^30}{:^2}{:^30}{:^2}{:^30}'.format(diaSemana,'|',diaSemana,'|',diaSemana,'|',diaSemana))
            index = 1
            calendario=[]
            while index <=4:
                if mesActual == 4 or mesActual == 6 or mesActual == 9 or mesActual == 11:
                    calendario.append(imprimir_mes(30))
                    index +=1
                    mesActual +=1
                    
                elif mesActual == 2:
                    if bisiesto(anno) == True :
                        calendario.append(imprimir_mes(29))
                        mesActual +=1
                        index +=1
                    else:
                        calendario.append(imprimir_mes(28))
                        mesActual +=1
                        index +=1
                else:
                    calendario.append(imprimir_mes(31))
                    mesActual +=1
                    index +=1
                    
            fila = 0
            while fila < len(max(calendario)):
                print('{:^30}{:^2}{:^30}{:^2}{:^30}{:^2}{:^30}'.format(calendario[0][fila],'|',calendario[1][fila],'|',calendario[2][fila],'|',calendario[3][fila]))
                fila += 1      

    else:
        return "Ingrese un año perteneciente al rango permitido."

##print(imprimir_mes(31))
##diaSemana='D '+ " " +'L '+ " " + 'K ' + " " + 'M ' + " " + 'J ' + " " + 'V ' + " " + 'S'
##print('{:^30}{:^30}'.format('Enero','Febrero'))
##print('{:^30}{:^30}'.format(diaSemana,diaSemana))
##print('{:^30}{:^30}'.format(imprimir_mes(31),imprimir_mes(30)))
##print('\n' '{:^30}{:^30}'.format('Enero','Febrero'))

imprimir_3x4(2000)
##n=31
##diaSemana=1
##space =''
##
##for i in range (1,n+1):
##    if diaSemana > 7:
##        print()
##        if i < 10:
##            print(str(i)+'  ', end="")
##           ## print(space.rjust(0, ' '), end ='')
##            diaSemana=2
##        else:
##            print(str(i)+' ', end="")
##            ##print(space.rjust(0, ' '), end ='')
##            diaSemana=2
##    else:
##        if i<10:
##            print(str(i)+'  ', end="") 
##            diaSemana += 1
##            
##        else:
##            print(str(i)+' ', end="") 
##            diaSemana += 1
        



        
if __name__ == '__main__':
    prueba = (1582, 10, 14)
    print(fecha_es_vailida(prueba))
  ##  print(imprimir_3x4(2000))
