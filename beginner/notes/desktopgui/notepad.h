#ifndef NOTEPAD_H
#define NOTEPAD_H

class NotePad{
    public: // methods
        static QWidget *notewindow;
        static QString s_filename;
    public: // methods
        NotePad(QString filename);
        static void savenote();
        static void closenote();
        static void renamenote();
};


#endif // NOTEPAD_H