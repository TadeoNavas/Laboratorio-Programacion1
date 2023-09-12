namespace TP1
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
            tbName = new TextBox();
            tbMonto = new TextBox();
            btEfectivo = new Button();
            lbTarjeta = new Button();
            lbProvi = new Label();
            btAdd = new Button();
            lbLista = new Label();
            label1 = new Label();
            label2 = new Label();
            SuspendLayout();
            // 
            // tbName
            // 
            tbName.Location = new Point(12, 38);
            tbName.Name = "tbName";
            tbName.Size = new Size(216, 23);
            tbName.TabIndex = 0;
            // 
            // tbMonto
            // 
            tbMonto.ImeMode = ImeMode.NoControl;
            tbMonto.Location = new Point(12, 77);
            tbMonto.Name = "tbMonto";
            tbMonto.Size = new Size(107, 23);
            tbMonto.TabIndex = 1;
            // 
            // btEfectivo
            // 
            btEfectivo.Location = new Point(12, 125);
            btEfectivo.Name = "btEfectivo";
            btEfectivo.Size = new Size(91, 23);
            btEfectivo.TabIndex = 2;
            btEfectivo.Text = "Efectivo -10%";
            btEfectivo.UseVisualStyleBackColor = true;
            btEfectivo.Click += btEfectivo_Click;
            // 
            // lbTarjeta
            // 
            lbTarjeta.Location = new Point(109, 125);
            lbTarjeta.Name = "lbTarjeta";
            lbTarjeta.Size = new Size(119, 23);
            lbTarjeta.TabIndex = 3;
            lbTarjeta.Text = "Crédito / Débito";
            lbTarjeta.UseVisualStyleBackColor = true;
            lbTarjeta.Click += lbTarjeta_Click;
            // 
            // lbProvi
            // 
            lbProvi.AutoSize = true;
            lbProvi.Location = new Point(292, 38);
            lbProvi.Name = "lbProvi";
            lbProvi.Size = new Size(0, 15);
            lbProvi.TabIndex = 4;
            // 
            // btAdd
            // 
            btAdd.Location = new Point(291, 125);
            btAdd.Name = "btAdd";
            btAdd.Size = new Size(75, 23);
            btAdd.TabIndex = 5;
            btAdd.Text = "Agregar";
            btAdd.UseVisualStyleBackColor = true;
            btAdd.Click += btAdd_Click;
            // 
            // lbLista
            // 
            lbLista.AutoSize = true;
            lbLista.Location = new Point(38, 211);
            lbLista.Name = "lbLista";
            lbLista.Size = new Size(0, 15);
            lbLista.TabIndex = 6;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Font = new Font("Segoe UI", 8F, FontStyle.Regular, GraphicsUnit.Point);
            label1.Location = new Point(12, 22);
            label1.Name = "label1";
            label1.Size = new Size(105, 13);
            label1.TabIndex = 7;
            label1.Text = "Nombre y Apellido:";
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Font = new Font("Segoe UI", 8F, FontStyle.Regular, GraphicsUnit.Point);
            label2.Location = new Point(12, 64);
            label2.Name = "label2";
            label2.Size = new Size(70, 13);
            label2.TabIndex = 8;
            label2.Text = "Monto en $:";
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(547, 450);
            Controls.Add(label2);
            Controls.Add(label1);
            Controls.Add(lbLista);
            Controls.Add(btAdd);
            Controls.Add(lbProvi);
            Controls.Add(lbTarjeta);
            Controls.Add(btEfectivo);
            Controls.Add(tbMonto);
            Controls.Add(tbName);
            Name = "Form1";
            Text = "Form1";
            Load += Form1_Load;
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private TextBox tbName;
        private TextBox tbMonto;
        private Button btEfectivo;
        private Button lbTarjeta;
        private Label lbProvi;
        private Button btAdd;
        private Label lbLista;
        private Label label1;
        private Label label2;
    }
}