-- Script creates a trigger that resets the attribute valid_email
-- only when email has been changed

DROP TRIGGER IF EXISTS attr_reset;


DELIMITER //
CREATE TRIGGER attr_reset
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	IF OLD.email <> NEW.email THEN
		SET NEW.valid_email = 0;
	END IF;
END//

DELIMITER ;
