/*
 * Implementation of a Trie Data Structure
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "trie.h"

// returns a new pointer trie node
struct trie * node(){
	// allocating new node in the heap
	struct trie * tempnode = (struct trie*)malloc(sizeof(struct trie));	
	// all the 26 possibilites are NULL
	for (int i = 0; i < POS; i++){
		tempnode->alphabetlinks[i] = NULL;
	}
	// tempnode is not the end of the word
	tempnode->leaf = 0;
	return tempnode;
}

// inserting a word into a trie
void insert(struct trie *head, char *string){
	// temporary pointer to hold head
	struct trie *tempnode = head;	

	int stringlength = strlen(string);
	// iterating through the nodes till we reach the 
	// correct letter
	for (int CHAR = 0; CHAR < stringlength; CHAR++){
		// create a new node if the trie node doesnt exist
		// string[CHAR] - 'a', we are finding the value between 0 - 26
		// to insert the letter 
		if (tempnode->alphabetlinks[string[CHAR] - 'a'] == NULL){
			tempnode->alphabetlinks[string[CHAR] - 'a'] = node();
		}
		tempnode = tempnode->alphabetlinks[string[CHAR] - 'a'];
	}
	// end of the string
	tempnode->leaf = 1;
}

// searching a word in the data structure
// found = 1, not found = 0
int search(struct trie *head, char * string){
	// check if the tree is empty
	if (head == NULL){
		return 0;
	}
	// temporary pointer to hold head
	struct trie *tempnode = head;	
	while (*string){
		tempnode = tempnode->alphabetlinks[*string - 'a'];
		printf("%d \n", *string - 'a');
		if (tempnode == NULL){
			return 0;
		}
		string++;
	}
	// reached the end of the string
	// return state of leaf of the tempnode
	return tempnode->leaf;
}

char * concatString(char * string, int slice){
	int length = strlen(string)+ 2;
	char *str = malloc( sizeof (char) * length);
	int i = 0;
	while (string[i] != '\0'){
		str[i] = string[i];
		i++;
	}
	str[i++] = (char) slice;
	str[i] = '\0';
	return str;
}

// prints the tree
void printTrie(struct trie * temp, char *string){
	if (temp == NULL){
		return;
	}else if (temp->leaf == 1){
		printf("%s\n", string);
	}
	
	for (int i = 0; i < POS; i++){
		if (temp->alphabetlinks[i] != NULL){
			printTrie(temp->alphabetlinks[i], concatString(string, i + 97));
		}
	}
}

// prints all the children of a given string
void autocomplete(struct trie *temp, char * string){
	int length = strlen(string);
	for (int i = 0; i < length; i++){
		temp = temp->alphabetlinks[string[i]  % 97];
	}
	printTrie(temp, string);
}
