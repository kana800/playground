#include <stdio.h>
void newentrypoint(void){
	printf("new entry point?\n");
	return;
}

int main(){
	printf("hello world\n");
	newentrypoint();
	return 0;
}
