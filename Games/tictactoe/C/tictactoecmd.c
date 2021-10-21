#include <stdio.h>
#include <stdbool.h>

void PrintBoard(char cells[])
{
  printf("\t Player (1) --> 'X' & Player (2) --> 'O'\n\n\n");
  printf("-------\n");
  printf("|%c|%c|%c|\n",cells[1],cells[2],cells[3]);
  printf("-------\n");
  printf("|%c|%c|%c|\n",cells[4],cells[5],cells[6]);
  printf("-------\n");
  printf("|%c|%c|%c|\n",cells[7],cells[8],cells[9]);
  printf("-------\n");
}

void InitializeBoard(char cells[],int size)
{
  for (int i = 0; i < size ; i++)
  {
    char let = i + 48;
    cells[i] = let;
  }
}

void UpdateBoard(char cells[],int *player_no, int *choice)
{
  if (*player_no == 1)
  {
    cells[*choice] = 'X';
  }
  if (*player_no == 2)
  {
    cells[*choice] = 'O';
  }
}

int IsWinner(char cells[], int *size)
{
  if (cells[1] == cells[2] && cells[2] == cells[3])
  {
    return 1;
  }
  else if (cells[4] == cells[5] && cells[5] == cells[6])
  {
    return 1;
  }
  else if (cells[7] == cells[8] && cells[8] == cells[9]) 
  {
    return 1;
  }
  else if (cells[1] == cells[4] && cells[4] == cells[7])
  {
    return 1;
  }
  else if (cells[2] == cells[5] && cells[5] == cells[8])
  {
    return 1;
  }
  else if (cells[3] == cells[6] && cells[6] == cells[9])
  {
    return 1;
  }
  else if (cells[1] == cells[5] && cells[5] == cells[9])
  {
    return 1;
  }
  else if (cells[3] == cells[5] && cells[5] == cells[7])
  {
    return 1;
  }
  else if (cells[1] != '1' && cells[2] != '2' && cells[3] != '3'
      && cells[4] != '4' && cells[5] != '5' && cells[6] != '6' && cells[7] != '7' && cells[8] != '8' && cells[9] != '9')
  {
    return 0;
  }
  else
  {
    return -1;
  }
}

int main()
{
  char cells[11];
  int player = 1;
  int choice;
  int i;
  
  int size = sizeof(cells)/sizeof(cells[0]); 
  InitializeBoard(cells,size);
  PrintBoard(cells);
  do {
    printf("Player %d, enter the square number: ",player);
    scanf("%d",&choice);
    UpdateBoard(cells, &player, &choice);
    PrintBoard(cells);
    i = IsWinner(cells,&size);
    if (player == 1)
    {
      player = 2;
    }
    else if (player == 2) {
      player = 1;
    }
  }while(i -= 1);
  
  if (i == 1)
  {
    printf("winner player %d\n",player);
  }
  else
  {
    printf("draw\n");
  }
  return 0;
}
