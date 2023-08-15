CREATE TABLE elections_2019 (
	question_id SERIAL PRIMARY KEY,
	end_date DATE,
	pollster TEXT,
	sample_size NUMERIC,
	population TEXT,
	politician TEXT,
	favorable NUMERIC,
	unfavorable NUMERIC,
	very_favorable NUMERIC,
	somewhat_favorable NUMERIC,
	somewhat_unfavorable NUMERIC,
	very_unfavorable NUMERIC,
	results INTEGER
);

CREATE TABLE elections_2023 (
	question_id SERIAL PRIMARY KEY,
	end_date DATE,
	pollster TEXT,
	sample_size NUMERIC,
	population TEXT,
	politician TEXT,
	favorable NUMERIC,
	unfavorable NUMERIC,
	very_favorable NUMERIC,
	somewhat_favorable NUMERIC,
	somewhat_unfavorable NUMERIC,
	very_unfavorable NUMERIC,
	results INTEGER
);