#include <QApplication>
#include <QLabel>
#include <QWidget>
#include <QLineEdit>
#include <QVBoxLayout>
#include <QSize>
#include <curl/curl.h>


int main(int argc, char **argv)
{
	/*
	 * Initializing CURL
	 */
	CURL *curl;
	CURLcode res;
	curl_global_init(CURL_GLOBAL_DEFAULT);

	curl = curl_easy_init();

	if (curl){
		curl_easy_setopt(curl, CURLOPT_URL, "http://api.openweathermap.org/data/2.5/weather?q=Colombo&appid=9830d9d09b5209707a3c33379153c3a5&units=standard");
		res = curl_easy_perform(curl);

		if (res != CURLE_OK){
			fprintf(stderr, "curl_easy_perform() failed: %s\n",
					curl_easy_strerror(res));
		curl_easy_cleanup(curl);
		}
	}
	curl_global_cleanup();
	return 0;
	/*
	 * creating an application instance
	 * and widget
	 */
	QApplication app(argc, argv);
	QWidget *window = new QWidget;
	/*line widget that takes in the country*/
	QLineEdit *lineedit = new QLineEdit;

	/*main layout*/
	QVBoxLayout *mainLayout = new QVBoxLayout(window);
	mainLayout->addWidget(lineedit);




	window->setWindowTitle("weather app");
	window->setFixedSize(QSize(640,480));
    	window->show();
   	return app.exec();
}
