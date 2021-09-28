#ifndef DATABASE_H
#define DATABASE_H

char databasename[] = "employee.db";

std::string tablesql = "CREATE TABLE PERSON("
                       "ID INT PRIMARY KEY     NOT NULL, "
                       "NAME           TEXT    NOT NULL, "
                       "SURNAME          TEXT     NOT NULL, "
                       "AGE            INT     NOT NULL, "
                       "ADDRESS        CHAR(50), "
                       "SALARY         REAL );";

#endif // DATABASE_H