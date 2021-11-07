#include "polygon.h"
#include <cmath>
// initializing the polygon count

Polygon::Polygon(const Point tpoints[], const int size): points(tpoints, size){
    polygonCount++;
}

Polygon::Polygon(const PointArray &pointarr): points(pointarr){
    polygonCount++;
}

int Polygon::getNumSides() const {
    return points.getSize();
}

const PointArray * Polygon::getPoints() const {
    return &points;
}

Polygon::~Polygon(){
    polygonCount--;
}

Point constructorPoints[4]; 
Point *updateConstructorPoints( const Point &p1, const Point &p2, 
const Point &p3, const Point &p4 = Point (0,0)) { 
    constructorPoints[0] = p1; 
    constructorPoints[1] = p2; 
    constructorPoints[2] = p3; 
    constructorPoints[3] = p4; 
    return constructorPoints; 
}

Rectangle::Rectangle(const Point &left, const Point &right):
    Polygon(
        updateConstructorPoints(
            left,Point(left.getX(), right.getY()),
            Point(right.getX(), left.getY())), 4){
}

Rectangle::Rectangle(const int leftX, const int leftY, const int rightX, const int rightY):
    Polygon(
        updateConstructorPoints(
            Point(leftX, leftY), Point(leftX, rightY),
            Point(rightX, rightY), Point(rightX, leftY)), 4){

}

double Rectangle::area() const {
    int length = abs(points.get(1)->getX() - points.get(0)->getX());
    int width = abs(points.get(2)->getY() - points.get(1)->getY());
    double a = (double)length * width;
    return a;
}