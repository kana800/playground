#ifndef GASOFFER_H
#define GASOFFER_H

#include "offervisitor.h"
#include <iostream>

class GasOffer: public OfferVisitor {

public:
    virtual void visitGoldCreditCard(const GoldCard *goldcard) const override{
        std::cout << "Gas Offer for Gold Cards" << std::endl;
    };
    virtual void visitSilverCreditCard(const SilverCard *silvercard) const override {
        std::cout << "Gas Offer for Silver Cards" << std::endl;
    };
    virtual void visitBronzeCreditCard(const BronzeCard *bronzecard) const override {
        std::cout << "Gas Offer for Bronze Cards" << std::endl;
    };

};

#endif // GASOFFER_H