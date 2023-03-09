#include "ui_main.h"
#include <QValidator>
#include <QString>
#include <iostream>
#include <QTextStream>
#include <QPushButton>
#include <string>
#include <math.h>
#include <QMessageBox>

QString units = "MPH"; /*global variable to store the units of either metric or standard*/
Ui::Form form; /*badstyle of coding; dont do this*/

/*
 * changes the units according to the 
 * state of the checkbox
 *
 * Note: units is currently a global variable, to avoid
 * this we need to define everything in a class. This is
 * bad coding style dont try copy this !. I am still learning
 * cpp.
 */
void changeUnits(int state){
	if (state == 2){
        	form.windspeedlabel->setText("wind speed (KMPH)");
        	form.airtemplabel->setText("Air temperature (C)");
		units = "KMPH";
	}
}

/*
 * calculates the windchill and display
 * it in a popup window.
 *
 * Note: again we need to implement this function 
 * as method in  a class, we cant use global variables
 */
void calculatewindchill(bool clicked){
	QTextStream out{stdout};
	if (units == "PH"){
		return;
	}else {
		QString windspeedstr = form.windspeed->text();
		QString airtempstr = form.airtemp->text();
		bool ok = false;
		int windspeed = windspeedstr.toInt(&ok, 10);
		int airtemp = airtempstr.toInt(&ok, 10);
		double windchill = (0.0817*(3.71*(pow(windspeed, 0.5))+5.81-0.25*windspeed)*(airtemp-91.4)+91.4);
		QString messageboxanswer;
		messageboxanswer = QString("Answer is %1 %2").arg(windchill)
			.arg(units);
		QMessageBox(QMessageBox::Information, "WindChill",messageboxanswer).exec();
		return;
	}

}

int main(int argc, char **argv){
    QApplication app(argc, argv);

    QWidget widget;

    form.setupUi(&widget);

    /*setting up validators for the line edits*/
    QValidator * validator = new QIntValidator(0,1000);
    form.windspeed->setValidator(validator);
    form.airtemp->setValidator(validator);

    /*connecting check box with changeunits function*/
    QObject::connect(form.units, &QCheckBox::stateChanged,
        changeUnits);

    /*connecting calculate button with the calculate windchill function*/
    QObject::connect(form.windchillbtn, &QPushButton::clicked,
        calculatewindchill);


    widget.show();
    widget.setWindowTitle("Wind Chill App");
    return app.exec();
}
