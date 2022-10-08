#include <iostream>
#include <utility>

#include "bronzecard.h"
#include "gasoffer.h"

int main(int argc, char* argv[]){

    BronzeCard *bronzeCard = new BronzeCard();

    GasOffer *gasOffer = new GasOffer();

    bronzeCard->accept(gasOffer);


    return 0;
}