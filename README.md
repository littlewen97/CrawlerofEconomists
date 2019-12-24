# CrawlerofEconomists
课程作业：关于经济学家的知识图谱，这里主要是爬虫

### 杰出经济学家数据
- economist.txt: 历史上获得巨大成就的经济学家（通常是获得诺贝尔经济学奖，某经济学派创始人，某经济理论提出者）
- baidubaikeSearch.py: 搜索economist.txt中的经济学家，保存url地址到baike_url.txt
<br/> 
<br/> 

### 经济学家数据
- ideas_url.py: 从"[Author Information](https://ideas.repec.org/i/e.html)"获取所有经济学家详情页面的地址，存到ideas_all_url.txt中。
- ideas_detail.py: 从经济学家详情页面获取姓名、所属组织（通常是xx大学）、已发表的文章，存储到economists_all.csv。
<br/>
<br/> 

### 经济学家所属机构数据
- aff_url: 从aff.txt文件中读取组织的名称查百度百科，保存url地址到aff_url.txt
- aff_detail: 爬取aff_url.txt中的地址，只爬取xxx大学的词条，爬取中文名，外文名，简称，创办时间等信息，存到aff_detail.csv
