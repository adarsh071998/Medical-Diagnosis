
create table male(
	min_age int,max_age int,
	min_wbc float(6,2),max_wbc float(6,2),
	min_rbc float(6,2),max_rbc float(6,2),
	min_hgb float(6,2),max_hgb float(6,2),
	min_hct float(6,2),max_hct float(6,2),
	min_mcv float(6,2),max_mcv float(6,2),
	min_mch float(6,2),max_mch float(6,2),
	min_mchc float(6,2),max_mchc float(6,2),
	min_chcm float(6,2),max_chcm float(6,2),
	min_rdw float(6,2),max_rdw float(6,2),
	min_hdw float(6,2),max_hdw float(6,2),
	min_plt float(6,2),max_plt float(6,2),
	min_mpv float(6,2),max_mpv float(6,2),
	min_neu float(6,2),max_neu float(6,2),
	min_lymph float(6,2),max_lymph float(6,2),
	min_mono float(6,2),max_mono float(6,2),
	min_eosin float(6,2),max_eosin float(6,2),
	min_baso float(6,2),max_baso float(6,2)
	);

create table female(min_age int,max_age int,
	min_wbc float(6,2),max_wbc float(6,2),
	min_rbc float(6,2),max_rbc float(6,2),
	min_hgb float(6,2),max_hgb float(6,2),
	min_hct float(6,2),max_hct float(6,2),
	min_mcv float(6,2),max_mcv float(6,2),
	min_mch float(6,2),max_mch float(6,2),
	min_mchc float(6,2),max_mchc float(6,2),
	min_chcm float(6,2),max_chcm float(6,2),
	min_rdw float(6,2),max_rdw float(6,2),
	min_hdw float(6,2),max_hdw float(6,2),
	min_plt float(6,2),max_plt float(6,2),
	min_mpv float(6,2),max_mpv float(6,2),
	min_neu float(6,2),max_neu float(6,2),
	min_lymph float(6,2),max_lymph float(6,2),
	min_mono float(6,2),max_mono float(6,2),
	min_eosin float(6,2),max_eosin float(6,2),
	min_baso float(6,2),max_baso float(6,2)
	);


LOAD DATA Local INFILE '/home/pritesh/Desktop/COM/lib/data/female.csv' 
INTO TABLE female 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;