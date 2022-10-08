#ifndef SILVERCARD_H
#define SILVERCARD_H

#include "creditcard.h"
#include "offervisitor.h"
#include <iostream>


class SilverCard: public CreditCard{

public:

    void accept(OfferVisitor* visitor)const override {
        visitor->visitSilverCreditCard(this);
    };
};

#endif // SILVERCARD_H