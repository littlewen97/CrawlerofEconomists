# KnowledgeGraphofEconomists
课程作业：关于经济学家的知识图谱，这里主要是爬虫

- baidubaikeSearch.py: 搜索economist.txt中的经济学家，保存url地址到baike_url.txt
- ideas_url.py: 从"[Top 10% Authors, as of October 2019](https://ideas.repec.org/top/top.person.all.html)"获取前10%的经济学家详情页面的地址，存到ideas_url.txt中。
- ideas_detail.py: 从经济学家详情页面获取姓名、所属组织（通常是xx大学）、10篇已发表的文章，存储到economists.csv。
- ideas_shorttop.py:从"[Top 10% Authors, as of October 2019](https://ideas.repec.org/top/top.person.all.html)"获取前5%的经济学家的姓名和所属组织，存储到top2858.csv。（后来舍弃不用，用economists.csv替代）