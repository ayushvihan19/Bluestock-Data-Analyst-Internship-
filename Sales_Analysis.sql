-- WEEK 1: SALES ANALYSIS SQL PRACTICE
-- Dataset: Synthetic Sales Dataset
-- Columns: Order_ID, Order_Date, Customer_ID, Product,
-- Category, Quantity, Unit_Price, Region,
-- Payment_Method, Revenue, Month

-- 1. View all records
SELECT *
FROM sales;

-- 2. View the first 10 records
SELECT *
FROM sales
LIMIT 10;

-- 3. Calculate total revenue
SELECT SUM(Revenue) AS Total_Revenue
FROM sales;

-- 4. Count distinct orders
SELECT COUNT(DISTINCT Order_ID) AS Total_Orders
FROM sales;

-- 5. Calculate total units sold
SELECT SUM(Quantity) AS Units_Sold
FROM sales;

-- 6. Revenue by product
SELECT Product, SUM(Revenue) AS Total_Revenue
FROM sales
GROUP BY Product
ORDER BY Total_Revenue DESC;

-- 7. Revenue by category
SELECT Category, SUM(Revenue) AS Total_Revenue
FROM sales
GROUP BY Category
ORDER BY Total_Revenue DESC;

-- 8. Revenue by region
SELECT Region, SUM(Revenue) AS Total_Revenue
FROM sales
GROUP BY Region
ORDER BY Total_Revenue DESC;

-- 9. Monthly revenue trend
SELECT Month, SUM(Revenue) AS Monthly_Revenue
FROM sales
GROUP BY Month
ORDER BY Month;

-- 10. Products with revenue above 10000
SELECT Product, SUM(Revenue) AS Total_Revenue
FROM sales
GROUP BY Product
HAVING SUM(Revenue) > 10000;

-- 11. Average order value
SELECT
    ROUND(
        1.0 * SUM(Revenue) / COUNT(DISTINCT Order_ID),
        2
    ) AS Average_Order_Value
FROM sales; 
-- 12. Payment method analysis
SELECT Payment_Method, COUNT(*) AS Order_Count,
       SUM(Revenue) AS Total_Revenue
FROM sales
GROUP BY Payment_Method
ORDER BY Total_Revenue DESC;