#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <QApplication>
#include <QLabel>
#include <string>
#include "sqlite3.h"
#include "database.h"


static int callback(void * data, int argc, char **argv, char ** azColName){
    int i;
    fprintf(stderr, "%s: ",(const char *)data);
    for (i = 0; i < argc; i++){
        printf("%s = %s \n",azColName[i], argv[i] ? argv[i]: "NULL");
    }
    printf("\n");
    return 0;
}

/*
 * return sqlite3 pointer
 * creates a database & table
 */
sqlite3 *  createDatabase(){
    sqlite3 * database;
    int status = 0;
    status = sqlite3_open(databasename, &database);

    if (status) {
        std::cerr << "ERR: CANNOT OPEN DATABASE " << sqlite3_errmsg(database) << std::endl;
        exit(EXIT_FAILURE);
    } else {
        std::cout << "SUCCESS: DATABASE OPENED SUCCESFULLY" << std::endl;
        sqlite3_close(database);
        return database;
    }
}

std::string generateSqlString(int id, char *firstname, char *secondname, int age, int salary){
    char bufferstring[100];
    std::snprintf(bufferstring, 99,
        "INSERT INTO PERSON VALUES(%d, '%s', '%s', %d, %d);", id, firstname, secondname, age, salary);
    return bufferstring;
}

int main(int argc, char **argv)
{

    /*initializing DB*/
    sqlite3* database = createDatabase();
    /*creating a table*/
    int exit = 0;
    exit = sqlite3_open(databasename, &database);
    char * errorMessage;

    /*creating the employee table*/
    exit = sqlite3_exec(database, tablesql.c_str(), NULL, 0, &errorMessage);
    if (exit != SQLITE_OK){
        std::cerr << "ERR: CANNOT CREATE TABLE" << std::endl;
        sqlite3_free(errorMessage);
    } else {
        std::cout << "SUCCESS: TABLE CREATED SUCCESFULLY" << std::endl;
        sqlite3_close(database);
    }
    return 0;

//    QApplication app(argc, argv);
//    QLabel hello("Hello world!");

//    hello.show();
//    return app.exec();
}
