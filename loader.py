import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox

def load_svi_csv():
    input_path = filedialog.askopenfilename(
        title="Select SVI file",
        filetypes=[("CSV files", "*.csv")]
    )

    if not input_path:
        return
    
    try:
        # Load the data first to ensure it works
        # We store it in 'root' so other functions can access it
        root.svi_df = pd.read_csv(input_path)
        root.svi_path = input_path
        
        # Now change the button appearance
        svi_btn.config(bg="green", fg="white", text="SVI File Uploaded!")
        messagebox.showinfo("Success", f"File loaded successfully:\n{input_path}")
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


def load_vetClinics_csv():
    input_path = filedialog.askopenfilename(
        title="Select Vet Clinics CSV file",
        filetypes=[("CSV files", "*.csv")]
    )

    if not input_path:
        return
    
    try:
        root.vetClinics_df = pd.read_csv(input_path)
        root.vetClinics_path = input_path
        
        # Change the button appearance
        vetClinics_btn.config(bg="green", fg="white", text="Vet Clinics File Uploaded!")
        messagebox.showinfo("Success", f"File loaded successfully:\n{input_path}")
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


def process_csv():
    # Check if the SVI file was uploaded first
    if not hasattr(root, 'svi_df'):
        messagebox.showwarning("Warning", "Please upload the SVI file first!")
        return
    
    if not hasattr(root, 'vetClinics_df'):
        messagebox.showwarning("Warning", "Please upload the Vet Clinics CSV file first!")
        return

    # 1. Open File Dialog for the main data
    input_path = filedialog.askopenfilename(
        title="Select Main CSV file to Process",
        filetypes=[("CSV files", "*.csv")]
    )
    
    if not input_path:
        return

    try:
        main_df = pd.read_csv(input_path)
        
        # PROCESSING STEP:
        # Now you can use BOTH main_df and root.svi_df!
        # Example: main_df['svi_count'] = len(root.svi_df) 
        
        output_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv")],
            title="Save processed file as"
        )
        
        if output_path:
            main_df.to_csv(output_path, index=False)
            messagebox.showinfo("Success", "Processing complete and file saved.")
            
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Setup simple GUI
root = tk.Tk()
root.title("CSV Processor")
root.geometry("400x250") # Slightly larger to fit buttons comfortably

svi_btn = tk.Button(root, text="Upload SVI file", command=load_svi_csv, pady=10)
svi_btn.pack(pady=10, fill='x', padx=50)

vetClinics_btn = tk.Button(root, text="Upload Vet Clinics CSV", command = load_vetClinics_csv, pady=10)
vetClinics_btn.pack(pady=10, fill='x', padx=50)

btn = tk.Button(root, text="Upload & Process Main CSV", command=process_csv, pady=10)
btn.pack(pady=10, fill='x', padx=50)

root.mainloop()