#ifndef ACCOUNT_H
#define ACCOUNT_H

class Account {
    protected:
        double balance;

    public:
        bool deposit(double amount);
        const double display() const;
        bool withdraw(double amount);
};

#endif // ACCOUNT_H