#ifndef CREDITCARD_H
#define CREDITCARD_H


#include "offervisitor.h"

class CreditCard{

public:
    virtual ~CreditCard() = default;

    virtual void accept(OfferVisitor* visit) const =  0;

};

#endif // CREDITCARD_H