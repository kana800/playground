#include "ui_main.h"


int main(int argc, char **argv){
    QApplication app(argc, argv);
    QWidget widget;

    Ui::Form ui;
    ui.setupUi(&widget);

    widget.show();
    return app.exec();
}