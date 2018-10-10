namespace ProjectD
{
    partial class Form1
    {
        /// <summary>
        /// Обязательная переменная конструктора.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Освободить все используемые ресурсы.
        /// </summary>
        /// <param name="disposing">истинно, если управляемый ресурс должен быть удален; иначе ложно.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Код, автоматически созданный конструктором форм Windows

        /// <summary>
        /// Требуемый метод для поддержки конструктора — не изменяйте 
        /// содержимое этого метода с помощью редактора кода.
        /// </summary>
        private void InitializeComponent()
        {
            this.history = new System.Windows.Forms.RichTextBox();
            this.textBoxOut = new System.Windows.Forms.TextBox();
            this.textBoxIn = new System.Windows.Forms.TextBox();
            this.comboBoxIn = new System.Windows.Forms.ComboBox();
            this.comboBoxOut = new System.Windows.Forms.ComboBox();
            this.Swap = new System.Windows.Forms.Button();
            this.convert = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // history
            // 
            this.history.Location = new System.Drawing.Point(684, 383);
            this.history.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.history.Name = "history";
            this.history.Size = new System.Drawing.Size(349, 202);
            this.history.TabIndex = 0;
            this.history.Text = "";
            // 
            // textBoxOut
            // 
            this.textBoxOut.Location = new System.Drawing.Point(933, 196);
            this.textBoxOut.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.textBoxOut.Name = "textBoxOut";
            this.textBoxOut.Size = new System.Drawing.Size(203, 22);
            this.textBoxOut.TabIndex = 1;
            // 
            // textBoxIn
            // 
            this.textBoxIn.Location = new System.Drawing.Point(575, 196);
            this.textBoxIn.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.textBoxIn.Name = "textBoxIn";
            this.textBoxIn.Size = new System.Drawing.Size(203, 22);
            this.textBoxIn.TabIndex = 2;
            this.textBoxIn.TextChanged += new System.EventHandler(this.textBoxIn_TextChanged);
            // 
            // comboBoxIn
            // 
            this.comboBoxIn.FormattingEnabled = true;
            this.comboBoxIn.Items.AddRange(new object[] {
            "Двоичной",
            "Троичной",
            "Восьмеричной",
            "Десятичной",
            "Двенадцатиричной",
            "Шестнадцатеричной"});
            this.comboBoxIn.Location = new System.Drawing.Point(575, 106);
            this.comboBoxIn.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.comboBoxIn.Name = "comboBoxIn";
            this.comboBoxIn.Size = new System.Drawing.Size(203, 24);
            this.comboBoxIn.TabIndex = 4;
            this.comboBoxIn.SelectedIndexChanged += new System.EventHandler(this.comboBoxIn_SelectedIndexChanged);
            // 
            // comboBoxOut
            // 
            this.comboBoxOut.FormattingEnabled = true;
            this.comboBoxOut.Items.AddRange(new object[] {
            "Двоичную",
            "Троичную",
            "Восьмеричную",
            "Десятичную",
            "Двенадцатиричную",
            "Шестнадцатеричную"});
            this.comboBoxOut.Location = new System.Drawing.Point(933, 106);
            this.comboBoxOut.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.comboBoxOut.Name = "comboBoxOut";
            this.comboBoxOut.Size = new System.Drawing.Size(203, 24);
            this.comboBoxOut.TabIndex = 5;
            this.comboBoxOut.SelectedIndexChanged += new System.EventHandler(this.comboBoxOut_SelectedIndexChanged);
            // 
            // Swap
            // 
            this.Swap.BackgroundImage = global::ProjectD.Properties.Resources.swap;
            this.Swap.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.Swap.Location = new System.Drawing.Point(832, 94);
            this.Swap.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.Swap.Name = "Swap";
            this.Swap.Size = new System.Drawing.Size(68, 48);
            this.Swap.TabIndex = 3;
            this.Swap.UseVisualStyleBackColor = true;
            this.Swap.Click += new System.EventHandler(this.Swap_Click);
            // 
            // convert
            // 
            this.convert.Location = new System.Drawing.Point(799, 261);
            this.convert.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.convert.Name = "convert";
            this.convert.Size = new System.Drawing.Size(131, 28);
            this.convert.TabIndex = 6;
            this.convert.Text = "Конвертировать";
            this.convert.UseVisualStyleBackColor = true;
            this.convert.Click += new System.EventHandler(this.convert_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1924, 991);
            this.Controls.Add(this.convert);
            this.Controls.Add(this.comboBoxOut);
            this.Controls.Add(this.comboBoxIn);
            this.Controls.Add(this.Swap);
            this.Controls.Add(this.textBoxIn);
            this.Controls.Add(this.textBoxOut);
            this.Controls.Add(this.history);
            this.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.RichTextBox history;
        private System.Windows.Forms.TextBox textBoxOut;
        private System.Windows.Forms.TextBox textBoxIn;
        private System.Windows.Forms.Button Swap;
        private System.Windows.Forms.ComboBox comboBoxIn;
        private System.Windows.Forms.ComboBox comboBoxOut;
        private System.Windows.Forms.Button convert;
    }
}

