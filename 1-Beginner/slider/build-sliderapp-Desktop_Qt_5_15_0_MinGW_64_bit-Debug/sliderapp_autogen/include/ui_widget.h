/********************************************************************************
** Form generated from reading UI file 'widget.ui'
**
** Created by: Qt User Interface Compiler version 5.15.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_WIDGET_H
#define UI_WIDGET_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Widget
{
public:
    QWidget *verticalLayoutWidget;
    QVBoxLayout *mainlayout;
    QLabel *picture;
    QHBoxLayout *optionlayout;
    QPushButton *left;
    QPushButton *right;
    QPushButton *directory;

    void setupUi(QWidget *Widget)
    {
        if (Widget->objectName().isEmpty())
            Widget->setObjectName(QString::fromUtf8("Widget"));
        Widget->resize(500, 250);
        Widget->setMinimumSize(QSize(500, 250));
        Widget->setMaximumSize(QSize(500, 250));
        verticalLayoutWidget = new QWidget(Widget);
        verticalLayoutWidget->setObjectName(QString::fromUtf8("verticalLayoutWidget"));
        verticalLayoutWidget->setGeometry(QRect(-1, -1, 502, 251));
        mainlayout = new QVBoxLayout(verticalLayoutWidget);
        mainlayout->setSpacing(0);
        mainlayout->setObjectName(QString::fromUtf8("mainlayout"));
        mainlayout->setContentsMargins(0, 0, 0, 0);
        picture = new QLabel(verticalLayoutWidget);
        picture->setObjectName(QString::fromUtf8("picture"));
        picture->setMinimumSize(QSize(500, 220));
        picture->setMaximumSize(QSize(500, 220));

        mainlayout->addWidget(picture);

        optionlayout = new QHBoxLayout();
        optionlayout->setObjectName(QString::fromUtf8("optionlayout"));
        left = new QPushButton(verticalLayoutWidget);
        left->setObjectName(QString::fromUtf8("left"));

        optionlayout->addWidget(left);

        right = new QPushButton(verticalLayoutWidget);
        right->setObjectName(QString::fromUtf8("right"));

        optionlayout->addWidget(right);

        directory = new QPushButton(verticalLayoutWidget);
        directory->setObjectName(QString::fromUtf8("directory"));

        optionlayout->addWidget(directory);


        mainlayout->addLayout(optionlayout);


        retranslateUi(Widget);

        QMetaObject::connectSlotsByName(Widget);
    } // setupUi

    void retranslateUi(QWidget *Widget)
    {
        Widget->setWindowTitle(QCoreApplication::translate("Widget", "Widget", nullptr));
        picture->setText(QCoreApplication::translate("Widget", "select directory", nullptr));
        left->setText(QCoreApplication::translate("Widget", "left", nullptr));
        right->setText(QCoreApplication::translate("Widget", "right", nullptr));
        directory->setText(QCoreApplication::translate("Widget", "directory", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Widget: public Ui_Widget {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_WIDGET_H
