#include <QWidget>
#include <QObject>
#include <QString>
#include <QPushButton>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QTextEdit>
#include <QFile>
#include "notepad.h"


QWidget * NotePad::notewindow;
QString NotePad::s_filename;

NotePad::NotePad(QString filename){
    notewindow = new QWidget;
    s_filename = filename;
    QVBoxLayout *notelayout = new QVBoxLayout(notewindow);
    QHBoxLayout *optionlayout = new QHBoxLayout();
    QPushButton *closenotebtn = new QPushButton("close note");    
    QPushButton *savenotebtn = new QPushButton("save note");    
    QPushButton *renamenotebtn = new QPushButton("rename note");    
    QTextEdit *notepad = new QTextEdit();

    notelayout->addWidget(notepad);  
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

    /*scan and add the contents of the file into the text
    edit*/
    s_filename.prepend("notes/");
    QFile f(s_filename);
    QTextStream in{&f};
    QString line;
    while (!in.atEnd()) {
        line = in.readAll();
    }
    notepad->setText(line);
    notepad->setPlaceholderText("seems bit lonely here");
    /*adding the layout into the main layout*/
    notelayout->addLayout(optionlayout);
    notewindow->setWindowTitle("notepad");
    notewindow->show();
}
void NotePad::closenote(){
    notewindow->close();
}

void NotePad::savenote(){
    QTextStream out{stdout};

    QFile f{s_filename};

    if (f.open(QIODevice::WriteOnly)) {
        QTextStream out{&f};
        out << "cake";
    } else {
        qWarning("Could not open file");
    }
}

void NotePad::renamenote(){

}