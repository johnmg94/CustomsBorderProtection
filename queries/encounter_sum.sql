SELECT FISCAL_YEAR, MONTH, SUM(ENCOUNTER_COUNT)
FROM nationwide_encounters_fy22_25
GROUP BY MONTH, FISCAL_YEAR
ORDER BY FISCAL_YEAR,
	CASE MONTH
  	WHEN 'JAN' THEN 4
    WHEN 'FEB' THEN 5
    WHEN 'MAR' THEN 6
    WHEN 'APR' THEN 7
    WHEN 'MAY' THEN 8
    WHEN 'JUN' THEN 9
    WHEN 'JUL' THEN 10
    WHEN 'AUG' THEN 11
    WHEN 'SEP' THEN 12
    WHEN 'OCT' THEN 1
    WHEN 'NOV' THEN 2
    WHEN 'DEC' THEN 3
 	END;