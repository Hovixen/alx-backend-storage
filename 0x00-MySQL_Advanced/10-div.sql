-- Script creates a function SafeDiv that divides (and returns) the first by the second number
-- or returns 0 if the second number is equal to 0

DROP FUNCTION IF EXISTS SafeDiv;

DELIMITER //
CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT
DETERMINISTIC
BEGIN
	DECLARE ans INT;
	IF b = 0 THEN
		SET ans = 0;
	ELSE
		SET ans = a / b;
	END IF;

	RETURN ans;
	
END //
DELIMITER ;
