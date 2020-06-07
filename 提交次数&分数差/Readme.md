+ result.json的结构：

```
res是一个字典，key为user_id，value为以case_id为索引的对象case，
对象case包含case_type, valid_time, commit_num, score_inc
```

+ 脚本说明：
  + 考虑到debug时期第一次提交可能出现的0分情况，提交次数没有从第一次非零分提交算起，而是直接取全部提交次数
  + 存在某case无提交记录的情况，按分数差0分，提交次数取所有记录中的最大次数处理
  + 归一化方法采用``(x - min) / (max - min)``

