
select h.hacker_id, h.name, sum(ms.m_score) as sum_from_m_score
from hackers h
inner join (
  select hacker_id, challenge_id, max(score) as m_score
  from submissions
  group by hacker_id, challenge_id
) ms on h.hacker_id = ms.hacker_id
group by h.hacker_id, h.name
having sum_from_m_score > 0
order by sum_from_m_score desc, h.hacker_id asc;