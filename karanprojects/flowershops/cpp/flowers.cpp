/*
* create a flower shop application which deals in flower objects
* and use those flower objects ina  bouquet object which can be sold.
* keep track of the number of objects and wehn you may need to order more.
*/
#include <iostream>
#include <map>
#include <string>
#include <tuple>

/*
 * flower object
 * holds the flower name and price
 */

class Flower{
    public:
        std::string flowername;
        double price = 0;
};

class Bouquet{
    private:
        /*since map function needs compare the key values to be
         *sorted we need to define operator 
        https://stackoverflow.com/questions/
            1102392/how-can-i-use-stdmaps-with-user-defined-types-as-key
        */
        struct classcompare{
            bool operator() (const Flower& lhs, const Flower& rhs) const {
                return lhs.price < rhs.price;
            }
        };
        std::string bouquetname;
        std::map< Flower,int, classcompare > flower;
    public:
        double price = 0;
        Bouquet(std::string a_bouquetname){
            bouquetname = a_bouquetname;
            price = 0;
        }
    private:        
        void updateprice(double newprice) {
            price = newprice;
        };
    public:
        /*return and update the price of the class instance*/
        double getprice(){
            int size = flower.size();
            if (size == 0){
                return 0.00;
            }
            double tempprice = 0;
            for (auto it = flower.cbegin(); it != flower.cend(); it++){
                tempprice += it->first.price * it->second;
            }
            /*updating bouquet price*/
            updateprice(tempprice);
            return tempprice;
        }

        void addFlower(Flower f, int quantity){
            flower[f] = quantity;
        }
};

class Shop{
    private:
        struct classcompare{
            bool operator() (const Bouquet& lhs, const Bouquet& rhs) const {
                return lhs.price < rhs.price;
            }
        };
        std::string shopname;
        std::map< Bouquet,int, classcompare > inventory;
    public:
        Shop(std::string a_Shopname){
            shopname = a_Shopname;
        }
        double income = 0;
    public:
        /*returns the inventory of the bouquet.
         *returns -1 if there is none
         */
        int bouquetInventory(std::string a_bouquetname){
            if (inventory.count(a_bouquetname) < 0){
                return -1;
            }else{
                return inventory.find(a_bouquetname)->second;
            }
        }

        double bouquetPrice(std::string a_bouquetname){
            if (inventory.count(a_bouquetname) < 0){
                return -1;
            }else{
                return inventory.find(a_bouquetname)->first.price;
            }
        }

        /*adds bouquets to the inventory*/
        void addBouquet(Bouquet b, int quantity){
            inventory[b] = quantity;
        }

        void sellItem(std::string a_bouquetname, int a_quantity){
            /*checking the current inventory*/
            if (bouquetInventory(a_bouquetname) == -1){
                std::cout << "Item not available" << "\n";
                return;
            }else{
                int currentquantity = bouquetInventory(a_bouquetname);
                if (a_quantity > currentquantity){
                    std::cout << "Quantity Not Available" << "\n";
                    std::cout << "Only " << currentquantity << " in stock" << "\n";
                    return;
                }
                inventory[inventory.find(a_bouquetname)->first] = currentquantity - a_quantity;
                income += bouquetPrice(a_bouquetname) * a_quantity;
            }
        }

        double getIncome(){
            return income;
        }
};


int main(int argc, char *argv[]){
    
    /*creating flower objects*/
    Flower tulip;
    tulip.flowername = "tulip";
    tulip.price = 9.99;
    Flower rose;
    rose.flowername = "rose";
    rose.price = 4.50;
    Flower orchid;
    orchid.flowername = "orchid";
    orchid.price = 4.33;

    /*creating a bouqet*/
    Bouquet justfriends("justfriends");
    justfriends.addFlower(tulip, 50);
    justfriends.addFlower(rose, 5);

    justfriends.getprice();
    Bouquet justmarried("justmarried");
    justfriends.addFlower(orchid, 10);

    Shop flowerhub("flowerhub");
    flowerhub.addBouquet(justfriends, 5);
    flowerhub.sellItem("justfriends", 4);
    std::cout << flowerhub.bouquetPrice("justfriends");
    std::cout << flowerhub.getIncome();
    return 0;
}