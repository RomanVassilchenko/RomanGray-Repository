using System;
using System.Windows.Forms;

namespace ProjectD
{
    public partial class SystemConverter : Form
    {
        public SystemConverter()
        {
            InitializeComponent();
        }

        private void comboBoxIn_SelectedIndexChanged( object sender, EventArgs e )
        {
        }

        private void textBoxIn_TextChanged( object sender, EventArgs e )
        {
        }

        private void convert_Click( object sender, EventArgs e )
        {
            string OutText = "", InText = "";
            if (comboBoxIn.SelectedIndex == 0) { InText = "Двоичное число"; }
            if (comboBoxIn.SelectedIndex == 1) { InText = "Троичное число"; }
            if (comboBoxIn.SelectedIndex == 2) { InText = "Восьмиричное число"; }
            if (comboBoxIn.SelectedIndex == 3) { InText = "Десятиричное число"; }
            if (comboBoxIn.SelectedIndex == 4) { InText = "Двенадцатиричное число"; }
            if (comboBoxIn.SelectedIndex == 5) { InText = "Шестнадцатиричное число"; }

            if (comboBoxOut.SelectedIndex == 0) { OutText = "Двоичное число"; }
            if (comboBoxOut.SelectedIndex == 1) { OutText = "Троичное число"; }
            if (comboBoxOut.SelectedIndex == 2) { OutText = "Восьмиричное число"; }
            if (comboBoxOut.SelectedIndex == 3) { OutText = "Десятиричное число"; }
            if (comboBoxOut.SelectedIndex == 4) { OutText = "Двенадцатиричное число"; }
            if (comboBoxOut.SelectedIndex == 5) { OutText = "Шестнадцатиричное число"; }
            //Двоичная
            if (comboBoxOut.SelectedIndex == 0)
            {
                if (comboBoxOut.SelectedIndex == 0)
                {
                    string Num = Convert.ToString(ToDecimal(textBoxIn.Text, 2));
                    string Final = ToNotDecimal(Num, 2);
                    textBoxOut.Text = "" + Final;
                    history.Text += (DateTime.Now + " " + InText + textBoxIn.Text + " перевелся в " + OutText + " " + Final + "\n");
                }
                if (comboBoxOut.SelectedIndex == 1)
                {
                    string Num = Convert.ToString(ToDecimal(textBoxIn.Text, 2));
                    string Final = ToNotDecimal(Num, 3);
                    textBoxOut.Text = "" + Final;
                    history.Text += (DateTime.Now + " " + InText + textBoxIn.Text + " перевелся в " + OutText + " " + Final + "\n");
                }
                if (comboBoxOut.SelectedIndex == 2)
                {
                    string Num = Convert.ToString(ToDecimal(textBoxIn.Text, 2));
                    string Final = ToNotDecimal(Num, 8);
                    textBoxOut.Text = "" + Final;
                    history.Text += (DateTime.Now + " " + InText + textBoxIn.Text + " перевелся в " + OutText + " " + Final + "\n");
                }
                if (comboBoxOut.SelectedIndex == 3)
                {
                    string Num = Convert.ToString(ToDecimal(textBoxIn.Text, 2));
                    textBoxOut.Text = "" + Num;
                    history.Text += (DateTime.Now + " " + InText + textBoxIn.Text + " перевелся в " + OutText + " " + Num + "\n");
                }
                if (comboBoxOut.SelectedIndex == 4)
                {
                    string Num = Convert.ToString(ToDecimal(textBoxIn.Text, 2));
                    string Final = ToNotDecimal(Num, 12);
                    textBoxOut.Text = "" + Final;
                    history.Text += (DateTime.Now + " " + InText + textBoxIn.Text + " перевелся в " + OutText + " " + Final + "\n");
                }
                if (comboBoxOut.SelectedIndex == 5)
                {
                    string Num = Convert.ToString(ToDecimal(textBoxIn.Text, 2));
                    string Final = ToNotDecimal(Num, 16);
                    textBoxOut.Text = "" + Final;
                    history.Text += (DateTime.Now + " " + InText + textBoxIn.Text + " перевелся в " + OutText + " " + Final + "\n");
                }
            }
            //Троичная
            if (comboBoxIn.SelectedIndex == 1)
            {
                if (comboBoxOut.SelectedIndex == 0)
                {
                    string Num = Convert.ToString(ToDecimal(textBoxIn.Text, 3));
                    string Final = ToNotDecimal(Num, 2);
                    textBoxOut.Text = "" + Final;
                    history.Text += (DateTime.Now + " " + InText + textBoxIn.Text + " перевелся в " + OutText + " " + Final + "\n");
                }
                if (comboBoxOut.SelectedIndex == 1)
                {
                    string Num = Convert.ToString(ToDecimal(textBoxIn.Text, 3));
                    string Final = ToNotDecimal(Num, 3);
                    textBoxOut.Text = "" + Final;
                    history.Text += (DateTime.Now + " " + InText + textBoxIn.Text + " перевелся в " + OutText + " " + Final + "\n");
                }
                if (comboBoxOut.SelectedIndex == 2)
                {
                    string Num = Convert.ToString(ToDecimal(textBoxIn.Text, 3));
                    string Final = ToNotDecimal(Num, 8);
                    textBoxOut.Text = "" + Final;
                    history.Text += (DateTime.Now + " " + InText + textBoxIn.Text + " перевелся в " + OutText + " " + Final + "\n");
                }
                if (comboBoxOut.SelectedIndex == 3)
                {
                    string Num = Convert.ToString(ToDecimal(textBoxIn.Text, 3));
                    textBoxOut.Text = "" + Num;
                    history.Text += (DateTime.Now + " " + InText + textBoxIn.Text + " перевелся в " + OutText + " " + Num + "\n");
                }
                if (comboBoxOut.SelectedIndex == 4)
                {
                    string Num = Convert.ToString(ToDecimal(textBoxIn.Text, 3));
                    string Final = ToNotDecimal(Num, 12);
                    textBoxOut.Text = "" + Final;
                    history.Text += (DateTime.Now + " " + InText + textBoxIn.Text + " перевелся в " + OutText + " " + Final + "\n");
                }
                if (comboBoxOut.SelectedIndex == 5)
                {
                    string Num = Convert.ToString(ToDecimal(textBoxIn.Text, 3));
                    string Final = ToNotDecimal(Num, 16);
                    textBoxOut.Text = "" + Final;
                    history.Text += (DateTime.Now + " " + InText + textBoxIn.Text + " перевелся в " + OutText + " " + Final + "\n");
                }
            }
            //Восьмеричная
            if (comboBoxIn.SelectedIndex == 2)
            {
                if (comboBoxOut.SelectedIndex == 0)
                {
                    string Num = Convert.ToString(ToDecimal(textBoxIn.Text, 8));
                    string Final = ToNotDecimal(Num, 2);
                    textBoxOut.Text = "" + Final;
                    history.Text += (DateTime.Now + " " + InText + textBoxIn.Text + " перевелся в " + OutText + " " + Final + "\n");
                }
                if (comboBoxOut.SelectedIndex == 1)
                {
                    string Num = Convert.ToString(ToDecimal(textBoxIn.Text, 8));
                    string Final = ToNotDecimal(Num, 3);
                    textBoxOut.Text = "" + Final;
                    history.Text += (DateTime.Now + " " + InText + textBoxIn.Text + " перевелся в " + OutText + " " + Final + "\n");
                }
                if (comboBoxOut.SelectedIndex == 2)
                {
                    string Num = Convert.ToString(ToDecimal(textBoxIn.Text, 8));
                    string Final = ToNotDecimal(Num, 8);
                    textBoxOut.Text = "" + Final;
                    history.Text += (DateTime.Now + " " + InText + textBoxIn.Text + " перевелся в " + OutText + " " + Final + "\n");
                }
                if (comboBoxOut.SelectedIndex == 3)
                {
                    string Num = Convert.ToString(ToDecimal(textBoxIn.Text, 8));
                    textBoxOut.Text = "" + Num;
                    history.Text += (DateTime.Now + " " + InText + textBoxIn.Text + " перевелся в " + OutText + " " + Num + "\n");
                }
                if (comboBoxOut.SelectedIndex == 4)
                {
                    string Num = Convert.ToString(ToDecimal(textBoxIn.Text, 8));
                    string Final = ToNotDecimal(Num, 12);
                    textBoxOut.Text = "" + Final;
                    history.Text += (DateTime.Now + " " + InText + textBoxIn.Text + " перевелся в " + OutText + " " + Final + "\n");
                }
                if (comboBoxOut.SelectedIndex == 5)
                {
                    string Num = Convert.ToString(ToDecimal(textBoxIn.Text, 8));
                    string Final = ToNotDecimal(Num, 16);
                    textBoxOut.Text = "" + Final;
                    history.Text += (DateTime.Now + " " + InText + textBoxIn.Text + " перевелся в " + OutText + " " + Final + "\n");
                }
            }
            //Десятиричная
            if (comboBoxIn.SelectedIndex == 3)
            {
                if (comboBoxOut.SelectedIndex == 0)
                {
                    string Num = Convert.ToString(ToDecimal(textBoxIn.Text, 10));
                    string Final = ToNotDecimal(Num, 2);
                    textBoxOut.Text = "" + Final;
                    history.Text += (DateTime.Now + " " + InText + textBoxIn.Text + " перевелся в " + OutText + " " + Final + "\n");
                }
                if (comboBoxOut.SelectedIndex == 1)
                {
                    string Num = Convert.ToString(ToDecimal(textBoxIn.Text, 10));
                    string Final = ToNotDecimal(Num, 3);
                    textBoxOut.Text = "" + Final;
                    history.Text += (DateTime.Now + " " + InText + textBoxIn.Text + " перевелся в " + OutText + " " + Final + "\n");
                }
                if (comboBoxOut.SelectedIndex == 2)
                {
                    string Num = Convert.ToString(ToDecimal(textBoxIn.Text, 10));
                    string Final = ToNotDecimal(Num, 8);
                    textBoxOut.Text = "" + Final;
                    history.Text += (DateTime.Now + " " + InText + textBoxIn.Text + " перевелся в " + OutText + " " + Final + "\n");
                }
                if (comboBoxOut.SelectedIndex == 3)
                {
                    textBoxOut.Text = "" + textBoxIn.Text;
                    history.Text += (DateTime.Now + " " + InText + textBoxIn.Text + " перевелся в " + OutText + " " + textBoxIn.Text + "\n");
                }
                if (comboBoxOut.SelectedIndex == 4)
                {
                    string Num = Convert.ToString(ToDecimal(textBoxIn.Text, 10));
                    string Final = ToNotDecimal(Num, 12);
                    textBoxOut.Text = "" + Final;
                    history.Text += (DateTime.Now + " " + InText + textBoxIn.Text + " перевелся в " + OutText + " " + Final + "\n");
                }
                if (comboBoxOut.SelectedIndex == 5)
                {
                    string Num = Convert.ToString(ToDecimal(textBoxIn.Text, 10));
                    string Final = ToNotDecimal(Num, 16);
                    textBoxOut.Text = "" + Final;
                    history.Text += (DateTime.Now + " " + InText + textBoxIn.Text + " перевелся в " + OutText + " " + Final + "\n");
                }
            }
            //Двенадцатиричная
            if (comboBoxIn.SelectedIndex == 4)
            {
                if (comboBoxOut.SelectedIndex == 0)
                {
                    string Num = Convert.ToString(ToDecimal(textBoxIn.Text, 12));
                    string Final = ToNotDecimal(Num, 2);
                    textBoxOut.Text = "" + Final;
                    history.Text += (DateTime.Now + " " + InText + textBoxIn.Text + " перевелся в " + OutText + " " + Final + "\n");
                }
                if (comboBoxOut.SelectedIndex == 1)
                {
                    string Num = Convert.ToString(ToDecimal(textBoxIn.Text, 12));
                    string Final = ToNotDecimal(Num, 3);
                    textBoxOut.Text = "" + Final;
                    history.Text += (DateTime.Now + " " + InText + textBoxIn.Text + " перевелся в " + OutText + " " + Final + "\n");
                }
                if (comboBoxOut.SelectedIndex == 2)
                {
                    string Num = Convert.ToString(ToDecimal(textBoxIn.Text, 12));
                    string Final = ToNotDecimal(Num, 8);
                    textBoxOut.Text = "" + Final;
                    history.Text += (DateTime.Now + " " + InText + textBoxIn.Text + " перевелся в " + OutText + " " + Final + "\n");
                }
                if (comboBoxOut.SelectedIndex == 3)
                {
                    string Num = Convert.ToString(ToDecimal(textBoxIn.Text, 12));
                    textBoxOut.Text = "" + Num;
                    history.Text += (DateTime.Now + " " + InText + textBoxIn.Text + " перевелся в " + OutText + " " + Num + "\n");
                }
                if (comboBoxOut.SelectedIndex == 4)
                {
                    string Num = Convert.ToString(ToDecimal(textBoxIn.Text, 12));
                    string Final = ToNotDecimal(Num, 12);
                    textBoxOut.Text = "" + Final;
                    history.Text += (DateTime.Now + " " + InText + textBoxIn.Text + " перевелся в " + OutText + " " + Final + "\n");
                }
                if (comboBoxOut.SelectedIndex == 5)
                {
                    string Num = Convert.ToString(ToDecimal(textBoxIn.Text, 12));
                    string Final = ToNotDecimal(Num, 16);
                    textBoxOut.Text = "" + Final;
                    history.Text += (DateTime.Now + " " + InText + textBoxIn.Text + " перевелся в " + OutText + " " + Final + "\n");
                }
            }
            //Шестнадцатиричная
            if (comboBoxIn.SelectedIndex == 5)
            {
                if (comboBoxOut.SelectedIndex == 0)
                {
                    string Num = Convert.ToString(ToDecimal(textBoxIn.Text, 16));
                    string Final = ToNotDecimal(Num, 2);
                    textBoxOut.Text = "" + Final;
                    history.Text += (DateTime.Now + " " + InText + textBoxIn.Text + " перевелся в " + OutText + " " + Final + "\n");
                }
                if (comboBoxOut.SelectedIndex == 1)
                {
                    string Num = Convert.ToString(ToDecimal(textBoxIn.Text, 16));
                    string Final = ToNotDecimal(Num, 3);
                    textBoxOut.Text = "" + Final;
                    history.Text += (DateTime.Now + " " + InText + textBoxIn.Text + " перевелся в " + OutText + " " + Final + "\n");
                }
                if (comboBoxOut.SelectedIndex == 2)
                {
                    string Num = Convert.ToString(ToDecimal(textBoxIn.Text, 16));
                    string Final = ToNotDecimal(Num, 8);
                    textBoxOut.Text = "" + Final;
                    history.Text += (DateTime.Now + " " + InText + textBoxIn.Text + " перевелся в " + OutText + " " + Final + "\n");
                }
                if (comboBoxOut.SelectedIndex == 3)
                {
                    string Num = Convert.ToString(ToDecimal(textBoxIn.Text, 16));
                    textBoxOut.Text = "" + Num;
                    history.Text += (DateTime.Now + " " + InText + textBoxIn.Text + " перевелся в " + OutText + " " + Num + "\n");
                }
                if (comboBoxOut.SelectedIndex == 4)
                {
                    string Num = Convert.ToString(ToDecimal(textBoxIn.Text, 16));
                    string Final = ToNotDecimal(Num, 12);
                    textBoxOut.Text = "" + Final;
                    history.Text += (DateTime.Now + " " + InText + textBoxIn.Text + " перевелся в " + OutText + " " + Final + "\n");
                }
                if (comboBoxOut.SelectedIndex == 5)
                {
                    string Num = Convert.ToString(ToDecimal(textBoxIn.Text, 16));
                    string Final = ToNotDecimal(Num, 16);
                    textBoxOut.Text = "" + Final;
                    history.Text += (DateTime.Now + " " + InText + textBoxIn.Text + " перевелся в " + OutText + " " + Final + "\n");
                }
            }
        }

        private string ToDecimal( string Number, int NumberSystem )
        {
            int Pow = textBoxIn.Text.Length - 1;
            double result = 0;
            for (int i = 0; i < Number.Length; i++)
            {
                if (Number[i] >= 65)
                {
                    int buffer = Number[i] - 'A' + 10;
                    int x = Convert.ToInt32(buffer.ToString());
                    result += x * Math.Pow(NumberSystem, Pow);
                    Pow--;
                }
                else
                {
                    int x = Convert.ToInt32(Number[i].ToString());
                    result += x * Math.Pow(NumberSystem, Pow);
                    Pow--;
                }
            }
            return Convert.ToString(result);
        }

        private string ToNotDecimal( string number, int NumberSystem )
        {
            string binarynum = "";
            int Number = Convert.ToInt32(number);
            while (Number != 0)
            {
                if (Number % NumberSystem <= 9) binarynum += Number % NumberSystem;
                else
                {
                    if (Number % Number == 10) binarynum += 'A';
                    if (Number % Number == 11) binarynum += 'B';
                    if (Number % Number == 12) binarynum += 'C';
                    if (Number % Number == 13) binarynum += 'D';
                    if (Number % Number == 14) binarynum += 'E';
                    if (Number % Number == 15) binarynum += 'F';
                }
                Number /= NumberSystem;
            }
            char[] inputarray = binarynum.ToCharArray();
            Array.Reverse(inputarray);
            binarynum = new string(inputarray);
            return binarynum;
        }

        private void Swap_Click( object sender, EventArgs e )
        {
            if (comboBoxIn.SelectedIndex != -1 || comboBoxOut.SelectedIndex != -1)
            {
                int buffer = comboBoxOut.SelectedIndex;
                comboBoxOut.SelectedIndex = comboBoxIn.SelectedIndex;
                comboBoxIn.SelectedIndex = buffer;
            }
        }

        private void comboBoxOut_SelectedIndexChanged( object sender, EventArgs e )
        {
        }
    }
}