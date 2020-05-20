import csv
#将待处理的几列数据单独提取出来
with open('cbg_patterns.csv','r',encoding='utf-8') as csvfile:
    reader=csv.DictReader(csvfile)
    related_same_day_brand=[]
    related_same_month_brand=[]
    top_brands=[]
    for row in reader:
        top_brands.append(row['top_brands'])
        related_same_day_brand.append(row['related_same_day_brand'])
        related_same_month_brand.append(row['related_same_month_brand'])
#将三列数据分别存放在三个.csv文件中
def savecsv(filename,filedata):
    f = open(filename, 'w', newline="", encoding='utf-8')
    csv_writer = csv.writer(f)
    for a in filedata:
        b = a.replace('[', '').replace(']', '')
        if b == '': continue
        csv_writer.writerow([b])
    f.close()
savecsv('top_brands.csv',top_brands)
savecsv('related_same_day_brand.csv',related_same_day_brand)
savecsv('related_same_month_brand.csv',related_same_day_brand)