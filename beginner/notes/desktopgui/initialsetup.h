#ifndef INITIALSETUP_H
#define INITIALSETUP_H

bool directoryExists(const char * directory);
bool createDirectory(const char * directory);
void createUntitledFile(const char * directory);
void initializeProgram(const char * directory);

#endif // INITIALSETUP_H