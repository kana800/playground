#include <QApplication>
#include <QWidget>
#include <QDir>
#include <QFile>
#include <QTextStream>
#include <cstdio>
#include <iostream>
#include <ostream>
#include <string.h>
#include <QTime>
#include <QDate>

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

 */

int main(int argc, char **argv){

    // creating an application instance
    // and widget

    QApplication app(argc, argv);
    QWidget window;

    const char * directory = "notes";
    bool t = directoryExists(directory);
    createUntitledFile(directory);
    /*
    window.resize(250,100);
    window.setWindowTitle("test example");
    window.show();

    return app.exec();
    */
    return 0;
}
