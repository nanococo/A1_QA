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

#Esta función se encarga de escribir el mes
def imprimir_mes(dias, dia_semana):
    semana_temp = []
    semana = ''
    salida = []
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


def cacular_dia(anno):
    valor = (1 + 5 * ((anno - 1) % 4) + 4 * ((anno - 1) % 100) + 6 * ((anno - 1) % 400)) % 7
    return valor


def imprimir_3x4(anno):
    meses = {1: 'Enero', 2: 'Febrero', 3: 'Marzo',
             4: 'Abril', 5: 'Mayo', 6: 'Junio', 7: 'Julio',
             8: 'Agosto', 9: 'Setiembre', 10: 'Octubre',
             11: 'Noviembre', 12: 'Diciembre'}

    dias_semanas = 'L ' + " " + 'K ' + " " + 'M ' + " " + 'J ' + " " + 'V ' + " " + 'S' + " " + ' D'

    if anno > 1582:
        print('Calendario del año ' + str(anno) + ' D.C' + '\n')
        mes_actual = 1
        dia_semana = cacular_dia(anno)
        while mes_actual <= 12:
            print('\n''{:^30}{:^2}{:^30}{:^2}{:^30}{:^2}{:^30}'.format(meses[mes_actual], '|', meses[mes_actual + 1], '|',
                                                                       meses[mes_actual + 2], '|', meses[mes_actual + 3]))
            print('{:^30}{:^2}{:^30}{:^2}{:^30}{:^2}{:^30}'.format(dias_semanas, '|', dias_semanas, '|', dias_semanas, '|',
                                                                   dias_semanas))
            index = 1
            calendario = []
            while index <= 4:
                if mes_actual == 1:
                    calendario.append(imprimir_mes(31, dia_semana))
                    dia_semana = int(calendario[len(calendario) - 1].pop()) // 2 + 1
                    index += 1
                    mes_actual += 1

                elif mes_actual == 4 or mes_actual == 6 or mes_actual == 9 or mes_actual == 11:

                    calendario.append(imprimir_mes(30, dia_semana))
                    dia_semana = int(calendario[len(calendario) - 1].pop()) // 2 + 1
                    index += 1
                    mes_actual += 1

                elif mes_actual == 2:
                    if bisiesto(anno):
                        calendario.append(imprimir_mes(29, dia_semana))
                        dia_semana = int(calendario[len(calendario) - 1].pop()) // 2 + 1
                        mes_actual += 1
                        index += 1
                    else:
                        calendario.append(imprimir_mes(28, dia_semana))
                        dia_semana = int(calendario[len(calendario) - 1].pop()) // 2 + 1
                        mes_actual += 1
                        index += 1
                else:
                    calendario.append(imprimir_mes(31, dia_semana))
                    dia_semana = int(calendario[len(calendario) - 1].pop()) // 2 + 1
                    mes_actual += 1
                    index += 1

            fila = 0
            while fila < len(max(calendario)):
                print(
                    '{:^30}{:^2}{:^30}{:^2}{:^30}{:^2}{:^30}'.format(calendario[0][fila], '|', calendario[1][fila], '|',
                                                                     calendario[2][fila], '|', calendario[3][fila]))
                fila += 1
    else:
        return "Ingrese un año perteneciente al rango permitido."

