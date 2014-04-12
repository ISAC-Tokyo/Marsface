namespace Mpga.jp
{
    partial class MainForm
    {
        /// <summary>
        /// 必要なデザイナー変数です。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 使用中のリソースをすべてクリーンアップします。
        /// </summary>
        /// <param name="disposing">マネージ リソースが破棄される場合 true、破棄されない場合は false です。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows フォーム デザイナーで生成されたコード

        /// <summary>
        /// デザイナー サポートに必要なメソッドです。このメソッドの内容を
        /// コード エディターで変更しないでください。
        /// </summary>
        private void InitializeComponent()
        {
            this.panel1 = new System.Windows.Forms.Panel();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.label1 = new System.Windows.Forms.Label();
            this.panel2 = new System.Windows.Forms.Panel();
            this.labelOutputSize = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.numericUpDownXY = new System.Windows.Forms.NumericUpDown();
            this.label3 = new System.Windows.Forms.Label();
            this.buttonCreateStl = new System.Windows.Forms.Button();
            this.label2 = new System.Windows.Forms.Label();
            this.numericUpDownZ = new System.Windows.Forms.NumericUpDown();
            this.checkBox1 = new System.Windows.Forms.CheckBox();
            this.panel1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.panel2.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownXY)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownZ)).BeginInit();
            this.SuspendLayout();
            // 
            // panel1
            // 
            this.panel1.AllowDrop = true;
            this.panel1.AutoScroll = true;
            this.panel1.BackColor = System.Drawing.SystemColors.ControlDark;
            this.panel1.Controls.Add(this.pictureBox1);
            this.panel1.Controls.Add(this.label1);
            this.panel1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.panel1.Location = new System.Drawing.Point(0, 76);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(564, 294);
            this.panel1.TabIndex = 0;
            this.panel1.DragDrop += new System.Windows.Forms.DragEventHandler(this.panel1_DragDrop);
            this.panel1.DragEnter += new System.Windows.Forms.DragEventHandler(this.panel1_DragEnter);
            // 
            // pictureBox1
            // 
            this.pictureBox1.Location = new System.Drawing.Point(0, 0);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(100, 50);
            this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.pictureBox1.TabIndex = 0;
            this.pictureBox1.TabStop = false;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(165, 142);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(224, 12);
            this.label1.TabIndex = 1;
            this.label1.Text = "ここに画像ファイルを Drag ＆ Drop してください";
            // 
            // panel2
            // 
            this.panel2.BackColor = System.Drawing.SystemColors.Control;
            this.panel2.Controls.Add(this.labelOutputSize);
            this.panel2.Controls.Add(this.label4);
            this.panel2.Controls.Add(this.numericUpDownXY);
            this.panel2.Controls.Add(this.label3);
            this.panel2.Controls.Add(this.buttonCreateStl);
            this.panel2.Controls.Add(this.label2);
            this.panel2.Controls.Add(this.numericUpDownZ);
            this.panel2.Controls.Add(this.checkBox1);
            this.panel2.Dock = System.Windows.Forms.DockStyle.Top;
            this.panel2.Location = new System.Drawing.Point(0, 0);
            this.panel2.Name = "panel2";
            this.panel2.Size = new System.Drawing.Size(564, 76);
            this.panel2.TabIndex = 3;
            // 
            // labelOutputSize
            // 
            this.labelOutputSize.AutoSize = true;
            this.labelOutputSize.Location = new System.Drawing.Point(315, 44);
            this.labelOutputSize.Name = "labelOutputSize";
            this.labelOutputSize.Size = new System.Drawing.Size(23, 12);
            this.labelOutputSize.TabIndex = 35;
            this.labelOutputSize.Text = "---";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(297, 19);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(60, 12);
            this.label4.TabIndex = 34;
            this.label4.Text = "出力サイズ:";
            // 
            // numericUpDownXY
            // 
            this.numericUpDownXY.Location = new System.Drawing.Point(127, 17);
            this.numericUpDownXY.Maximum = new decimal(new int[] {
            300,
            0,
            0,
            0});
            this.numericUpDownXY.Minimum = new decimal(new int[] {
            1,
            0,
            0,
            0});
            this.numericUpDownXY.Name = "numericUpDownXY";
            this.numericUpDownXY.Size = new System.Drawing.Size(77, 19);
            this.numericUpDownXY.TabIndex = 33;
            this.numericUpDownXY.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            this.numericUpDownXY.Value = new decimal(new int[] {
            100,
            0,
            0,
            0});
            this.numericUpDownXY.ValueChanged += new System.EventHandler(this.numericUpDownXY_ValueChanged);
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(12, 19);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(105, 12);
            this.label3.TabIndex = 32;
            this.label3.Text = "X-Y方向拡大率 (%):";
            // 
            // buttonCreateStl
            // 
            this.buttonCreateStl.Enabled = false;
            this.buttonCreateStl.Location = new System.Drawing.Point(466, 36);
            this.buttonCreateStl.Name = "buttonCreateStl";
            this.buttonCreateStl.Size = new System.Drawing.Size(75, 23);
            this.buttonCreateStl.TabIndex = 31;
            this.buttonCreateStl.Text = ".stl 生成";
            this.buttonCreateStl.UseVisualStyleBackColor = true;
            this.buttonCreateStl.Click += new System.EventHandler(this.buttonCreateStl_Click);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(12, 44);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(92, 12);
            this.label2.TabIndex = 2;
            this.label2.Text = "Z方向拡大率 (%):";
            // 
            // numericUpDownZ
            // 
            this.numericUpDownZ.Location = new System.Drawing.Point(127, 42);
            this.numericUpDownZ.Maximum = new decimal(new int[] {
            300,
            0,
            0,
            0});
            this.numericUpDownZ.Minimum = new decimal(new int[] {
            1,
            0,
            0,
            0});
            this.numericUpDownZ.Name = "numericUpDownZ";
            this.numericUpDownZ.Size = new System.Drawing.Size(77, 19);
            this.numericUpDownZ.TabIndex = 30;
            this.numericUpDownZ.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            this.numericUpDownZ.Value = new decimal(new int[] {
            5,
            0,
            0,
            0});
            this.numericUpDownZ.ValueChanged += new System.EventHandler(this.numericUpDownZ_ValueChanged);
            // 
            // checkBox1
            // 
            this.checkBox1.AutoSize = true;
            this.checkBox1.Checked = true;
            this.checkBox1.CheckState = System.Windows.Forms.CheckState.Checked;
            this.checkBox1.Location = new System.Drawing.Point(224, 43);
            this.checkBox1.Name = "checkBox1";
            this.checkBox1.Size = new System.Drawing.Size(68, 16);
            this.checkBox1.TabIndex = 0;
            this.checkBox1.Text = "深さ反転";
            this.checkBox1.UseVisualStyleBackColor = true;
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(564, 370);
            this.Controls.Add(this.panel1);
            this.Controls.Add(this.panel2);
            this.Name = "MainForm";
            this.Text = "Image2Stl";
            this.panel1.ResumeLayout(false);
            this.panel1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.panel2.ResumeLayout(false);
            this.panel2.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownXY)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownZ)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Panel panel2;
        private System.Windows.Forms.CheckBox checkBox1;
        private System.Windows.Forms.NumericUpDown numericUpDownZ;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label labelOutputSize;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.NumericUpDown numericUpDownXY;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Button buttonCreateStl;
    }
}

