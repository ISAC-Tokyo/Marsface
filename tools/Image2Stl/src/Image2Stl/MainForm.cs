using Mpga.MeshGen;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Mpga.jp
{
    public partial class MainForm : Form
    {
        Bitmap bitmap = new Bitmap(640,480);
        string lastFileName = "";
        public MainForm()
        {
            InitializeComponent();
        }

        private void panel1_DragEnter(object sender, DragEventArgs e)
        {
            if (e.Data.GetDataPresent(DataFormats.FileDrop)){
                e.Effect = DragDropEffects.Copy;
            }
            else
            {
                e.Effect = DragDropEffects.None;
            }
        }

        private void panel1_DragDrop(object sender, DragEventArgs e)
        {
            string[] fileName = (string[])e.Data.GetData(DataFormats.FileDrop, false);

            try
            {
                if (bitmap != null)
                {
                    lastFileName = fileName[0];
                    bitmap.Dispose();
                    Bitmap bitmap2 = new Bitmap(lastFileName);
                    bitmap = new Bitmap(bitmap2);
                    this.pictureBox1.Image = bitmap;
                    this.label1.Text = "";
                    bitmap2.Dispose();
                    this.buttonCreateStl.Enabled = true;
                    UpdateSize();
                }
            }
            catch (Exception)
            {
                MessageBox.Show("ファイルが開けませんでした", "読み込み失敗", MessageBoxButtons.OK);
            }
        }

        private void buttonCreateStl_Click(object sender, EventArgs e)
        {
            MeshGenerator mg = new MeshGenerator();
            mg.Add(new Depth(bitmap, ((double)this.numericUpDownXY.Value) / 100.0, ((double)this.numericUpDownZ.Value) / 100.0, this.checkBox1.Checked));
            mg.Save(lastFileName + ".stl");
            MessageBox.Show("保存しました");
        }

        private void numericUpDownZ_ValueChanged(object sender, EventArgs e)
        {
            UpdateSize();
        }

        private void numericUpDownXY_ValueChanged(object sender, EventArgs e)
        {
            UpdateSize();
        }

        private void UpdateSize()
        {
            if(bitmap != null){
                int x = (int)(this.bitmap.Width * (double)this.numericUpDownXY.Value / 100.0);
                int y = (int)(this.bitmap.Height * (double)this.numericUpDownXY.Value / 100.0);
                int z = (int)(255.0 * (double)this.numericUpDownZ.Value / 100.0);

                this.labelOutputSize.Text = x + " x " + y + " x " + z + " mm";
            }
        }

    }
}
