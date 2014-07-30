select name
from sqlite_master
where type = 'table';
pragma table_info(a);
pragma table_info(b);
select *
from a
where a.row_num = 2;
select *
from b
where b.col_num = 3;
select a.row_num, b.col_num, sum(a.value*b.value)
from a,b
where a.row_num = 2 and b.col_num = 3
and a.col_num = b.row_num
group by a.row_num, b.col_num;
