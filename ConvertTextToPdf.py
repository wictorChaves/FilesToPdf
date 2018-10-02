import pdfkit
import logging
from shutil import copyfile
from ConfigFile import options_pdf
from ConfigFile import path_wkthmltopdf

logging.basicConfig(filename='process.log',level=logging.DEBUG)

source = ''

def convert(source, destiny):
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    pdfkit.from_file(source, destiny, configuration=config, options=options_pdf)

def textToPdf(source, destiny):
    logging.debug('Processing the ' + source + ' file ')
    copyfile(source, 'temp/temp.txt')
    convert('temp/temp.txt', destiny)
    logging.debug('Finished')


