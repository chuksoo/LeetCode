<h2>2877. Create a DataFrame from List</h2><h3>Easy</h3>
Write a solution to create a DataFrame from a 2D list called student_data. This 2D list contains the IDs and ages of some students.

The DataFrame should have two columns, student_id and age, and be in the same order as the original 2D list.

The result format is in the following example.

Example 1:

Input:
student_data:
[
[1, 15],
[2, 11],
[3, 11],
[4, 20]
]
Output:

| student_id | age |
|------------|-----|
| 1 | 15 |
| 2 | 11 |
| 3 | 11 |
| 4 | 20 |

Explanation:
A DataFrame was created on top of student_data, with two columns named student_id and age.

```python
import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns=['student_id', 'age'])
```

<h2>2878. Get the Size of a DataFrame</h2><h3>Easy</h3>
DataFrame players:

| Column Name | Type   |
|-------------|--------|
| player_id   | int    |
| name        | object |
| age         | int    |
| position    | object |
| ...         | ...    |

Write a solution to calculate and display the number of rows and columns of players.

Return the result as an array:

[number of rows, number of columns]

The result format is in the following example.

Example 1:

Input:

| player_id | name | age | position | team |
|-----------|----------|-----|-------------|--------------------|
| 846 | Mason | 21 | Forward | RealMadrid |
| 749 | Riley | 30 | Winger | Barcelona |
| 155 | Bob | 28 | Striker | ManchesterUnited |
| 583 | Isabella | 32 | Goalkeeper | Liverpool |
| 388 | Zachary | 24 | Midfielder | BayernMunich |
| 883 | Ava | 23 | Defender | Chelsea |
| 355 | Violet | 18 | Striker | Juventus |
| 247 | Thomas | 27 | Striker | ParisSaint-Germain |
| 761 | Jack | 33 | Midfielder | ManchesterCity |
| 642 | Charlie | 36 | Center-back | Arsenal |

Output:
[10, 5]
Explanation:
This DataFrame contains 10 rows and 5 columns.

```python
import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape)
```

<h2>2880. Select Data</h2><h3>Easy</h3>
DataFrame students

| Column Name | Type   |
|-------------|--------|
| student_id  | int    |
| name        | object |
| age         | int    |


Write a solution to select the name and age of the student with student_id = 101.

The result format is in the following example.

Example 1:
Input:

| student_id | name | age |
|------------|---------|-----|
| 101 | Ulysses | 13 |
| 53 | William | 10 |
| 128 | Henry | 6 |
| 3 | Henry | 11 |

Output:

| name | age |
|---------|-----|
| Ulysses | 13 |

Explanation:
Student Ulysses has student_id = 101, we select the name and age.

```python
import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students['student_id'] == 101, ['name', 'age']]
```

<h2>2882. Drop Duplicate Rows</h2><h3>Easy</h3>
DataFrame customers

| Column Name | Type   |
|-------------|--------|
| customer_id | int    |
| name        | object |
| email       | object |

There are some duplicate rows in the DataFrame based on the email column.

Write a solution to remove these duplicate rows and keep only the first occurrence.

The result format is in the following example.

Example 1:
Input:

| customer_id | name | email |
|-------------|---------|---------------------|
| 1 | Ella | emily@example.com |
| 2 | David | michael@example.com |
| 3 | Zachary | sarah@example.com |
| 4 | Alice | john@example.com |
| 5 | Finn | john@example.com |
| 6 | Violet | alice@example.com |

Output:  

| customer_id | name | email |
|-------------|---------|---------------------|
| 1 | Ella | emily@example.com |
| 2 | David | michael@example.com |
| 3 | Zachary | sarah@example.com |
| 4 | Alice | john@example.com |
| 6 | Violet | alice@example.com |

Explanation:
Alic (customer_id = 4) and Finn (customer_id = 5) both use john@example.com, so only the first occurrence of this email is retained.

```python
import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers = customers.drop_duplicates(subset=['email'], keep='first', inplace=False)
    return customers
```

<h2>2883. Drop Missing Data</h2><h3>Easy</h3>
DataFrame students

| Column Name | Type   |
|-------------|--------|
| student_id  | int    |
| name        | object |
| age         | int    |

There are some rows having missing values in the name column.

Write a solution to remove the rows with missing values.

The result format is in the following example.

 

Example 1:

Input:

| student_id | name    | age |
|------------|---------|-----|
| 32         | Piper   | 5   |
| 217        | None    | 19  |
| 779        | Georgia | 20  |
| 849        | Willow  | 14  |

Output:

| student_id | name    | age |
|------------|---------|-----|
| 32         | Piper   | 5   |
| 779        | Georgia | 20  | 
| 849        | Willow  | 14  | 

Explanation: 
Student with id 217 havs empty value in the name column, so it will be removed.

```python
import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    students.dropna(subset=['name'], inplace=True)
    return students
```


<h2>2884. Modify Columns</h2><h3>Easy</h3>
DataFrame employees

| Column Name | Type   |
|-------------|--------|
| name        | object |
| salary      | int    |

A company intends to give its employees a pay rise.

Write a solution to modify the salary column by multiplying each salary by 2.

The result format is in the following example.

 

Example 1:

Input:
DataFrame employees

| name    | salary |
|---------|--------|
| Jack    | 19666  |
| Piper   | 74754  |
| Mia     | 62509  |
| Ulysses | 54866  |

Output:

| name    | salary |
|---------|--------|
| Jack    | 39332  |
| Piper   | 149508 |
| Mia     | 125018 |
| Ulysses | 109732 |

Explanation:
Every salary has been doubled.

```python
import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'] * 2
    return employees
```

<h2>2885. Rename Columns</h2><h3>Easy</h3>
DataFrame students

| Column Name | Type   |
|-------------|--------|
| id          | int    |
| first       | object |
| last        | object |
| age         | int    |

Write a solution to rename the columns as follows:

id to student_id
first to first_name
last to last_name
age to age_in_years
The result format is in the following example.

 

Example 1:
Input:

| id | first   | last     | age |
|----|---------|----------|-----|
| 1  | Mason   | King     | 6   |
| 2  | Ava     | Wright   | 7   |
| 3  | Taylor  | Hall     | 16  |
| 4  | Georgia | Thompson | 18  |
| 5  | Thomas  | Moore    | 10  |

Output:

| student_id | first_name | last_name | age_in_years |
|------------|------------|-----------|--------------|
| 1          | Mason      | King      | 6            |
| 2          | Ava        | Wright    | 7            |
| 3          | Taylor     | Hall      | 16           |
| 4          | Georgia    | Thompson  | 18           |
| 5          | Thomas     | Moore     | 10           |

Explanation: 
The column names are changed accordingly.

```python
import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students.rename(columns = {'id': 'student_id', 'first': 'first_name', 'last': 'last_name', 'age': 'age_in_years'}, inplace = True)
    return students
```