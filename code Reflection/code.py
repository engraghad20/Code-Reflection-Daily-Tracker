import tkinter as tk
from tkinter import ttk
import random
from datetime import date


root = tk.Tk()
root.title("Code Reflection — Daily Progress")
root.geometry("600x650")
root.config(bg="#E6F0FA")

# ======= الألوان =======
BG_COLOR = "#E6F0FA"
CARD_COLOR = "#FFFFFF"
TEXT_DARK = "#1F2937"
ACCENT = "#6366F1"
ACCENT_LIGHT = "#8B5CF6"
BUTTON_GRADIENT_1 = "#6366F1"
BUTTON_GRADIENT_2 = "#8B5CF6"

# ======= العبارات اليومية =======
messages = [
    "Keep building your future, Raghad!",
    "One line of code at a time 💻",
    "Your consistency is your superpower ⚡",
    "Progress, not perfection 🌸",
    "Stay curious, keep coding 🌈",
    "You're becoming who you dreamed of 🤍",
    "Small steps make big changes 🚀",
    "Every code you write builds your skill 🔥",
    "Keep going, your dream is loading ⏳",
    "You’re coding your own success ✨",
]
daily_message = random.choice(messages)

# ======= الإطار الرئيسي =======
main_frame = tk.Frame(root, bg=CARD_COLOR, padx=25, pady=30)
main_frame.place(relx=0.5, rely=0.5, anchor="center")

# ======= العنوان =======
tk.Label(
    main_frame,
    text="Code Reflection 💻",
    font=("Poppins", 20, "bold"),
    fg=ACCENT,
    bg=CARD_COLOR
).pack()

tk.Label(
    main_frame,
    text=date.today().strftime("%B %d, %Y"),
    font=("Poppins", 10),
    fg="#6B7280",
    bg=CARD_COLOR
).pack(pady=(0, 15))

tk.Label(
    main_frame,
    text=f"💬 {daily_message}",
    font=("Poppins", 11, "italic"),
    fg=ACCENT_LIGHT,
    bg=CARD_COLOR,
    wraplength=400,
    justify="center"
).pack(pady=(0, 25))

# ======= خانات الإدخال =======
def create_input(label_text):
    frame = tk.Frame(main_frame, bg=CARD_COLOR)
    frame.pack(fill="x", pady=7)
    tk.Label(frame, text=label_text, font=("Poppins", 11), bg=CARD_COLOR, fg=TEXT_DARK).pack(anchor="w")
    entry = tk.Entry(frame, font=("Poppins", 10), relief="solid", bd=0.8, bg="#F9FAFB", highlightthickness=1, highlightcolor="#C7D2FE")
    entry.pack(fill="x", ipady=5)
    return entry

minutes_entry = create_input("Minutes coded today:")
concepts_entry = create_input("New concepts learned:")
rating_entry = create_input("Productivity rating (1–10):")
highlight_entry = create_input("Highlight of the day:")

# ======= شريط التقدم =======
tk.Label(main_frame, text="Your Progress", font=("Poppins", 11, "bold"), bg=CARD_COLOR, fg=ACCENT).pack(pady=(20, 5))

style = ttk.Style()
style.theme_use("clam")
style.configure("blue.Horizontal.TProgressbar",
                troughcolor="#E0E7FF",
                bordercolor="#E0E7FF",
                background="#6366F1",
                lightcolor="#818CF8",
                darkcolor="#6366F1",
                thickness=18,
                borderwidth=0)

progress = ttk.Progressbar(main_frame, orient="horizontal", length=350, mode="determinate", style="blue.Horizontal.TProgressbar")
progress.pack(pady=(0, 15))
progress["value"] = 60

# ======= دالة الحفظ =======
def save_progress():
    minutes = minutes_entry.get()
    concepts = concepts_entry.get()
    rating = rating_entry.get()
    highlight = highlight_entry.get()
    today = date.today().strftime("%B %d, %Y")

    with open("progress.txt", "a", encoding="utf-8") as f:
        f.write(f"📅 {today}\n")
        f.write(f"⏱️ Minutes coded: {minutes}\n")
        f.write(f"🧠 Concepts learned: {concepts}\n")
        f.write(f"⭐ Productivity rating: {rating}/10\n")
        f.write(f"🌟 Highlight: {highlight}\n")
        f.write("=" * 45 + "\n")

    saved_popup = tk.Toplevel(root)
    saved_popup.title("Saved")
    saved_popup.geometry("300x120")
    saved_popup.config(bg="#F3F4F6")
    tk.Label(saved_popup, text="✅ Progress saved successfully!", font=("Poppins", 11), fg="#16A34A", bg="#F3F4F6").pack(expand=True)

# ======= زر الحفظ =======
save_btn = tk.Button(
    main_frame,
    text="Save my progress",
    font=("Poppins", 12, "bold"),
    bg=BUTTON_GRADIENT_1,
    fg="white",
    activebackground=BUTTON_GRADIENT_2,
    relief="flat",
    cursor="hand2",
    padx=20,
    pady=8,
    command=save_progress
)
save_btn.pack(pady=10)

# ======= تشغيل الواجهة =======
root.mainloop()
