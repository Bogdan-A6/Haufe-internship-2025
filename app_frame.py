import customtkinter
import gemma3_promt
from customtkinter import filedialog   
import pyperclip  # Pentru functionalitatea de clipboard

def putQuestion(mesaj):
    raspuns = gemma3_promt.putQuestion(str(mesaj))
    return raspuns

def selectfile():
        filename = filedialog.askopenfilename()
        file = open(filename,'r')
        continut = file.read()
        file.close()
        return continut

    
    
class displayFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame...
        self.label = customtkinter.CTkLabel(self, text="Ask away", justify="left")
        self.label.grid(row=0, column=0, sticky="w")    
    
    def update_label(self, new_text):
        self.label.configure(text=new_text) 



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.rowconfigure(0, weight=3) 
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.title("teste")
        
        #button for sending the code to be reviewed
        self.button1 = customtkinter.CTkButton(self, text="Send the code", command=self.button_click)
        self.button1.grid(row=2, column=0, padx=5, pady=5)
        
        #file selector button
        self.button2 = customtkinter.CTkButton(self, text="Redo the code", command=self.gaseste_cod)
        self.button2.grid(row=2, column=1, padx=5, pady=5)
        
        # NEW: Copy code button
        self.button3 = customtkinter.CTkButton(self, text="Copy Code", command=self.copy_code)
        self.button3.grid(row=3, column=1, padx=5, pady=5)
        
        #where the code review will be displayed
        self.my_frame = displayFrame(master=self, fg_color="transparent")
        self.my_frame.grid(row=0, columnspan=2, sticky="nsew", padx=10, pady=10)
        
        
        
        #where the code from the input file will be displayed - WITH SCROLLBAR
        self.code_frame = customtkinter.CTkScrollableFrame(self, fg_color="transparent")
        self.code_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)
        
        # Label inside the scrollable frame
        self.code_label = customtkinter.CTkLabel(self.code_frame, text="Redone code here", justify="left", wraplength=400)
        self.code_label.grid(row=0, column=0, sticky="w")
        
        #where the code to review inputs
        self.textbox1 = customtkinter.CTkTextbox(master=self, width=50, corner_radius=0)
        self.textbox1.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        self.textbox1.configure(text_color="red")


    def button_click(self):
        raspuns  = str(putQuestion(app.textbox1.get("1.0", "end-1c")))
        self.my_frame.update_label(raspuns)
        
    def deschideFile(self):
        continut = selectfile()
        self.code_label.configure(text=continut)
        
        
    def gaseste_cod(self):
        raspuns = self.my_frame.label.cget('text')
        inceput_cod = raspuns.find("Redone code")
        if inceput_cod == -1:
            inceput_cod = 1
        lungime = len(raspuns)
        print(inceput_cod)
        print(lungime)
        print(raspuns[inceput_cod:])
        self.code_label.configure(text=raspuns[inceput_cod:len(raspuns)])
    
    def copy_code(self):
        code_text = self.code_label.cget('text')
        if code_text and code_text != "Redone code here":
            try:
                pyperclip.copy(code_text)
                # Show confirmation message
                self.button3.configure(text="Copied!", fg_color="green")
                self.after(2000, lambda: self.button3.configure(text="Copy Code", fg_color=["#3B8ED0", "#1F6AA5"]))
            except Exception as e:
                print(f"Error copying to clipboard: {e}")
        else:
            # Show error message
            self.button3.configure(text="No code!", fg_color="red")
            self.after(2000, lambda: self.button3.configure(text="Copy Code", fg_color=["#3B8ED0", "#1F6AA5"]))

if __name__ == "__main__":
    app = App()
    app.after(0, lambda:app.state('zoomed'))
    app.mainloop()