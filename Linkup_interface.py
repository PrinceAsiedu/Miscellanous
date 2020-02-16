from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread 

import tkinter as tk 
from tkinter import ttk 
from tkinter import PhotoImage

from tkinter.filedialog import askopenfilename
from tkinter import messagebox as mb
from tkinter.constants import END


class App(tk.Tk):
	def run(self):
		self.img1 = PhotoImage("frameFocusBorder", data="""
		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
		Ry/99NIz//oGrZpUUEAAOw==""")

		self.img2 = PhotoImage("frameBorder", data="""
		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""")

		
		self.data = """
		R0lGODlhKgAaAOfnAFdZVllbWFpcWVtdWlxeW11fXF9hXmBiX2ZnZWhpZ2lraGxua25wbXJ0
		cXR2c3V3dHZ4dXh6d3x+e31/fH6AfYSGg4eJhoiKh4qMiYuNio2PjHmUqnqVq3yXrZGTkJKU
		kX+asJSWk32cuJWXlIGcs5aYlX6euZeZloOetZial4SftpqbmIWgt4GhvYahuIKivpudmYei
		uYOjv5yem4ijuoSkwIWlwYmlu56gnYamwp+hnoenw4unvaCin4ioxJCnuZykrImpxZmlsoaq
		zI2pv6KkoZGouoqqxpqms4erzaOloo6qwYurx5Kqu5untIiszqSmo5CrwoysyJeqtpOrvJyo
		tZGsw42typSsvaaopZKtxJWtvp6qt4+uy6epppOuxZCvzKiqp5quuZSvxoyx06mrqJWwx42y
		1JKxzpmwwaqsqZaxyI6z1ZqxwqutqpOzz4+01qyuq56yvpizypS00Jm0y5W10Zq1zJa20rCy
		rpu3zqizwbGzr6C3yZy4z7K0saG4yp250LO1sqK5y5660Z+70qO7zKy4xaC806S8zba4taG9
		1KW9zq66x6+7yLi6t6S/1rC8yrm7uLO8xLG9y7q8ubS9xabB2anB07K+zLW+xrO/za7CzrTA
		zrjAyLXBz77BvbbC0K/G2LjD0bnE0rLK28TGw8bIxcLL07vP28HN28rMycvOyr/T38DU4cnR
		2s/RztHT0NLU0cTY5MrW5MvX5dHX2c3Z59bY1dPb5Nbb3dLe7Nvd2t3f3NXh797g3d3j5dnl
		9OPl4eTm4+Ln6tzo9uXn5Obo5eDp8efp5uHq8uXq7ejq5+nr6OPs9Ovu6unu8O3v6+vw8+7w
		7ezx9O/x7vDy7/Hz8O/19/P18vT38/L3+fb49Pf59vX6/fj69/b7/vn7+Pr8+ff9//v9+vz/
		+/7//P//////////////////////////////////////////////////////////////////
		/////////////////////////////////yH/C05FVFNDQVBFMi4wAwEAAAAh+QQJZAD/ACwC
		AAIAKAAWAAAI/gD/CRz4bwUGCg8eQFjIsGHDBw4iTLAQgqBFgisuePCiyJOpUyBDihRpypMi
		Lx8qaLhIMIyGFZ5sAUsmjZrNmzhzWpO2DJgtTysqfGDpxoMbW8ekeQsXzty4p1CjRjUXrps3
		asJsuclQ4uKKSbamMR3n1JzZs2jRkh1HzuxVXX8y4CDYAwqua+DInVrRwMGJU2kDp31KThy1
		XGWGDlxhi1rTPAUICBBAoEAesoIzn6Vm68MKgVAUHftmzhOCBCtQwQKSoABgzZnJdSMmyIPA
		FbCotdUQAIhNa9B6DPCAGbZac+SowVIMRVe4pwkA4GpqDlwuAAmMZx4nTtfnf1mO5JEDNy46
		MHJkxQEDgKC49rPjwC0bqGaZuOoZAKjBPE4NgAzUvYcWOc0QZF91imAnCDHJ5JFAAJN0I2Ba
		4iRDUC/gOEVNDwIUcEABCAgAAATUTIgWOMBYRFp80ghiAQIIVAAEAwJIYI2JZnUji0XSYAYO
		NcsQA8wy0hCTwAASXGOiONFcxAtpTokTHznfiLMNMAkcAMuE43jDC0vLeGOWe2R5o4sn1LgH
		GzkWsvTPMgEOaA433Ag4TjjMuDkQMNi0tZ12sqWoJ0HATMPNffAZZ6U0wLAyqJ62RGoLLrhI
		aqmlpzwaEAAh+QQJZAD/ACwAAAAAKgAaAAAI/gD/CRw40JEhQoEC+fGjcOHCMRAjRkxDsKLF
		f5YcAcID582ZjyBDJhmZZIjJIUySEDHiBMhFghrtdNnRAgSHmzhz6sTZQcSLITx+CHn5bxSk
		Nz5MCMGy55CjTVCjbuJEtSrVQ3uwqDBRQwrFi476SHHxow8qXcemVbPGtm21t3CnTaP27Jgu
		VHtuiIjBsuImQkRiiEEFTNo2cOTMKV7MuLE5cN68QUOGSgwKG1EqJqJDY8+rZt8UjxtNunTj
		cY3DgZOWS46KIFgGjiI0ZIsqaqNNjWjgYMUpx8Adc3v2aosNMAI1DbqyI9WycOb4IAggQEAB
		A3lQBxet/TG4cMpI/tHwYeSfIzxM0uTKNs7UgAQrYL1akaDA7+3bueVqY4NJlUhIcQLNYx8E
		AIQ01mwjTQ8DeNAdfouNA8440GBCQxJY3MEGD6p4Y844CQCAizcSgpMLAAlAuJ03qOyQRBR3
		nEHEK+BMGKIui4kDDAAIPKiiYuSYSMQQRCDCxhiziPMYBgDkEaEaAGQA3Y+MjUPOLFoMoUUh
		cKxRC4ngeILiH8Qkk0cCAUzSDZWpzbLEE1EwggcYqWCj2DNADFDAAQUgIAAAEFDDJmPYqNJF
		F1s4cscTmCDjDTjdSPOHBQggUAEQDAgggTWDPoYMJkFoUdRmddyyjWLeULMMMcAsIw0x4wkM
		IME1g25zyxpHxFYUHmyIggw4H4ojITnfiLMNMAkcAAub4BQjihRdDGTJHmvc4Qo1wD6Imje6
		eILbj+BQ4wqu5Q3ECSJ0FOKKMtv4mBg33Pw4zjbKuBIIE1xYpIkhdQQiyi7OtAucj6dt48wu
		otQhBRa6VvSJIRwhIkotvgRTzMUYZ6xxMcj4QkspeKDxxRhEmUfIHWjAgQcijEDissuXvCyz
		zH7Q8YQURxDhUsn/bCInR3AELfTQZBRt9BBJkCGFFVhMwTNBlnBCSCGEIJQQIAklZMXWRBAR
		RRRWENHwRQEBADs="""

		self.style = ttk.Style()

		self.style.element_create("RoundedFrame", "image", "frameBorder",
		    ("focus", "frameFocusBorder"), border=16, sticky="nsew")

		self.style.layout("RoundedFrame", [("RoundedFrame", {"sticky": "nsew"})])
		self.style.configure("TEntry", borderwidth=0)

		self.s1 = PhotoImage("search1", data=self.data ,format="gif -index 0")
		self.s2 = PhotoImage("search2", data=self.data, format="gif -index 1")


		self.style1 =ttk.Style()
		self.style1.map("C.TButton",
		    foreground=[('pressed', 'white'), ('active', 'white')],
		    background=[('pressed', '!disabled', 'black'), ('active', 'forestgreen')]
		    )
		self.style1.element_create("Search.field", "image", "search1",
		    ("focus", "search2"), border=[22, 7, 14], sticky="ew")

		self.style1.layout("Search.entry", [
		    ("Search.field", {"sticky": "nswe", "border": 1, "children":
		        [("Entry.padding", {"sticky": "nswe", "children":
		            [("Entry.textarea", {"sticky": "nswe"})]
		        })]
		    })]
		)

		self.style1.configure("Search.entry", background="white")

		
		self.title("YenKasa")
		# self.resizable(False,False)
		self.mainWin = ttk.Frame(self, style="RoundedFrame", 
			padding=10,
			border=3, relief='groove')
		self.signup_btn = ttk.Button(self.mainWin, 
									text="Sign Up", 
									style="C.TButton")#,
									# command = self.signup_window)
		self.signup_btn.grid(row = 2, column = 0, padx= 40, pady = 30)
		self.login_btn = ttk.Button(self.mainWin, 
									text = "Log In", 
									style="C.TButton",
									command = self.login_window)
		self.login_btn.grid(row = 2, column = 2, padx = 40, pady = 30)

		self.mainWin.pack(fill = tk.BOTH, expand =True)

		self.mainloop()

	def login_window(self):
		self.signup_btn.destroy()
		self.login_btn.destroy()

		self.title('Log In')
		#Entries of this frame are host, port name and password and corresponding labels and entries are created
		self.username_label = ttk.Label(self.mainWin, text = 'Username:',
			background="white",
			anchor = tk.W,
			justify = tk.LEFT,
			font=('Candara',15,'italic'))

		self.username_entry = ttk.Entry(self.mainWin, style= "Search.entry")

		self.password_label = ttk.Label(self.mainWin, text = 'Password:'
			,background="white", 
			anchor=tk.W,
			justify=tk.LEFT,
			font=('Candara',15,'italic'))

		self.password_entry = ttk.Entry(self.mainWin, show = '*', style="Search.entry")

		#Attempt a Log in.
		self.login_btn = ttk.Button(self.mainWin, 
									text = 'Log In', 
									style="C.TButton",
									command = self.login)
	
		#Positioning the labels and text boxes appropriately
		self.username_label.grid(row = 2, column = 0, pady = 10, padx = 5)
		self.username_entry.grid(row = 2, column = 1, pady = 10, padx = 5)
		self.password_label.grid(row = 3, column = 0, pady = 10, padx = 5)
		self.password_entry.grid(row = 3, column = 1, pady = 10, padx = 5)
		self.login_btn.grid(row 	 = 5, column = 1, pady = 10, padx = 5)
		self.username_entry.focus_set()
		self.mainWin.pack(fill=tk.BOTH, expand= True)

	def login(self):
		self.username_label.destroy()
		self.username_entry.destroy()
		self.password_label.destroy()
		self.password_entry.destroy()
		self.login_btn.destroy()
		self.mainWin.pack_forget()

		self.title('YenKasa') #Window title

		self.should_quit = False

		self.wm_protocol("WM_DELETE_WINDOW", self.destroy)
		self.chat_frame = ttk.Frame(self.mainWin, borderwidth = 5)#for the actual display of chat
		self.clients_frame = ttk.Frame(self.mainWin)  #for radio buttons
		self.entry_frame = ttk.Frame(self, style="RoundedFrame",
		padding=10,border=3, relief='groove') #for input text
		self.button_frame = ttk.Frame(self.entry_frame)

		self.chat_image = PhotoImage(file='glade/yk1.png')
		self.s_bar = tk.Label(text='YenKasa ',
			border=4,font=('Candara',14,'bold'),
			image=self.chat_image,compound='right',
			background='steelblue',foreground='white')

		self.s_bar.pack(anchor="n", fill="x")

		#state indicates the chat history so far, and is uneditable
		self.chat_text = tk.Text(self.chat_frame, 
								 # state = tk.DISABLED,
								 # height=20,
								background="lemonchiffon4",
								foreground="white",
								font=('Comic Sans MS', 14, 'bold'))
								# width=40,
								# insertborderwidth=5,
								# pady=7)

		#Adding a scroll bar to the text Area
		self.scroll = tk.Scrollbar(self.chat_frame)
		self.scroll.configure(command = self.chat_text.yview)
		self.chat_text.configure(yscrollcommand = self.scroll.set)
		# self.chat_text.bell()

		#Chat entry area consists of Send Message, Send Multimedia and Chat entry
		self.chat_entry = tk.Entry(self.entry_frame,
								font = ("Candara", 13, 'italic'),
								background="white",
								foreground="gray30",
								# height=1,
								width=40,
								selectbackground='gray30',
								selectforeground='steelblue')
								# cursor='')

		self.send_image = PhotoImage(file='send1.png')
		self.attach_image = PhotoImage(file='attach1.png')

		self.send_button = ttk.Button(self.button_frame, 
									  style="C.TButton",
									  # text = 'Send',
									  image=self.send_image,
									  compound='right',
									  width = 0.2,
									  command =self.send)      
									  #For actually sending the message
		
		self.browsebutton = ttk.Button(self.button_frame,
										style="C.TButton",
										image=self.attach_image,
										width =0.2,
										compound='right')
										# command = self.browse)

		# self.send_button.bind('<Button-1>', self.send)  #press button-1 to send message
		self.chat_entry.bind('<Return>', self.send)  	  #Alternate to sending messages, 
													      #hitting the return button

		#Packing the above created objects and giving them positions while packing
		self.entry_frame.pack(side = tk.BOTTOM, fill = tk.X, expand=True)
		self.mainWin.pack(side = tk.TOP, fill = tk.BOTH, expand = True)
		self.clients_frame.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)
		self.chat_frame.pack(side = tk.RIGHT, fill = tk.BOTH, expand = True)
		self.chat_entry.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)
		self.send_button.grid(row=0,column=0, padx = 10, pady = 5)
		self.browsebutton.grid(row=0,column=1, padx = 10, pady = 10)
		self.button_frame.pack(side = tk.RIGHT)

		self.radio_label = ttk.Label(self.clients_frame,
					width = 5,
					foreground='gray30',
					wraplength = 125,
					anchor = tk.W,
					justify = tk.LEFT,
					font=('Candara',12,'roman'),
					text = 'Online  ',
					image=self.chat_image,
					compound='right'
					)

		# self.radio_label.pack()
		self.scroll.pack(side = tk.RIGHT,fill=tk.Y)
		self.chat_text.pack(fill = tk.BOTH, expand = True)

		self.checks = []

		# self.enable = dict()

		# for client in self.list_of_active_user:
		   # self.enable[client] = tk.IntVar()
		   # l = ttk.Checkbutton(self.clients_frame, text=client, variable=self.enable[client])
		   # l.pack(anchor = tk.W)
		   # self.checks.append(l)
		
		self.chat_entry.focus()

		self.buffer_size = 100000
		self.server_address = ('127.0.0.1', 33000)

		self.client_socket = socket(AF_INET, SOCK_STREAM)
		try:
			self.client_socket.connect(self.server_address)

			self.receive_thread = Thread(target=self.receive)
			self.receive_thread.start()

		except Exception as error:
			mb.showinfo('An Error Has Occurred',str(error))
			exit(0)

	# def send(self,event=None):
		# msg = self.chat_entry.get(tk.END)
		# self.chat_entry.delete(tk.END)  # Clears input field.
		# pass

	def receive(self):
	    """Handles receiving of messages."""
	    while True:
	        try:
	            self.msg = self.client_socket.recv(self.buffer_size).decode("utf8")
	            self.chat_text.insert(tk.END, '\n'+self.msg)
	        except OSError:  # Possibly client has left the chat.
	        	self.client_socket.close()
	        	break


	def send(self, event=None):  # event is passed by binders.
	    """Handles sending of messages."""
	    self.msg = self.chat_entry.get()
	    self.chat_entry.delete(0,END)  # Clears input field.
	    self.client_socket.send(bytes(self.msg, "utf8"))
	    if self.msg == "{quit}":
	        self.client_socket.close()
	        self.mainWin.quit()


	def on_closing(self, event=None):
	    """This function is to be called when the window is closed."""
	    self.chat_entry.set("{quit}")
	    self.client_socket.close()
	    send()

if __name__ == '__main__':
	app = App()
	app.run()
