select name
from sqlite_master
where type = 'table';
pragma table_info(frequency);
select a.docid, b.docid, sum(a.count*b.count)
from frequency a, frequency b
where a.term = b.term
  and a.docid = '10080_txt_crude' and b.docid = '17035_txt_earn'
group by a.docid, b.docid;
drop view q;
create view q as 
select *
from frequency
union
select 'q' as docid, 'washington' as term, 1 as count
union 
select 'q' as docid, 'taxes' as term, 1 as count
union 
select 'q' as docid, 'treasury' as term, 1 as count;
select a.docid, b.docid, sum(a.count*b.count)
from q a, q b
where a.term = b.term
  and b.docid = 'q'
group by a.docid, b.docid
order by sum(a.count*b.count) desc;
