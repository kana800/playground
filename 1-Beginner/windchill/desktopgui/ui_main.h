/********************************************************************************
** Form generated from reading UI file 'mainuSCwai.ui'
**
** Created by: Qt User Interface Compiler version 5.15.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef MAINUSCWAI_H
#define MAINUSCWAI_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QFormLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Form
{
public:
    QWidget *formLayoutWidget;
    QFormLayout *formLayout;
    QLabel *windspeedlabel;
    QLineEdit *windspeed;
    QLabel *airtemplabel;
    QLineEdit *airtemp;
    QPushButton *windchillbtn;
    QCheckBox *units;
    QLabel *unitslabel;

    void setupUi(QWidget *Form)
    {
        if (Form->objectName().isEmpty())
            Form->setObjectName(QString::fromUtf8("Form"));
        Form->resize(240, 115);
        Form->setMinimumSize(QSize(240, 115));
        Form->setMaximumSize(QSize(240, 115));
        formLayoutWidget = new QWidget(Form);
        formLayoutWidget->setObjectName(QString::fromUtf8("formLayoutWidget"));
        formLayoutWidget->setGeometry(QRect(0, 0, 241, 112));
        formLayout = new QFormLayout(formLayoutWidget);
        formLayout->setObjectName(QString::fromUtf8("formLayout"));
        formLayout->setContentsMargins(0, 0, 0, 0);
        windspeedlabel = new QLabel(formLayoutWidget);
        windspeedlabel->setObjectName(QString::fromUtf8("windspeedlabel"));

        formLayout->setWidget(0, QFormLayout::LabelRole, windspeedlabel);

        windspeed = new QLineEdit(formLayoutWidget);
        windspeed->setObjectName(QString::fromUtf8("windspeed"));

        formLayout->setWidget(0, QFormLayout::FieldRole, windspeed);

        airtemplabel = new QLabel(formLayoutWidget);
        airtemplabel->setObjectName(QString::fromUtf8("airtemplabel"));

        formLayout->setWidget(1, QFormLayout::LabelRole, airtemplabel);

        airtemp = new QLineEdit(formLayoutWidget);
        airtemp->setObjectName(QString::fromUtf8("airtemp"));

        formLayout->setWidget(1, QFormLayout::FieldRole, airtemp);

        windchillbtn = new QPushButton(formLayoutWidget);
        windchillbtn->setObjectName(QString::fromUtf8("windchillbtn"));

        formLayout->setWidget(3, QFormLayout::SpanningRole, windchillbtn);

        units = new QCheckBox(formLayoutWidget);
        units->setObjectName(QString::fromUtf8("units"));
        units->setTristate(false);

        formLayout->setWidget(2, QFormLayout::FieldRole, units);

        unitslabel = new QLabel(formLayoutWidget);
        unitslabel->setObjectName(QString::fromUtf8("unitslabel"));

        formLayout->setWidget(2, QFormLayout::LabelRole, unitslabel);


        retranslateUi(Form);

        QMetaObject::connectSlotsByName(Form);
    } // setupUi

    void retranslateUi(QWidget *Form)
    {
        Form->setWindowTitle(QCoreApplication::translate("Form", "Form", nullptr));
        windspeedlabel->setText(QCoreApplication::translate("Form", "wind speed (MPH)", nullptr));
        windspeed->setPlaceholderText(QCoreApplication::translate("Form", "input the windspeed", nullptr));
        airtemplabel->setText(QCoreApplication::translate("Form", "Air temperature (F)", nullptr));
        airtemp->setPlaceholderText(QCoreApplication::translate("Form", "input the air temp", nullptr));
        windchillbtn->setText(QCoreApplication::translate("Form", "calculate windchill", nullptr));
        units->setText(QString());
        unitslabel->setText(QCoreApplication::translate("Form", "Check for Metric", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Form: public Ui_Form {};
} // namespace Ui

QT_END_NAMESPACE

#endif // MAINUSCWAI_H
