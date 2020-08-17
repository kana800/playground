#include <stdio.h>

int main()
{
  float length_of_tile;
  float width_of_tile;
  float length_of_floor;
  float width_of_floor;
  float price_per_tile;
  float area;
  float price;

  printf("Enter the Length of Tile(cm)\n");
  scanf("%f",&length_of_tile);
  printf("Enter the Width of Tile(cm)\n");
  scanf("%f",&width_of_tile);
  printf("Enter the Length of floor(cm)\n");
  scanf("%f",&length_of_floor);
  printf("Enter the Width of floor(cm)\n");
  scanf("%f",&width_of_floor);
  printf("Enter the Price Per Tile\n");
  scanf("%f",&price_per_tile);

  area = (length_of_floor * width_of_floor)/(length_of_tile*width_of_tile);
  price = area * price_per_tile;

  printf("Your Price is $%f\n",price);


  return 0;
}

