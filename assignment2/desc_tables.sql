select name
from sqlite_master
where type = 'table';
pragma table_info(frequency);
select *
from frequency
limit 5;
select count(*)
from (select *
from frequency where docid='10398_txt_earn') x;
select *
from frequency where docid='10398_txt_earn' and count=1;
select count(term), count(distinct(term))
from frequency where docid='10398_txt_earn' and count=1;
select count(term), count(distinct(term))
from (
select term
from frequency where docid='10398_txt_earn' and count=1
union
select term
from frequency where docid='925_txt_trade' and count=1) x;
select docid, count(docid), sum(term)
from frequency where term='parliament';
select count(*) from (select distinct(docid)
from frequency
group by docid
having sum(count)>300) x;
select a.docid, b.docid, a.term, b.term
from frequency a, frequency b
where a.docid = b.docid
and a.term = 'transactions'
and b.term = 'world';
