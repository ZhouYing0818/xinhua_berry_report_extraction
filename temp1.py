ngs=re.findall(r'NGS_\d+',filename)[0]
inform=defaultdict(list)
temp=defaultdict(list)

'''提取页面布局'''
i=0
for page in doc.get_pages():
    i+=1
    interpreter.process_page(page)
    exec('layout'+str(i)+'=device.get_result()')
page_num=i

'''提取页面中的水平文本信息'''
i=0    
for x in layout1:
    if(isinstance(x,LTTextBoxHorizontal)):
        i+=1
        results=x.get_text()
        if ngs in results:
            continue           
        else:
            inform['layout1'].append(results.split('\n')[0])
            
for x in layout2:
    if(isinstance(x,LTTextBoxHorizontal)):
        i+=1
        results=x.get_text()
        if ngs in results:
            continue           
        else:
            inform['layout2'].append(results.split('\n')[0])
            
temp['NGS编号'].append(ngs)
temp['报告名称'].append(inform['layout1'][0])
temp['检测类型'].append(inform['layout1'][1].split('：')[1])

for i in range(len(inform['layout1'])):
    text=inform['layout1'][i]
	tmp=''
    if '检测结果' in text:
		while i>0：
			tmp+=text
			if '检测人' in text:
				break
print(tmp)

temp['基因'].append(inform['layout2'][8])
temp['突变位置'].append(inform['layout2'][9])
temp['外显子'].append(inform['layout2'][10])
temp['HGVS'].append(inform['layout2'][11])
temp['突变类型'].append(inform['layout2'][12])
temp['杂合性'].append(inform['layout2'][13])
temp['变异评级'].append(inform['layout2'][14])
temp['疾病及遗传方式'].append(inform['layout2'][15])
temp=pd.DataFrame(temp)