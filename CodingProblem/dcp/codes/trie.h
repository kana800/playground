#ifndef TRIE_H
#define TRIE_H

// Each node has 26 (alphabet) possibilites of
// characters 
#define POS 26

struct trie{
	struct trie* alphabetlinks[POS]; 
	int leaf; // used to identify the end of the word
};

struct trie *node();
void insert(struct trie *head, char *string);
int search(struct trie *head, char *string);
void autocomplete(struct trie *temp, char * string);
void printTrie(struct trie * temp, char *string);
char * concatString(char * string, int slice);

#endif
