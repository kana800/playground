#include <stdio.h>
#include <stdlib.h>
#include "SDL2/SDL.h"

#include "rendering.h"
#include "game.h"
#include "logic.h"

int main(int argc, char *argv[]){
	
	// initializing the SDL system
	if (SDL_Init(SDL_INIT_VIDEO) != 0){
		// if there is an error while initializing
		fprintf(stderr, "couldnt initialize sdl2 %s\n", SDL_GetError());
		return EXIT_FAILURE;
	}

	// after initializing the system, we need to create a window
	SDL_Window *window = SDL_CreateWindow("TICTACTOE",
			100,100,
			SCREEN_WIDTH, SCREEN_HEIGHT,
			SDL_WINDOW_SHOWN);

	// error handling for window
	if (window == NULL){
		fprintf(stderr,"SDL_CreateWindow Error: $s\n", SDL_GetError());
		return EXIT_FAILURE;

	}

	// creating  a render that enables us with the rendering of the window
	SDL_Renderer *renderer = SDL_CreateRenderer(window,
		   	-1,
		   SDL_RENDERER_ACCELERATED |
		   SDL_RENDERER_PRESENTVSYNC);


	// error handling for the render
	if (renderer == NULL){
		SDL_DestroyWindow(window);
		fprintf(stderr,"SDL_CreateRenderer Error: $s\n", SDL_GetError());
		return EXIT_FAILURE;
	}

	// initialize state of the game, consists of nine empty boxes (N = 3)
	game_t game = {
		.board = {  EMPTY, EMPTY, EMPTY, 
					EMPTY, EMPTY, EMPTY, 
					EMPTY, EMPTY, EMPTY },
		.player = PLAYER_X,
		.state = RUNNING_STATE
	};

	// size of the cell
	const float CELL_HEIGHT = SCREEN_HEIGHT / N;
	const float CELL_WIDTH = SCREEN_WIDTH / N;

	// event loop
	SDL_Event e;
	while (game.state != QUIT_STATE) {
		// pulling the events from the event
		// queue
		while (SDL_PollEvent(&e)) {
			switch (e.type){
				// if event is SDLQUIT exit program
				case SDL_QUIT:
					game.state = QUIT_STATE;
					break;
				// mouse down event
				case SDL_MOUSEBUTTONDOWN:
					// invoking click on cell function
					click_on_cell(&game,
							e.button.y / CELL_HEIGHT,
							e.button.x / CELL_WIDTH);
					break;
				default: {}
			}
		}
		// rendering the next frame
		SDL_SetRenderDrawColor(renderer, 0,0,0,255);
		SDL_RenderClear(renderer);
		// rendering the game
		render_game(renderer, &game);
		SDL_RenderPresent(renderer);
	}
	// exiting event loop
	// deallocating all the resources
	SDL_DestroyWindow(window);
	SDL_Quit();

	return EXIT_SUCCESS;
}
