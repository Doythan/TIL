-- Active: 1728541897102@@127.0.0.1@3306

-- 01. Querying data
SELECT
  LastName
FROM
  employees;

SELECT LastName, FirstName
FROM employees;

SELECT *
FROM employees;

SELECT FirstName AS '이름'
FROM employees

SELECT Name AS 이름, Milliseconds / 60000 AS '재생 시간(분)'
FROM tracks

-- 02. Sorting data
SELECT FirstName
FROM employees
ORDER BY "FirstName" ASC;

SELECT FirstName
FROM employees
ORDER BY "FirstName" DESC;

SELECT Country, City
FROM customers
ORDER BY "Country" DESC, "City" ASC;

SELECT Name, Milliseconds / 60000 AS '재생 시간(분)'
FROM tracks
ORDER BY "Milliseconds" DESC;

-- NULL 정렬 예시
SELECT ReportsTo
From employees
ORDER BY "ReportsTo";

-- 03. Filtering data
SELECT Country
FROM customers
ORDER BY "Country" ASC;

SELECT DISTINCT Country 
FROM customers
ORDER BY "Country" ASC;

SELECT "LastName", "FirstName", "City"
FROM customers
WHERE City = 'Prague';

SELECT "LastName", "FirstName", "City"
FROM customers
WHERE City != 'Prague';

SELECT LastName, FirstName, Company, Country
FROM customers
WHERE Company IS NULL AND "Country" = 'USA';

SELECT LastName, FirstName, Company, Country
FROM customers
WHERE Company IS NULL OR "Country" = 'USA';

SELECT Name, Bytes
FROM tracks
-- WHERE "Bytes" >= 10000 AND "Bytes" <= 500000;
WHERE "Bytes" BETWEEN 10000 AND 500000;

SELECT LastName, FirstName, Country
FROM customers 
-- WHERE "Country" = 'Canada' OR "Country" = 'Germany' OR "Country" = 'France';
WHERE "Country" IN ('Canada', 'Germany', 'France');

SELECT LastName, FirstName, Country
FROM customers 
WHERE "Country" NOT IN ('Canada', 'Germany', 'France');

SELECT LastName, FirstName
FROM customers
WHERE "LastName" Like '%son';

SELECT LastName, FirstName
FROM customers
WHERE "FirstName" Like '___a';

SELECT "TrackId", "Name", "Bytes"
FROM tracks
ORDER BY "Bytes" DESC
LIMIT 7;

SELECT "TrackId", "Name", "Bytes"
FROM tracks
ORDER BY "Bytes" DESC
-- LIMIT 3, 4;
LIMIT 4 OFFSET 3; 

-- 04. Grouping data
SELECT COUNTRY
FROM customers
GROUP BY "Country";

SELECT COUNTRY, count(*)
FROM customers
GROUP BY "Country";

SELECT "Composer", avg("Bytes") AS avg0fBytes
FROM tracks 
GROUP BY "Composer"
ORDER BY avg0fBytes DESC;

SELECT "Composer", avg("Milliseconds" / 60000) AS avg0fMinute
FROM tracks 
GROUP BY "Composer"
HAVING avg0fMinute < 10;

