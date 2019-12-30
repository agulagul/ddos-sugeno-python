from sugeno import *
from scan_report import *
from calc_report import *
import pandas as pd


def load_csv(path):
    df = pd.read_csv(path)
    df = df[df['Protocol'].isin(['ICMP', 'IPv4'])]
    df.Time = df.Time.astype(int)
    return df


def filter_server(df, destination):
    df = df[df['Source'] != destination]
    df = df[df['Destination'] == destination]
    return df


def calculate(df):
    report_dict = {
        'interval(second)': [],
        'attacker_count': [],
        'attacker_ip': [],
        'average_length': [],
        'packet_sent': [],
        'class': []
    }

    keanggotaan_length = {
        'interval': [],
        'average_length': [],
        'length_pendek': [],
        'length_normal': [],
        'length_panjang': []
    }

    keanggotaan_source = {
        'interval': [],
        'source_count': [],
        'source_single': [],
        'source_multi': []
    }

    keanggotaan_packet = {
        'interval': [],
        'packet_count': [],
        'packet_sedikit': [],
        'packet_banyak': []
    }

    rule_dict = {
        'interval': [],
        'rule': [],
        'a': [],
        'b': [],
        'c': [],
        'alfapredikat': [],
        'x': []
    }
    rule_set = ['IF jmldata = sedikit AND source = single AND length = pendek THEN kategori = NOT_POD',
                'IF jmldata = sedikit AND source = single AND length = normal THEN kategori = POD',
                'IF jmldata = sedikit AND source = single AND length = panjang THEN kategori = POD',
                'IF jmldata = sedikit AND source = multi AND length = pendek THEN kategori = NOT_POD',
                'IF jmldata = sedikit AND source = multi AND length = normal THEN kategori = POD',
                'IF jmldata = sedikit AND source = multi AND length = panjang THEN kategori = POD',
                'IF jmldata = banyak AND source = single AND length = pendek THEN kategori = POD',
                'IF jmldata = banyak AND source = single AND length = normal THEN kategori = POD',
                'IF jmldata = banyak AND source = single AND length = panjang THEN kategori = POD',
                'IF jmldata = banyak AND source = multi AND length = pendek THEN kategori = POD',
                'IF jmldata = banyak AND source = multi AND length = normal THEN kategori = POD',
                'IF jmldata = banyak AND source = multi AND length = panjang THEN kategori = POD']
    Z = []
    for i in range(len(df.Time.unique())):
        report_dict['interval(second)'].append(i)
        keanggotaan_length['interval'].append(i)
        keanggotaan_source['interval'].append(i)
        keanggotaan_packet['interval'].append(i)

        time_group = df.groupby(['Time'])
        jml_source = len(time_group.Source.get_group(i).unique())
        report_dict['attacker_count'].append(jml_source)
        keanggotaan_source['source_count'].append(jml_source)
        u_source = derajat_source(jml_source)
        keanggotaan_source['source_single'].append(u_source.single)
        keanggotaan_source['source_multi'].append(u_source.multi)
        source = time_group.Source.get_group(i).unique()
        report_dict['attacker_ip'].append(source)
        packet_length = 0
        source_group = df.groupby(['Time', 'Source'])
        for j in source:
            packet_length += source_group.get_group((i, j)).Length.sum()
        avg_length = round(packet_length / len(source), 2)
        report_dict['average_length'].append(avg_length)
        keanggotaan_length['average_length'].append(avg_length)
        u_length = derajat_length(avg_length)
        keanggotaan_length['length_pendek'].append(u_length.pendek)
        keanggotaan_length['length_normal'].append(u_length.normal)
        keanggotaan_length['length_panjang'].append(u_length.panjang)
        jml_data = time_group['No.'].get_group(i).count()
        report_dict['packet_sent'].append(jml_data)
        keanggotaan_packet['packet_count'].append(jml_data)
        u_jmldata = derajat_jmldata(jml_data)
        keanggotaan_packet['packet_sedikit'].append(u_jmldata.sedikit)
        keanggotaan_packet['packet_banyak'].append(u_jmldata.banyak)
        alfa, z = inferensi(u_length, u_source, u_jmldata)
        for j in range(len(rule_set)):
            rule_dict['interval'].append(i)
            rule_dict['rule'].append(rule_set[j])
            if j == 0:
                rule_dict['a'].append(u_jmldata.sedikit)
                rule_dict['b'].append(u_source.single)
                rule_dict['c'].append(u_length.pendek)
            elif j == 1:
                rule_dict['a'].append(u_jmldata.sedikit)
                rule_dict['b'].append(u_source.single)
                rule_dict['c'].append(u_length.normal)
            elif j == 2:
                rule_dict['a'].append(u_jmldata.sedikit)
                rule_dict['b'].append(u_source.single)
                rule_dict['c'].append(u_length.panjang)
            elif j == 3:
                rule_dict['a'].append(u_jmldata.sedikit)
                rule_dict['b'].append(u_source.multi)
                rule_dict['c'].append(u_length.pendek)
            elif j == 4:
                rule_dict['a'].append(u_jmldata.sedikit)
                rule_dict['b'].append(u_source.multi)
                rule_dict['c'].append(u_length.normal)
            elif j == 5:
                rule_dict['a'].append(u_jmldata.sedikit)
                rule_dict['b'].append(u_source.multi)
                rule_dict['c'].append(u_length.panjang)
            elif j == 6:
                rule_dict['a'].append(u_jmldata.banyak)
                rule_dict['b'].append(u_source.single)
                rule_dict['c'].append(u_length.pendek)
            elif j == 7:
                rule_dict['a'].append(u_jmldata.banyak)
                rule_dict['b'].append(u_source.single)
                rule_dict['c'].append(u_length.normal)
            elif j == 8:
                rule_dict['a'].append(u_jmldata.banyak)
                rule_dict['b'].append(u_source.single)
                rule_dict['c'].append(u_length.panjang)
            elif j == 9:
                rule_dict['a'].append(u_jmldata.banyak)
                rule_dict['b'].append(u_source.multi)
                rule_dict['c'].append(u_length.pendek)
            elif j == 10:
                rule_dict['a'].append(u_jmldata.banyak)
                rule_dict['b'].append(u_source.multi)
                rule_dict['c'].append(u_length.normal)
            else:
                rule_dict['a'].append(u_jmldata.banyak)
                rule_dict['b'].append(u_source.multi)
                rule_dict['c'].append(u_length.panjang)
            rule_dict['alfapredikat'].append(alfa[j])
            rule_dict['x'].append(z[j])
        defuzzy = defuzzyikasi(alfa, z)
        if defuzzy < 0.6:
            report_dict['class'].append("NOT_POD")
        else:
            report_dict['class'].append("POD")
        Z.append(defuzzy)
    Z_class = []
    for z in Z:
        if z < 0.5:
            Z_class.append("NOT_POD")
        else:
            Z_class.append("POD")

    if Z_class.count('POD') < Z_class.count('NOT_POD'):
        klasifikasi = 'NOT_POD'
    elif Z_class.count('POD') > Z_class.count('NOT_POD'):
        klasifikasi = 'POD'
    else:
        klasifikasi = 'NOT_POD'

    return report_dict, keanggotaan_length, keanggotaan_source, keanggotaan_packet, rule_dict, \
           Z, Z_class, klasifikasi


def generate_report(report_dict, path, destination, klasifikasi):
    report = pd.DataFrame(report_dict)
    filename = path.split('/')[-1]
    output = filename.split('.')[0] + '-scan.html'
    output_path = path.strip(filename) + output
    to_html_scan(report, output_path, path, destination, klasifikasi)


def generate_calculation(report_dict, keanggotaan_length, keanggotaan_source, keanggotaan_packet, rule_dict,
                         path, destination, klasifikasi):
    report_df = pd.DataFrame(report_dict)
    length_df = pd.DataFrame(keanggotaan_length)
    source_df = pd.DataFrame(keanggotaan_source)
    packet_df = pd.DataFrame(keanggotaan_packet)
    rule_df = pd.DataFrame(rule_dict)
    filename = path.split('/')[-1]
    output = filename.split('.')[0] + '-calculation.html'
    output_path = path.strip(filename) + output
    to_html_calc(report_df, length_df, source_df, packet_df, rule_df, output_path, path, destination, klasifikasi)
