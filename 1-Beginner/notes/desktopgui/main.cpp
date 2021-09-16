#include <QApplication>
#include <QWidget>
#include <QListWidget>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QPushButton>
#include <cstdio>
#include <iostream>
#include <ostream>
#include "initialsetup.cpp"
#include <QDir>
#include <QListWidgetItem>


/* return;
 * args:
    QListWidget *templist -> list widget pointer hold the list widget
    Directory -> location of the folder which contains the files
 * summary:
    add name of the file to the templist (ListWidget), the files are scanned
    from the "Directory" folder
*/
void addFilesInDirectory(QListWidget *templist, const char * directory){
    QDir dir{directory};
    /*checking if the directory exists*/
    if (!dir.exists()){
        qWarning("The directory doesnt exist");
        return;
    }
    /* set filter to specify which kind of files that is needed */
    dir.setFilter(QDir::Files);
    QFileInfoList list = dir.entryInfoList();

    for (int i = 0; i < list.size(); i++){
        QString name = list[i].fileName();
        new QListWidgetItem(name, templist);
    }
    return;
}


void closenote(){
}

void savenote(){
}

void renamenote(){
}

void openNote(QListWidgetItem *item){
    QString filename = item->text();
    QWidget *notewindow = new QWidget;
    QVBoxLayout *notelayout = new QVBoxLayout(notewindow);
    QHBoxLayout *optionlayout = new QHBoxLayout();
    QPushButton *closenotebtn = new QPushButton("create note");    
    QPushButton *savenotebtn = new QPushButton("save note");    
    QPushButton *renamenotebtn = new QPushButton("rename note");    
    
    optionlayout->addWidget(closenotebtn);
    optionlayout->addWidget(savenotebtn);
    optionlayout->addWidget(renamenotebtn);

    /* adding signals to the list widget */
    QObject::connect(closenotebtn, &QPushButton::clicked,
        closenote);
    /* adding signals to the list widget */
    QObject::connect(savenotebtn, &QPushButton::clicked,
        savenote);
    /* adding signals to the list widget */
    QObject::connect(renamenotebtn, &QPushButton::clicked,
        renamenote);

    notewindow->setWindowTitle("notepad");
    notewindow->show();
}



int main(int argc, char **argv){

    /*  creating an application instance
     *  and widget
     */
    QApplication app(argc, argv);
    QWidget *window = new QWidget;
    /* list widget that contains all the notes*/
    QListWidget *list = new QListWidget;

    /* main layout */
    QVBoxLayout *mainlayout = new QVBoxLayout(window);
    /* second layout */
    QHBoxLayout *secondlayout = new QHBoxLayout();
    QPushButton *createnote = new QPushButton("create note");    
    /* addwidgets to the second layout */
    secondlayout->addWidget(createnote);
    /*adding widgets to the main layout*/
    mainlayout->addWidget(list);    
    mainlayout->addLayout(secondlayout);
    
    const char * directory = "notes";
    initializeProgram(directory);

    /*  listing the contents of the directory and adding
        them tot the listwidget
    */    
    addFilesInDirectory(list, directory);
    
    /* adding signals to the list widget */
    QObject::connect(list, &QListWidget::itemDoubleClicked,
        openNote);

    /* finializing the window details */ 
    window->setWindowTitle("quick notes");
    window->show();

    return app.exec();
}