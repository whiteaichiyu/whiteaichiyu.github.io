#!/usr/bin/python
from algoliasearch.search_client import SearchClient
import json
import time
import xlrd
#加载algolia的APIKey和要用的index名
client = SearchClient.create('V4MIQS4IRJ', '45a0ed93c463082f8ec0c481b1ef23dc')
index = client.init_index('jx3wmv')

i=0
def strengthenIndexs(xtext,inum):
    #准备一条新增object范本res
    res = [
        {'title': 'ex', 'permalink': '#'}
    ]
    res[0]['title'] = xtext
    #print(res[0][0]['title'])

    #搜索文本x
    obj = index.search(xtext, {
        'attributesToRetrieve': [
            'objectID'
        ]
    })
    #print(obj)
    #查找搜索文本对应的第一条objectID，未找到则提示未找到目标
    nbhits = obj['nbHits']
    if nbhits == 0:
        print('未找到该团，开始添加')
        #添加新object，objectID自动生成，permalink为#则不会跳转页面
        res = index.save_objects(res, {'autoGenerateObjectIDIfNotExist': True})
    else:
        #objid = obj['hits'][0]['objectID']
        #print('该团已存在，id为：'+objid)
        print('该团已存在')
        #查找对应规则
        exitrule = index.search_rules(xtext)
        print(exitrule)
        r = exitrule['hits']
        if len(r)!=0:                    
            #删除对应规则
            index.delete_rule(exitrule['hits'][0]['objectID'])
        else:
            print('未找到相关规则,请到前台检查规则集中是否添加该规则')
    #构建对应规则
    rule = {
    "conditions": [
        {
        "anchoring": "contains",
        "pattern": "example",
        "alternatives": True
        },
        {
        "anchoring": "contains",
        "pattern": "ex",
        "alternatives": True
        },
        {
        "anchoring": "contains",
        "pattern": "exa",
        "alternatives": True
        },
        {
        "anchoring": "contains",
        "pattern": "exam",
        "alternatives": True
        },
        {
        "anchoring": "contains",
        "pattern": "examp",
        "alternatives": True
        }               
    ],
    "consequence": {
        "promote": [
        {
            "objectIDs": [
            "需要绑定的对应obj的objectID"
            ],
            "position": 0
        }
        ],
        "filterPromotes": True
    },
    "enabled": True,
    "objectID": "需要新增的规则objectID"
    }
    #此规则触发条件pattern值,除了完全匹配还支持第1-第5个字符间查询
    rule['conditions'][0]['pattern'] = str(xtext)           
    rule['conditions'][1]['pattern'] = str(xtext)[0:2]
    rule['conditions'][2]['pattern'] = str(xtext)[0:3]
    rule['conditions'][3]['pattern'] = str(xtext)[0:4]
    rule['conditions'][4]['pattern'] = str(xtext)[0:5]            
    #此规则需要绑定的目标索引obj值位置
    zzz = rule['consequence']['promote'][0]['objectIDs']
    ttype = ['w0001','w0002','w0003','w0004']
    ttypen = 0
    if (inum+1)%4==1:
        ttypen = 0
    elif (inum+1)%4==2:
        ttypen = 1
    elif (inum+1)%4==3:
        ttypen = 2
    elif (inum+1)%4==0:
        ttypen = 3
    zzz[0] = ttype[ttypen]
    #制做该规则的objectID
    lb="rules"
    #需要新增的objectID位置以及将其赋值为lb+当前时间数字的拼接字符串
    rule['objectID'] = lb+str(int(time.time()))
    print(rule['objectID'])
    print(rule['consequence']['promote'][0]['objectIDs'])
    #提交规则
    response = index.save_rule(rule)
    print(response)
# #搜索文本
# obj = index.search('纯阳', {
#     'attributesToRetrieve': [
#         'objectID'
#     ]
# })
# # print(obj)
# #查找搜索文本对应的第一条objectID，未找到则提示未找到目标
# nbhits = obj['nbHits']
# # ord(nbhits)
# if nbhits == 0:
#     print('未找到目标')
# else:
#     x = obj['hits'][0]['objectID']
#     print(x)


#添加一条object，objectID自动生成，permalink为#则不会跳转页面
# res = index.save_objects([
#     {'title': '200', 'answer': 'gget', 'permalink': '#'}
# ], {'autoGenerateObjectIDIfNotExist': True})



# #添加一条规则
# rule = {
# "conditions": [
#     {
#       "anchoring": "contains",
#       "pattern": "气纯",
#       "alternatives": True
#     }
#   ],
#   "consequence": {
#     "promote": [
#       {
#         "objectIDs": [
#           "需要绑定的obj值"
#         ],
#         "position": 0
#       }
#     ],
#     "filterPromotes": True
#   },
#   "enabled": True,
#   "objectID": "需要新增的objectID"
# }

# #此规则需要绑定的目标索引obj值位置
# zzz = rule['consequence']['promote'][0]['objectIDs']

# zzz[0] = x
# #制做该规则的objectID
# lb="white"
# #需要新增的objectID位置以及将其赋值为lb+当前时间数字的拼接字符串
# rule['objectID'] = lb+str(int(time.time()))
# print(rule['objectID'])
# print(rule['consequence']['promote'][0]['objectIDs'])
# #提交规则
# response = index.save_rule(rule)
# print(response)

#-----副本表格数据批量导入algolia搜索-----

#表格文件路径
file = 'yxt.xlsx'
#打开表格
wb = xlrd.open_workbook(filename=file)
print(wb.sheet_names())
#通过索引获取表格
sheet_yxt = wb.sheet_by_index(0)
#获取表格行数
nrows = sheet_yxt.nrows

#遍历表格行列

for n in range(1,nrows):
#获取第n行内容，存入数组rows
    rows = sheet_yxt.row_values(n)
    for x in rows:
        if (i+1)%4==1 and len(x)!=0:
            strengthenIndexs(xtext=x,inum=i)
            # print('金团：'+x)
            # #准备一条新增object范本res
            # res = [
            #     {'title': 'ex', 'permalink': '#'}
            # ]
            # res[0]['title'] = x
            # #print(res[0][0]['title'])
            # #搜索文本x
            # obj = index.search(x, {
            #     'attributesToRetrieve': [
            #         'objectID'
            #     ]
            # })
            # print(obj)
            # #查找搜索文本对应的第一条objectID，未找到则提示未找到目标
            # nbhits = obj['nbHits']
            # if nbhits == 0:
            #     print('未找到该团，开始添加')
            #     #添加新object，objectID自动生成，permalink为#则不会跳转页面
            #     res = index.save_objects(res, {'autoGenerateObjectIDIfNotExist': True})
            # else:
            #     objid = obj['hits'][0]['objectID']
            #     print('该团已存在，id为：'+objid)
            #     #查找对应规则
            #     exitrule = index.search_rules(x)
            #     print(exitrule)
            #     r = exitrule['hits']
            #     if len(r)!=0:                    
            #         #删除对应规则
            #         index.delete_rule(exitrule['hits'][0]['objectID'])
            #     else:
            #         print('未找到相关规则')
            # #构建对应规则
            # #添加一条规则
            # rule = {
            # "conditions": [
            #     {
            #     "anchoring": "contains",
            #     "pattern": "example",
            #     "alternatives": True
            #     },
            #     {
            #     "anchoring": "contains",
            #     "pattern": "ex",
            #     "alternatives": True
            #     },
            #     {
            #     "anchoring": "contains",
            #     "pattern": "exa",
            #     "alternatives": True
            #     },
            #     {
            #     "anchoring": "contains",
            #     "pattern": "exam",
            #     "alternatives": True
            #     },
            #     {
            #     "anchoring": "contains",
            #     "pattern": "examp",
            #     "alternatives": True
            #     }               
            # ],
            # "consequence": {
            #     "promote": [
            #     {
            #         "objectIDs": [
            #         "需要绑定的obj值"
            #         ],
            #         "position": 0
            #     }
            #     ],
            #     "filterPromotes": True
            # },
            # "enabled": True,
            # "objectID": "需要新增的规则objectID"
            # }
            # #此规则触发条件pattern值,除了完全匹配还支持第1-第5个字符间查询
            # rule['conditions'][0]['pattern'] = str(x)           
            # rule['conditions'][1]['pattern'] = str(x)[0:2]
            # rule['conditions'][2]['pattern'] = str(x)[0:3]
            # rule['conditions'][3]['pattern'] = str(x)[0:4]
            # rule['conditions'][4]['pattern'] = str(x)[0:5]            
            # #此规则需要绑定的目标索引obj值位置
            # zzz = rule['consequence']['promote'][0]['objectIDs']
            # zzz[0] = 'w0001'
            # #制做该规则的objectID
            # lb="rules"
            # #需要新增的objectID位置以及将其赋值为lb+当前时间数字的拼接字符串
            # rule['objectID'] = lb+str(int(time.time()))
            # print(rule['objectID'])
            # print(rule['consequence']['promote'][0]['objectIDs'])
            # #提交规则
            # response = index.save_rule(rule)
            # print(response)
        elif (i+1)%4==2 and len(x)!=0:
            strengthenIndexs(xtext=x,inum=i)
            #print('能进的团：'+x)
        elif (i+1)%4==3 and len(x)!=0:
            strengthenIndexs(xtext=x,inum=i)
            #print('坑团：'+x)
        elif (i+1)%4==0 and len(x)!=0:
            strengthenIndexs(xtext=x,inum=i)
            #print('人品不行但是能打的团：'+x)
        i=i+1
