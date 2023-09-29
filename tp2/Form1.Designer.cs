using System.Drawing;

namespace tp2
{
    partial class Form1
    {
        /// <summary>
        /// Variable del diseñador necesaria.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Limpiar los recursos que se estén usando.
        /// </summary>
        /// <param name="disposing">true si los recursos administrados se deben desechar; false en caso contrario.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Código generado por el Diseñador de Windows Forms

   

        private void InitializeComponent()
        {
            this.btBarajar = new System.Windows.Forms.Button();
            this.btSalir = new System.Windows.Forms.Button();
            this.lbCartas = new System.Windows.Forms.Label();
            this.lbMano = new System.Windows.Forms.Label();
            this.SuspendLayout();
          

            this.btBarajar.BackColor = System.Drawing.Color.Gold;
            this.btBarajar.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btBarajar.ForeColor = System.Drawing.Color.DarkGreen;
            this.btBarajar.Location = new System.Drawing.Point(0, 12);
            this.btBarajar.Name = "Mezclar_btn";
            this.btBarajar.Size = new System.Drawing.Size(106, 29);
            this.btBarajar.TabIndex = 0;
            this.btBarajar.Text = "Barajar";
            this.btBarajar.UseVisualStyleBackColor = false;
            this.btBarajar.Click += new System.EventHandler(this.Mezclar_btn_Click);
           

            this.btSalir.BackColor = System.Drawing.Color.Red;
            this.btSalir.FlatAppearance.BorderColor = System.Drawing.Color.White;
            this.btSalir.FlatAppearance.BorderSize = 0;
            this.btSalir.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btSalir.ForeColor = System.Drawing.Color.White;
            this.btSalir.Location = new System.Drawing.Point(215, 233);
            this.btSalir.Name = "Salir_btn";
            this.btSalir.Size = new System.Drawing.Size(75, 23);
            this.btSalir.TabIndex = 1;
            this.btSalir.Text = "Salir";
            this.btSalir.UseVisualStyleBackColor = false;
            this.btSalir.Click += new System.EventHandler(this.Salir_btn_Click);
            

            this.lbCartas.AutoSize = true;
            this.lbCartas.ForeColor = System.Drawing.Color.White;
            this.lbCartas.Location = new System.Drawing.Point(119, 73);
            this.lbCartas.Name = "label2";
            this.lbCartas.Size = new System.Drawing.Size(52, 13);
            this.lbCartas.TabIndex = 2;
            this.lbCartas.Text = "Tu mano:";
            this.lbCartas.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
         

            this.lbMano.AutoSize = true;
            this.lbMano.ForeColor = System.Drawing.Color.White;
            this.lbMano.Location = new System.Drawing.Point(63, 103);
            this.lbMano.Name = "Cartas_lbl";
            this.lbMano.Size = new System.Drawing.Size(0, 13);
            this.lbMano.TabIndex = 3;
            this.lbMano.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
         

            this.BackColor = System.Drawing.Color.Green;
            this.ClientSize = new System.Drawing.Size(302, 259);
            this.Controls.Add(this.lbMano);
            this.Controls.Add(this.lbCartas);
            this.Controls.Add(this.btSalir);
            this.Controls.Add(this.btBarajar);
            this.Name = "Form1";
            this.Text = "Baraja de Cartas";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label lblCartas;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button btBarajar;
        private System.Windows.Forms.Button btSalir;
        private System.Windows.Forms.Label lbCartas;
        private System.Windows.Forms.Label lbMano;
    }
}

