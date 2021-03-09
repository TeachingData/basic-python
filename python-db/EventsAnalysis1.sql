select * from attending;

SELECT 
    ROUND(
    (SELECT count(last_update) FROM contacts WHERE last_update NOT LIKE '%2020' AND added NOT LIKE '%2020') * 1.0 
    / (SELECT count(last_update) FROM contacts) * 100, 2) AS updated_percentage
FROM contacts limit 1;

-- let's rebuild this with two CTEs (note where the semicolon)
WITH not_updated AS (SELECT count(last_update)
    FROM contacts 
    WHERE last_update NOT LIKE '%2020' AND added NOT LIKE '%2020')
SELECT * FROM not_updated;

WITH total_contacts AS (SELECT count(last_update) FROM contacts)
SELECT * from total_contacts; 

-- Note if we run the select it will fail because not_updated & total_contacts don't exist anymore
-- we use 2 at a time by using a comma (not second WITH)
WITH not_updated AS (SELECT count(last_update)
    FROM contacts 
    WHERE last_update NOT LIKE '%2020' AND added NOT LIKE '%2020'), -- see comma
    
    total_contacts AS (SELECT count(last_update) FROM contacts) -- second part of with

SELECT ROUND((SELECT * FROM not_updated) * 1.0 / 
    (SELECT * FROM total_contacts) * 100.0, 2) 
    AS to_update_percent
FROM contacts limit 1;

-- let's make a view of this because Developers will need it a lot during calculations
DROP VIEW 'updated';
CREATE VIEW 'updated' AS 
WITH total_contacts AS (SELECT count(last_update) FROM contacts)
    SELECT 
        ROUND(
        (SELECT count(*) FROM contacts WHERE last_update NOT LIKE '%2020' AND added NOT LIKE '%2020') * 1.0 
        / (SELECT * from total_contacts) * 100, 2) AS updated_percentage
        FROM contacts limit 1;
        
select updated_percentage from updated;
-- WHY NOT A TABLE?
CREATE TABLE 'updatedTB' AS SELECT 
        ROUND(
        (SELECT count(*) FROM contacts WHERE last_update NOT LIKE '%2020' AND added NOT LIKE '%2020') * 1.0 
        / (SELECT count(*) FROM contacts) * 100, 2) AS updated_percentage
        FROM contacts limit 1;
        
-- NOTE SOMETIMES I WANT A TABLE SOMETIMES NOT

-- Let's look at something else fun we can do with this: like a count of events being attended
select event_id, count(event_id) from attending group by event_id;
-- and let's see whose attending events (and how many)
select c.comp_id, c.comp_name, count(a.event_id) from attending a
    inner join competitors c on c.comp_id = a.comp_id
    group by c.comp_id;
-- now let's build an attendance (popularity) calculator
-- build the attendance calculator cte for total people attending (use having) vs. number that could attend
-- i.e. 1 person out of 10 attended - it was 10% popular
-- ALWAYS DROP VIEWS (cause we need fresh data)
drop view if exists event_popularity;
create view 'event_popularity' as
with popular(cur_id, cur_event, num_attended) as (select e.event_id, e.event_descript, count(a.event_id) 
    from attending a 
    inner join events e on e.event_id = a.event_id group by a.event_id),
    -- the above is actually kinda silly but meant to show 3 column cte - I could just use num_attended
    total_attend as (select count(comp_id) from competitors)
select cur_id, cur_event, (num_attended * 1.0 / (select * from total_attend)) as popularity from popular where cur_id == 1011;

select * from event_popularity;
-- now make the first part a view (why is this good as a view?) - why would we make total_attend into a table?
-- option 2: of the people who did attend, how many attended each event (percentage)?
with total_attended(eid, attend_per) as (select event_id, count(event_id) from attending group by event_id),
     total_did(attend_all) as (select count(event_id) from attending)

select eid, (attend_per * 1.0 / (select attend_all from total_did)) from total_attended;
