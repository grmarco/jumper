import math

nombre_verso = ['', 'Bisílabo', 'Trisílabo', 'Tetrasílabo', 'Pentasílabo', 'Hexasílabo', 'Heptasílabo', 'Octosílabo',
                'Eneasílabo', 'Decasílabo', 'Endecasílabo', 'Dodecasílabo', 'Tridecasílabo', 'Alejandrino',
                'Pentadecasílabo', 'Hexadecasílabo', 'Heptadecasílabo', 'Octodecasílabo']
tipos_verso = [
    [['', [1]]],
    [['', [2]]],
    [['', [1, 3]], ['', [3]]],
    # pentasílabos
    [['heroico', [2, 4]], ['sáfico', [4]], ['dactílico', [1, 4]]],
    # hexasílabos
    [['heroico', [2, 5]], ['melódico puro', [3, 5]], ['melódico pleno', [1, 3, 5]], ['enfático', [1, 5]],
     ['vacío', [5]]],
    # heptasilabos
    [['heroico puro', [2, 6]], ['heroico pleno', [2, 4, 6]], ['melódico puro', [3, 6]], ['melódico puro', [1, 3, 6]],
     ['sáfico puro', [4, 6]], ['sáfico pleno', [1, 4, 6]], ['enfático', [1, 6]], ['vacío', [6]]],
    # octosílabos
    [['heroico puro', [2, 4, 7]], ['heroico pleno', [2, 5, 7]], ['heroico difuso', [2, 7]], ['melódico puro', [3, 7]],
     ['melódico pleno', [1, 3, 5, 7]], ['melódico semipleno', [3, 5, 7]], ['melódico corto hemistiquial', [1, 3, 7]],
     ['dactílicos', [1, 4, 7]], ['sáfico', [4, 7]], ['enfático corto', [1, 5, 7]], ['enfático largo', [1, 7]],
     ['vacío corto', [5, 7]], ['vacío largo', [7]]],
    # eneasilabos
    [['heroico puro corto', [2, 4, 8]], ['heroico pleno', [2, 4, 6, 8]], ['heroico puro largo', [2, 6, 8]],
     ['heroico difuso', [2, 8]], ['sáfico puro', [4, 8]], ['sáfico pleno', [1, 4, 6, 8]],
     ['sáfico semipleno', [1, 4, 8]], ['sáfico largo', [4, 6, 8]], ['melódico puro', [3, 5, 8]],
     ['melódico pleno corto', [1, 3, 5, 8]], ['melódico corto', [1, 3, 8]], ['melódico largo', [3, 6, 8]],
     ['melódico pleno largo', [1, 3, 6, 8]], ['melódico difuso', [3, 8]], ['dactílico (de gaita gallega)', [2, 5, 8]],
     ['enfático puro', [1, 6, 8]], ['enfático corto', [1, 5, 8]], ['enfático largo', [1, 8]], ['vacío corto', [6, 8]],
     ['vacío largo', [8]], ['vacío difuso', [5, 8]]],
    # decasílabos
    [['heroico hemistiquial puro', [2, 4, 9]], ['heroico hemistiquial pleno', [2, 4, 6, 9]],
     ['heroico hemistiquial pleno doble', [2, 4, 7, 9]], ['heroico no hemistiquial puro', [2, 6, 9]],
     ['heroico no hemistiquial pleno', [2, 5, 7, 9]], ['heroico no hemistiquial largo', [2, 7, 9]],
     ['heroico no hemistiquial corto', [2, 5, 9]], ['heroico no hemistiquial difuso', [2, 9]],
     ['melódico puro', [3, 5, 9]], ['melódico pleno', [1, 3, 5, 7, 9]], ['melódico semipleno corto', [1, 3, 5, 9]],
     ['melódico largo', [3, 7, 9]], ['melódico semipleno largo', [1, 3, 7, 9]], ['melódico semipleno', [3, 5, 7, 9]],
     ['melódico difuso', [3, 9]], ['melódico difuso pleno', [1, 3, 9]], ['sáfico puro', [4, 6, 9]],
     ['sáfico dactílico doble (1,4+1,4)', [1, 4, 6, 9]], ['sáfico corto', [1, 4, 9]], ['sáfico largo', [4, 7, 9]],
     ['sáfico pleno ', [1, 4, 7, 9]], ['sáfico doble', [4, 9]], ['enfático corto', [1, 5, 9]],
     ['enfático puro', [1, 6, 9]], ['enfático pleno', [1, 5, 7, 9]], ['enfático largo', [1, 7, 9]],
     ['dactílico puro ', [3, 6, 9]], ['dactílico pleno', [1, 3, 6, 9]], ['vacío puro', [6, 9]],
     ['vacío difuso', [5, 9]], ['vacío largo', [5, 7, 9]]],
    # endecasilabos
    [['heroico puro', [2, 6, 10]], ['heroico pleno', [2, 4, 6, 8, 10]], ['heroico corto', [2, 4, 6, 10]],
     ['heroico largo', [2, 6, 8, 10]], ['heroico difuso', [2, 4, 10]], ['melódico puro', [3, 6, 10]],
     ['melódico pleno', [1, 3, 6, 8, 10]], ['melódico largo', [3, 6, 8, 10]], ['melódico corto', [1, 3, 6, 10]],
     ['sáfico puro', [4, 8, 10]], ['sáfico puro pleno', [1, 4, 8, 10]], ['sáfico pleno', [1, 4, 6, 8, 10]],
     ['sáfico corto', [4, 6, 10]], ['sáfico corto pleno', [1, 4, 6, 10]], ['sáfico largo', [4, 6, 8, 10]],
     ['sáfico largo pleno', [2, 4, 8, 10]], ['sáfico difuso', [4, 10]], ['sáfico difuso pleno', [1, 4, 10]],
     ['enfático puro', [1, 6, 10]], ['enfático pleno', [1, 6, 8, 10]], ['vacío puro', [6, 10]],
     ['vacío pleno tipo 1', [6, 8, 10]], ['vacío pleno tipo 2', [1, 4, 10]], ['vacío heroico', [2, 4, 10]]]]


vocales_no_acentuadas = ['a', 'e', 'i', 'o', 'u']
vocales_acentuadas = ['á', 'é', 'í', 'ó', 'ú']
de_no_a_si_acentuadas = {'a': 'á', 'e': 'é', 'i': 'í', 'o': 'ó', 'u': 'ú', 'ï': 'ï', 'ü': 'ü'}
dieresis = ['ï', 'ü']
vocales = vocales_no_acentuadas + vocales_acentuadas + dieresis
vocales_y = vocales + ['y']
diptongos = ['ai', 'au', 'ei', 'eu', 'oi', 'ou', 'ui', 'iu', 'ia', 'ua', 'ie', 'ue', 'io', 'uo', 'ió', 'ey', 'oy', 'ié',
             'éi', 'ué', 'ái', 'iá', 'uá']

atonas_a_veces_acentuadas = {'oh': 'ó', 'quien': 'quién', 'do': 'dó'}

atonas = [
    'el', 'los', 'la', 'las', 'me', 'nos', 'te', 'os', 'lo', 'le', 'les', 'se', 'mi',
    'mis', 'tu', 'tus', 'su', 'sus', 'nuestro', 'nuestros', 'nuestra', 'nuestras', 'vuestro',
    'vuestra', 'vuestros', 'vuestras', 'que', 'quien', 'quienes', 'cuyo', 'cuya', 'cuyos',
    'cuyas', 'cual', 'cuales', 'como', 'cuando', 'do', 'donde', 'adonde', 'cuan', 'tan',
    'cuanto', 'cuanta', 'cuantos', 'cuantas', 'a', 'ante', 'bajo', 'cabe', 'con', 'contra',
    'de', 'desde', 'durante', 'en', 'entre', 'hacia', 'hasta', 'mediante', 'para', 'por',
    'sin', 'so', 'sobre', 'tras', 'versus', 'aunque', 'conque', 'cuando', 'mas',
    'mientras', 'ni', 'o', 'u', 'pero', 'porque', 'pues', 'que', 'si', 'sino', 'y', 'e',
    'aun', 'excepto', 'hasta', 'incluso', 'don', 'doña', 'fray', 'frey', 'san', 'sor',
    'al', 'del', 'desde']

puntos = [':', ',', '.', ';', '.', '–', '(', ')', '\n', '\r', '¿', '?', '!', '¡', '—', '»', '”', '“', '«', '-','/','//']

FACTOR_AGUDA, FACTOR_LLANA, FACTOR_ESDRUJULA = 1, 0, -1

'''
MÓDULO DE ANALISIS DE PALABRA: COMPUTO DE SILABAS Y ACENTOS DE PALABRAS
'''


def quitar_puntuacion(texto):
    quitar = [':', ',', '.', ';', '.', '–', '(', ')', '\n', '\r', '¿', '?', '!', '¡', '—', '»', '”', '“', '«', '-','/', '/']
    for q in quitar:
        texto = texto.replace(q, '')
    return texto


def normalizar(texto):
    """Quita puntuación, mayusculas y espacios laterales

        Args:
            texto (str): La palabra a normalizar
        Returns:
            str: palabra sin puntuación, mayusculas y espacios laterales
    """
    return quitar_puntuacion(texto).strip().lower()


def normalizar_qu_gu(palabra):
    """Normaliza palabras con digrafos qu y gu, para que no se tenga en cuenta la vocal del digrafo en el cómputo

        Args:
            palabra (str): La palabra con posible digrafo
        Returns:
            str: palabra sin el digrafo
    """
    quitar = [('qu', 'q'), ('gue', 'ge'), ('gui', 'gi')]
    for q in quitar:
        palabra = palabra.replace(q[0], q[1])
    return palabra


def empieza_por_vocal(palabra):
    return (palabra[0] in vocales_y) or (palabra[0] == 'h' and palabra[1] in vocales_y)


def termina_por_vocal(palabra):
    return (palabra[-1] in vocales_y) or (palabra[-1] == 'h' and palabra[-2] in vocales_y)


def yeye(palabra):
    """Comprueba que la palabra que empieza por y griega no tiene un sonido vocálico. Se emplea para no hacer sinalefa

        Args:
            palabra (str): La palabra que puede empezar por y griega
        Returns:
            bool: devuelve True si la y griega no es vocálica en esa palabra
    """
    return (palabra[:2] in ['y' + vocal for vocal in vocales]) or (palabra[:3] == 'hie') or (palabra[:3] == 'hue') or (palabra[:3] == 'hon')


def palabra_silabas_acentos(palabra):
    """Toma una palabra y devuelve el número de síalabas, la posición del acento y un factor
    de palabra aguda(1), llana (0) o esdrújula (-1) por si cae al final del verso

        Args:
            palabra (str): La palabra para contar sus sílabas
        Returns:
            tuple: una tupla con el número de síalabas, donde cae el acento y su clasificación
            (Número_de_sílabas, Sílaba_en_la_que_recae_el_acento, Factor_final_de_verso)
    """
    # si una sola letra
    if len(palabra) == 1:
        return 1, 1, 1

    factor_final = 0
    num_silabas = 0
    palabra = normalizar_qu_gu(palabra)
    acento = None
    for i, c in enumerate(palabra):
        if c in vocales:
            num_silabas += 1
            if palabra[i - 1] + c in diptongos and not palabra[i - 1] in dieresis and num_silabas > 1:
                num_silabas -= 1
            # tilde
            if c in vocales_acentuadas:
                acento = num_silabas
    # como todas las esdrújulas se acentúan...
    if acento is None:
        # llana
        if palabra[-1] in ['n', 's'] + vocales:
            acento = num_silabas - 1
        # aguda
        else:
            acento = num_silabas
    
    if num_silabas == 1:
        acento = 1

    factor = num_silabas - acento
    if factor == 0:
        factor_final = FACTOR_AGUDA
    elif factor == 1:
        factor_final = FACTOR_LLANA
    elif factor > 1:
        factor_final = FACTOR_ESDRUJULA

    return num_silabas, acento, factor_final


'''
SUBMODULO DE AMBIGUEDADES: FUNCIONES PARA LA COMPARACION DE VECTORES DE ACENTOS
'''


def convertir_a_vector_binario(vector):
    """Toma un vector de acentos y lo convierte en vector binario
        Args:
            vector (list): Vector de acentos. Ej.: [2,6,10]
        Returns:
            list: un vector binario. Ej.: [False,True,False,False,False,False,True,False,False,False,True]
    """
    vec_binario = []
    vec_op = vector[:]
    for j in range(vector[-1]):
        if j == vec_op[0]:
            vec_binario.append(True)
            vec_op.pop(0)
        else:
            vec_binario.append(False)
    return vec_binario


def comparar_acentos(vec_acentos1, vec_acentos2):
    """Toma dos vectores de acentos y devuelve un ratio de coincidencia

        Args:
            vec_acentos1 (list of ints): esquema acentual del verso a comparar
            vec_acentos2 (list of ints): esquema acentual del verso de referencia
        Returns:
            float: ratio de coincidencia (entre 0 y 1) entre ambos vectores
    """

    # si no son de la misma medida nos vamos
    if vec_acentos1[-1] != vec_acentos2[-1]:
        return 0

    comp1 = convertir_a_vector_binario(vec_acentos1)
    comp2 = convertir_a_vector_binario(vec_acentos2)
    puntos_vec = 0
    for i in range(len(comp1)):
        if comp1[i] == comp2[i]:
            puntos_vec += 1
    return puntos_vec / len(comp1)


def clasificar(num_silabas, acentos):
    """Toma el número de sílabas y acentos, y devuelve el tipo de verso más cercano dentro de la tradición métrica

        Args:
            num_silabas (int): Número de sílabas del verso
            acentos (list): Esquema de los acentos del verso
        Returns:
            tuple: una tupla con la clasificion del verso en la forma:
            (Numbre_del_verso, Acentos_ideales, Ratio_de_coincidencia_con_acentos_ideales)
    """
    nombre = nombre_verso[num_silabas - 1] if num_silabas <= 18 else 'versículo'
    mejor_tipo = ['', []]
    mejor_ratio = 0
    if num_silabas <= 11:
        for tipo in tipos_verso:
            if tipo[0][1][-1] == acentos[-1]:
                for subtipo in tipo:
                    ratio_v = comparar_acentos(acentos, subtipo[1])
                    if ratio_v > mejor_ratio:
                        mejor_ratio = ratio_v
                        mejor_tipo = subtipo
    else:
        return nombre, '-', 1.0
    return nombre + ' ' + mejor_tipo[0], mejor_tipo[1], mejor_ratio


'''
SUBMODULO DE TRATAMIENTO DE AMBIGUEDADES 
'''


def hay_diptongo(palabra):
    """Informa de la aparición de un diptongo en una palabra
        Args:
            palabra (str): Palabra con posible diptongo
        Returns:
            bool: devuelve True si se ha encontrado un diptongo
    """
    for diptongo in diptongos:
        lugar_dip = normalizar_qu_gu(palabra).find(diptongo)
        if lugar_dip > -1:
            return True
    return False


def hay_hiato(palabra):
    """Informa de la aparición de un hiato en una palabra
        Args:
            palabra (str): Palabra con posible hiato
        Returns:
            bool: devuelve True si se ha encontrado un hiato
    """
    # quitamos hs por si hay intercaladas. Ej.: ahora
    palabra = palabra.replace('h', '')
    for i, c in enumerate(palabra):
        if i + 1 < len(palabra):
            if palabra[i] in vocales and palabra[i + 1] in vocales and not palabra[i:i + 2] in diptongos:
                return True
    return False


def quitar_hiato(palabra_op):
    """Toma una palabra donde puede haber un hiato y devuelve la palabra con el hiato eliminado y etiquetado (sineresis)

        Args:
            palabra_op (str): Palabra con hiato
        Returns:
            str: palabra sin el hiato. Ej.: de poema > p#ema
    """
    simbolo_sineresis = '#'
    # quitamos hs intercaladas
    palabra = palabra_op[0]
    palabra += palabra_op[1:].replace('h', '')
    s_palabra_op, a_palabra_op, f_palabra_op = palabra_silabas_acentos(palabra_op)
    ya_tildada = False
    for i, c in enumerate(palabra_op):
        if c in vocales_acentuadas:
            ya_tildada = True
        if i + 1 < len(palabra):
            if palabra[i] in vocales and palabra[i + 1] in vocales and not palabra[i:i + 2] in diptongos:
                if palabra[i + 1] in vocales_acentuadas:
                    palabra = palabra[:i] + palabra[i + 1:]
                elif palabra[i] in vocales_acentuadas:
                    palabra = palabra[:i + 1] + palabra[i + 2:]
                else:
                    palabra = palabra[:i] + palabra[i + 1:]
                    # hay que mantener el acento
                    s_palabra, a_palabra, _ = palabra_silabas_acentos(palabra)
                    # colocamos el acento cuando la palabra tiene 3 sílabas o menos (tema sacaabuelas)
                    if not ya_tildada and f_palabra_op != 1 and a_palabra != a_palabra_op and s_palabra_op <= 3:
                        palabra = palabra[:i] + de_no_a_si_acentuadas[palabra[i]] + palabra[i + 1:]
                # insertamos simbolo para indicar la operacion de sineresis
                if i == 1 or i == len(palabra) - 1:
                    palabra = palabra[:i] + simbolo_sineresis + palabra[i:]

    return palabra


def separar_diptongo(palabra):
    """Toma una palabra donde puede haber un diptongo y devuelve la palabra con el diptongo separado (dieresis)

        Args:
            palabra (str): Palabra con diptongo
        Returns:
            str: palabra con dieresis etiquetada. Ej.: de ruido > ru~ido
    """
    palabra = normalizar_qu_gu(palabra)
    for diptongo in diptongos:
        lugar_dip = palabra.find(diptongo)
        if lugar_dip > -1 and not yeye(palabra[lugar_dip + 1:lugar_dip + 3]):
            return palabra[:lugar_dip + 1] + '~' + palabra[lugar_dip + 1:]
    return palabra


def combinar_con_simbolo(versos_amb, sep_v_amb, simbolo):
    """Toma una lista de versos ambiguos dada desde el módulo de analisis de verso, la lista de versos ambiguos dada
    desde el submodulo de combinación de ambigüedades y el simbolo a combinar. De momento, solo se dan dos símbolos:
    el de la sineresis # y dieresis ~

        Args:
            versos_amb (list of str):
            sep_v_amb (list of str):
            simbolo (char):
        Returns:
            list: versos combinados con las dieresis y sineresis
    """
    palabras_con_simbolo = []
    composicion_simbolo = []
    for v_padre in versos_amb:
        v_padre = v_padre.split()
        for palabra_v_padre in v_padre:
            if palabra_v_padre.find(simbolo) > -1:
                palabras_con_simbolo.append(palabra_v_padre)

    for v_padre in sep_v_amb:
        v_padre = v_padre.split()
        for pos_palabra_v_padre, palabra_v_padre in enumerate(v_padre):
            for palabra_simbolo in palabras_con_simbolo:
                if palabra_v_padre == palabra_simbolo.replace(simbolo, ''):
                    v_amb_compuesto = v_padre[:]
                    v_amb_compuesto[pos_palabra_v_padre] = palabra_simbolo
                    composicion_simbolo.append(' '.join(v_amb_compuesto))
    return composicion_simbolo


def combinar_ambiguedades(versos_amb, hacer_composicion_hiatos=False, hacer_composicion_atonas=False,
                          hacer_composicion_diptongos=False):
    """Toma una lista de versos ambiguos dada desde el módulo de analisis de verso y las combina: un verso puede
    presentar varias ambiguedades al mismo tiempo. Por ejemplo, dialefas y sineresis a al vez.

       Args:
           versos_amb (list of str): todos los versos ambiguos detectados que se quieren combinar
           hacer_composicion_hiatos (bool): (Prueba) Se componen los versos que presentan varias dieresis
           hacer_composicion_atonas (bool): (Prueba) Se componen los versos que presentan palabras
                                            atonas a veces acentuadas: por ejemplo: 'oh'
           hacer_composicion_diptongos (bool): (Prueba) Se componen los versos que presentan varias sineresis
       Returns:
           list: todas las posibles ambiguedades del verso combinadas
   """
    composicion_amb_sinalefas = []
    composicion_hiatos = []
    composicion_diptongos = []
    composicion_atonas = []
    sep_v_amb = versos_amb[:]

    # composicion de sinalefas
    for v_padre in sep_v_amb:
        v_padre = v_padre.split(' ')
        for v_hijo in sep_v_amb:
            v_hijo = v_hijo.split(' ')
            if v_padre != v_hijo:
                # combinar sinalefas
                if '' in v_padre:
                    desplazamiento = 0
                    nuevo_v_amb = v_hijo[:]
                    i_espacio = v_padre.index('')
                    if '' in v_hijo and v_hijo.index('') < i_espacio:
                        desplazamiento = 2
                    nuevo_v_amb.insert(i_espacio + desplazamiento, '')
                    nuevo_v_amb.insert(i_espacio + desplazamiento + 1, '')
                    composicion_amb_sinalefas.append(' '.join(nuevo_v_amb))

    sep_v_amb += composicion_amb_sinalefas

    # composicion de atonas
    if hacer_composicion_atonas:
        for v_padre in sep_v_amb:
            v_padre = v_padre.split()
            for pos_palabra_v_padre, palabra_v_padre in enumerate(v_padre):
                for atonas_a_veces_acentuada in atonas_a_veces_acentuadas:
                    if palabra_v_padre == atonas_a_veces_acentuada:
                        v_amb_compuesto = v_padre[:]
                        v_amb_compuesto[pos_palabra_v_padre] = atonas_a_veces_acentuadas[atonas_a_veces_acentuada]
                        composicion_atonas.append(' '.join(v_amb_compuesto))
        sep_v_amb += composicion_atonas

    # composicion de diptongos
    if hacer_composicion_diptongos:
        composicion_diptongos = combinar_con_simbolo(versos_amb, sep_v_amb, '#')
        sep_v_amb += composicion_diptongos

    # composicion de hiatos
    if hacer_composicion_hiatos:
        composicion_hiatos = combinar_con_simbolo(versos_amb, sep_v_amb, '~')
        sep_v_amb += composicion_hiatos

    return versos_amb + composicion_amb_sinalefas + composicion_hiatos + composicion_diptongos


def resolver_ambiguedades(v_final, versos_amb, arte, detectar_amb):
    """Toma una lista de versos ambiguos dada desde el módulo de analisis de verso y resuelve el verso teniendo en
    cuenta su arte y el número de sílabas al que se quiere tender.

       Args:
           v_final (list of str): verso sin desambiguar, se sobreescribe si la ambiguación resulta exitosa
           versos_amb (list of str): todas las formas ambiguas posible del verso
           arte (int): número de sílabas del verso si es de más de once sílabas
           detectar_amb (int): medida hacia la que resolver la ambiguedad
       Returns:
           list: lista con el verso ambiguo elegido y etiquetado, el número de sílabas que tiene,
           su vector de acentos y su clasificación
   """
    # resolvemos las ambiguedades
    v_amb_ratio_mejor = 0
    versos_amb = combinar_ambiguedades(versos_amb)
    for v_amb in versos_amb:
        _, v_amb_silabas, v_amb_acentos, _ = verso_silabas_acentos_tipo(v_amb, arte, 0)
        if v_amb_silabas == detectar_amb:
            # si se ha resuelto bien la ambiguedad
            clasificacion = clasificar(v_amb_silabas, v_amb_acentos)
            v_amb_ratio = clasificacion[2]
            if v_amb_ratio_mejor <= v_amb_ratio:
                if v_amb_ratio_mejor == v_amb_ratio and (v_amb.find('~') > -1 or v_amb.find('#') > -1):
                    continue
                v_amb_ratio_mejor = v_amb_ratio
                v_final = v_amb, v_amb_silabas, v_amb_acentos, clasificacion
    return v_final


'''
MÓDULO DE ANALISIS DE VERSO
'''


def en_hemistiquio(num_silabas, factor, arte):
    """Toma un verso y devuelve su análisis métrico

        Args:
            num_silabas (int): numero de sílabas contadas hasta la palabra en proceso
            factor (int): factor de compensación de la palabra en proceso
            arte (int) número de silabas del verso de arte mayor cuyo hemistiquio se quiere detectar

        Returns:
            bool: devuelve True si el verso, con la palabra que se está procesando, llega a su hemistiquio, si no False
    """

    hemistiquio = arte / 2
    # para esdrújulas, se redondea hacia arriba
    if factor == FACTOR_ESDRUJULA:
        return num_silabas + factor == math.floor(hemistiquio)
    # para agudas y llanas hacia abajo
    else:
        return num_silabas + factor == math.ceil(hemistiquio)


def verso_silabas_acentos_tipo(verso, arte=0, detectar_amb=0):
    """Toma un verso y devuelve su análisis métrico

        Args:
            verso (str): El verso en forma de cadena de texto
            arte (int): El número de sílabas del verso para computar los hemistiquios (se activa recursivamente)
            detectar_amb (int): Número de sílabas hacia el que se quiere comprobar la ambiguedad del verso

        Returns:
            list: una lista con el análisis métrico. Consiste en el número de síalabas (int), una lista
            de los acentos del verso (list of ints) y una tupla con la clasificion del verso con la forma
            (Numbre_del_verso, Acentos_ideales, Ratio_de_coincidencia_con_acentos_ideales)
    """

    num_silabas = 0
    verso_op = quitar_puntuacion(verso.lower()).strip().split(' ')
    acentos = []
    versos_amb = []
    palabra_final = verso_op[-1]

    for i, palabra in enumerate(verso_op):
        if palabra:
            # silabas, acentos y factor de la palabra en proceso
            silabas, acento, factor = palabra_silabas_acentos(palabra)
            palabra_siguiente = None if i == len(verso_op) - 1 else verso_op[i + 1]
            # sumamos las silabas de la palabra en proceso
            num_silabas += silabas

            # cómputo de los abverbios en -mente (dos acentos)
            if palabra[-5:] == "mente" and len(palabra) > 5:
                palabra_sin_mente = palabra.replace('mente', '')
                silabas_mente, acento_mente = 2, 1
                silabas_sin_mente, acento_sin_mente, factor_sin_mente = palabra_silabas_acentos(palabra_sin_mente)
                acento_sin_mente = num_silabas - (silabas_sin_mente - acento_sin_mente) - silabas_mente
                # el acento del principio del adbervio
                acentos.append(acento_sin_mente)
                acentos.append(num_silabas - (silabas_mente - acento_mente))
            else:
                # cómputo del acento para el resto de palabras (un acento)
                if palabra not in atonas or i == len(verso_op) - 1:
                    acento_nuevo = num_silabas - (silabas - acento)
                    if acentos:
                        if acentos[-1] != acento_nuevo:
                            acentos.append(acento_nuevo)
                    else:
                        acentos.append(acento_nuevo)

            # sinalefas
            if palabra_siguiente and termina_por_vocal(palabra) and empieza_por_vocal(
                    palabra_siguiente) and not en_hemistiquio(num_silabas, factor, arte) \
                    and not yeye(palabra_siguiente):
                num_silabas -= 1
                # anotamos dialefa 
                if detectar_amb > 0:
                    v_amb = verso_op[:]
                    v_amb.insert(i + 1, ' ')
                    v_amb = ' '.join(v_amb)
                    versos_amb.append(v_amb)

            # dieresis y senereis
            if detectar_amb > 0:
                # anotamos sineresis
                if hay_hiato(palabra):
                    v_amb = verso_op[:]
                    v_amb.pop(i)
                    v_amb.insert(i, quitar_hiato(palabra))
                    v_amb = ' '.join(v_amb)
                    versos_amb.append(v_amb)
                # anotamos dieresis
                if hay_diptongo(palabra):
                    v_amb = verso_op[:]
                    v_amb.pop(i)
                    v_amb.insert(i, separar_diptongo(palabra))
                    v_amb = ' '.join(v_amb)
                    versos_amb.append(v_amb)

            # hemistiquios
            if arte > 0 and palabra not in atonas and en_hemistiquio(num_silabas, factor, arte):
                num_silabas += factor

    factor_palabra_final = palabra_silabas_acentos(palabra_final)[2] if palabra_final[-5:] != "mente" else 0
    num_silabas += factor_palabra_final

    # si es mayor de once, se vuelve a contar teniendo en cuenta el hemistiquio (llamada recursiva)
    if num_silabas > 11 and arte == 0:
        _, num_silabas, acentos, _ = verso_silabas_acentos_tipo(verso, num_silabas, 0)

    v_final = verso, num_silabas, acentos, clasificar(num_silabas, acentos)

    # modulo detección de ambiguedades
    if detectar_amb > 0:
        v_final = resolver_ambiguedades(v_final, versos_amb, arte, detectar_amb)

    return v_final


'''
MÓDULO DE ANÁLISIS DE POEMAS ENTEROS
'''


def most_frequent(lista, constante=0.15):
    """Recibe una lista y extrae los elementos más frecuentes, por encima de una constante

       Args:
           lista (list): lista de elementos
           constante (float): valor entre 0 y 1 para indicar que no se tenga como frecuente la medida que no supere
                              esa frecuencia. Por defecto, no se consideran frecuentes las medidas por debajo de un 15%
       Returns:
           list: elementos más frecuentes de la lista
   """

    tabla_frecuencias = {}
    for item in lista:
        if item in tabla_frecuencias:
            tabla_frecuencias[item] += 1
        else:
            tabla_frecuencias[item] = 1
    tabla_frecuencias_iter = tabla_frecuencias.copy()
    for item in tabla_frecuencias_iter:
        tabla_frecuencias[item] /= len(lista)
        # si se repite más de un 15% (por defecto) lo consideramos como frecuente
        if tabla_frecuencias[item] < constante:
            tabla_frecuencias.pop(item)
    return dict(sorted(tabla_frecuencias.items(), key=lambda item_sort: item_sort[1], reverse=True))


def trocear_columna(x, c, i, contexto):
    """Recibe una tabla y trocea la columna que se indica desde la posicion i en un contexto del tamaño de 'contexto'.
    Se utiliza para obtener el contexto de un número determinado de versos. Posteriormente, se extraerá el número
    de sílabas más frecuente.

        Args:
            x (list): Lista del analizador de poemas
            c (int): Columna de la tabla
            i (int): posición del vector a partir de la que se quiere trocear
            contexto (int): contexto que se quiere extraer
        Returns:
            list: la rodaja de columna
    """

    if i < contexto:
        rodaja = x[:contexto]
    elif i + contexto >= len(x):
        rodaja = x[i:]
    else:
        rodaja = x[i - contexto:i + contexto]
    return list(map(list, zip(*rodaja)))[c]


def escandir_lista_versos(versos, contexto=14):
    """Toma una lista de versos y devuelve el análisis métrico

        Args:
            versos (list of str): Lista de versos
            contexto (int): en el caso en que se detecte un poema polimétrico, es el contexto para obtener
                            las medidas frecuentes
        Returns:
            list: una lista con el análisis métrico de todos los versos. Forma: [verso, v_etiquetado, silabas_v, acentos_v, acentos_ideales_v, tipo_v, ratio_v]
    """
    x = []
    nuevo = []
    # computo con modulo de ambiguedades desactivado
    for verso_a in versos:
        v = verso_a.strip().replace('\n', '')
        if not v:
            continue
        v_final, silabas_v, acentos_v, clasificacion_v = verso_silabas_acentos_tipo(verso_a, 0, 0)
        tipo_v, acentos_ideales_v, ratio_v = clasificacion_v
        x.append([v, v_final, silabas_v, acentos_v, acentos_ideales_v, tipo_v, ratio_v])

    # cálculo de versos frecuentes
    columna_silabas_v = list(map(list, zip(*x)))[2]
    versos_frecuentes = most_frequent(columna_silabas_v)
    if len(versos_frecuentes) == 1:
        metrica_mixta = False
    else:
        metrica_mixta = True

    # computo de versos ambiguos
    for i, dato_v in enumerate(x):
        silabas_v = dato_v[2]
        desambiguado = False

        # si es metrica mixta, se calculan las medidas frecuentes en un contexto n
        if metrica_mixta:
            columna_silabas_v = trocear_columna(x, 2, i, contexto)
            versos_frecuentes = most_frequent(columna_silabas_v)

        # aproximamos a los versos más frecuentes
        for verso_frecuente in versos_frecuentes:
            if silabas_v not in versos_frecuentes:
                v_final, silabas_v, acentos_v, clasificacion_v = verso_silabas_acentos_tipo(dato_v[0], 0,
                                                                                            verso_frecuente)
                tipo_v, acentos_ideales_v, ratio_v = clasificacion_v
                if silabas_v == verso_frecuente:
                    nuevo.append([dato_v[0], v_final, silabas_v, acentos_v, acentos_ideales_v, tipo_v, ratio_v])
                    desambiguado = True
        if not desambiguado:
            nuevo.append(dato_v)
    return nuevo


def escandir_texto(texto):
    """Toma un poema y devuelve el análisis métrico

        Args:
            texto (str): Poema en forma de cadena de texto
        Returns:
            list: una lista con el análisis métrico de todos los versos
    """
    return escandir_lista_versos(texto.split('\n'))
