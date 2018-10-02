import pdfkit
import os
import logging

logging.basicConfig(filename='process.log',level=logging.DEBUG)

options = {
    'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'custom-header' : [
        ('Accept-Encoding', 'gzip')
    ],
    'cookie': [
        ('cookie-name1', 'cookie-value1'),
        ('cookie-name2', 'cookie-value2'),
    ],
    'no-outline': None,
    #'load-error-handling': 'ignore'
}

logging.basicConfig(filename="logfilename.log", level=logging.INFO)

def textToPdf(source, destiny):
    logging.debug('Processing the ' + source + ' file ')
    os.rename(source, source + '.txt')
    path_wkthmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    pdfkit.from_file(source + '.txt', destiny, configuration=config, options=options)
    os.rename(source + '.txt', source)
    logging.debug('Finished')
