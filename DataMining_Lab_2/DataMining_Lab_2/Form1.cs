using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace DataMining_Lab_2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void OpenFileDialogButton_Click(object sender, EventArgs e)
        {
            if (openFileDialog.ShowDialog(this) == DialogResult.OK)
            {
                filePassTextBox.Text = openFileDialog.FileName;
            }
        }

        private void ClassifyButton_Click(object sender, EventArgs e)
        {
            string filepass = filePassTextBox.Text;
            string message = messageTextBox.Text.Replace('\"', ' ');
            if (filepass.Length == 0) {
                MessageBox.Show("The filepass wasn't brought in");
                return;
            }
            if (message.Length == 0) {
                MessageBox.Show("The message wasn't brought in");
                return;
            }/*
            System.Diagnostics.ProcessStartInfo procStartInfo =
                new System.Diagnostics.ProcessStartInfo("cmd", "/c " + command);
            procStartInfo.RedirectStandardOutput = true;
            procStartInfo.UseShellExecute = false;
            procStartInfo.CreateNoWindow = true;
            System.Diagnostics.Process proc = new System.Diagnostics.Process();
            proc.StartInfo = procStartInfo;
            proc.Start();
            string result = proc.StandardOutput.ReadToEnd();
            */
            try
            {
                // create the ProcessStartInfo using "cmd" as the program to be run,
                // and "/c " as the parameters.
                // Incidentally, /c tells cmd that we want it to execute the command that follows,
                // and then exit.
                string command = "py lab_2.py --file \"" + filepass + "\" --message \"" + message + "\"";
                System.Diagnostics.ProcessStartInfo procStartInfo =
                    new System.Diagnostics.ProcessStartInfo("cmd", "/c " + command);

                // The following commands are needed to redirect the standard output.
                // This means that it will be redirected to the Process.StandardOutput StreamReader.
                procStartInfo.RedirectStandardOutput = true;
                procStartInfo.UseShellExecute = false;
                // Do not create the black window.
                procStartInfo.CreateNoWindow = true;
                // Now we create a process, assign its ProcessStartInfo and start it
                System.Diagnostics.Process proc = new System.Diagnostics.Process();
                proc.StartInfo = procStartInfo;
                proc.Start();
                // Get the output into a string
                string hamResult = proc.StandardOutput.ReadLine();
                string spamResult = proc.StandardOutput.ReadLine();
                StringBuilder result = new StringBuilder();
                result.Append("ham = " + hamResult + "\nspam = " + spamResult + "\nresut: it is ");
                if (double.Parse(hamResult.Trim().Replace('.', ',')) > double.Parse(spamResult.Trim().Replace('.', ',')))
                {
                    result.Append("ham message");
                }
                else {
                    result.Append("spam message");
                }
                MessageBox.Show(result.ToString());
            }
            catch (Exception objException)
            {
                MessageBox.Show(objException.Message);
            }
        }
    }
}
