-- Script creates a trigger that decreases the quantitiy of an item
-- after adding a new order

DELIMITER //
CREATE TRIGGER desc_qty
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
	UPDATE items
	SET quantity = quantity - NEW.number
	WHERE name = NEW.item_name;
END//
DELIMITER ;
