#ifndef GEOMETRY_H
#define GEOMETRY_H

class Point{

    private:
        int x;
        int y;

    public:
        Point(int aX = 0, int aY = 0);
        int getX() const;
        int getY() const;
        void setX(const int new_x);
        void setY(const int new_y);
};


class PointArray{
    private:
        int size;
        Point *points;
    public:
        PointArray();
        PointArray(const Point givenPoints[], const int givenSize);
        PointArray(const PointArray &pv);
        ~PointArray();

        void resize(int n);
        void push_back(const Point &p);
        void insert(const int position, const Point &p);
        void remove(const int pos);
        const int getSize() const;
        void clear();
        Point get(const int position);
        const Point get(const int position) const;
};

#endif //GEOMETRY_H