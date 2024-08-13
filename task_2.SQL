WITH m_names AS (
	SELECT fn.name AS full_name, sn.status
	FROM full_names fn
	JOIN short_names sn
	ON fn.name = SPLIT_PART(sn.name, '.', 1)
)
UPDATE full_names fn
SET status = mn.status
FROM m_names mn
WHERE fn.name = mn.full_name