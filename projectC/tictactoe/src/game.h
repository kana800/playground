#ifndef GAME_H_
#define GAME_H_

// board size
#define N 3
// screen width and height
#define SCREEN_WIDTH 640
#define SCREEN_HEIGHT 480

// players
#define EMPTY 0
#define PLAYER_X 1
#define PLAYER_O 2 

// game states
#define RUNNING_STATE 0
#define PLAYER_X_WON_STATE 1
#define PLAYER_O_WON_STATE 2
#define TIE_STATE 3
#define QUIT_STATE 4

// state of the game
typedef struct {
	int board[N * N];
	int player;
	int state;
} game_t;

#endif //GAME_H_
