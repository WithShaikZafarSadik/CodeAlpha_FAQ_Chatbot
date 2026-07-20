import tkinter as tk
from tkinter import scrolledtext
from chatbot import get_response
class ChatbotUI:
    def __init__(self, root):
        self.root = root
        self.root.title("CodeAlpha FAQ Chatbot")
        self.root.geometry("700x700")
        self.root.configure(bg="#EAF4FC")
        # Title
        self.title = tk.Label(
            self.root,
            text="🤖 CodeAlpha FAQ Chatbot",
            font=("Arial", 18, "bold"),
            bg="#EAF4FC",
            fg="#003366"
        )
        self.title.pack(pady=10)
        # Chat Area
        self.chat_area = scrolledtext.ScrolledText(
            self.root,
            wrap=tk.WORD,
            width=70,
            height=22,
            font=("Arial", 11)
        )
        self.chat_area.pack(padx=10, pady=10)
        self.chat_area.insert(
            tk.END,
            "🤖 Bot: Hello! Welcome to the CodeAlpha FAQ Chatbot.\n"
            "Ask me any question.\n\n"
        )
        self.chat_area.config(state="disabled")
        # Input Box
        self.user_input = tk.Entry(
            self.root,
            width=70,
            font=("Arial", 12),
            bd=3,
            relief="solid"
        )
        self.user_input.pack(fill="x", padx=15, pady=10)
        # Button Frame
        self.button_frame = tk.Frame(self.root, bg="#EAF4FC")
        self.button_frame.pack(pady=10)

        # Send Button
        self.send_button = tk.Button(
            self.button_frame,
            text="Send",
            width=12,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 11, "bold"),
            command=self.send_message
        )
        self.send_button.grid(row=0, column=0, padx=5)

        # Clear Chat Button
        self.clear_button = tk.Button(
            self.button_frame,
            text="Clear Chat",
            width=12,
            bg="#2196F3",
            fg="white",
            font=("Arial", 11, "bold"),
            command=self.clear_chat
        )
        self.clear_button.grid(row=0, column=1, padx=5)

        # Exit Button
        self.exit_button = tk.Button(
            self.button_frame,
            text="Exit",
            width=12,
            bg="#F44336",
            fg="white",
            font=("Arial", 11, "bold"),
            command=self.root.destroy
        )
        self.exit_button.grid(row=0, column=2, padx=5)
    def send_message(self):
        user_message = self.user_input.get().strip()

        if user_message == "":
            return

        bot_reply = get_response(user_message)

        self.chat_area.config(state="normal")

        self.chat_area.insert(tk.END, f"You: {user_message}\n")
        self.chat_area.insert(tk.END, f"Bot: {bot_reply}\n\n")

        self.chat_area.config(state="disabled")
        self.chat_area.see(tk.END)

        self.user_input.delete(0, tk.END)

    def clear_chat(self):
        self.chat_area.config(state="normal")
        self.chat_area.delete("1.0", tk.END)
        self.chat_area.insert(
            tk.END,
            "🤖 Bot: Hello! Welcome to the CodeAlpha FAQ Chatbot.\n"
            "Ask me any question.\n\n"
        )
        self.chat_area.config(state="disabled")

    