using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Imaging;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;

namespace Mpga.MeshGen
{
    public class Depth : IModel
    {
        MeshGenerator _mg = new MeshGenerator();
        Bitmap _bitmap;
        bool _invert = true;
        double _depthFactor = 0.5;
        double _zoomFactor = 1.0;

        public Depth(Bitmap bitmap, double zoomFactor, double depthFactor, bool invert)
        {
            _invert = invert;
            _bitmap = bitmap;
            _depthFactor = depthFactor;
            _zoomFactor = zoomFactor;
        }

        public Triangle[] ToMesh()
        {
            byte[] data = BitmapToByteArray(_bitmap);

            int w = _bitmap.Width;
            int h = _bitmap.Height;

            if(_invert)
            {
                for (int i = 0; i < w * h * 4; i+= 4)
                {
                    data[i] = (byte)(255 - data[i]);
                }
            }

            List<Triangle> t = new List<Triangle>();
            double zs = _depthFactor;
            double zOffset = 255 * zs;
            
            // 表側
            for (int py = 0; py < h - 1; py++)
            {
                for (int px = 0; px < w - 1; px++)
                {
                    //  0   1
                    //  2   3
                    double _c0 = zs * data[(px + (h - 1 - py) * w) * 4];
                    double _c1 = zs * data[(px + 1 + (h - 1 - py) * w) * 4];
                    double _c2 = zs * data[(px + (h - 1 - py - 1) * w) * 4];
                    double _c3 = zs * data[(px + 1 + (h - 1 - py - 1) * w) * 4];
                    double _x0 = px * _zoomFactor;
                    double _y0 = py * _zoomFactor;
                    double _x1 = (px + 1) * _zoomFactor;
                    double _y1 = py * _zoomFactor;
                    double _x2 = px * _zoomFactor;
                    double _y2 = (py + 1) * _zoomFactor;
                    double _x3 = (px + 1) * _zoomFactor;
                    double _y3 = (py + 1) * _zoomFactor;

                    t.Add(new Triangle(_x0, _y0, _c0, _x1, _y1, _c1, _x3, _y3, _c3));
                    t.Add(new Triangle(_x0, _y0, _c0, _x3, _y3, _c3, _x2, _y2, _c2));

                }
            };

            // 左側
            for (int py = 0; py < h - 1 ; py++)
            {
                for (int px = 0; px <= 0; px++)
                {
                    //  0   2
                    //  1   3
                    double _c0 = zs * data[(px + (h - 1 - py) * w) * 4];
                    double _c1 = 0;
                    double _c2 = zs * data[(px + (h - 1 - py - 1) * w) * 4];
                    double _c3 = 0;
                    double _x0 = px * _zoomFactor;
                    double _y0 = py * _zoomFactor;
                    double _x1 = px * _zoomFactor;
                    double _y1 = py * _zoomFactor;
                    double _x2 = px * _zoomFactor;
                    double _y2 = (py + 1) * _zoomFactor;
                    double _x3 = px * _zoomFactor;
                    double _y3 = (py + 1) * _zoomFactor;

                    t.Add(new Triangle(_x0, _y0, _c0, _x2, _y2, _c2, _x3, _y3, _c3));
                    t.Add(new Triangle(_x0, _y0, _c0, _x3, _y3, _c3, _x1, _y1, _c1));

                }
            };

            // 右側
            for (int py = 0; py < h - 1; py++)
            {
                for (int px = w - 1; px <= w - 1; px++)
                {
                    //  0   2
                    //  1   3
                    double _c0 = zs * data[(px + (h - 1 - py - 1) * w) * 4];
                    double _c1 = 0;
                    double _c2 = zs * data[(px + (h - 1 - py) * w) * 4];
                    double _c3 = 0;
                    double _x0 = px * _zoomFactor;
                    double _y0 = (py + 1) * _zoomFactor;
                    double _x1 = px * _zoomFactor;
                    double _y1 = (py + 1) * _zoomFactor;
                    double _x2 = px * _zoomFactor;
                    double _y2 = py * _zoomFactor;
                    double _x3 = px * _zoomFactor;
                    double _y3 = py * _zoomFactor;

                    t.Add(new Triangle(_x0, _y0, _c0, _x2, _y2, _c2, _x3, _y3, _c3));
                    t.Add(new Triangle(_x0, _y0, _c0, _x3, _y3, _c3, _x1, _y1, _c1));

                }
            }

            // 上側
            for (int py = 0; py <=0; py++)
            {
                for (int px = 0; px < w - 1; px++)
                {
                    //  0   2
                    //  1   3
                    double _c0 = zs * data[(px + 1 + (h - 1 - py) * w) * 4];
                    double _c1 = 0;
                    double _c2 = zs * data[(px + (h - 1 - py) * w) * 4];
                    double _c3 = 0;
                    double _x0 = (px + 1) * _zoomFactor;
                    double _y0 = py * _zoomFactor;
                    double _x1 = (px + 1) * _zoomFactor;
                    double _y1 = py * _zoomFactor;
                    double _x2 = px * _zoomFactor;
                    double _y2 = py * _zoomFactor;
                    double _x3 = px * _zoomFactor;
                    double _y3 = py * _zoomFactor;

                    t.Add(new Triangle(_x0, _y0, _c0, _x2, _y2, _c2, _x3, _y3, _c3));
                    t.Add(new Triangle(_x0, _y0, _c0, _x3, _y3, _c3, _x1, _y1, _c1));

                }
            }

            // 下側
            for (int py = h-1; py <= h-1; py++)
            {
                for (int px = 0; px < w - 1; px++)
                {
                    //  0   2
                    //  1   3
                    double _c0 = zs * data[(px + (h - 1 - py) * w) * 4];
                    double _c1 = 0;
                    double _c2 = zs * data[(px + 1 + (h - 1 - py) * w) * 4];
                    double _c3 = 0;
                    double _x0 = px * _zoomFactor;
                    double _y0 = py * _zoomFactor;
                    double _x1 = px * _zoomFactor;
                    double _y1 = py * _zoomFactor;
                    double _x2 = (px + 1) * _zoomFactor;
                    double _y2 = py * _zoomFactor;
                    double _x3 = (px + 1) * _zoomFactor;
                    double _y3 = py * _zoomFactor;

                    t.Add(new Triangle(_x0, _y0, _c0, _x2, _y2, _c2, _x3, _y3, _c3));
                    t.Add(new Triangle(_x0, _y0, _c0, _x3, _y3, _c3, _x1, _y1, _c1));

                }
            }

            // 底面
            // 0 1
            // 2 3
            {
                double _c0 = 0;
                double _c1 = 0;
                double _c2 = 0;
                double _c3 = 0;
                double _x0 = (w - 1) * _zoomFactor;
                double _y0 = 0;
                double _x1 = 0;
                double _y1 = 0;
                double _x2 = (w - 1) * _zoomFactor;
                double _y2 = (h - 1) * _zoomFactor;
                double _x3 = 0;
                double _y3 = (h - 1) * _zoomFactor;


                t.Add(new Triangle(_x0, _y0, _c0, _x1, _y1, _c1, _x3, _y3, _c3));
                t.Add(new Triangle(_x0, _y0, _c0, _x3, _y3, _c3, _x2, _y2, _c2));

            }


            return t.ToArray();
        }


        /// <summary>
        /// Bitmapをbyte[]に変換する
        /// </summary>
        /// <param name="bitmap">変換元のBitmap</param>
        /// <returns>1 pixel = 4 byte (+3:A, +2:R, +1:G, +0:B) に変換したbyte配列</returns>
        private byte[] BitmapToByteArray(Bitmap bmp)
        {
            Rectangle rect = new Rectangle(0, 0, bmp.Width, bmp.Height);
            System.Drawing.Imaging.BitmapData bmpData =
                bmp.LockBits(rect, System.Drawing.Imaging.ImageLockMode.ReadWrite,
                PixelFormat.Format32bppArgb);

            // Bitmapの先頭アドレスを取得
            IntPtr ptr = bmpData.Scan0;

            // 32bppArgbフォーマットで値を格納
            int bytes = bmp.Width * bmp.Height * 4;
            byte[] rgbValues = new byte[bytes];

            // Bitmapをbyte[]へコピー
            Marshal.Copy(ptr, rgbValues, 0, bytes);

            bmp.UnlockBits(bmpData);
            return rgbValues;
        }
    }
}
