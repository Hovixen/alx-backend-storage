-- Script creates a stored procedure ComputeAverageScoreForUser that computes
-- and store the average score of a user

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN p_user_id INT)
BEGIN
	DECLARE var_score FLOAT;

	SELECT AVG(score) INTO var_score
	FROM corrections
	WHERE user_id = p_user_id;

	UPDATE users
	SET average_score = var_score
	WHERE id = p_user_id;
END //
DELIMITER ;
