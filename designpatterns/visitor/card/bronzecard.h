#ifndef BRONZECARD_H
#define BRONZECARD_H

#include "CreditCard.h"
#include <iostream>

class BronzeCard: public CreditCard{

public:

    void accept(OfferVisitor* visitor)const override {
        visitor->visitBronzeCreditCard(this);
    };
};

#endif // BRONZECARD_H