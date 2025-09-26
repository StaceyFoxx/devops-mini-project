# MySQL Join Types Explained

## 1. Equi-Join
A join that uses equality (`=`) in the join condition.  

**Example**:
```sql
SELECT e.id, e.name, d.department_name
FROM employees e JOIN departments d 
ON e.department_id = d.id;
```



## 2. Non-Equi Join
A join that uses conditions other than equality (e.g., `<`, `>`, `BETWEEN`).  

**Example**:
```sql
SELECT e.name, s.grade
FROM employees e JOIN salary_grades s
ON e.salary BETWEEN s.min_salary AND s.max_salary;
```


## 3. Non-Keyword Join
An older SQL style (not recommended anymore) where tables are listed in the `FROM` clause and the join condition is written in the `WHERE` clause (no `JOIN` keyword).  

**Example**:
```sql
SELECT e.id, e.name, d.department_name
FROM employees e, departments d
WHERE e.department_id = d.id;
```


## 4. Natural Join
Automatically joins tables based on columns with the same name and compatible data types. No `ON` clause is needed.  

**Example**: *(Assumes both tables have a column named `department_id`.)*
```sql
SELECT e.id, e.name, d.department_name
FROM employees e
NATURAL JOIN departments d;
```

