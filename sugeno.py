from collections import namedtuple


def derajat_length(packet_length):
    length = namedtuple('Length',['pendek','normal','panjang'])
    if (packet_length <= 60):
        length.pendek = 1
        length.normal = 0
        length.panjang = 0
    elif (packet_length > 60 and packet_length < 90):
        length.pendek = (90 - packet_length) / (90 - 60)
        length.pendek = round(length.pendek, 2)
        if length.pendek < 0:
            length.pendek = 0
        length.normal = (packet_length - 60 ) / (90 - 60)
        length.normal = round(length.normal, 2)
        if length.normal < 0:
            length.normal = 0
        length.panjang = 0
    elif (packet_length >= 90 and packet_length < 120):
        length.pendek = 0
        length.normal = (120 - packet_length) / (120 - 90)
        length.normal = round(length.normal, 2)
        if length.normal < 0:
            length.normal = 0
        length.panjang = (packet_length - 90) / (120 - 90)
        length.panjang = round(length.panjang, 2)
        if length.panjang < 0:
            length.panjang = 0
    else:
        length.pendek = 0
        length.normal = 0
        length.panjang = 1
    return length


def derajat_source(source_count):
    source = namedtuple('Source',['single','multi'])
    if(source_count <= 1):
        source.single = 1
        source.multi = 0
    elif(source_count > 1 and source_count < 3):
        source.single = (3 - source_count) / (3 - 1)
        source.single = round(source.single, 2)
        if source.single < 0:
            source.single = 0
        source.multi = (source_count - 1) / (3 - 1)
        source.multi = round(source.multi, 2)
        if source.multi < 0:
            source.multi = 0
    else:
        source.single = 0
        source.multi = 1
    return source


def derajat_jmldata(data_count):
    jmldata = namedtuple('Count',['sedikit','banyak'])
    if(data_count <= 10):
        jmldata.sedikit = 1
        jmldata.banyak = 0
    elif(data_count > 10 and data_count < 50):
        jmldata.sedikit = (50 - data_count) / (50 - 10)
        jmldata.sedikit = round(jmldata.sedikit, 2)
        if jmldata.sedikit < 0:
            jmldata.sedikit = 0
        jmldata.banyak = (data_count - 10) / (50 -10)
        jmldata.banyak = round(jmldata.banyak, 2)
        if jmldata.banyak < 0:
            jmldata.banyak = 0
    else:
        jmldata.sedikit = 0
        jmldata.banyak = 1
    return jmldata


def derajat_POD(z):
    kategori = namedtuple('Kategori',['NOT_POD','POD'])
    if(z <= 0.4):
        kategori.NOT_POD = 1
        kategori.POD = 0
    elif(z > 0.4 and z < 0.6):
        kategori.NOT_POD = (50 - z) / (50 - 10)
        kategori.NOT_POD = round(kategori.NOT_POD, 2)
        kategori.POD = (z - 10) / (50 -10)
        kategori.POD = round(kategori.POD, 2)
    else:
        kategori.NOT_POD = 0
        kategori.POD = 1
    return kategori


def z_NOTPOD(alfapredikat):
    z = 0.6 - (alfapredikat * (0.2))
    z = round(z, 2)
    return z


def z_POD(alfapredikat):
    z = (alfapredikat * (0.2)) + 0.4
    z = round(z, 2)
    return z


def inferensi(length, source, jmldata):
    alfa = []
    z = []

    ## RULE 1. IF jmldata = sedikit AND source = single AND length = pendek THEN kategori = NOT_POD
    a1 = min(jmldata.sedikit, source.single, length.pendek)
    z1 = z_NOTPOD(a1)
    alfa.append(a1)
    z.append(z1)

    ## RULE 2. IF jmldata = sedikit AND source = single AND length = normal THEN kategori = POD
    a2 = min(jmldata.sedikit, source.single, length.normal)
    z2 = z_POD(a2)
    alfa.append(a2)
    z.append(z2)

    ## RULE 3. IF jmldata = sedikit AND source = single AND length = panjang THEN kategori = POD
    a3 = min(jmldata.sedikit, source.single, length.panjang)
    z3 = z_POD(a3)
    alfa.append(a3)
    z.append(z3)

    ## RULE 4. IF jmldata = sedikit AND source = multi AND length = pendek THEN kategori = NOT_POD
    a4 = min(jmldata.sedikit, source.multi, length.pendek)
    z4 = z_NOTPOD(a4)
    alfa.append(a4)
    z.append(z4)

    ## RULE 5. IF jmldata = sedikit AND source = multi AND length = normal THEN kategori = POD
    a5 = min(jmldata.sedikit, source.multi, length.normal)
    z5 = z_POD(a5)
    alfa.append(a5)
    z.append(z5)

    ## RULE 6. IF jmldata = sedikit AND source = multi AND length = panjang THEN kategori = POD
    a6 = min(jmldata.sedikit, source.multi, length.panjang)
    z6 = z_POD(a6)
    alfa.append(a6)
    z.append(z6)

    ## RULE 7. IF jmldata = banyak AND source = single AND length = pendek THEN kategori = POD
    a7 = min(jmldata.banyak, source.single, length.pendek)
    z7 = z_POD(a7)
    alfa.append(a7)
    z.append(z7)

    ## RULE 8. IF jmldata = banyak AND source = single AND length = normal THEN kategori = POD
    a8 = min(jmldata.banyak, source.single, length.normal)
    z8 = z_POD(a8)
    alfa.append(a8)
    z.append(z8)

    ## RULE 9. IF jmldata = banyak AND source = single AND length = panjang THEN kategori = POD
    a9 = min(jmldata.banyak, source.single, length.panjang)
    z9 = z_POD(a9)
    alfa.append(a9)
    z.append(z9)

    ## RULE 10. IF jmldata = banyak AND source = multi AND length = pendek THEN kategori = POD
    a10 = min(jmldata.banyak, source.multi, length.pendek)
    z10 = z_POD(a10)
    alfa.append(a10)
    z.append(z10)

    ## RULE 11. IF jmldata = banyak AND source = multi AND length = normal THEN kategori = POD
    a11 = min(jmldata.banyak, source.multi, length.normal)
    z11 = z_POD(a11)
    alfa.append(a11)
    z.append(z11)

    ## RULE 12. IF jmldata = banyak AND source = multi AND length = panjang THEN kategori = POD
    a12 = min(jmldata.banyak, source.multi, length.panjang)
    z12 = z_POD(a12)
    alfa.append(a12)
    z.append(z12)

    return alfa, z


def defuzzyikasi(alfa, z):
    alfa_z = []
    for i in range(len(alfa)):
        alfa_z.append(alfa[i] * z[i])

    Z = sum(alfa_z) / sum(alfa)
    return Z

