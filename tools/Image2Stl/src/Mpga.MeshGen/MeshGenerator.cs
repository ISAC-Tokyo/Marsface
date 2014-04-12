using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

namespace Mpga.MeshGen
{
    public class MeshGenerator
    {
        List<Triangle> _triangles = new List<Triangle>();
        object lockObject = new object();
        /// <summary>
        /// 三角形メッシュを取得します。
        /// </summary>
        /// <returns></returns>
        public Triangle[] ToMesh()
        {
            return _triangles.ToArray();
        }
        /// <summary>
        /// 三角形メッシュを取得します。
        /// </summary>
        /// <param name="x">平行移動量 x</param>
        /// <param name="y">平行移動量 y</param>
        /// <param name="z">平行移動量 z</param>
        /// <returns></returns>
        public Triangle[] ToMesh(double x, double y, double z)
        {
            List<Triangle> list = new List<Triangle>();
            foreach (Triangle t in _triangles)
            {
                list.Add(new Triangle(
                    t.X0 + x, t.Y0 + y, t.Z0 + z,
                    t.X1 + x, t.Y1 + y, t.Z1 + z,
                    t.X2 + x, t.Y2 + y, t.Z2 + z));
            }
            return list.ToArray();
        }
        /// <summary>
        /// 三角形メッシュを追加します。頂点の順序は反時計回りが表側です。
        /// </summary>
        /// <param name="triangles">三角形メッシュ</param>
        public void Add(Triangle[] triangles)
        {
            AddTriangles(triangles);
        }
        /// <summary>
        /// モデルを追加します。
        /// </summary>
        /// <param name="model">モデルデータ</param>
        public void Add(IModel model)
        {
            AddTriangles(model.ToMesh());
        }
        public void Add(MeshGenerator mg)
        {
            AddTriangles(mg.ToMesh());
        }
        public void Add(MeshGenerator mg, double x, double y, double z)
        {
            AddTriangles(mg.ToMesh(x, y, z));
        }
        /// <summary>
        /// Z軸回りに回転する
        /// </summary>
        /// <param name="rad">反時計回りの回転角(rad)</param>
        public void RotateZ(double rad)
        {
            foreach (Triangle t in _triangles)
            {
                double x0 = Math.Cos(rad) * t.X0 - Math.Sin(rad) * t.Y0;
                double y0 = Math.Sin(rad) * t.X0 + Math.Cos(rad) * t.Y0;
                t.X0 = x0; t.Y0 = y0;

                double x1 = Math.Cos(rad) * t.X1 - Math.Sin(rad) * t.Y1;
                double y1 = Math.Sin(rad) * t.X1 + Math.Cos(rad) * t.Y1;
                t.X1 = x1; t.Y1 = y1;

                double x2 = Math.Cos(rad) * t.X2 - Math.Sin(rad) * t.Y2;
                double y2 = Math.Sin(rad) * t.X2 + Math.Cos(rad) * t.Y2;
                t.X2 = x2; t.Y2 = y2;
            }
        }
        private void AddTriangles(Triangle[] triangles)
        {
            List<Triangle> queue = new List<Triangle>();
            Triangle[] triInput = (Triangle[])triangles.Clone();

            // a b c と a c b, c b a, b a c の重複を確認
            foreach(Triangle s in triInput)
            {
                if (_triangles.Count == 0)
                {
                    _triangles.Add(new Triangle(s));
                    continue;
                }
                Triangle target = null;
                // 位置が同じで法線ベクトルが逆向きの三角形がないかどうかを探す
                lock (lockObject)
                {
                    foreach (Triangle t in _triangles)
                    {
                        if (t.IsSweeped)
                        {
                            continue;
                        }
                        if (
                           (Math.Abs(t.X0 - s.X0) < 0.001 && Math.Abs(t.Y0 - s.Y0) < 0.001 && Math.Abs(t.Z0 - s.Z0) < 0.001
                        && Math.Abs(t.X1 - s.X2) < 0.001 && Math.Abs(t.Y1 - s.Y2) < 0.001 && Math.Abs(t.Z1 - s.Z2) < 0.001
                        && Math.Abs(t.X2 - s.X1) < 0.001 && Math.Abs(t.Y2 - s.Y1) < 0.001 && Math.Abs(t.Z2 - s.Z1) < 0.001)
                        ||
                           (Math.Abs(t.X0 - s.X2) < 0.001 && Math.Abs(t.Y0 - s.Y2) < 0.001 && Math.Abs(t.Z0 - s.Z2) < 0.001
                        && Math.Abs(t.X1 - s.X1) < 0.001 && Math.Abs(t.Y1 - s.Y1) < 0.001 && Math.Abs(t.Z1 - s.Z1) < 0.001
                        && Math.Abs(t.X2 - s.X0) < 0.001 && Math.Abs(t.Y2 - s.Y0) < 0.001 && Math.Abs(t.Z2 - s.Z0) < 0.001)
                            ||
                           (Math.Abs(t.X0 - s.X1) < 0.001 && Math.Abs(t.Y0 - s.Y1) < 0.001 && Math.Abs(t.Z0 - s.Z1) < 0.001
                        && Math.Abs(t.X1 - s.X0) < 0.001 && Math.Abs(t.Y1 - s.Y0) < 0.001 && Math.Abs(t.Z1 - s.Z0) < 0.001
                        && Math.Abs(t.X2 - s.X2) < 0.001 && Math.Abs(t.Y2 - s.Y2) < 0.001 && Math.Abs(t.Z2 - s.Z2) < 0.001)

                            )
                        {
                            target = t;
                            break;
                        }
                    }
                }
                if(target != null)
                { // 法線ベクトルが逆で同じ三角形なら削除フラグを立てる
                    target.IsSweeped = true;
                }
                else
                { // 新しい三角形を追加
                    queue.Add(new Triangle(s));
                }
            }
            lock (lockObject)
            {
                List<Triangle> update = new List<Triangle>();
                foreach (Triangle t in _triangles)
                {
                    if (!t.IsSweeped)
                    {
                        update.Add(new Triangle(t));
                    }
                }
                _triangles = update;
                _triangles.AddRange(queue);
            }
        }
        /// <summary>
        /// X軸に対称となるようにメッシュをコピーします
        /// </summary>
        /// <param name="x">対象となるx座標</param>
        public void MirrorX(double x)
        {
            List<Triangle> s = new List<Triangle>();
            foreach (Triangle t in _triangles)
            {
                if (!t.IsSweeped)
                {
                    s.Add(new Triangle(x - t.X0, t.Y0, t.Z0, x - t.X2, t.Y2, t.Z2, x - t.X1, t.Y1, t.Z1)); 
                }
            }
            AddTriangles(s.ToArray());
        }

        /// <summary>
        /// Y軸に対称となるようにメッシュをコピーします
        /// </summary>
        /// <param name="y">対象となるy座標</param>
        public void MirrorY(double y)
        {
            List<Triangle> s = new List<Triangle>();
            foreach (Triangle t in _triangles)
            {
                if (!t.IsSweeped)
                {
                    s.Add(new Triangle(t.X0, y - t.Y0, t.Z0, t.X2, y - t.Y2, t.Z2, t.X1, y - t.Y1, t.Z1));
                }
            }
            AddTriangles(s.ToArray());
        }


        /// <summary>
        /// メッシュをクリアします。
        /// </summary>
        public void Clear()
        {
            _triangles.Clear();
        }
        /// <summary>
        /// メッシュを平行移動します。
        /// </summary>
        /// <param name="x">移動量 x (mm)</param>
        /// <param name="y">移動量 y (mm)</param>
        /// <param name="z">移動量 z (mm)</param>
        public void Translate(double x, double y, double z)
        {
            foreach (Triangle t in _triangles)
            {
                t.X0 += x; t.Y0 += y; t.Z0 += z;
                t.X1 += x; t.Y1 += y; t.Z1 += z;
                t.X2 += x; t.Y2 += y; t.Z2 += z;
            }
        }

        /// <summary>
        /// メッシュの中心が(0,0,0)に来るように平行移動します。
        /// Zの最小値は0になるように補正します。
        /// </summary>
        public void ToCenter()
        {
            double minX = double.MaxValue;
            double minY = double.MaxValue;
            double maxX = double.MinValue;
            double maxY = double.MinValue;
            double minZ = double.MaxValue;

            foreach (Triangle t in _triangles)
            {
                if (t.X0 < minX) minX = t.X0;
                if (t.X1 < minX) minX = t.X1;
                if (t.X2 < minX) minX = t.X2;

                if (t.X0 > maxX) maxX = t.X0;
                if (t.X1 > maxX) maxX = t.X1;
                if (t.X2 > maxX) maxX = t.X2;

                if (t.Y0 < minY) minY = t.Y0;
                if (t.Y1 < minY) minY = t.Y1;
                if (t.Y2 < minY) minY = t.Y2;

                if (t.Y0 > maxY) maxY = t.Y0;
                if (t.Y1 > maxY) maxY = t.Y1;
                if (t.Y2 > maxY) maxY = t.Y2;

                if (t.Z0 < minZ) minZ = t.Z0;
                if (t.Z1 < minZ) minZ = t.Z1;
                if (t.Z2 < minZ) minZ = t.Z2;
            }
            double sx = (maxX + minX) / 2.0;
            double sy = (maxY + minY) / 2.0;
            this.Translate(-sx, -sy, -minZ);
        }
        /// <summary>
        /// STL形式でメッシュを保存します
        /// </summary>
        /// <param name="filename">保存するファイル名</param>
        public void Save(string filename)
        {
            string name = "meshgen";
            using (StreamWriter sw = new StreamWriter(filename, false, Encoding.ASCII))
            {
                sw.Write("solid " + name + "\n");
                foreach (Triangle t in _triangles)
                {
                    if (!t.IsSweeped)
                    {
                        double x1 = t.X1 - t.X0;
                        double y1 = t.Y1 - t.Y0;
                        double z1 = t.Z1 - t.Z0;

                        double x2 = t.X2 - t.X0;
                        double y2 = t.Y2 - t.Y0;
                        double z2 = t.Z2 - t.Z0;

                        double vx = y1 * z2 - y2 * z1;
                        double vy = z1 * x2 - z2 * x1;
                        double vz = x1 * y2 - x2 * y1;
                        double d = Math.Sqrt(vx * vx + vy * vy + vz * vz);
                        vx /= d;
                        vy /= d;
                        vz /= d;

                        sw.Write("  facet normal " + ConvertToString(vx, vy, vz) + "\n");
                        sw.Write("    outer loop\n");
                        sw.Write("      vertex " + ConvertToString(t.X0, t.Y0, t.Z0) + "\n");
                        sw.Write("      vertex " + ConvertToString(t.X1, t.Y1, t.Z1) + "\n");
                        sw.Write("      vertex " + ConvertToString(t.X2, t.Y2, t.Z2) + "\n");
                        sw.Write("    endloop\n");
                        sw.Write("  endfacet\n");
                    }
                    else
                    {
                        Console.WriteLine("Sweeped");
                    }
                }
                sw.Write("endsolid " + name + "\n");
            }
        }
        private string ConvertToString(double x, double y, double z)
        {
            return x.ToString("F3") + " " + y.ToString("F3") + " " + z.ToString("F3");
        }
    }
}
