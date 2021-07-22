/*
 * Implementation of ls command
 */
#include <stdio.h>
#include <dirent.h>


int main() { 

	// pointer to store the file
	// return 0 if success , -1 if there
	// is an error
	DIR *folder;

	struct dirent *directoryContent;

	folder = opendir(".");

	if (folder == NULL){
		printf("cannot open directory\n");
		return 1;
	}

	while (directoryContent = readdir(folder)) {
		printf("%s ",directoryContent->d_name);
	}
	printf("\n");
	// closing the directory
	closedir(folder);
	return 0;
}
