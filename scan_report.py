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


def to_html_scan(df, filename, path, target, result):
    """
    Write an entire dataframe to an HTML file
    with nice formatting.
    Thanks to @stackoverflowuser2010 for the
    pretty printer see https://stackoverflow.com/a/47723330/362951
    """
    ht = ''
    ht += '<h1> DDOS Ping of Death Scan Report </h1>\n'
    ht += '<h1> %s </h1>\n' % now.strftime("%Y-%m-%d %H:%M")
    ht += '<p>Source file : %s </p>' % path
    ht += '<p>Server IP : %s </p>' % target
    ht += '<p>Scan Result : '
    if result == 'NOT_POD':
        ht += '<span style="color: #00ff00;"> %s </span></p>' % result
    else:
        ht += '<span style="color: #ff0000;"> %s </span></p>' % result
    ht += df.to_html(classes='wide', escape=False, index=False, justify='center')

    with open(filename, 'w') as f:
         f.write(HTML_TEMPLATE1 + ht + HTML_TEMPLATE2)