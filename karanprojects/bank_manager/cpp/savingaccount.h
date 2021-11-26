#ifndef SAVINGACCOUNT_H
#define SAVINGACCOUNT_H

#include "account.h"

class SavingAccount: public Account {
    public:
        SavingAccount(){
            this->balance = 0.00;
        }
        ~SavingAccount();
        void deposit(double amount){
            this->balance += amount;
        }
        const double display() const {
            std::cout << "current balance: " << this->balance;
            return this->balance;
        }            
        void withdraw(double amount) {
            this->balance -= amount;
        }
};

#endif // SAVINGACC_H