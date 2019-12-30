import datetime


HTML_TEMPLATE1 = '''
<html>
<head>
<style>
  h1 {
    text-align: center;
  }
  table { 
    margin-left: auto;
    margin-right: auto;
  }
  table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
    text-align: center;
  }
  th, td {
    padding: 5px;
    text-align: center;
    font-family: Helvetica, Arial, sans-serif;
    font-size: 90%;
  }
  th{
    background-color: #595b5d
  }
  table tbody tr:hover {
    background-color: #dddddd;
  }
  .wide {
    width: 90%; 
  }
</style>
</head>
<body>
'''

HTML_TEMPLATE2 = '''
</body>
</html>
'''

now = datetime.datetime.now()


def to_html_calc(report, length, source, packet, rule, filename, path, target, result):
    """
    Write an entire dataframe to an HTML file
    with nice formatting.
    Thanks to @stackoverflowuser2010 for the
    pretty printer see https://stackoverflow.com/a/47723330/362951
    """
    ht = ''
    ht += '<h1><b>DDOS Ping of Death Calculation Report</b></h1>\n'
    ht += '<h1><b> %s </b></h1>\n' % now.strftime("%Y-%m-%d %H:%M")
    ht += '<h2><b><br>Source file : %s </b></h2>' % path
    ht += '<h2><b>Server IP : %s </b></h2>' % target
    ht += '<h2><b>Scan Result : '
    if result == 'NOT_POD':
        ht += '<span style="color: #00ff00;"> %s </span></b></h2>' % result
    else:
        ht += '<span style="color: #ff0000;"> %s </span></b></h2>' % result
    ht += '<h2><b>Calculation Result : </b></h2>'
    Z = []
    for i in range(len(rule.interval.unique())):
        alfa = rule.alfapredikat[rule['interval'] == i].tolist()
        x = rule.x[rule['interval'] == i].tolist()
        alfa_x = []
        alfax = []
        for j in range(len(alfa)):
            alfa_x.append(str(alfa[j]) + '*' + str(x[j]))
            alfax.append(round(alfa[j] * x[j], 2))
        Z.append(round(sum(alfax) / sum(alfa), 2))
        ht += '<p><b><br>&emsp;%s. Interval ke-%s</b></p>' % (i + 1, i)
        ht += '<p>&emsp;&emsp;&emsp;Derajat keanggotaan panjang paket : <p>'
        ht += length[length['interval'] == i].to_html(classes='wide', escape=False, index=False, justify='center')
        ht += '<p>&emsp;&emsp;&emsp;Derajat keanggotaan jumlah attacker : <p>'
        ht += source[source['interval'] == i].to_html(classes='wide', escape=False, index=False, justify='center')
        ht += '<p>&emsp;&emsp;&emsp;Derajat keanggotaan jumlah paket : <p>'
        ht += packet[packet['interval'] == i].to_html(classes='wide', escape=False, index=False, justify='center')
        ht += '<p>&emsp;&emsp;&emsp;Inferensi : <p>'
        ht += rule[rule['interval'] == i].to_html(classes='wide', escape=False, index=False, justify='center')
        ht += '<p>&emsp;&emsp;&emsp;Defuzzyfikasi : </p>'
        ht += '<p><br>&emsp;&emsp;&emsp;Z%s = ' % i
        ht += '(' + ' + '.join(alfa_x) + ')' + ' : <span style="color: #ff0000;">' + '(' + ' + '.join(
            map(str, alfa)) + ')'
        ht += '</p>'
        ht += '<p>&emsp;&emsp;&emsp;Z%s = ' % i
        ht += '(' + ' + '.join(map(str, alfax)) + ')' + ' : <span style="color: #ff0000;">' + str(sum(alfa))
        ht += '</p>'
        ht += '<p>&emsp;&emsp;&emsp;Z%s = ' % i
        ht += str(sum(alfax)) + ' : <span style="color: #ff0000;">' + str(sum(alfa))
        ht += '</p>'
        ht += '<p>&emsp;&emsp;&emsp;Z%s = ' % i
        ht += str(round(sum(alfax) / sum(alfa), 2))
        ht += '</p>'
        kelas = report['class'][report['interval(second)'] == i].tolist()[0]
        ht += '<p>&emsp;&emsp;&emsp;Hasil deteksi : %s</p>' % kelas
    ht += '<h2><center><br><b>Final Result : </b></center></h2>'
    ht += '<h2><center><span style="color: #00ff00;">NOT_POD : %s</center></h2>' % \
          report[report['class'] == 'NOT_POD'].count()[0]
    ht += '<h2><center><span style="color: #ff0000;">POD : %s</center></h2>' % report[report['class'] == 'POD'].count()[
        0]

    with open(filename, 'w') as f:
        f.write(HTML_TEMPLATE1 + ht + HTML_TEMPLATE2)