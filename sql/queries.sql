-- Total revenue
SELECT SUM(revenue) AS total_revenue FROM sales;

-- Top selling products
SELECT product, SUM(revenue) AS total
FROM sales
GROUP BY product
ORDER BY total DESC;

-- Daily revenue
SELECT date, SUM(revenue) AS daily_revenue
FROM sales
GROUP BY date
ORDER BY date;
