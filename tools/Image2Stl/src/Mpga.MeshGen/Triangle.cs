using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Mpga.MeshGen
{
    public class Triangle
    {
        public double X0, Y0, Z0;
        public double X1, Y1, Z1;
        public double X2, Y2, Z2;
        public bool IsSweeped = false;

        public Triangle()
        {
        }

        public Triangle(Triangle t)
        {
            X0 = t.X0; Y0 = t.Y0; Z0 = t.Z0;
            X1 = t.X1; Y1 = t.Y1; Z1 = t.Z1;
            X2 = t.X2; Y2 = t.Y2; Z2 = t.Z2;
        }

        public Triangle(double x0, double y0, double z0,
            double x1, double y1, double z1,
            double x2, double y2, double z2)
        {
            X0 = x0; Y0 = y0; Z0 = z0;
            X1 = x1; Y1 = y1; Z1 = z1;
            X2 = x2; Y2 = y2; Z2 = z2;
        }

    }
}
