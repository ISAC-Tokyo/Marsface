using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Mpga.MeshGen
{
    public class Box : IModel
    {
        public double _x0, _y0, _x1, _y1, _x2, _y2, _x3, _y3;
        public double _zh, _zl;

        /// <summary>
        /// 四角柱(反時計回りに四角形を定義)
        /// </summary>
        /// <param name="x0"></param>
        /// <param name="y0"></param>
        /// <param name="x1"></param>
        /// <param name="y1"></param>
        /// <param name="x2"></param>
        /// <param name="y2"></param>
        /// <param name="x3"></param>
        /// <param name="y3"></param>
        /// <param name="z"></param>
        /// <param name="height"></param>
        public Box(double x0, double y0, double x1, double y1, double x2, double y2, double x3, double y3, double z, double height)
        {
            Initialize(x0, y0, x1, y1, x2, y2, x3, y3, z, height);
        }

        private void Initialize(double x0, double y0, double x1, double y1, double x2, double y2, double x3, double y3, double z, double height)
        {
            _x0 = x0; _y0 = y0;
            _x1 = x1; _y1 = y1;
            _x2 = x2; _y2 = y2;
            _x3 = x3; _y3 = y3;

            _zl = z;
            _zh = z + height;
        }
        /// <summary>
        /// X,Y軸に平行な四角形を生成します
        /// </summary>
        /// <param name="x0"></param>
        /// <param name="y0"></param>
        /// <param name="x2"></param>
        /// <param name="y2"></param>
        /// <param name="z"></param>
        /// <param name="height"></param>
        public Box(double x0, double y0,double x2, double y2,double z, double height)
        {
            if (x0 <= x2 && y0 <= y2)
            {
                Initialize(x0, y0, x2, y0, x2, y2, x0, y2, z, height);
            }
            else if(x2 <= x0 && y0 <= y2)
            {
                Initialize(x2, y0, x0, y0, x0, y2, x2, y2, z, height);
            }
            else if (x2 <= x0 && y2 <= y0)
            {
                Initialize(x2, y2, x0, y2, x0, y0, x2, y0, z, height);
            }
            else
            {
                Initialize(x0, y2, x2, y2, x2, y0, x0, y0, z, height);
            }
        }
        public Triangle[] ToMesh()
        {
            List<Triangle> t = new List<Triangle>();
            t.Add(new Triangle(_x0, _y0, _zh, _x1, _y1, _zh, _x3, _y3, _zh));
            t.Add(new Triangle(_x1, _y1, _zh, _x2, _y2, _zh, _x3, _y3, _zh));
            t.Add(new Triangle(_x0, _y0, _zl, _x3, _y3, _zl, _x1, _y1, _zl));
            t.Add(new Triangle(_x1, _y1, _zl, _x3, _y3, _zl, _x2, _y2, _zl));

            t.Add(new Triangle(_x3, _y3, _zl, _x3, _y3, _zh, _x2, _y2, _zl));
            t.Add(new Triangle(_x3, _y3, _zh, _x2, _y2, _zh, _x2, _y2, _zl));
            t.Add(new Triangle(_x0, _y0, _zl, _x1, _y1, _zl, _x0, _y0, _zh));
            t.Add(new Triangle(_x0, _y0, _zh, _x1, _y1, _zl, _x1, _y1, _zh));

            t.Add(new Triangle(_x1, _y1, _zl, _x2, _y2, _zl, _x1, _y1, _zh));
            t.Add(new Triangle(_x2, _y2, _zl, _x2, _y2, _zh, _x1, _y1, _zh));
            t.Add(new Triangle(_x0, _y0, _zl, _x0, _y0, _zh, _x3, _y3, _zl));
            t.Add(new Triangle(_x3, _y3, _zl, _x0, _y0, _zh, _x3, _y3, _zh));

            return t.ToArray();
        }
    }
}
