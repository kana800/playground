/*
 * Implementation of an autocomplete system
 */
#include <stdio.h>
#include "trie.h"
#include "trie.c"

// global head
struct trie *HEAD;

// loading words in the file into a array
void readFile(char *filename){
	// file pointer in read mode
	FILE *fp;
	
	// temp string to hold the word
	char string[20];
	char ch;
	int i = 0;
	fp = fopen(filename, "r");
	while ((ch = fgetc(fp)) != EOF){
		if (ch == '\n'){
			string[i] = '\0';
			// inserting the node here
			insert(HEAD, string);	
			i = 0;
			memset(string, 0 ,sizeof(string));
			continue;
		}
		string[i++] = ch;
	}
	fclose(fp);
	return;
}

int main(){
	HEAD = node();
	char *filename = "words.txt";
	readFile(filename);

	autocomplete(HEAD, "de");
	return 0;
}
