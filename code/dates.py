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


def imprimir_3x4():
    print("Hello World")


if __name__ == '__main__':
    prueba = (1582, 10, 14)
    print(fecha_es_vailida(prueba))
