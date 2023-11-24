namespace TpRecuperatorioLP
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            tbDesc = new TextBox();
            tbPrecio = new TextBox();
            listView1 = new ListView();
            Id = new ColumnHeader();
            Descripcion = new ColumnHeader();
            Precio = new ColumnHeader();
            btAgregar = new Button();
            btModificar = new Button();
            label1 = new Label();
            tbId = new TextBox();
            btEliminar = new Button();
            SuspendLayout();
            // 
            // tbDesc
            // 
            tbDesc.Location = new Point(12, 57);
            tbDesc.Name = "tbDesc";
            tbDesc.PlaceholderText = "Descripcion";
            tbDesc.Size = new Size(168, 23);
            tbDesc.TabIndex = 0;
            // 
            // tbPrecio
            // 
            tbPrecio.Location = new Point(12, 106);
            tbPrecio.Name = "tbPrecio";
            tbPrecio.PlaceholderText = "Precio en $";
            tbPrecio.Size = new Size(100, 23);
            tbPrecio.TabIndex = 1;
            // 
            // listView1
            // 
            listView1.Columns.AddRange(new ColumnHeader[] { Id, Descripcion, Precio });
            listView1.Location = new Point(400, 35);
            listView1.Name = "listView1";
            listView1.Size = new Size(388, 229);
            listView1.TabIndex = 2;
            listView1.UseCompatibleStateImageBehavior = false;
            listView1.View = View.Details;
            // 
            // Id
            // 
            Id.Text = "Id";
            // 
            // Descripcion
            // 
            Descripcion.Text = "Descripcion";
            Descripcion.Width = 150;
            // 
            // Precio
            // 
            Precio.Text = "Precio";
            Precio.Width = 100;
            // 
            // btAgregar
            // 
            btAgregar.Location = new Point(221, 74);
            btAgregar.Name = "btAgregar";
            btAgregar.Size = new Size(102, 39);
            btAgregar.TabIndex = 3;
            btAgregar.Text = "Agregar";
            btAgregar.UseVisualStyleBackColor = true;
            btAgregar.Click += btAgregar_Click;
            // 
            // btModificar
            // 
            btModificar.Location = new Point(158, 240);
            btModificar.Name = "btModificar";
            btModificar.Size = new Size(98, 44);
            btModificar.TabIndex = 4;
            btModificar.Text = "Modificar";
            btModificar.UseVisualStyleBackColor = true;
            btModificar.Click += btModificar_Click;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Font = new Font("Sitka Small", 9.75F, FontStyle.Regular, GraphicsUnit.Point);
            label1.Location = new Point(7, 180);
            label1.Name = "label1";
            label1.Size = new Size(316, 57);
            label1.TabIndex = 5;
            label1.Text = "Ingrese el Id del producto que desea modificar \r\ny escriba en los espacios superiores.\r\nO Elimínelo.\r\n";
            // 
            // tbId
            // 
            tbId.Location = new Point(12, 281);
            tbId.Name = "tbId";
            tbId.PlaceholderText = "Id";
            tbId.Size = new Size(100, 23);
            tbId.TabIndex = 6;
            // 
            // btEliminar
            // 
            btEliminar.Location = new Point(158, 305);
            btEliminar.Name = "btEliminar";
            btEliminar.Size = new Size(98, 43);
            btEliminar.TabIndex = 7;
            btEliminar.Text = "Eliminar";
            btEliminar.UseVisualStyleBackColor = true;
            btEliminar.Click += btEliminar_Click;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(btEliminar);
            Controls.Add(tbId);
            Controls.Add(label1);
            Controls.Add(btModificar);
            Controls.Add(btAgregar);
            Controls.Add(listView1);
            Controls.Add(tbPrecio);
            Controls.Add(tbDesc);
            Name = "Form1";
            Text = "Form1";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private TextBox tbDesc;
        private TextBox tbPrecio;
        private ListView listView1;
        private Button btAgregar;
        private ColumnHeader Id;
        private ColumnHeader Descripcion;
        private ColumnHeader Precio;
        private Button btModificar;
        private Label label1;
        private TextBox tbId;
        private Button btEliminar;
    }
}