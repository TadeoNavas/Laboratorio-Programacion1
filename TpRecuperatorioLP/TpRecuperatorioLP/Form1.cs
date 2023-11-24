namespace TpRecuperatorioLP
{
    public partial class Form1 : Form
    {
        public List<Producto> Productos = new List<Producto>();
        public Form1()
        {
            InitializeComponent();           
        }

        private void btAgregar_Click(object sender, EventArgs e)
        {
            try
            {
                var producto = new Producto();

                var descripcion = tbDesc.Text.ToString();
                var precio = tbPrecio.Text.ToString();
                int id;

                if (string.IsNullOrEmpty(descripcion)) throw new Exception();

                if (Productos.Count > 0)
                {
                    id = Productos.Last().Id + 1;
                }
                else
                {
                    id = 1;
                }
                producto.Id = id;
                producto.Descripcion = descripcion;
                producto.Precio = decimal.Parse(precio);
                Productos.Add(producto);

                ActualizarListView();
                Limpiar();
            }
            catch (Exception) 
            {
                MessageBox.Show("Ambos campos deben estar completados y en formatos validos", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void btModificar_Click(object sender, EventArgs e)
        {
            var id = Convert.ToInt32(tbId.Text.ToString());
            var nuevaDesc = tbDesc.Text.ToString();
            var nuevoPrecio = tbPrecio.Text.ToString();

            if (!string.IsNullOrEmpty(nuevaDesc))
                Productos.FirstOrDefault(x => x.Id == id).Descripcion = nuevaDesc;

            if (!string.IsNullOrEmpty(nuevoPrecio))
                Productos.FirstOrDefault(x => x.Id == id).Precio = decimal.Parse(nuevoPrecio);

            Limpiar();
            ActualizarListView();
        }

        private void btEliminar_Click(object sender, EventArgs e)
        {

            DialogResult result = MessageBox
             .Show("¿Desea borrar el producto?",
             "Confirmacion",
             MessageBoxButtons.OKCancel,
             MessageBoxIcon.Warning);
            if (result == DialogResult.OK)
            {
                var id = Convert.ToInt32(tbId.Text.ToString());
                Productos.RemoveAll(x => x.Id == id);
            }
            Limpiar();
            ActualizarListView();
        }

        private void ActualizarListView()
        {
            listView1.Items.Clear();

            foreach (Producto p in Productos)
            {
                ListViewItem item = new ListViewItem(p.Id.ToString());
                item.SubItems.Add(p.Descripcion);
                item.SubItems.Add(p.Precio.ToString("C"));
                listView1.Items.Add(item);
            }
        }


        private void Limpiar()
        {
            tbDesc.Text = string.Empty;
            tbPrecio.Text = string.Empty;
            tbId.Text = string.Empty;
        }


    }
}