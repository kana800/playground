#include <QDir>
#include <QFile>
#include <QTextStream>
#include <cstdio>
#include <iostream>
#include <ostream>
#include <string.h>
#include <QTime>
#include <QDate>
#include "initialsetup.h"

/*
 * return boolean;
 * args: 
        const char * directory -> name of the 
        directory
 * summary:
        check if the current directory is available
        and return true or false according to the 
        availiability
 */
bool directoryExists(const char * directory){
    // instiating directory class
    QDir dir;
    return dir.exists(directory);
}

/*
 * return boolean;
 * args: 
        const char * directory -> name of the 
        directory
 * summary:
        creates a directory return true if success
        else false
 */
bool createDirectory(const char * directory){
    QDir dir;
    return dir.mkdir(directory);
}

/*
 * return;
 * args:
        const char * directory -> name of the 
        directory
 * summary:
        creates an untitled file and save it
        inside the directory given by the user
 */
void createUntitledFile(const char * directory){
    QString filename = "untitled.txt";
    QTime currenttime = QTime::currentTime();
    // appending time to the file name
    filename.append(currenttime.toString());
    filename.prepend("/");
    filename.prepend(directory);
    QTextStream out{stdout};
    QFile f{filename};

    if (f.open(QIODevice::WriteOnly)){
        QTextStream out{&f};
    }else{
        qWarning("cannot open file");
    }
    return;
}

/*
 * return;
 * args:  
        const char * directory -> name of the 
        directory
 * summary:
        setups the program at the intital stage.
        will scan for the notes folder, create one
        if it isnt present and create untitlted note
 */
 void initializeProgram(const char * directory){
    if (directoryExists(directory) == false){
        createDirectory(directory);
    }
    createUntitledFile(directory);
    return;
 }