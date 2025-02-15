
#  Database Automation with Azure MySQL & GitHub Actions

##  Project Overview
This project demonstrates how to automate MySQL database schema changes using:
- **Azure Database for MySQL Flexible Server**
- **GitHub Actions for CI/CD**
- **Python Automation Scripts**
- **SQL Scripts for Schema Management**

The workflow applies changes to the database automatically when code is pushed to the repository.

---

## Tools & Technologies Used
- **Azure MySQL Flexible Server (version 8.0)**  
- **Python 3.x**  
- **MySQL Connector Python**  
- **GitHub Actions**  
- **Git**  

---

##  Database Automation Pipeline

The CI/CD pipeline runs through **GitHub Actions** and performs the following steps:

1. **Install MySQL Connector:**  
    Installs the necessary Python package to connect to the MySQL database.

2. **Apply Database Changes:**  
    - Executes the SQL scripts:
      - `schema_changes.sql`
      - `add_departments.sql`
    - Adds or modifies tables and columns as specified.

3. **Verify Execution:**  
    Logs confirmation messages in the GitHub Actions run.

---

##  Folder Structure
```plaintext
📂 Database Automation
    ├── schema_automation.py    # Python script for database automation
    ├── schema_changes.sql       # SQL file for initial schema changes
    ├── add_departments.sql      # SQL file for departments table
    └── .github
        └── workflows
            └── ci_cd_pipeline.yml  # GitHub Actions workflow
```

---

##  Setup Instructions

Follow these steps to replicate the setup:

1. **Clone the Repository:**

```bash
git clone https://github.com/Puneet0812/database-automation.git
cd database-automation
```

2. **Install Dependencies:**

```bash
pip install mysql-connector-python
```

3. **Run the Automation Script Locally:**

```bash
python schema_automation.py
```

4. **Access Azure MySQL Database:**

```bash
mysql -h puneet-mysql-server.mysql.database.azure.com -u puneetadmin -p --ssl-mode=REQUIRED
```

---

## 🛢️ Database Schema Information

The database contains the following tables:

###  **1. `projects` Table**

| Column       | Data Type      | Constraints     |
|---------------|----------------|----------------|
| `project_id`   | `INT`           | `PRIMARY KEY`, `AUTO_INCREMENT` |
| `project_name` | `VARCHAR(255)`  | `NOT NULL` |
| `start_date`   | `DATE`          | `NULLABLE` |
| `end_date`     | `DATE`          | `NULLABLE` |
| `budget`       | `DECIMAL(10,2)` | `NULLABLE` |

---

###  **2. `departments` Table**

| Column           | Data Type      | Constraints     |
|-------------------|----------------|----------------|
| `department_id`     | `INT`           | `PRIMARY KEY`, `AUTO_INCREMENT` |
| `department_name`   | `VARCHAR(100)`  | `NOT NULL` |
| `location`          | `VARCHAR(100)`  | `NOT NULL` |

---

## CI/CD Pipeline Overview

The CI/CD pipeline is defined in **GitHub Actions** with the workflow file:  
```plaintext
.github/workflows/ci_cd_pipeline.yml
```

###  **Pipeline Steps:**

1. **Code Checkout:** Pulls the latest code from the repository.  
2. **Install Dependencies:** Installs required Python libraries.  
3. **Run SQL Automation:** Executes the SQL files on the **Azure MySQL server**.  
4. **Verify Changes:** Confirms successful database updates.  

### **Trigger:**  
- The pipeline is triggered on **every push** to the **`main`** branch.

---

##  Testing & Verification

To verify the database schema changes:

1. **Connect to MySQL Server**:  
    ```bash
    mysql -h puneet-mysql-server.mysql.database.azure.com -u puneetadmin -p --ssl-mode=REQUIRED
    ```

2. **Verify Tables:**

    ```sql
    SHOW DATABASES;
    USE companydb;
    SHOW TABLES;
    DESC projects;
    DESC departments;
    ```

---

**GitHub Repository:** [https://github.com/Puneet0812/database-automation](https://github.com/Puneet0812/database-automation)
