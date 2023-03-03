import sys
import tkinter as tk
from tkinter import ttk
from tkinter import *
import requests
import stmol
from stmol import showmol
import py3Dmol


class CoreGUI(object):
    def render_mol(pdb):
        pdbview = py3Dmol.view()
        pdbview.addModel(pdb,'pdb')
        pdbview.setStyle({'cartoon':{'color':'spectrum'}})
        pdbview.setBackgroundColor('white')#('0xeeeeee')
        pdbview.zoomTo()
        pdbview.zoom(2, 800)
        pdbview.spin(True)
        showmol(pdbview, height = 500,width=800)
        showmol(render_pdb_resn(viewer = render_pdb(id = '1A2C'),resn_lst = ['ALA',]),height=700,width=700)
        render_mol(pdb_string)
    
    
    def __init__(self,parent):
        self.parent = parent
       
        self.InitUI()
        button = Button(self.parent, text="Start", command=self.main)
       # buttontwo = Button(self.parent, text="Starttwo", command=pdb.render_mol)
        button.grid(column=0, row=1, columnspan=2)
       # buttontwo.grid(column=0, row=1, columnspan=3)
    def main(self):
        print('whatever')
        master = tk.Tk()
        master.geometry('500x450')
        master.resizable(0,0)
        e = Entry(master)
        e.pack()

        e.focus_set()

        DEFAULT_SEQ = "MGSSHHHHHHSSGLVPRGSHMRGPNPTAASLEASAGPFTVRSFTVSRPSGYGAGTVYYPTNAGGTVGAIAIVPGYTARQSSIKWWGPRLASHGFVVITIDTNSTLDQPSSRSSQQMAALRQVASLNGTSSSPIYGKVDTARMGVMGWSMGGGGSLISAANNPSLKAAAPQAPWDSSTNFSSVTVPTLIFACENDSIAPVNSSALPIYDSMSRNAKQFLEINGGSHSCANSGNSNQALIGKKGVAWMKRFMDNDTRYSTFACENPNSTRVSDFRTANCSLEDPAANKARKEAELAAATAEQ"

        sequence=DEFAULT_SEQ

        headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
            }
        response = requests.post('https://api.esmatlas.com/foldSequence/v1/pdb/', headers=headers, data=sequence)
        name = sequence[:3] + sequence[-3:]
        pdb_string = response.content.decode('utf-8')
        print(pdb_string)
        print(name)
        txt = Button(master, text = "OK", width = 10, command = requests.post('https://api.esmatlas.com/foldSequence/v1/pdb/', headers=headers, data=sequence) )
        txt.pack()

        sys.stdout = StdoutRedirector(self.text_box)
        master.mainloop()
        
    
    def InitUI(self):
        self.text_box = Text(self.parent, wrap='word', height = 11, width=50)
        self.text_box.grid(column=0, row=0, columnspan = 2, sticky='NSWE', padx=5, pady=5)
        sys.stdout = StdoutRedirector(self.text_box)

class StdoutRedirector(object):
    def __init__(self,text_widget):
        self.text_space = text_widget

    def write(self,string):
        self.text_space.insert('end', string)
        self.text_space.see('end')

class Interface(ttk.Frame):
    def __init__(self,parent=None):
        ttk.Frame.__init__(self,parent)
        self.parent = parent
        self.New_Window()

    def New_Window(self):
        self.newWindow = Tk.Toplevel(self.parent)
        self.app = CoreGUI(self.newWindow)
        
        
        
root = Tk()

gui = CoreGUI(root)
root.mainloop()
