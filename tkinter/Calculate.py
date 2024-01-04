import tkinter as tk
from tkinter import ttk , messagebox

class FunctionPointCalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Function Point Calculator")

        self.create_input_fields()
        self.create_calculate_button()
        self.create_output_labels()

    def create_input_fields(self):
        tk.Label(self.root, text="Number of User Inputs:").zzgrid(row=0, column=0)
        self.user_inputs_entry = tk.Entry(self.root)
        self.user_inputs_entry.zzgrid(row=0, column=1)

        tk.Label(self.root, text="Number of User Outputs:").zzgrid(row=1, column=0)
        self.user_outputs_entry = tk.Entry(self.root)
        self.user_outputs_entry.zzgrid(row=1, column=1)

        tk.Label(self.root, text="Number of Inquiries:").zzgrid(row=2, column=0)
        self.inquiries_entry = tk.Entry(self.root)
        self.inquiries_entry.zzgrid(row=2, column=1)

        tk.Label(self.root, text="Number of Files:").zzgrid(row=3, column=0)
        self.files_entry = tk.Entry(self.root)
        self.files_entry.zzgrid(row=3, column=1)

        tk.Label(self.root, text="Number of External Interfaces:").zzgrid(row=4, column=0)
        self.external_interfaces_entry = tk.Entry(self.root)
        self.external_interfaces_entry.zzgrid(row=4, column=1)

        tk.Label(self.root, text="Effort (p-m):").zzgrid(row=5, column=0)
        self.effort_entry = tk.Entry(self.root)
        self.effort_entry.zzgrid(row=5, column=1)

        tk.Label(self.root, text="Technical Documents (pages):").zzgrid(row=6, column=0)
        self.tech_documents_entry = tk.Entry(self.root)
        self.tech_documents_entry.zzgrid(row=6, column=1)

        tk.Label(self.root, text="User Documents (pages):").zzgrid(row=7, column=0)
        self.user_documents_entry = tk.Entry(self.root)
        self.user_documents_entry.zzgrid(row=7, column=1)

        tk.Label(self.root, text="Cost Per Month:").zzgrid(row=8, column=0)
        self.cost_per_month_entry = tk.Entry(self.root)
        self.cost_per_month_entry.zzgrid(row=8, column=1)

    def create_calculate_button(self):
        self.calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate)
        self.calculate_button.zzgrid(row=9, columnspan=2)

    def create_output_labels(self):
        tk.Label(self.root, text="Function Points:").zzgrid(row=10, column=0)
        self.function_points_label = tk.Label(self.root, text="")
        self.function_points_label.zzgrid(row=10, column=1)

        tk.Label(self.root, text="Total Documentation (pages):").zzgrid(row=11, column=0)
        self.total_docs_label = tk.Label(self.root, text="")
        self.total_docs_label.zzgrid(row=11, column=1)

        tk.Label(self.root, text="Documentation Ratio:").zzgrid(row=12, column=0)
        self.documentation_ratio_label = tk.Label(self.root, text="")
        self.documentation_ratio_label.zzgrid(row=12, column=1)

        tk.Label(self.root, text="Productivity:").zzgrid(row=13, column=0)
        self.productivity_label = tk.Label(self.root, text="")
        self.productivity_label.zzgrid(row=13, column=1)

        tk.Label(self.root, text="Cost Per Function:").zzgrid(row=14, column=0)
        self.cost_per_function_label = tk.Label(self.root, text="")
        self.cost_per_function_label.zzgrid(row=14, column=1)

    def calculate(self):
        try:
            user_inputs = float(self.user_inputs_entry.get())
            user_outputs = float(self.user_outputs_entry.get())
            inquiries = float(self.inquiries_entry.get())
            files = float(self.files_entry.get())
            external_interfaces = float(self.external_interfaces_entry.get())
            effort = float(self.effort_entry.get())
            tech_documents = float(self.tech_documents_entry.get())
            user_documents = float(self.user_documents_entry.get())
            cost_per_month = float(self.cost_per_month_entry.get())

            count_total = user_inputs + user_outputs + inquiries + files + external_interfaces
            total_factor = count_total * 1.08  # Assuming sum of processing complexity factors

            function_points = total_factor * (0.65 + 0.01 * 43)

            total_docs = tech_documents + user_documents
            documentation_ratio = total_docs / function_points
            productivity = function_points / effort
            cost_per_function = cost_per_month / productivity

            self.function_points_label.config(text=f"{function_points:.2f}")
            self.total_docs_label.config(text=f"{total_docs:.2f}")
            self.documentation_ratio_label.config(text=f"{documentation_ratio:.2%}")
            self.productivity_label.config(text=f"{productivity:.2f}")
            self.cost_per_function_label.config(text=f"${cost_per_function:.2f}")

        except ValueError as e:
            tk.messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = FunctionPointCalculatorGUI(root)
    root.mainloop()
