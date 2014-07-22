from lxml import etree
import csv

settings = open('settings.txt').read().strip()
output_file = 'csv/' + settings.split('.')[0] + '.csv'
document = etree.parse(open(settings), etree.XMLParser())
output = csv.writer(open(output_file, 'wb'))
output.writerow(('id', 'in', 'out', 'start', 'end', 'duration', 'text'))

i = 0

for item in document.xpath('//generatoritem'):
    output.writerow((i, item.xpath('in')[0].text.encode('utf-8'), item.xpath('out')[0].text.encode('utf-8'), item.xpath('start')[0].text.encode('utf-8'), item.xpath('end')[0].text.encode('utf-8'), item.xpath('duration')[0].text.encode('utf-8'), item.xpath('effect/parameter/value')[0].text.encode('utf-8')))

    i = i + 1
