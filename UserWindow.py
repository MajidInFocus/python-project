import tkinter as tk
from tkinter import ttk, messagebox

class UserWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("User Window")
        self.master.geometry("800x600")

        # Screen Block
        self.screen_frame = ttk.Frame(self.master)
        self.screen_frame.pack(pady=20)

        ttk.Label(self.screen_frame, text="Time", font=("Helvetica", 12, "bold")).grid(row=0, column=0, padx=10)
        ttk.Label(self.screen_frame, text="Seats Available", font=("Helvetica", 12, "bold")).grid(row=0, column=1, padx=10)

        self.display_screen()

        # Tool Block
        self.tool_frame = ttk.Frame(self.master)
        self.tool_frame.pack(pady=20)

        ttk.Label(self.tool_frame, text="Select Time", font=("Helvetica", 12)).grid(row=0, column=0, padx=10)
        ttk.Label(self.tool_frame, text="Select Return Time", font=("Helvetica", 12)).grid(row=0, column=2, padx=10)

        self.style = ttk.Style()
        self.style.configure("TButton", font=("Helvetica", 12))

        self.departure_time_var = tk.StringVar()
        self.return_time_var = tk.StringVar()

        departure_times = ["09:00", "11:00", "13:00", "15:00"]
        return_times = ["10:00", "12:00", "14:00", "16:00"]

        self.departure_time_dropdown = ttk.Combobox(self.tool_frame, values=departure_times, textvariable=self.departure_time_var, state="readonly", font=("Helvetica", 12))
        self.departure_time_dropdown.grid(row=1, column=0, padx=10)

        self.return_time_dropdown = ttk.Combobox(self.tool_frame, values=return_times, textvariable=self.return_time_var, state="readonly", font=("Helvetica", 12))
        self.return_time_dropdown.grid(row=1, column=2, padx=10)

        ttk.Label(self.tool_frame, text="Number of Tickets", font=("Helvetica", 12)).grid(row=2, column=0, padx=10)
        self.tickets_entry = ttk.Entry(self.tool_frame, font=("Helvetica", 12))
        self.tickets_entry.grid(row=2, column=1, padx=10)

        ttk.Button(self.tool_frame, text="Calculate", command=self.calculate_fees, style="TButton").grid(row=2, column=2, padx=10)
        ttk.Button(self.tool_frame, text="Clear", command=self.clear_info, style="TButton").grid(row=2, column=3, padx=10)

        ttk.Label(self.tool_frame, text="Fees", font=("Helvetica", 12)).grid(row=3, column=0, padx=10)
        self.fees_label = ttk.Label(self.tool_frame, text="", font=("Helvetica", 12))
        self.fees_label.grid(row=3, column=1, padx=10)

        ttk.Label(self.tool_frame, text="Payment Option", font=("Helvetica", 12)).grid(row=4, column=0, padx=10)
        self.payment_option_var = tk.StringVar()
        self.payment_option_dropdown = ttk.Combobox(self.tool_frame, values=["Cash", "Online"], textvariable=self.payment_option_var, state="readonly", font=("Helvetica", 12))
        self.payment_option_dropdown.grid(row=4, column=1, padx=10)

        ttk.Button(self.tool_frame, text="Proceed to Payment", command=self.proceed_to_payment, style="TButton").grid(row=4, column=2, padx=10)

        ttk.Button(self.tool_frame, text="Close Window", command=self.close_window, style="TButton").grid(row=5, columnspan=4, pady=10)

    def display_screen(self):
        # This is a placeholder. You should update this part based on your logic for displaying train times and seats availability.
        departure_times = ["09:00", "11:00", "13:00", "15:00"]
        return_times = ["10:00", "12:00", "14:00", "16:00"]
        departure_seats = [480, 480, 480, 480]
        return_seats = [480, 480, 480, 480]

        for i, (dep_time, dep_seat, ret_time, ret_seat) in enumerate(zip(departure_times, departure_seats, return_times, return_seats), start=1):
            ttk.Label(self.screen_frame, text=dep_time, font=("Helvetica", 12)).grid(row=i, column=0, padx=10)
            ttk.Label(self.screen_frame, text=str(dep_seat), font=("Helvetica", 12)).grid(row=i, column=1, padx=10)

            ttk.Label(self.screen_frame, text=ret_time, font=("Helvetica", 12)).grid(row=i+len(departure_times), column=0, padx=10)
            ttk.Label(self.screen_frame, text=str(ret_seat), font=("Helvetica", 12)).grid(row=i+len(departure_times), column=1, padx=10)

    def calculate_fees(self):
        # This is a placeholder. You should implement the actual logic for calculating fees based on the selected options.
        fees = 25.0  # Placeholder value
        self.fees_label.config(text=f"RM {fees:.2f}")

    def proceed_to_payment(self):
        # This is a placeholder. You should implement the actual logic for handling payments based on the selected payment option.
        payment_option = self.payment_option_var.get()
        if payment_option == "Cash":
            messagebox.showinfo("Payment", "Please pay at the counter.")
        elif payment_option == "Online":
            messagebox.showinfo("Payment", "Redirecting to online payment.")

    def clear_info(self):
        # Clear all input and output fields
        self.departure_time_var.set('')
        self.return_time_var.set('')
        self.tickets_entry.delete(0, tk.END)
        self.fees_label.config(text='')
        self.payment_option_var.set('')

    def close_window(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    app = UserWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
