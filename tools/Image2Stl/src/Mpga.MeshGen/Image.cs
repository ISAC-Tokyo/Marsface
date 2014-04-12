using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Drawing;
using System.Threading.Tasks;
using System.Drawing.Imaging;
using System.Runtime.InteropServices;

namespace Mpga.MeshGen
{
    public class Image : IModel
    {
        MeshGenerator mg = new MeshGenerator();
        public Image(string filename, double pixelPerMm, double x, double y, double z, double height)
        {
            Bitmap bitmap = new Bitmap(filename);
            byte[] data = BitmapToByteArray(bitmap);
            int w = bitmap.Width;
            int h = bitmap.Height;
            for(int py =0; py <h;py++)//{r(0, h - 1, py =>
            {
                for (int px = 0; px < w; px++)
                {
                    byte c = data[(px+(h-1-py)*w)*4];
                    if (c < 128)
                    {
                        Box box = new Box(x + px / pixelPerMm, y + py / pixelPerMm, x + (px + 1) / pixelPerMm, y + (py + 1) / pixelPerMm, z, height);
                        mg.Add(box.ToMesh());
                    }

                }
            };
        }
        public Triangle[] ToMesh()
        {
            return mg.ToMesh();
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
