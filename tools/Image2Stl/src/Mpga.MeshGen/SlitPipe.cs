using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Mpga.MeshGen
{
    public class SlitPipe : IModel
    {
        MeshGenerator mg = new MeshGenerator();
        public SlitPipe(double x, double y, double z, double height, double innerPhi, double outerPhi)
        {
            int poly = 16;
            for (int i = 0; i < poly - 1; i++)
            {
                double dl = (360.0 * i / poly) * Math.PI / 180.0;
                double dh = (360.0 * i / poly + 360.0 / poly) * Math.PI / 180.0;

                double x0 = x + Math.Cos(dl) * innerPhi / 2.0;
                double y0 = y + Math.Sin(dl) * innerPhi / 2.0;
                double x1 = x + Math.Cos(dl) * outerPhi / 2.0;
                double y1 = y + Math.Sin(dl) * outerPhi / 2.0;

                double x2 = x + Math.Cos(dh) * outerPhi / 2.0;
                double y2 = y + Math.Sin(dh) * outerPhi / 2.0;
                double x3 = x + Math.Cos(dh) * innerPhi / 2.0;
                double y3 = y + Math.Sin(dh) * innerPhi / 2.0;

                Box box = new Box(x0, y0, x1, y1, x2, y2, x3, y3, z, height);
                mg.Add(box.ToMesh());
            }
        }
        public Triangle[] ToMesh()
        {
            return mg.ToMesh();
        }
    }
}
