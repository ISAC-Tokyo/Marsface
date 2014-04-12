using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Mpga.MeshGen
{
    public class BoxZHole : IModel
    {
        MeshGenerator mg = new MeshGenerator();
        public BoxZHole(
            double x0, double y0, double x1, double y1,
            double x2, double y2, double x3, double y3,
            double holeX, double holeY, double z, double height, double phi)
        {
            // 中点を求める
            double x5 = (x0 + x1) / 2.0;
            double y5 = (y0 + y1) / 2.0;
            double x6 = (x1 + x2) / 2.0;
            double y6 = (y1 + y2) / 2.0;
            double x7 = (x2 + x3) / 2.0;
            double y7 = (y2 + y3) / 2.0;
            double x8 = (x3 + x0) / 2.0;
            double y8 = (y3 + y0) / 2.0;

            // 四角形の回転量を求める
            double phase = Math.Atan2(y6, x6);

            // 多角柱の各座標を求める
            int poly = 16;
            Vector2[] p = new Vector2[poly];
            for (int i = 0; i < poly; i++)
            {
                double d = phase + 2.0 * Math.PI * i / poly;
                p[i] = new Vector2(
                    holeX + Math.Cos(d) * phi / 2.0,
                    holeY + Math.Sin(d) * phi / 2.0);
            }

            // 四角柱で物体を構成
            mg.Add(new Box(p[0].X, p[0].Y, x6, y6, (x2 + x6) / 2, (y2 + y6) / 2, p[1].X, p[1].Y, z, height));
            mg.Add(new Box(p[1].X, p[1].Y, (x2 + x6) / 2, (y2 + y6) / 2, x2, y2, p[2].X, p[2].Y, z, height));
            mg.Add(new Box(p[2].X, p[2].Y, x2, y2, (x2 + x7) / 2, (y2 + y7) / 2, p[3].X, p[3].Y, z, height));
            mg.Add(new Box(p[3].X, p[3].Y, (x2 + x7) / 2, (y2 + y7) / 2, x7, y7, p[4].X, p[4].Y, z, height));

            mg.Add(new Box(p[4].X, p[4].Y, x7, y7, (x3 + x7) / 2, (y3 + y7) / 2, p[5].X, p[5].Y, z, height));
            mg.Add(new Box(p[5].X, p[5].Y, (x3 + x7) / 2, (y3 + y7) / 2, x3, y3, p[6].X, p[6].Y, z, height));
            mg.Add(new Box(p[6].X, p[6].Y, x3, y3, (x3 + x8) / 2, (y3 + y8) / 2, p[7].X, p[7].Y, z, height));
            mg.Add(new Box(p[7].X, p[7].Y, (x3 + x8) / 2, (y3 + y8) / 2, x8, y8, p[8].X, p[8].Y, z, height));

            mg.Add(new Box(p[8].X, p[8].Y, x8, y8, (x8 + x0) / 2, (y8 + y0) / 2, p[9].X, p[9].Y, z, height));
            mg.Add(new Box(p[9].X, p[9].Y, (x8 + x0) / 2, (y8 + y0) / 2, x0, y0, p[10].X, p[10].Y, z, height));
            mg.Add(new Box(p[10].X, p[10].Y, x0, y0, (x5 + x0) / 2, (y5 + y0) / 2, p[11].X, p[11].Y, z, height));
            mg.Add(new Box(p[11].X, p[11].Y, (x5 + x0) / 2, (y5 + y0) / 2, x5, y5, p[12].X, p[12].Y, z, height));

            mg.Add(new Box(p[12].X, p[12].Y, x5, y5, (x1 + x5) / 2, (y1 + y5) / 2, p[13].X, p[13].Y, z, height));
            mg.Add(new Box(p[13].X, p[13].Y, (x1 + x5) / 2, (y1 + y5) / 2, x1, y1, p[14].X, p[14].Y, z, height));
            mg.Add(new Box(p[14].X, p[14].Y, x1, y1, (x1 + x6) / 2, (y1 + y6) / 2, p[15].X, p[15].Y, z, height));
            mg.Add(new Box(p[15].X, p[15].Y, (x1 + x6) / 2, (y1 + y6) / 2, x6, y6, p[0].X, p[0].Y, z, height));
        }
        public Triangle[] ToMesh()
        {
            return mg.ToMesh();
        }
    }
}
