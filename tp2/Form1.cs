using System;
using System.Windows.Forms;

namespace tp2
{
    public partial class Form1 : Form
    {
        private string[] numeros = { "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12" };
        private string[] palos = { "Copa", "Basto", "Espada", "Oro" };
        private Random random = new Random();
        public Form1()
        {
            InitializeComponent();
        }

        private void Mezclar_btn_Click(object sender, EventArgs e)
        {
            string carta1 = Barajar();
            string carta2 = Barajar();
            string carta3 = Barajar();

            lbMano.Text = carta1 + " | " + carta2 + " | " + carta3;
        }
        private string Barajar()
        {
            string numero = numeros[random.Next(numeros.Length)];
            string palo = palos[random.Next(palos.Length)];

            return (numero+" de "+palo);
        }

        private void Salir_btn_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
