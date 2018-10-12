namespace ProjectD
{
    partial class SystemConverter
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(SystemConverter));
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
            this.history.BackColor = System.Drawing.SystemColors.InactiveCaptionText;
            this.history.ForeColor = System.Drawing.SystemColors.Window;
            this.history.Location = new System.Drawing.Point(513, 311);
            this.history.Name = "history";
            this.history.Size = new System.Drawing.Size(263, 165);
            this.history.TabIndex = 0;
            this.history.Text = "";
            // 
            // textBoxOut
            // 
            this.textBoxOut.BackColor = System.Drawing.SystemColors.InactiveCaptionText;
            this.textBoxOut.ForeColor = System.Drawing.SystemColors.Window;
            this.textBoxOut.Location = new System.Drawing.Point(700, 216);
            this.textBoxOut.Name = "textBoxOut";
            this.textBoxOut.Size = new System.Drawing.Size(153, 20);
            this.textBoxOut.TabIndex = 1;
            // 
            // textBoxIn
            // 
            this.textBoxIn.BackColor = System.Drawing.SystemColors.InactiveCaptionText;
            this.textBoxIn.ForeColor = System.Drawing.SystemColors.Window;
            this.textBoxIn.Location = new System.Drawing.Point(431, 216);
            this.textBoxIn.Name = "textBoxIn";
            this.textBoxIn.Size = new System.Drawing.Size(153, 20);
            this.textBoxIn.TabIndex = 2;
            this.textBoxIn.TextChanged += new System.EventHandler(this.textBoxIn_TextChanged);
            // 
            // comboBoxIn
            // 
            this.comboBoxIn.BackColor = System.Drawing.SystemColors.InactiveCaptionText;
            this.comboBoxIn.ForeColor = System.Drawing.SystemColors.Window;
            this.comboBoxIn.FormattingEnabled = true;
            this.comboBoxIn.Items.AddRange(new object[] {
            "Двоичной",
            "Троичной",
            "Восьмеричной",
            "Десятичной",
            "Двенадцатиричной",
            "Шестнадцатеричной"});
            this.comboBoxIn.Location = new System.Drawing.Point(431, 143);
            this.comboBoxIn.Name = "comboBoxIn";
            this.comboBoxIn.Size = new System.Drawing.Size(153, 21);
            this.comboBoxIn.TabIndex = 4;
            this.comboBoxIn.SelectedIndexChanged += new System.EventHandler(this.comboBoxIn_SelectedIndexChanged);
            // 
            // comboBoxOut
            // 
            this.comboBoxOut.BackColor = System.Drawing.SystemColors.InactiveCaptionText;
            this.comboBoxOut.ForeColor = System.Drawing.SystemColors.Window;
            this.comboBoxOut.FormattingEnabled = true;
            this.comboBoxOut.Items.AddRange(new object[] {
            "Двоичную",
            "Троичную",
            "Восьмеричную",
            "Десятичную",
            "Двенадцатиричную",
            "Шестнадцатеричную"});
            this.comboBoxOut.Location = new System.Drawing.Point(700, 143);
            this.comboBoxOut.Name = "comboBoxOut";
            this.comboBoxOut.Size = new System.Drawing.Size(153, 21);
            this.comboBoxOut.TabIndex = 5;
            this.comboBoxOut.SelectedIndexChanged += new System.EventHandler(this.comboBoxOut_SelectedIndexChanged);
            // 
            // Swap
            // 
            this.Swap.BackColor = System.Drawing.SystemColors.Window;
            this.Swap.BackgroundImage = global::ProjectD.Properties.Resources.swap;
            this.Swap.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.Swap.Location = new System.Drawing.Point(619, 143);
            this.Swap.Name = "Swap";
            this.Swap.Size = new System.Drawing.Size(51, 39);
            this.Swap.TabIndex = 3;
            this.Swap.UseVisualStyleBackColor = false;
            this.Swap.Click += new System.EventHandler(this.Swap_Click);
            // 
            // convert
            // 
            this.convert.BackColor = System.Drawing.SystemColors.Desktop;
            this.convert.ForeColor = System.Drawing.SystemColors.Window;
            this.convert.Location = new System.Drawing.Point(592, 269);
            this.convert.Name = "convert";
            this.convert.Size = new System.Drawing.Size(98, 23);
            this.convert.TabIndex = 6;
            this.convert.Text = "Конвертировать";
            this.convert.UseVisualStyleBackColor = false;
            this.convert.Click += new System.EventHandler(this.convert_Click);
            // 
            // SystemConverter
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.Desktop;
            this.ClientSize = new System.Drawing.Size(1443, 805);
            this.Controls.Add(this.convert);
            this.Controls.Add(this.comboBoxOut);
            this.Controls.Add(this.comboBoxIn);
            this.Controls.Add(this.Swap);
            this.Controls.Add(this.textBoxIn);
            this.Controls.Add(this.textBoxOut);
            this.Controls.Add(this.history);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "SystemConverter";
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

