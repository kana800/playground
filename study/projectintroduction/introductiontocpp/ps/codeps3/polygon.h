#ifndef POLYGON_H
#define POLYGON_H

#include "geometry.h"

class Polygon{
    protected:
        static int polygonCount;
        PointArray points;
    public:
        Polygon(const Point tpoints[], const int size);
        Polygon(const PointArray &pointarr);
        virtual double area() const = 0;
        static int getNumPolygons(){return polygonCount;};
        int getNumSides() const;
        const PointArray * getPoints() const;
        ~Polygon();
};


class Rectangle: public Polygon{
    public:
        Rectangle(const Point &left, const Point &right);
        Rectangle(const int leftX, const int leftY, const int rightX, const int rightY);
        virtual double area() const;
};


class Triangle : public Polygon {
    public:
        Triangle(const Point &a, const Point &b, const Point &c);
        virtual double area() const;
};

#endif // POLYGON_H