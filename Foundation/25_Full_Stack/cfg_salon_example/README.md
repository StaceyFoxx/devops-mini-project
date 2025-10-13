# CFG Salon Example


### How to setup the DB and Data
* run the "create_salon_db_script" to create the DB and table
* populate the table using the "filldates" procedure. (Note that the long int are dates yymmdd)
* 
```sql
CALL `salon`.`filldates`(20240701, 20240705, 'Peter');
CALL `salon`.`filldates`(20240701, 20240705, 'Mandy');
```
