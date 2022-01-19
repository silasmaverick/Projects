{{
    config(
        materialized='table'
    )

}}

with source as (

    select * from {{ ref('stg__events') }}

),

get_previous_timestamp as (

    select
        *,
        LAG(event_timestamp) OVER (PARTITION BY cookie_id ORDER BY event_timestamp) as get_previous_timestamp
    from source
),

flag_new_session as (

    select
        *,
        CASE WHEN data_diff('minute', previous_timestamp, event_timestamp) >=30 OR previous_timestamp is NULL THEN 1 ELSE 0 END as new_session
    from get_previous_timestamp

)

get_session_idx as (

    select
    *,
    SUM(new_session)OVER (PARTITION BY cookie_id) ORDER BY event_timestamp ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS session_idx 
from flag_new_session

),

create_session_id as (
select
    *,
    {{ dbt_utils.surrogate_key(['cookie_id','session_idx']) }} as session_id
from get_session_idx

)


select * from get_previous_timestamp

