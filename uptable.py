#!/usr/bin/env python
import time
import xlrd
#表格文件路径
file = 'yxt.xlsx';
#打开表格
wb = xlrd.open_workbook(filename=file);
print(wb.sheet_names());
#通过索引获取表格
sheet_yxt = wb.sheet_by_index(0);
#获取表格行数
nrows = sheet_yxt.nrows;

today = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime());
f=open('source\_posts\page.md', 'w', encoding='utf-8');
#data = f.read()
f.write('---\ntitle: 蝶服英雄团\n');
f.write('date: ');
f.write(today);
f.write('\n');
f.write('tags:\n---\n');
f.write('|金团|能进的团|坑团|人品不行但是能打的团|\n');
f.write('| -------------  | ------------- | ------------- | ------------- |\n');

#遍历表格行列,写入markdown文档
for n in range(1,nrows):
    #获取第n行内容，存入数组rows
    rows = sheet_yxt.row_values(n);
    for x in rows:
        f.write('|');
        f.write(x);
    f.write('|');
    f.write('\n');

f.write('\n{% img [fullimage] /images/all-foot.jpg [title 全门派 [alt text]] %}')