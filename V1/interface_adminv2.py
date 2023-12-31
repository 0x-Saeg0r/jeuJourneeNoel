# fais une feneêtre sous customtkinter
from customtkinter import *
import csv
import socket
import threading

tab = []
#  open csv file
with open("questions.csv", newline='', encoding='utf-8-sig') as csvfile:
    fichier = csv.DictReader(csvfile, delimiter=";")
    # pour remplir notre tableau, une boucle for parcourant chaque ligne du fichier csv sera utilisée
    for ligne in fichier:
        tab.append(dict(ligne))


app = CTk()
app.title("Panneau de contrôle et d'administration")
app.geometry("1250x600")
app.resizable(False, False)


points_j1, points_j2, points_j3, points_j4, points_j5 = 0, 0, 0, 0, 0
temp_points_j1, temp_points_j2, temp_points_j3, temp_points_j4, temp_points_j5 = 0, 0, 0, 0, 0

# Grid on the left to add points to each of 5 players

"""self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="CustomTkinter", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))"""

### Functions ###


def activate_button_j1():
    player1_button_ajouter.grid_forget()
    player1_button_remove.grid_forget()
    player1_button_1.grid(row=0, column=1, padx=3, pady=20)
    player1_button_3.grid(row=0, column=2, padx=3, pady=20)
    player1_button_5.grid(row=0, column=3, padx=3, pady=20)


def desactivate_button_j1():
    player1_button_1.grid_forget()
    player1_button_3.grid_forget()
    player1_button_5.grid_forget()
    player1_button_ajouter.grid(row=0, column=1, padx=8, pady=10)


def add_point_j1(nb):
    global temp_points_j1
    player1_button_remove.grid(row=0, column=2, padx=8, pady=10)
    temp_points_j1 = nb
    admin_points()
    print(f"+{nb} point pour joueur 1")
    desactivate_button_j1()


def activate_button_j2():
    player2_button_ajouter.grid_forget()
    player2_button_remove.grid_forget()
    player2_button_1.grid(row=0, column=1, padx=3, pady=20)
    player2_button_3.grid(row=0, column=2, padx=3, pady=20)
    player2_button_5.grid(row=0, column=3, padx=3, pady=20)


def desactivate_button_j2():
    player2_button_1.grid_forget()
    player2_button_3.grid_forget()
    player2_button_5.grid_forget()
    player2_button_ajouter.grid(row=0, column=1, padx=8, pady=10)


def add_point_j2(nb):
    global temp_points_j2
    player2_button_remove.grid(row=0, column=2, padx=8, pady=10)
    temp_points_j2 = nb
    admin_points()
    print(f"+{nb} point pour joueur 2")
    desactivate_button_j2()


def activate_button_j3():
    player3_button_ajouter.grid_forget()
    player3_button_remove.grid_forget()
    player3_button_1.grid(row=0, column=1, padx=3, pady=20)
    player3_button_3.grid(row=0, column=2, padx=3, pady=20)
    player3_button_5.grid(row=0, column=3, padx=3, pady=20)


def desactivate_button_j3():
    player3_button_1.grid_forget()
    player3_button_3.grid_forget()
    player3_button_5.grid_forget()
    player3_button_ajouter.grid(row=0, column=1, padx=8, pady=10)


def add_point_j3(nb):
    global temp_points_j3
    player3_button_remove.grid(row=0, column=2, padx=8, pady=10)
    temp_points_j3 = nb
    admin_points()
    print(f"+{nb} point pour joueur 3")
    desactivate_button_j3()


def activate_button_j4():
    player4_button_remove.grid_forget()
    player4_button_ajouter.grid_forget()
    player4_button_1.grid(row=0, column=1, padx=3, pady=20)
    player4_button_3.grid(row=0, column=2, padx=3, pady=20)
    player4_button_5.grid(row=0, column=3, padx=3, pady=20)


def desactivate_button_j4():
    player4_button_1.grid_forget()
    player4_button_3.grid_forget()
    player4_button_5.grid_forget()
    player4_button_ajouter.grid(row=0, column=1, padx=8, pady=10)


def add_point_j4(nb):
    global temp_points_j4
    player4_button_remove.grid(row=0, column=2, padx=8, pady=10)
    temp_points_j4 = nb
    admin_points()
    print(f"+{nb} point pour joueur 4")
    desactivate_button_j4()


def activate_button_j5():
    player5_button_remove.grid_forget()
    player5_button_ajouter.grid_forget()
    player5_button_1.grid(row=0, column=1, padx=3, pady=20)
    player5_button_3.grid(row=0, column=2, padx=3, pady=20)
    player5_button_5.grid(row=0, column=3, padx=3, pady=20)


def desactivate_button_j5():
    player5_button_1.grid_forget()
    player5_button_3.grid_forget()
    player5_button_5.grid_forget()
    player5_button_ajouter.grid(row=0, column=1, padx=8, pady=10)


def add_point_j5(nb):
    global temp_points_j5
    player5_button_remove.grid(row=0, column=2, padx=8, pady=10)
    temp_points_j5 = nb
    admin_points()
    print(f"+{nb} point pour joueur 5")
    desactivate_button_j5()


def retirer_j1():
    global temp_points_j1
    temp_points_j1 = 0
    admin_points()


def retirer_j2():
    global temp_points_j2
    temp_points_j2 = 0
    admin_points()


def retirer_j3():
    global temp_points_j3
    temp_points_j3 = 0
    admin_points()


def retirer_j4():
    global temp_points_j4
    temp_points_j4 = 0
    admin_points()


def retirer_j5():
    global temp_points_j5
    temp_points_j5 = 0
    admin_points()


### Points functions ###


def admin_points():
    global temp_points_j1, temp_points_j2, temp_points_j3, temp_points_j4, temp_points_j5
    points_j1_label.configure(text=f"J1: {temp_points_j1}")
    points_j2_label.configure(text=f"J2: {temp_points_j2}")
    points_j3_label.configure(text=f"J3: {temp_points_j3}")
    points_j4_label.configure(text=f"J4: {temp_points_j4}")
    points_j5_label.configure(text=f"J5: {temp_points_j5}")


def valider_points():
    global temp_points_j1, temp_points_j2, temp_points_j3, temp_points_j4, temp_points_j5, points_j1, points_j2, points_j3, points_j4, points_j5
    points_j1 += temp_points_j1
    points_j2 += temp_points_j2
    points_j3 += temp_points_j3
    points_j4 += temp_points_j4
    points_j5 += temp_points_j5
    temp_points_j1, temp_points_j2, temp_points_j3, temp_points_j4, temp_points_j5 = 0, 0, 0, 0, 0
    # buttonAnswer.configure(state="normal")
    valider_button.configure(state="disabled")
    # score_player1_2.configure(text=f"{points_j1} points")
    # score_player2_2.configure(text=f"{points_j2} points")
    # score_player3_2.configure(text=f"{points_j3} points")
    # score_player4_2.configure(text=f"{points_j4} points")
    # score_player5_2.configure(text=f"{points_j5} points")
    player1_button_ajouter.configure(state="disabled")
    player2_button_ajouter.configure(state="disabled")
    player3_button_ajouter.configure(state="disabled")
    player4_button_ajouter.configure(state="disabled")
    player5_button_ajouter.configure(state="disabled")
    player1_button_remove.configure(state="disabled")
    player2_button_remove.configure(state="disabled")
    player3_button_remove.configure(state="disabled")
    player4_button_remove.configure(state="disabled")
    player5_button_remove.configure(state="disabled")

    print(
        f"J1: {points_j1}\nJ2: {points_j2}\nJ3: {points_j3}\nJ4: {points_j4}\nJ5: {points_j5}")
    admin_points()


### Start game ###

def start_game():
    valider_button.configure(state="normal")
    player1_button_ajouter.configure(state="normal")
    player2_button_ajouter.configure(state="normal")
    player3_button_ajouter.configure(state="normal")
    player4_button_ajouter.configure(state="normal")
    player5_button_ajouter.configure(state="normal")
    player1_button_remove.configure(state="normal")
    player2_button_remove.configure(state="normal")
    player3_button_remove.configure(state="normal")
    player4_button_remove.configure(state="normal")
    player5_button_remove.configure(state="normal")
    # prop_A.configure(text=f"A : {tab[0]['A']}")
    # prop_B.configure(text=f"B : {tab[0]['B']}")
    # prop_C.configure(text=f"C : {tab[0]['C']}")
    # prop_D.configure(text=f"D : {tab[0]['D']}")
    # t = tab[0]['Question']
    # if len(t) > 85:
    #     t = t[:85] + "\n" + t[85:]
    # question.configure(text=t)
    # start_game_btn.configure(state="disabled")


def next_question():
    valider_button.configure(state="normal")
    player1_button_ajouter.configure(state="normal")
    player2_button_ajouter.configure(state="normal")
    player3_button_ajouter.configure(state="normal")
    player4_button_ajouter.configure(state="normal")
    player5_button_ajouter.configure(state="normal")
    player1_button_remove.configure(state="normal")
    player2_button_remove.configure(state="normal")
    player3_button_remove.configure(state="normal")
    player4_button_remove.configure(state="normal")
    player5_button_remove.configure(state="normal")
    # buttonsFrame_second.pack(fill="both", expand=True, padx=20, pady=0)
    # answerFrame.forget()
    # prop_A.configure(text=f"A : {tab[0]['A']}")
    # prop_B.configure(text=f"B : {tab[0]['B']}")
    # prop_C.configure(text=f"C : {tab[0]['C']}")
    # prop_D.configure(text=f"D : {tab[0]['D']}")
    t = tab[0]['Question']
    if len(t) > 90:
        t = t[:85] + "\n" + t[85:]
    # question.configure(text=t)
    # buttonQuestion.configure(state="disabled")


def afficher_rep():
    # buttonAnswer.configure(state="disabled")
    # answer.pack(pady=20)
    # question.configure(text=f"La bonne réponse était : ")
    # buttonsFrame_second.forget()
    # answerFrame.pack(fill="both", expand=True, padx=20, pady=0)
    # answer.configure(text=f"Réponse : {tab[0]['Reponse']}")
    # buttonQuestion.configure(state="normal")
    tab.pop(0)

##########################################################################################

server = None
HOST_ADDR = "127.0.0.1"
HOST_PORT = 1234
players = {}

clients = []
clients_names = []


def accept_clients(the_server, y):
    while True:
        client, addr = the_server.accept()
        clients.append(client)

        # use a thread so as not to clog the gui thread
        threading._start_new_thread(
            send_receive_client_message, (client, addr))


def launch_server():
    global server, HOST_ADDR, HOST_PORT  # code is fine without this

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(socket.AF_INET)
    print(socket.SOCK_STREAM)

    server.bind((HOST_ADDR, HOST_PORT))
    server.listen(5)  # server is listening for client connection

    threading._start_new_thread(accept_clients, (server, " "))


def get_client_index(client_list, curr_client):
    idx = 0
    for conn in client_list:
        if conn == curr_client:
            break
        idx = idx + 1

    return idx


def send_receive_client_message(client_connection, client_ip_addr):
    global server, client_name, clients, clients_addr, joueurs
    client_msg = " "

    # send welcome message to client
    client_name = client_connection.recv(4096).decode()
    if client_name == "1":
        entry1.delete(0, "end")
        entry1.insert("end", "Joueur "+client_name + " connecté")
    elif client_name == "2":
        entry2.delete(0, "end")
        entry2.insert("end", "Joueur "+client_name + " connecté")
    elif client_name == "3":
        entry3.delete(0, "end")
        entry3.insert("end", "Joueur "+client_name + " connecté")
    elif client_name == "4":
        entry4.delete(0, "end")
        entry4.insert("end", "Joueur "+client_name + " connecté")
    elif client_name == "5":
        entry5.delete(0, "end")
        entry5.insert("end", "Joueur "+client_name + " connecté")
        
    welcome_msg = "Welcome " + client_name + ". Use 'exit' to quit"
    client_connection.send(welcome_msg.encode())

    clients_names.append(client_name)

    update_client_names_display(clients_names)  # update client names display

    while True:
        data = client_connection.recv(4096).decode()
        if not data:
            break
        if data == "exit":
            break

        client_msg = data

        idx = get_client_index(clients, client_connection)
        sending_client_name = clients_names[idx]
        joueurs[sending_client_name].append(client_connection)
        joueurs[sending_client_name].append(client_msg)
        if sending_client_name == "1":
            entry1.delete(0, "end")
            entry1.insert("end", "Joueur "+sending_client_name + " a dit "+client_msg)
        elif sending_client_name == "2":
            entry2.delete(0, "end")
            entry2.insert("end", "Joueur "+sending_client_name + " a dit "+client_msg)
        elif sending_client_name == "3":
            entry3.delete(0, "end")
            entry3.insert("end", "Joueur "+sending_client_name + " a dit "+client_msg)
        elif sending_client_name == "4":
            entry4.delete(0, "end")
            entry4.insert("end", "Joueur "+sending_client_name + " a dit "+client_msg)
        elif sending_client_name == "5":
            entry5.delete(0, "end")
            entry5.insert("end", "Joueur "+sending_client_name + " a dit "+client_msg)
        
        print(joueurs)
        # for c in clients:
        #   if c != client_connection:
        #       server_msg = str(client_msg)
        #       c.send(server_msg.encode())

    # find the client index then remove from both lists(client name list and connection list)
    idx = get_client_index(clients, client_connection)
    del clients_names[idx]
    del clients[idx]
    server_msg = "BYE!"
    client_connection.send(server_msg.encode())
    client_connection.close()

    update_client_names_display(clients_names)  # update client names display

joueurs={}

def update_client_names_display(name_list):
    global joueurs
    affichage = [entry1, entry2]
    for i in range(len(name_list)):
        joueurs[name_list[i]] = []
        joueurs[name_list[i]].append(affichage[i])
    print(joueurs)



def send_question(question):
    for player in players:
        players[player].send(question.encode())
        print(f"Question sent to {player}")


def receive_answers():
    answers = {}
    for player in players:
        answer = players[player].recv(1024).decode()
        answers[player] = answer
        print(f"Answer from {player} received")
    return answers

# def send_good_answer(answer):


def stop_server():
    global server
    server.close()
    print("Server stopped")

##########################################################################################

def emission1():
    print("Emission 1 lancée")
    global tab
    print(tab[0])

def send_props():
    global tab
    print(tab[0])
    question = tab[0]["Question"]
    reponse = tab[0]["Reponse"]
    propA = tab[0]["A"]
    propB = tab[0]["B"]
    propC = tab[0]["C"]
    propD = tab[0]["D"]
    send_question(question)
    answers = receive_answers()
    print(answers)
    # send_good_answer(reponse)
    tab.pop(0)
    print(tab[0])
    # if len(tab) == 0:
    #     buttonQuestion.configure(state="disabled")
    #     buttonAnswer.configure(state="disabled")
    #     start_game_btn.configure(state="normal")
    #     question.configure(text="Fin de la partie")
    #     prop_A.configure(text="")
    #     prop_B.configure(text="")
    #     prop_C.configure(text="")
    #     prop_D.configure(text="")
    #     answer.configure(text="")
    #     entry1.delete(0, "end")
    #     entry2.delete(0, "end")
    #     entry3.delete(0, "end")
    #     entry4.delete(0, "end")
    #     entry5.delete(0, "end")
    #     entry1.insert("end", "Joueur 1 déconnecté")
    #     entry2.insert("end", "Joueur 2 déconnecté")
    #     entry3.insert("end", "Joueur 3 déconnecté")
    #     entry4.insert("end", "Joueur 4 déconnecté")
    #     entry5.insert("end", "Joueur 5 déconnecté")
    #     entry1.configure(state="disabled")
    #     entry2.configure(state="disabled")
    #     entry3.configure(state="disabled")
    #     entry4.configure(state="disabled")
    #     entry5.configure(state="disabled")
    #     joueurs.clear()
    #     clients.clear()
    #     clients_names.clear()
    #     players.clear()
    #     print("Fin de la partie")
    #     stop_server()
    # else:
    #     entry1.delete(0, "end")
    #     entry2.delete(0, "end")
    #     entry3.delete(0, "end")
    #     entry4.delete(0, "end")
    #     entry5.delete(

### Grid ###
app.grid_columnconfigure(1, weight=1)
# app.grid_columnconfigure(4, weight=0)
app.grid_rowconfigure((0, 1, 2), weight=1)

## Frames ###

sidebar = CTkFrame(app, width=140, corner_radius=0)
sidebar.grid(row=0, column=0, rowspan=4, sticky="nsew")
sidebar.grid_rowconfigure(7, weight=1)
logo_label = CTkLabel(sidebar, text="Ajouter des points",
                      font=CTkFont(size=20))
logo_label.grid(row=0, column=0, padx=20, pady=15)

### PLAYER 1 ###

player1 = CTkFrame(sidebar, width=140, corner_radius=0)
player1.grid(row=1, column=0, sticky="nsew")
player1.grid_rowconfigure(4, weight=1)
player1_label = CTkLabel(player1, text="Joueur 1",
                         font=CTkFont(size=20, weight="bold"))
player1_label.grid(row=0, column=0, padx=20, pady=20)

player1_button_ajouter = CTkButton(
    player1, text="Ajouter", width=89, command=activate_button_j1)
player1_button_ajouter.grid(row=0, column=1, padx=8, pady=10)
player1_button_remove = CTkButton(
    player1, text="Retirer", width=89, command=retirer_j1)
player1_button_remove.grid(row=0, column=2, padx=8, pady=10)
player1_button_1 = CTkButton(
    player1, text="+1", width=25, command=lambda: add_point_j1(1))
player1_button_3 = CTkButton(
    player1, text="+3", width=25, command=lambda: add_point_j1(3))
player1_button_5 = CTkButton(
    player1, text="+5", width=25, command=lambda: add_point_j1(5))

### PLAYER 2 ###

player2 = CTkFrame(sidebar, width=140, corner_radius=0)
player2.grid(row=2, column=0, sticky="nsew")
player2.grid_rowconfigure(4, weight=1)
player2_label = CTkLabel(player2, text="Joueur 2",
                         font=CTkFont(size=20, weight="bold"))
player2_label.grid(row=0, column=0, padx=20, pady=20)

player2_button_ajouter = CTkButton(
    player2, text="Ajouter", width=89, command=activate_button_j2)
player2_button_ajouter.grid(row=0, column=1, padx=8, pady=10)
player2_button_remove = CTkButton(
    player2, text="Retirer", width=89, command=retirer_j2)
player2_button_remove.grid(row=0, column=2, padx=8, pady=10)
player2_button_1 = CTkButton(
    player2, text="+1", width=25, command=lambda: add_point_j2(1))
player2_button_3 = CTkButton(
    player2, text="+3", width=25, command=lambda: add_point_j2(3))
player2_button_5 = CTkButton(
    player2, text="+5", width=25, command=lambda: add_point_j2(5))

### PLAYER 3 ###

player3 = CTkFrame(sidebar, width=140, corner_radius=0)
player3.grid(row=3, column=0, sticky="nsew")
player3.grid_rowconfigure(4, weight=1)
player3_label = CTkLabel(player3, text="Joueur 3",
                         font=CTkFont(size=20, weight="bold"))
player3_label.grid(row=0, column=0, padx=20, pady=20)

player3_button_ajouter = CTkButton(
    player3, text="Ajouter", width=89, command=activate_button_j3)
player3_button_ajouter.grid(row=0, column=1, padx=8, pady=10)
player3_button_remove = CTkButton(
    player3, text="Retirer", width=89, command=retirer_j3)
player3_button_remove.grid(row=0, column=2, padx=8, pady=10)
player3_button_1 = CTkButton(
    player3, text="+1", width=25, command=lambda: add_point_j3(1))
player3_button_3 = CTkButton(
    player3, text="+3", width=25, command=lambda: add_point_j3(3))
player3_button_5 = CTkButton(
    player3, text="+5", width=25, command=lambda: add_point_j3(5))

### PLAYER 4 ###

player4 = CTkFrame(sidebar, width=140, corner_radius=0)
player4.grid(row=4, column=0, sticky="nsew")
player4.grid_rowconfigure(4, weight=1)
player4_label = CTkLabel(player4, text="Joueur 4",
                         font=CTkFont(size=20, weight="bold"))
player4_label.grid(row=0, column=0, padx=20, pady=20)

player4_button_ajouter = CTkButton(
    player4, text="Ajouter", width=89, command=activate_button_j4)
player4_button_ajouter.grid(row=0, column=1, padx=8, pady=10)
player4_button_remove = CTkButton(
    player4, text="Retirer", width=89, command=retirer_j4)
player4_button_remove.grid(row=0, column=2, padx=8, pady=10)
player4_button_1 = CTkButton(
    player4, text="+1", width=25, command=lambda: add_point_j4(1))
player4_button_3 = CTkButton(
    player4, text="+3", width=25, command=lambda: add_point_j4(3))
player4_button_5 = CTkButton(
    player4, text="+5", width=25, command=lambda: add_point_j4(5))


### PLAYER 5 ###

player5 = CTkFrame(sidebar, width=140, corner_radius=0, height=100)
player5.grid(row=5, column=0, sticky="nsew")
player5.grid_rowconfigure(4, weight=1)
player5_label = CTkLabel(player5, text="Joueur 5",
                         font=CTkFont(size=20, weight="bold"))
player5_label.grid(row=0, column=0, padx=20, pady=20)

player5_button_ajouter = CTkButton(
    player5, text="Ajouter", width=89, command=activate_button_j5)
player5_button_ajouter.grid(row=0, column=1, padx=8, pady=10)
player5_button_remove = CTkButton(
    player5, text="Retirer", width=89, command=retirer_j5)
player5_button_remove.grid(row=0, column=2, padx=8, pady=10)
player5_button_1 = CTkButton(
    player5, text="+1", width=25, command=lambda: add_point_j5(1))
player5_button_3 = CTkButton(
    player5, text="+3", width=25, command=lambda: add_point_j5(3))
player5_button_5 = CTkButton(
    player5, text="+5", width=25, command=lambda: add_point_j5(5))

### Points ###

points_frame = CTkFrame(sidebar, corner_radius=0)
points_frame.grid(row=6, column=0, sticky="nsew")
points_frame.grid_rowconfigure(2, weight=1)
points_label = CTkLabel(points_frame, text="Points à assigner",
                        font=CTkFont(size=20, weight="bold"))
points_label.grid(row=0, column=0, padx=20, pady=20)

label_frame = CTkFrame(points_frame, corner_radius=0)
label_frame.grid(row=1, column=0, sticky="nsew")
label_frame.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)


points_j1_label = CTkLabel(label_frame, text="J1: 0", font=CTkFont(size=18))
points_j1_label.grid(row=1, column=0, padx=20, pady=10)

points_j2_label = CTkLabel(label_frame, text="J2: 0", font=CTkFont(size=18))
points_j2_label.grid(row=1, column=1, padx=20, pady=10)

points_j3_label = CTkLabel(label_frame, text="J3: 0", font=CTkFont(size=18))
points_j3_label.grid(row=1, column=2, padx=20, pady=10)

points_j4_label = CTkLabel(label_frame, text="J4: 0", font=CTkFont(size=18))
points_j4_label.grid(row=1, column=3, padx=20, pady=10)

points_j5_label = CTkLabel(label_frame, text="J5: 0", font=CTkFont(size=18))
points_j5_label.grid(row=1, column=4, padx=20, pady=10)

### Valider ###

valider_frame = CTkFrame(sidebar, corner_radius=0)
valider_frame.grid(row=7, column=0, sticky="nsew")
valider_frame.grid_columnconfigure(0, weight=1)
valider_button = CTkButton(
    valider_frame, text="Valider", width=250, command=valider_points)
valider_button.grid(row=0, column=0, padx=20, pady=20)


### Main Frame ###
main_frame = CTkFrame(app, corner_radius=0)
main_frame.grid(row=0, column=1, rowspan=4, sticky="nsew")
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_rowconfigure(0, weight=1)

# Ajouter un bouton question suivante et un bouton afficher la réponse

# Frame buttons


text = CTkLabel(main_frame, text="Panneau d'administration",
                font=CTkFont(size=20))
text.pack(pady=15)

buttonsFrame = CTkFrame(main_frame, corner_radius=0)
buttonsFrame.pack(fill="both", expand=True, padx=20, pady=0)

# start_game_btn = CTkButton(
#     buttonsFrame, text="Commencer la partie", width=250, command=start_game)
# start_game_btn.pack(pady=12)


# buttonAnswer = CTkButton(buttonsFrame, text="Afficher la réponse",
#                          width=250, command=afficher_rep)
# buttonAnswer.pack(pady=12)

# buttons to create emission 1 to 5

emission1 = CTkButton(buttonsFrame, text="Emission 1",
                      width=250, command=emission1)
emission1.pack(pady=12)

emission2 = CTkButton(buttonsFrame, text="Emission 2",
                      width=250, command=emission1)
emission2.pack(pady=12)

emission3 = CTkButton(buttonsFrame, text="Emission 3",
                      width=250, command=emission1)
emission3.pack(pady=12)

emission4 = CTkButton(buttonsFrame, text="Emission 4",
                      width=250, command=emission1)
emission4.pack(pady=12)

emission5 = CTkButton(buttonsFrame, text="Emission 5",
                      width=250, command=emission1)
emission5.pack(pady=12)


### Second frame ###

second_frame = CTkFrame(app, corner_radius=0)
second_frame.grid(row=0, column=2, rowspan=4, sticky="nsew")

text2 = CTkLabel(second_frame, text="Panneau de jeu",
                 font=CTkFont(size=20))
text2.pack(pady=15)

# Frame buttons

buttons_frame_2 = CTkFrame(second_frame, corner_radius=0)
buttons_frame_2.pack(fill="both", expand=True)

### Buttons ###

envoi_propositions = CTkButton(buttons_frame_2, text="Envoyer les propositions",
                               width=250, hover=True, command=send_props)
envoi_propositions.pack(pady=12)

afficher_reponse = CTkButton(buttons_frame_2, text="Afficher la réponse",
                             width=250, hover=True)
afficher_reponse.pack(pady=12)

afficher_score = CTkButton(buttons_frame_2, text="Afficher le score",
                           width=250, hover=True)
afficher_score.pack(pady=12)

x = 0


def test_button():
    global x
    x += 1
    entry1.delete(0, "end")
    entry2.delete(0, "end")
    entry3.delete(0, "end")
    entry4.delete(0, "end")
    entry5.delete(0, "end")
    entry1.insert(0, "test"+str(x))
    entry2.insert(0, "test"+str(x))
    entry3.insert(0, "test"+str(x))
    entry4.insert(0, "test"+str(x))
    entry5.insert(0, "test"+str(x))


buttonQuestion = CTkButton(buttons_frame_2, text="Question suivante",
                           width=250, hover=True)
buttonQuestion.pack(pady=12)

test_button = CTkButton(buttons_frame_2, text="Lancement serveur",
                        width=250, command=launch_server, hover=True)
test_button.pack(pady=25)


### Third frame ###

third_frame = CTkFrame(app, corner_radius=0)
third_frame.grid(row=0, column=3, rowspan=4, sticky="nsew")

text3 = CTkLabel(third_frame, text="Retour Clients",
                 font=CTkFont(size=20))

text3.pack(pady=15)

# Frame entry boxes

entry_frame = CTkFrame(third_frame, corner_radius=0)
entry_frame.pack(fill="both", expand=True, padx=20, pady=0)

### Entry boxes ###

entry1 = CTkEntry(entry_frame, width=250, height=85)
entry1.pack(pady=12)

entry2 = CTkEntry(entry_frame, width=250, height=85)
entry2.pack(pady=12)

entry3 = CTkEntry(entry_frame, width=250, height=85)
entry3.pack(pady=12)

entry4 = CTkEntry(entry_frame, width=250, height=85)
entry4.pack(pady=12)

entry5 = CTkEntry(entry_frame, width=250, height=85)
entry5.pack(pady=12)


### Seconde fenêtre ###

# window = CTkToplevel(app)
# window.title("Panneau de jeu")
# window.geometry("1920x1080")
# window.grid_columnconfigure(1, weight=1)
# window.grid_columnconfigure((2, 3), weight=0)
# window.grid_rowconfigure((0, 1, 2), weight=1)

# ### Sidebar ###
# sidebar_second = CTkFrame(window, width=550, corner_radius=0)
# sidebar_second.grid(row=0, column=0, rowspan=4, sticky="nsew")
# sidebar_second.grid_rowconfigure(7, weight=1)

# logo_label = CTkLabel(sidebar_second, text="Scores",
#                       font=CTkFont(size=45))
# logo_label.grid(row=0, column=0, padx=20, pady=30)

# ### PLAYERS ###

# score_player1 = CTkLabel(sidebar_second, text="Joueur 1 : ",
#                          font=CTkFont(size=40))
# score_player1.grid(row=1, column=0, padx=20, pady=55)
# score_player1_2 = CTkLabel(sidebar_second, text="0 points", text_color="#1d6ca4",
#                            font=CTkFont(size=40))
# score_player1_2.grid(row=1, column=1, padx=20, pady=55)

# score_player2 = CTkLabel(sidebar_second, text="Joueur 2 : ",
#                          font=CTkFont(size=40))
# score_player2.grid(row=2, column=0, padx=20, pady=55)
# score_player2_2 = CTkLabel(sidebar_second, text="0 points", text_color="#1d6ca4",
#                            font=CTkFont(size=40))
# score_player2_2.grid(row=2, column=1, padx=20, pady=55)

# score_player3 = CTkLabel(sidebar_second, text="Joueur 3 : ",
#                          font=CTkFont(size=40))
# score_player3.grid(row=3, column=0, padx=20, pady=55)
# score_player3_2 = CTkLabel(sidebar_second, text="0 points", text_color="#1d6ca4",
#                            font=CTkFont(size=40))
# score_player3_2.grid(row=3, column=1, padx=20, pady=55)

# score_player4 = CTkLabel(sidebar_second, text="Joueur 4 : ",
#                          font=CTkFont(size=40))
# score_player4.grid(row=4, column=0, padx=20, pady=55)
# score_player4_2 = CTkLabel(sidebar_second, text="0 points", text_color="#1d6ca4",
#                            font=CTkFont(size=40))
# score_player4_2.grid(row=4, column=1, padx=20, pady=55)

# score_player5 = CTkLabel(sidebar_second, text="Joueur 5 : ",
#                          font=CTkFont(size=40))
# score_player5.grid(row=5, column=0, padx=20, pady=55)
# score_player5_2 = CTkLabel(sidebar_second, text="0 points", text_color="#1d6ca4",
#                            font=CTkFont(size=40))
# score_player5_2.grid(row=5, column=1, padx=20, pady=55)

# ### Begining of the game frame ###


# ### Main Frame ###
# main_frame_second = CTkFrame(window, corner_radius=0)
# main_frame_second.grid(row=0, column=1, rowspan=4, sticky="nsew")

# ### Question ###
# # len = 85 == 1 ligne, len > 85 = 2 lignes
# question = CTkLabel(main_frame_second, text=f"Question", font=CTkFont(size=30))
# question.pack(pady=15)

# ### Labels ###

# buttonsFrame_second = CTkFrame(main_frame_second, corner_radius=0)
# buttonsFrame_second.pack(fill="both", expand=True, padx=20, pady=0)
# buttonsFrame_second.grid_columnconfigure(0, weight=1)
# buttonsFrame_second.grid_rowconfigure(5, weight=1)

# prop_A = CTkLabel(buttonsFrame_second, text=f"A : ", font=CTkFont(size=40))
# prop_A.grid(row=0, column=0, padx=20, pady=25)

# prop_B = CTkLabel(buttonsFrame_second, text=f"B : ", font=CTkFont(size=40))
# prop_B.grid(row=1, column=0, padx=20, pady=25)

# prop_C = CTkLabel(buttonsFrame_second, text=f"C : ", font=CTkFont(size=40))
# prop_C.grid(row=2, column=0, padx=20, pady=25)

# prop_D = CTkLabel(buttonsFrame_second, text=f"D : ", font=CTkFont(size=40))
# prop_D.grid(row=3, column=0, padx=20, pady=25)


### Affichage bonne réponse ###

# answerFrame = CTkFrame(main_frame_second, corner_radius=0)
# answerFrame.pack(fill="both", expand=True, padx=20, pady=0)


# answer = CTkLabel(answerFrame, text=f"Réponse : ", font=CTkFont(size=40))
# answer.pack(pady=20)

app.mainloop()
