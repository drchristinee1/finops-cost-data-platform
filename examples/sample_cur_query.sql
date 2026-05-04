-- Daily cost by service (AWS CUR via Athena)
SELECT
  DATE(line_item_usage_start_date) AS usage_date,
  product_product_name            AS service,
  SUM(line_item_unblended_cost)   AS cost_usd
FROM cur_db.cur_table
WHERE line_item_usage_start_date >= date_add('day', -7, current_date)
GROUP BY 1, 2
ORDER BY 1 DESC, 3 DESC;