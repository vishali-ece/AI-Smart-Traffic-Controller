import tkinter as tk
import random
import matplotlib.pyplot as plt

# ---- Settings ----
LANES = ["North", "South", "East", "West"]
FIXED_GREEN_TIME = 30  # seconds (fixed timer simulation)

# ---- AI Controller ----
def ai_green_time(vehicle_count):
    # More vehicles = more green time (10 to 60 seconds)
    return max(10, min(60, vehicle_count * 3))

# ---- Simulation Data ----
fixed_wait_times = []
ai_wait_times = []

def simulate():
    result_text.delete(1.0, tk.END)
    fixed_wait_times.clear()
    ai_wait_times.clear()

    for lane in LANES:
        count = random.randint(5, 20)  # random vehicles
        
        fixed_time = FIXED_GREEN_TIME
        ai_time = ai_green_time(count)
        
        fixed_wait = max(0, (count * 2) - fixed_time)
        ai_wait = max(0, (count * 2) - ai_time)
        
        fixed_wait_times.append(fixed_wait)
        ai_wait_times.append(ai_wait)
        
        result_text.insert(tk.END, f"{lane} Lane:\n")
        result_text.insert(tk.END, f"  Vehicles: {count}\n")
        result_text.insert(tk.END, f"  Fixed Timer Wait: {fixed_wait}s\n")
        result_text.insert(tk.END, f"  AI Timer Wait:    {ai_wait}s\n\n")

def show_graph():
    plt.figure(figsize=(8, 5))
    x = range(len(LANES))
    plt.bar([i - 0.2 for i in x], fixed_wait_times, width=0.4, label='Fixed Timer', color='red')
    plt.bar([i + 0.2 for i in x], ai_wait_times, width=0.4, label='AI Controller', color='green')
    plt.xticks(list(x), LANES)
    plt.ylabel("Wait Time (seconds)")
    plt.title("AI vs Fixed Timer - Traffic Wait Time Comparison")
    plt.legend()
    plt.tight_layout()
    plt.show()

# ---- UI ----
root = tk.Tk()
root.title("AI Smart Traffic Controller")
root.geometry("500x500")
root.configure(bg="#1a1a2e")

tk.Label(root, text="🚦 AI Smart Traffic Controller", font=("Arial", 16, "bold"),
         bg="#1a1a2e", fg="white").pack(pady=10)

tk.Button(root, text="Run Simulation", command=simulate,
          bg="#e94560", fg="white", font=("Arial", 12), padx=10, pady=5).pack(pady=5)

tk.Button(root, text="Show Graph", command=show_graph,
          bg="#0f3460", fg="white", font=("Arial", 12), padx=10, pady=5).pack(pady=5)

result_text = tk.Text(root, height=15, width=55, bg="#16213e", fg="#00ff88",
                      font=("Courier", 10))
result_text.pack(pady=10)

root.mainloop()
