import tkinter as tk

class KnowledgeRecorder:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Knowledge Recorder")
        self.window.configure(bg="#ADD8E6")

        # Create a frame for the title and content
        self.frame = tk.Frame(self.window, bg="#ADD8E6")
        self.frame.pack()

        # Create a label for the title
        self.title_label = tk.Label(self.frame, text="Title:", bg="#ADD8E6")
        self.title_label.grid(row=0, column=0)

        # Create an entry for the title
        self.title_entry = tk.Entry(self.frame, bg="#ADD8E6")
        self.title_entry.grid(row=0, column=1)

        # Create a label for the content
        self.content_label = tk.Label(self.frame, text="Content:", bg="#ADD8E6")
        self.content_label.grid(row=1, column=0)

        # Create a text box for the content
        self.content_text = tk.Text(self.frame, height=10, bg="#ADD8E6")
        self.content_text.grid(row=1, column=1)

        # Create a button to save the knowledge
        self.save_button = tk.Button(self.frame, text="Save", command=self.save_knowledge, bg="#ADD8E6")
        self.save_button.grid(row=2, column=0)

        # Create a button to load the knowledge
        self.load_button = tk.Button(self.frame, text="Load", command=self.load_knowledge, bg="#ADD8E6")
        self.load_button.grid(row=2, column=1)

        self.flashcard_button = tk.Button(self.frame, text="FlashCard", command=self, bg="#ADD8E6")
        self.flashcard_button.grid(row=2, column=2)

        # Start the mainloop
        self.window.mainloop()

    def save_knowledge(self):
        # Get the title and content from the GUI
        title = self.title_entry.get()
        content = self.content_text.get("1.0", "end-1c")

        # Save the knowledge to a file
        with open("knowledge.txt", "w") as f:
            f.write(f"{title}:{content}")

    def load_knowledge(self):
        # Clear the GUI before loading the knowledge
        self.title_entry.delete(0, "end")
        self.content_text.delete("1.0", "end-1c")

        # Load the knowledge from a file
        with open("knowledge.txt", "r") as f:
            knowledge = f.read()

        # Split the knowledge into the title and content
        title, content = knowledge.split(":")

        # Display the title and content in the GUI
        self.title_entry.insert(0, title)
        self.content_text.insert("1.0", content)



# Create a new KnowledgeRecorder object
knowledge_recorder = KnowledgeRecorder()

