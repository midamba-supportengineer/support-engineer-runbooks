-- log_analysis.sql
-- Sample queries I used daily at Microsoft Tier 2 and ModSquad
-- for customer log analysis and issue root-cause

-- 1. Find most common errors in last 7 days
SELECT 
    error_code,
    COUNT(*) as occurrences,
    MAX(timestamp) as last_occurred
FROM customer_logs
WHERE timestamp >= NOW() - INTERVAL '7 days'
GROUP BY error_code
ORDER BY occurrences DESC
LIMIT 10;

-- 2. Slow API calls (query optimization example)
SELECT 
    endpoint,
    AVG(response_time_ms) as avg_time,
    COUNT(*) as calls
FROM api_logs
WHERE response_time_ms > 2000
GROUP BY endpoint
HAVING COUNT(*) > 5
ORDER BY avg_time DESC;

-- 3. User-specific issue tracking (for Slack triage)
SELECT 
    user_id,
    COUNT(DISTINCT error_code) as unique_errors,
    STRING_AGG(error_code, ', ') as error_list
FROM customer_logs
WHERE user_id = 'example_user_123'
GROUP BY user_id;
