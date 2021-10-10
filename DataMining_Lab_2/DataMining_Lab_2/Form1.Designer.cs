
namespace DataMining_Lab_2
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
            this.filePassTextBox = new System.Windows.Forms.TextBox();
            this.messageTextBox = new System.Windows.Forms.TextBox();
            this.openFileDialog = new System.Windows.Forms.OpenFileDialog();
            this.openFileDialogButton = new System.Windows.Forms.Button();
            this.classifyButton = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // filePassTextBox
            // 
            this.filePassTextBox.Location = new System.Drawing.Point(24, 29);
            this.filePassTextBox.Name = "filePassTextBox";
            this.filePassTextBox.Size = new System.Drawing.Size(547, 27);
            this.filePassTextBox.TabIndex = 0;
            this.filePassTextBox.Text = "D:\\VisualStudioProjects\\DataMining_Lab_2\\DataMining_Lab_2\\bin\\Debug\\netcoreapp3.1" +
    "\\sms-spam-corpus.csv";
            // 
            // messageTextBox
            // 
            this.messageTextBox.Location = new System.Drawing.Point(24, 84);
            this.messageTextBox.Multiline = true;
            this.messageTextBox.Name = "messageTextBox";
            this.messageTextBox.ScrollBars = System.Windows.Forms.ScrollBars.Both;
            this.messageTextBox.Size = new System.Drawing.Size(750, 300);
            this.messageTextBox.TabIndex = 1;
            // 
            // openFileDialog
            // 
            this.openFileDialog.FileName = "openFileDialog1";
            this.openFileDialog.Filter = "CSV Files (*.csv)| *.csv";
            // 
            // openFileDialogButton
            // 
            this.openFileDialogButton.Location = new System.Drawing.Point(637, 27);
            this.openFileDialogButton.Name = "openFileDialogButton";
            this.openFileDialogButton.Size = new System.Drawing.Size(94, 29);
            this.openFileDialogButton.TabIndex = 2;
            this.openFileDialogButton.Text = "Select a file";
            this.openFileDialogButton.UseVisualStyleBackColor = true;
            this.openFileDialogButton.Click += new System.EventHandler(this.OpenFileDialogButton_Click);
            // 
            // classifyButton
            // 
            this.classifyButton.Location = new System.Drawing.Point(363, 409);
            this.classifyButton.Name = "classifyButton";
            this.classifyButton.Size = new System.Drawing.Size(94, 29);
            this.classifyButton.TabIndex = 3;
            this.classifyButton.Text = "Classify";
            this.classifyButton.UseVisualStyleBackColor = true;
            this.classifyButton.Click += new System.EventHandler(this.ClassifyButton_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.classifyButton);
            this.Controls.Add(this.openFileDialogButton);
            this.Controls.Add(this.messageTextBox);
            this.Controls.Add(this.filePassTextBox);
            this.Name = "Form1";
            this.Text = "Lab_2";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox filePassTextBox;
        private System.Windows.Forms.TextBox messageTextBox;
        private System.Windows.Forms.OpenFileDialog openFileDialog;
        private System.Windows.Forms.Button openFileDialogButton;
        private System.Windows.Forms.Button classifyButton;
    }
}

