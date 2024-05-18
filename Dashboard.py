import customtkinter as ctk
import tkintermapview
import tk_tools as tkt


ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = ctk.CTk()  # create CTk window like you do with the Tk window
app.title("Dashboard")
# app.overrideredirect(True)  # remove window border
# app.attributes('-fullscreen',True)


frame_0 = ctk.CTkFrame(master=app)
frame_0.place(relx=0.005, rely=0.005, relwidth=0.45, relheight=0.45)

frame_1 = ctk.CTkFrame(master=app)
frame_1.place(relx=0.005, rely=0.5, relwidth=0.45, relheight=0.45)

frame_2 = ctk.CTkFrame(master=app)
frame_2.place(relx=0.5, rely=0.005, relwidth=0.45, relheight=0.45)


# speed_label = ctk.CTkLabel(master=frame_0, text="Speed", fg_color="transparent")
# speed_label.pack(pady=10, padx=10, anchor="w")
# speed_entry = ctk.CTkEntry(master=frame_0, placeholder_text="")
# speed_entry.pack(pady=10, padx=10,fill="x", anchor="w")
#
# acc_label = ctk.CTkLabel(master=frame_0, text="Accelaration", fg_color="transparent")
# acc_label.pack(pady=10, padx=10, anchor="w")
# acc_entry = ctk.CTkEntry(master=frame_0, placeholder_text="")
# acc_entry.pack(pady=10, padx=10, fill="x", anchor="w")
#
# ot_label = ctk.CTkLabel(master=frame_0, text="Overtake", fg_color="transparent")
# ot_label.pack(pady=10, padx=10, anchor="w")
# ot_entry = ctk.CTkEntry(master=frame_0, placeholder_text="")
# ot_entry.pack(pady=10, padx=10, fill="x", anchor="w")

speed_gauge = tkt.Gauge(frame_0, max_value=100.0,label='speed', unit='km/h')
speed_gauge.pack(padx=10,side="left",expand=True)
speed_gauge.set_value(10) # set the value of the gauge

acc_gauge = tkt.Gauge(frame_0, max_value=100.0,label='Accelaration', unit='km/h^2')
acc_gauge.pack(padx=10,side="left",expand=True)
acc_gauge.set_value(10) # set the value of the gauge


# create map widget
map_widget = tkintermapview.TkinterMapView(frame_1, corner_radius=5)
map_widget.pack(padx=10,pady=10,fill="both",expand=True)

# set current widget position and zoom
map_widget.set_position(7.4089, 80.6080)  # Paris, France
map_widget.set_zoom(60)
marker_3 = map_widget.set_marker(7.4089, 80.6080)


def send_event():
    print("button pressed")

send_button = ctk.CTkButton(frame_2, text="CTkButton", command=send_event)
send_button.pack(pady=10, padx=10, anchor="w")

def button_event():
    print("button pressed")

button = ctk.CTkButton(frame_2, text="CTkButton", command=button_event)
button.pack(pady=10, padx=10, anchor="w")

app.mainloop()
