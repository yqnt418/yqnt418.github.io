# 利用临时表进行 批量 update
```
# 创建临时表 tmp
CREATE TEMPORARY TABLE tmp("name" text, "checked" BOOLEAN, "begin" numeric, "end" numeric);

# 批量插入数据 --> 临时表 tmp
insert INTO tmp VALUES
('APP4.10',	TRUE,	6614.965,	6620.86),
('TO1.32',	TRUE,	2263.14,	2266.9),
('TO1.34',	TRUE,	2297.38,	2304.69),
('TO1.35',	TRUE,	2324.285,	2336.69),
('TO1.36',	TRUE,	2333.136,	2338.256),
('TO4.18',	TRUE,	3301.081,	3327.37),
('TO4.2',	TRUE,	3301.081,	3327.37),
('TO4.3',	TRUE,	3301.081,	3327.37),
('TO6.11',	TRUE,	3575.66,	3578.74),
('TO6.12',	TRUE,	3587.16,	3591.6),
('TO6.13',	TRUE,	3587.16,	3591.6),
('TO6.14',	TRUE,	3587.16,	3591.6),
('TO6.15',	TRUE,	3587.16,	3591.6),
('TO6.16',	TRUE,	3587.16,	3591.6),
('TO6.17',	TRUE,	3606.619,	3606.779);

# 更新临时表 tmp 中的数据到目标表 sop
UPDATE sop
SET 
    "checked"=tmp."checked",
    "begin"=tmp."begin",
    "end"=tmp."end"
FROM tmp
WHERE sop."name"=tmp."name"
AND sop."flightItemId"='21062658-e08e-4749-9425-94cb5624330d';

# 删除临时表
DROP TABLE tmp;
```
