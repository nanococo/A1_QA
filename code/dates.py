from datetime import datetime

# Esta función se encarga de validar si una variable de entrada es una tupla de tamaño 3.
def fecha_es_tupla(fecha):
    return type(fecha) is tuple and len(fecha) == 3


# Esta función se encarga de revisar si una fecha está dentro de un rango permitido en cuanto a formato y rango del
# calendario gregoriano.
def fecha_es_valida(fecha):
    if fecha_es_tupla(fecha):
        anno = fecha[0]
        mes = fecha[1]
        dia = fecha[2]

        if dia > 0 and 0 < mes <= 12:
            if anno > 1582:
                if mes == 2:
                    if bisiesto(anno):
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


# Esta función recibe un int año y se encarga de revisar si es o no un bisiesto
def bisiesto(anno):
    if type(anno) == int:
        if anno > 1582:
            if (anno % 400 == 0) or (anno % 100 != 0) and (anno % 4 == 0):
                return True
            else:
                return False
        else:
            return "Error, seleccione un año mayor a 1582"
    else:
        return "Error, la funcion bisiesto debe recibir un numero entero"


# Esta función se encarga de generar una tupla de tipo fecha con la fecha del día siguiente al que entra a la funcion
def dia_siguiente(fecha):
    if fecha_es_valida(fecha):
        anno = fecha[0]
        mes = fecha[1]
        dia = fecha[2]

        if mes == 2:
            if bisiesto(anno):
                if dia == 29:
                    anno_nuevo = anno
                    mes_nuevo = mes + 1
                    dia_nuevo = 1
                else:
                    anno_nuevo = anno
                    mes_nuevo = mes
                    dia_nuevo = dia + 1
            else:
                if dia == 28:
                    anno_nuevo = anno
                    mes_nuevo = mes + 1
                    dia_nuevo = 1
                else:
                    anno_nuevo = anno
                    mes_nuevo = mes
                    dia_nuevo = dia + 1
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            if dia == 30:
                anno_nuevo = anno
                mes_nuevo = mes + 1
                dia_nuevo = 1
            else:
                anno_nuevo = anno
                mes_nuevo = mes
                dia_nuevo = dia + 1
        elif mes == 12 and dia == 31:
            anno_nuevo = anno + 1
            mes_nuevo = 1
            dia_nuevo = 1
        else:
            if dia == 31:
                anno_nuevo = anno
                mes_nuevo = mes + 1
                dia_nuevo = 1
            else:
                anno_nuevo = anno
                mes_nuevo = mes
                dia_nuevo = dia + 1
    else:
        return "Error, la fecha no es valida"

    return anno_nuevo, mes_nuevo, dia_nuevo


# Esta funcion se encarga de calcular el día del año
def ordinal_dia(fecha):
    if fecha_es_valida(fecha):
        anno = fecha[0]
        mes = fecha[1]
        dia = fecha[2]

        if anno > 1582:
            count = 0
            i = 1  # Empieza en uno
            while i < mes:
                if i == 2:
                    # Calcula si el febrero de ese año es bisiesto
                    if bisiesto(anno):
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
            return "Error, seleccione un año mayor a 1582"
    else:
        return "Error, la fecha no es valida"


# Esta función se encarga en realizar una lista con las filas que se mostraran en el calendario 3x4 , estas dependen del mes. 
# Toma en cuenta el dia de la semana en el que inicia el mes.
def imprimir_mes(dias, dia_semana):
    semana_temp = []
    semana = ''  # Esta variable guarda 'cada semana' del mes que se ingreso , lista para imprimir
    salida = []  # Esta variable guarda en una lista las semanas del mes , al recogerer la lista se muestra el calendario.
    contador = dia_semana
    if contador > 1:
        while contador != 1:
            semana = semana + '   '
            contador = contador - 1
    for i in range(1, dias + 1):
        if dia_semana == 7:
            semana = semana + str(i)
            salida.append(semana)
            semana = ''
            dia_semana = 1
        else:
            if i < 10:
                semana = semana + str(i) + '  '
                dia_semana += 1

            else:
                semana = semana + str(i) + ' '
                dia_semana += 1
    if len(semana) < 20:
        index = len(semana)
        semana_temp = list(semana)
        semana_temp.insert(0, ' ')
        index += 1
        while index < 22:
            semana_temp.append(' ')
            index += 1

    salida.append("".join(semana_temp))
    salida.append('      ')
    salida.append(len(semana.replace(" ", "")))
    return salida


#Esta funcion se encarga en determinar el día de la semana dada una fecha válida.
def dia_semana(fecha):
    # https://cs.uwaterloo.ca/~alopez-o/math-faq/node73.html
    if fecha_es_valida(fecha):
        anno = fecha[0]
        mes = fecha[1]
        dia = fecha[2]

        offset_Mes = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
        m = offset_Mes[mes - 1]
        c = (anno // 100)
        if mes == 1 or mes == 2:
            y = (anno % 100) - 1
        else:
            y = (anno % 100)

        w = (dia + m - 2 * c + y + (y // 4) + (c // 4)) % 7
        if w < 0:
            w + 7

        return w
    else:
        return "Error, la fecha no es valida"


# Esta funcion se encarga en mostrar el calendario de forma 3x4.
# Toma en cuenta si el año es bisiesto y el día de la semana en el que inicia el año.
def imprimir_3x4(anno):
    meses = {1: 'Enero', 2: 'Febrero', 3: 'Marzo',
             4: 'Abril', 5: 'Mayo', 6: 'Junio', 7: 'Julio',
             8: 'Agosto', 9: 'Setiembre', 10: 'Octubre',
             11: 'Noviembre', 12: 'Diciembre'}

    dias_semanas = 'L ' + " " + 'K ' + " " + 'M ' + " " + 'J ' + " " + 'V ' + " " + 'S' + " " + ' D'

    if anno > 1582:
        print('Calendario del año ' + str(anno) + ' D.C' + '\n')
        mes_actual = 1
        dia_inicio = dia_semana((anno,1,1))  #Se eliminó la funcion calcular_dia, debido a que cumplia la misma funcion que dia_semana()
        while mes_actual <= 12:
            print(
                '\n''{:^30}{:^2}{:^30}{:^2}{:^30}{:^2}{:^30}'.format(meses[mes_actual], '|', meses[mes_actual + 1], '|',
                                                                     meses[mes_actual + 2], '|', meses[mes_actual + 3]))
            print('{:^30}{:^2}{:^30}{:^2}{:^30}{:^2}{:^30}'.format(dias_semanas, '|', dias_semanas, '|', dias_semanas,
                                                                   '|',
                                                                   dias_semanas))
            index = 1
            calendario = []
            while index <= 4:  # Este loop guarda en una lista llamada calendario la lista de cada mes con sus semanas.
                if mes_actual == 1:
                    calendario.append(imprimir_mes(31, dia_inicio))
                    dia_inicio = int(calendario[len(calendario) - 1].pop()) // 2 + 1
                    index += 1
                    mes_actual += 1

                elif mes_actual == 4 or mes_actual == 6 or mes_actual == 9 or mes_actual == 11:

                    calendario.append(imprimir_mes(30, dia_inicio))
                    dia_inicio = int(calendario[len(calendario) - 1].pop()) // 2 + 1
                    index += 1
                    mes_actual += 1

                elif mes_actual == 2:
                    if bisiesto(anno):
                        calendario.append(imprimir_mes(29, dia_inicio))
                        dia_inicio = int(calendario[len(calendario) - 1].pop()) // 2 + 1
                        mes_actual += 1
                        index += 1
                    else:
                        calendario.append(imprimir_mes(28, dia_inicio))
                        dia_inicio = int(calendario[len(calendario) - 1].pop()) // 2 + 1
                        mes_actual += 1
                        index += 1
                else:
                    calendario.append(imprimir_mes(31, dia_inicio))
                    dia_inicio = int(calendario[len(calendario) - 1].pop()) // 2 + 1
                    mes_actual += 1
                    index += 1

            fila = 0
            while fila < len(
                    max(calendario)):  # Este loop permite imprimir las filas del calendario , de forma en que se muestren 4 meses seguidos.
                print(
                    '{:^30}{:^2}{:^30}{:^2}{:^30}{:^2}{:^30}'.format(calendario[0][fila], '|', calendario[1][fila], '|',
                                                                     calendario[2][fila], '|', calendario[3][fila]))
                fila += 1
    else:
        print("Ingrese un año perteneciente al rango permitido.")


#Esta función determina una fecha a n días de la fecha ingresada.
def fecha_futura(fecha, dias):
    if fecha_es_valida(fecha):
        if dias > 0:
            return_fecha = fecha
            for i in range(dias):
                return_fecha = dia_siguiente(return_fecha)
            return return_fecha
        else:
            return "Error, los dias deben ser positivos"
    else:
        return "Error, la fecha no es valida"


#Esta función determina el numero de dias naturales entre dos fechas ingresadas.
def dias_entre(fecha1, fecha2):
    if fecha_es_valida(fecha1):
        if fecha_es_valida(fecha2):
            if fecha1 == fecha2:
                return 0
            else:
                if fecha1 > fecha2:
                    fecha_menor = fecha2
                    fecha_mayor = fecha1
                else:
                    fecha_menor = fecha1
                    fecha_mayor = fecha2

                contador = 0
                while fecha_menor < fecha_mayor:
                    contador += 1
                    fecha_menor = dia_siguiente(fecha_menor)
                return contador

        else:
            return "Error, la fecha 2 no es valida"
    else:
        return "Error, la fecha 1 no es valida"

#Esta funcion se encarga en determinar la edad de una persona en años , meses y dias
#dadas dos fechas.
def edad_al(fecha1, fecha2):
    if fecha_es_valida(fecha1):
        if fecha_es_valida(fecha2):
            if fecha2[1] <= fecha1[1] and fecha2[2] < fecha1[2]:
                dias = (31-fecha1[2]) + fecha2[2]
                meses = 12 - fecha1[1] + fecha2[1]-1
                anno = (fecha2[0]-1) - fecha1[0]
                return anno,meses,dias
            else:
                if fecha2[2] - fecha1[2] < 0:
                    dias = (31-fecha1[2]) + fecha2[2]
                    meses = 0
                    anno = fecha2[0] - fecha1[0]
                    return anno,meses, dias
                else:
                    dias = fecha2[2] - fecha1[2]
                    meses = fecha2[1] - fecha1[1]
                    anno = fecha2[0] - fecha1[0]
                    return anno,meses, dias
        else:
            return "Error, la fecha 2 no es valida"
    else:
        return "Error, la fecha 1 no es valida"

#Esta funcion se encarga en determinar la fecha del día de hoy y devuelve una tupla.
def fecha_hoy():
    hoy = (datetime.today().strftime('%Y,%m,%d'))
    fecha_hoy = int(hoy[0:4]),int(hoy[5:7]),int(hoy[8:])
    return fecha_hoy


#Esta funcion se encarga en determinar la edad de una persona en años, meses y dias hasta
#la fecha de hoy.
def edad_hoy(fecha):
    hoy = fecha_hoy()
    if fecha_es_valida(fecha):
        if fecha <= hoy:
            tupla = edad_al(fecha, hoy)
            return tupla
        else:
            return "Error, la fecha ingresada debe ser menor a la actual"
    else:
        return "Error, la fecha ingresada no es valida"
    
    
if __name__ == '__main__':
    print(edad_hoy((2000, 4, 14)))

    
   # print(imprimir_3x4(2022))
       #print(edad_al((1957, 10, 25), (2022, 4, 6)))
