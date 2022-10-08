/*VISITOR INTERFACE*/
#ifndef OFFERVISITOR_H
#define OFFERVISITOR_H


// forward declartion
class BronzeCard;
class SilverCard;
class GoldCard;

class OfferVisitor {

public:
    virtual void visitGoldCreditCard(
        const GoldCard *goldcard) const = 0;
    virtual void visitSilverCreditCard(
        const SilverCard *silvercard) const = 0;
    virtual void visitBronzeCreditCard(
        const BronzeCard *bronzecard) const = 0;

};

#endif //OFFER_H