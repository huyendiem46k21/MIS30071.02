using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Dự_án_có_102
{
    public partial class Fbangbaocao : Form
    {
        public Fbangbaocao()
        {
            InitializeComponent();
        }

        private void label9_Click(object sender, EventArgs e)
        {

        }

        private void pictureBox3_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {

            Fthongbao f = new Fthongbao();
            f.Show();
        }

        private void button2_Click(object sender, EventArgs e)
        {

            Ftrangchu f = new Ftrangchu();
            f.Show();
        }

        private void bt_thoat_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Bạn có chắc muốn thoát không?",
                 "Error", MessageBoxButtons.YesNoCancel);
            this.Close();
        }
    }
}
