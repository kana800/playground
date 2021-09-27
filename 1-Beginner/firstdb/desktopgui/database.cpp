#include <cstddef>
#include <iostream>
#include <QApplication>
#include <QLabel>
#include <string>
#include "sqlite3.h"


static int callback(void * data, int argc, char **argv, char ** azColName){
    int i;
    fprintf(stderr, "%s: ",(const char *)data);
    for (i = 0; i < argc; i++){
        printf("%s = %s \n",azColName[i], argv[i] ? argv[i]: "NULL");
    }
    printf("\n");
    return 0;
}

int main(int argc, char **argv)
{

    // initializing DB
    sqlite3* DB;
    int exit = 0;
    exit = sqlite3_open("example.db", &DB);
    char *errorMessage;

    std::string query = "SELECT * FROM PERSON;";

    sqlite3_exec(DB, query.c_str(), callback, NULL,NULL);


    std::string sql("INSERT INTO PERSON VALUES(1, 'STEVE', 'GATES', 30, 'PALO ALTO', 1000.0);"
                    "INSERT INTO PERSON VALUES(2, 'BILL', 'ALLEN', 20, 'SEATTLE', 300.22);"
                    "INSERT INTO PERSON VALUES(3, 'PAUL', 'JOBS', 24, 'SEATTLE', 9900.0);");

    
    exit = sqlite3_exec(DB, sql.c_str(), NULL, 0, &errorMessage);
    
    if (exit != SQLITE_OK) {
        std::cerr << "ERROR INSERT" << std::endl;
        sqlite3_free(errorMessage);
        return -1;
    }else{
        std::cout << "RECORD CREATED" << std::endl;
    }

    std::cout << "STATE OF TABLE AFTER INSERT" << std::endl;
  
    sqlite3_exec(DB, query.c_str(), callback, NULL, NULL);
    sqlite3_close(DB);


    return 0;

//    QApplication app(argc, argv);
//    QLabel hello("Hello world!");

//    hello.show();
//    return app.exec();
}
