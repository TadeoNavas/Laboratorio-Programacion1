using System.Security.Cryptography;

namespace TP1
{
    public partial class Form1 : Form
    {
        string aux;
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void btEfectivo_Click(object sender, EventArgs e)
        {
            try
            {
                validarCampos();

                var nuevoMonto = (double.Parse(tbMonto.Text) / 1.1).ToString("0.00");

                lbProvi.Text = $"Nombre: {tbName.Text} - Monto: ${nuevoMonto}";
            }
            catch
            {
                MessageBox.Show("Debe completar ambos campos antes de continuar");
            }
        }

        private void lbTarjeta_Click(object sender, EventArgs e)
        {
            try
            {
                validarCampos();

                var monto = float.Parse(tbMonto.Text).ToString("0.00");

                lbProvi.Text = $"Nombre: {tbName.Text} - Monto: ${monto}";
            }
            catch 
            {
                MessageBox.Show("Debe completar ambos campos antes de continuar");
            }
        }

        private void btAdd_Click(object sender, EventArgs e)
        {

            if (!string.IsNullOrEmpty(lbProvi.Text))
            {
                if (string.IsNullOrEmpty(lbLista.Text))
                {
                    lbLista.Text = lbProvi.Text;
                    vaciar();
                }
                else
                {
                    lbLista.Text = lbLista.Text + "\n" + lbProvi.Text;
                    vaciar();
                }
            }
            else 
            {
                MessageBox.Show("Debe completar ambos campos antes de continuar");
            }

        }
        private void vaciar() 
        {
            lbProvi.Text = "";
            tbName.Text = "";
            tbMonto.Text = "";
        }
        private void validarCampos() 
        {
            if (string.IsNullOrEmpty(tbMonto.Text) || string.IsNullOrEmpty(tbName.Text)) 
            {                
                throw new Exception();
            }
        }
    }
}

//12) Formulario de registro de pago: 2 TextBox(1 que permita ingresar un monto y otro el nombre) y 2 Botones (en efectivo y con tarjeta).
//    Al presionar en efectivo debe tener un descuento del 10%, con tarjeta el precio de lista.
//Esto se ve en una label provisoria. Debe haber otro boton que diga agregar que debe agregar en otra Label (junto con las cargadas anteriormente) y vaciar la label provisoria donde esta el calculo.