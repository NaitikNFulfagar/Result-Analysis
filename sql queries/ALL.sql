"Topper List"
SELECT name,div,SGPA FROM SE_COMPUTER_2024_JUNE WHERE div NOT NULL and SGPA!='--' ORDER by SGPA DESC LIMIT 5;

"Actual Appeared"
SELECT count(name) FROM SE_COMPUTER_2024_JUNE WHERE div NOT NULL;

"Absent Count for specific Sub"
SELECT count(name) FROM SE_COMPUTER_2024_JUNE WHERE _210241_end="AB" and div NOT NULL;

"Pass Count for specific Sub"
SELECT count(name) FROM SE_COMPUTER_2024_JUNE WHERE _210241_tot>40 and div NOT NULL;

"Fail Count for specific Sub"
SELECT count(name) FROM SE_COMPUTER_2024_JUNE WHERE _210241_tot<40 and div NOT NULL;

"Topper for specific Sub"
SELECT name,_210255_tot FROM SE_COMPUTER_2024_JUNE WHERE _210255_end!="AB" and div NOT NULL ORDER by _210255_tot DESC LIMIT 1;

"Distinction"
SELECT count(name) FROM SE_COMPUTER_2024_JUNE WHERE div NOT NULL and SGPA!='--' and SGPA>=7.75 ORDER by SGPA DESC;

"First Class"
SELECT count(name) FROM SE_COMPUTER_2024_JUNE WHERE div NOT NULL and SGPA!='--' and SGPA<7.75 and SGPA>=6.75 ORDER by SGPA DESC;

"Higher Second Class"
SELECT count(name) FROM SE_COMPUTER_2024_JUNE WHERE div NOT NULL and SGPA!='--' and SGPA<6.75 and SGPA>=6.25 ORDER by SGPA DESC;

"Second Class"
SELECT count(name) FROM SE_COMPUTER_2024_JUNE WHERE div NOT NULL and SGPA!='--' and SGPA<6.25 and SGPA>=5.5 ORDER by SGPA DESC;

"Passed Class"
SELECT count(name) FROM SE_COMPUTER_2024_JUNE WHERE div NOT NULL and SGPA!='--' and SGPA<5.5 ORDER by SGPA DESC;