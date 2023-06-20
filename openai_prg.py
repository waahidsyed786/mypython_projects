from tkinter import * 
import customtkinter 
import openai
import os 
import pickle

app = customtkinter.CTk()
app.title ("ChatGPT Bot")
app.geometry("750x600")

app.iconbitmap("ai_lt.ico")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def speak():
    print("speak")
    filename = "api_key"
    try:
        if os.path.isfile(filename):
            input_file = open(filename, "rb")
            api_key_value = pickle.load(input_file)
            api_entry.insert(END,api_key_value)
            input_file.close() 

            openai.api_key = api_key_value
            openai.Model.list() 

            response = openai.Completion.create(
                model ="text-davinci-003",
                prompt =chat_entry.get(),
                temperature = 0,
                max_tokens = 4000,
                top_p =1,
                frequency_penalty = 0.0,
                presence_penalty = 0.0

             )
            #  my_text.insert(END,response)
            editedResponse = response["choices"][0]["text"].script()
            my_text.insert(END,0)
            my_text.insert(END, editedResponse)
        else:
            input_file=open(filename, "wb")
            input_file.close() 
    except Exception as  e: 
        print("Exception")

def clear():
    print("clear")
    my_text.delete(1.0,END)
    chat_entry.delete(0,END) 


def api(): 
    print("api")
    
    api_frame.pack(pady=10)
    app.geometry("750x750")

def save(): 
    filename = "api_key"
    try: 
        output_file = open(filename,"wb")
        pickle.dump(api_entry.get(), output_file)
        api_entry.delete(0,END)
        output_file.close() 
        api_frame.pack_forget() 
        # api_frame.forget()
        app.geometry("750x600")
        print("save")
    except Exception as e : 
        print("Exception " )



text_frame = customtkinter.CTkFrame( master = app) 
text_frame.pack(pady=20)
my_text= Text(text_frame, bg="#343638", width=75, relief="flat", wrap=WORD, fg="white")
my_text.grid(row=0, column=0) 

text_scroll = customtkinter.CTkScrollbar(text_frame, command=my_text.yview)
text_scroll.grid(row=0, column =1, sticky="ns")
my_text.configure(yscrollcommand=text_scroll.set)

chat_entry = customtkinter.CTkEntry(master=app, placeholder_text= "Please send a message...", width=330, height=50, border_width=1)
chat_entry.pack(pady=20)


# button_frame = customtkinter.CTkEntry(master=app,fg_color='#242424',border_width=1)
button_frame = customtkinter.CTkEntry(master=app, border_width=1)
button_frame.pack(pady=10)

#button 1 -> Submit Button 
submit_button = customtkinter.CTkButton(button_frame, text="Ask to ChatGPT",command=speak)
submit_button.grid(row=0,column=0, padx=20)
# button 2 -> clear button
clear_button = customtkinter.CTkButton(button_frame, text="Clear All", command=clear)
clear_button.grid(row=0,column=1, padx=20)
# button 3 -> Api Button
api_button = customtkinter.CTkButton(button_frame, text="Change API", command=api)
api_button.grid(row=0,column=2, padx=20)

api_frame = customtkinter.CTkFrame(master=app, border_width=1)
# api_frame.pack(pady=10)
  # move the above statement to api() method 

# api_entry = customtkinter.CTkButton(master=api_frame, placeholder_text= "Please send a message...", width=350, height=50, border_width=1)
api_entry = customtkinter.CTkEntry(master=api_frame, placeholder_text= "Enter your api key ", width=330, height=50, border_width=1)
api_entry.grid(row=0, column=0, padx=20, pady=20)

api_save_button = customtkinter.CTkButton(master=api_frame, text="save",command=save)
api_save_button.grid(row=0,column=1, padx=20) 

app.mainloop()