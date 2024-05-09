-- Script creates stored procedure AddBonus
-- that adds a new correction for a student

DELIMITER //
CREATE PROCEDURE AddBonus(IN p_user_id INT, IN p_proj_name VARCHAR(255), IN p_score INT)
BEGIN
	DECLARE var_proj_id INT;

	SELECT id INTO var_proj_id
	FROM projects
	WHERE name = p_proj_name;

	IF var_proj_id IS NULL THEN
		INSERT INTO projects (name) VALUES (p_proj_name);
		SET var_proj_id = LAST_INSERT_ID();
	END IF;

	INSERT INTO corrections (user_id, project_id, score)
	VALUES (p_user_id, var_proj_id, p_score);

END //

DELIMITER ;
