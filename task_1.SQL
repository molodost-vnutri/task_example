UPDATE full_names
SET status = short_names.status
FROM short_names
WHERE full_names.name = SPLIT_PART(short_names.name, '.', 1);