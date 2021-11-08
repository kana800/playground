#include "polygon.h"
#include <iostream>
#include <cmath>
// initializing the polygon count

Polygon::Polygon(const Point tpoints[], const int size)
    : points(tpoints, size) {
  polygonCount++;
}

Polygon::Polygon(const PointArray &pointarr) : points(pointarr) {
  polygonCount++;
}

int Polygon::getNumSides() const { return points.getSize(); }

const PointArray *Polygon::getPoints() const { return &points; }

Polygon::~Polygon() { polygonCount--; }

Point constructorPoints[4];
Point *updateConstructorPoints(const Point &p1, const Point &p2,
                               const Point &p3, const Point &p4 = Point(0, 0)) {
  constructorPoints[0] = p1;
  constructorPoints[1] = p2;
  constructorPoints[2] = p3;
  constructorPoints[3] = p4;
  return constructorPoints;
}

Rectangle::Rectangle(const Point &left, const Point &right)
    : Polygon(updateConstructorPoints(left, Point(left.getX(), right.getY()),
                                      Point(right.getX(), left.getY())),
              4) {}

Rectangle::Rectangle(const int leftX, const int leftY, const int rightX,
                     const int rightY)
    : Polygon(updateConstructorPoints(Point(leftX, leftY), Point(leftX, rightY),
                                      Point(rightX, rightY),
                                      Point(rightX, leftY)),
              4) {}

double Rectangle::area() const {
  int length = abs(points.get(1)->getX() - points.get(0)->getX());
  int width = abs(points.get(2)->getY() - points.get(1)->getY());
  double a = (double)length * width;
  return a;
}

Triangle::Triangle(const Point &a, const Point &b, const Point &c)
    : Polygon(updateConstructorPoints(a, b, c), 3) {}

double Triangle::area() const {
  // calculating the side lengths of the triangle
  int sideXab = points.get(0)->getX() - points.get(1)->getX();
  int sideYab = points.get(0)->getY() - points.get(1)->getY();
  int sideXbc = points.get(1)->getX() - points.get(2)->getX();
  int sideYbc = points.get(1)->getY() - points.get(2)->getY();
  int sideXca = points.get(2)->getX() - points.get(0)->getX();
  int sideYca = points.get(2)->getY() - points.get(0)->getY();

  // pythagorean theorem
  double a = std::sqrt(sideXab * sideXab + sideYab * sideYab);
  double b = std::sqrt(sideXbc * sideXbc + sideYbc * sideYbc);
  double c = std::sqrt(sideXca * sideXca + sideYca * sideYca);

  double s = (a + b +c) / 2;
  return std::sqrt(s * ( s - a) * (s - b) * (s-c));
}


void printAttributes(Polygon * polyptr){
    std::cout << "Area is: " << polyptr->area() << "\n";

    std::cout << "Points are:\n";
    // iterating through the point array
    const PointArray *pointarr = polyptr->getPoints();
    for(int i = 0; i < pointarr->getSize(); ++i){
        std::cout << "(" << pointarr->get(i)->getX() << "," << pointarr->get(i)->getY() << ") ";
    }
}

int main(int argc, char *argv[]){
    int llx, lly, urx, ury;
    std::cout << "Enter lower-left and upper-right position of a Rectangle: \t Example: lowerleftX lowerleftY upperLeftX upperLeftY ";
    std::cin >> llx >> lly >> urx >> ury;
    Rectangle rec(llx, lly, urx, ury);
    printAttributes(&rec);

    int x1, x2, x3, y1, y2, y3;
    std::cout << "Enter the coordinates of the traingle: Example x1 y1 x2 y2 x3 y3: ";
    std::cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;
    Point a(x1,y1);
    Point b(x2,y2);
    Point c(x3,y3);
    Triangle tri(a,b,c);
    printAttributes(&tri);

    return 0;
}