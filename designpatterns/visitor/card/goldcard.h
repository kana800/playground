#ifndef GOLDCARD_H
#define GOLDCARD_H

#include "creditcard.h"
#include "offervisitor.h"
#include <iostream>


class GoldCard: public CreditCard{

public:

    void accept(OfferVisitor* visitor)const override {
        visitor->visitGoldCreditCard(this);
    };
};

#endif // GOLDCARD_H