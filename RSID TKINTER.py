import sys
import stmol
from stmol import *
import tkinter as tk
from tkinter import ttk
from tkinter import *
import requests
import biotite.structure.io as bsio
import webbrowser
from stmol import showmol
import py3Dmol

DEFAULT_SEQ = "MGSSHHHHHHSSGLVPRGSHMRGPNPTAASLEASAGPFTVRSFTVSRPSGYGAGTVYYPTNAGGTVGAIAIVPGYTARQSSIKWWGPRLASHGFVVITIDTNSTLDQPSSRSSQQMAALRQVASLNGTSSSPIYGKVDTARMGVMGWSMGGGGSLISAANNPSLKAAAPQAPWDSSTNFSSVTVPTLIFACENDSIAPVNSSALPIYDSMSRNAKQFLEINGGSHSCANSGNSNQALIGKKGVAWMKRFMDNDTRYSTFACENPNSTRVSDFRTANCSLEDPAANKARKEAELAAATAEQ"

class CoreGUI(object):
    def __init__(self,parent):
        self.parent = parent
        self.InitUI()
        button = Button(self.parent, text="Start", command=lambda: [self.main, update(sequence=DEFAULT_SEQ), render_mol(pdb)])
        button.grid(column=0, row=1, columnspan=2)
        
        #buttontwo = Button(self, text = "test", lambda: [f() for f in [func1, funct2]])
        #buttontwo = Button(self.parent, text="Start", command=self.main)
        #buttontwo.grid(column=0, row=1, columnspan=2)
        
    def main(self):
        print('whatever')
        master = tk.Tk()
        master.geometry('500x450')
        master.resizable(0,0)
        e = Entry(master)
        e.pack()

        e.focus_set()
        
        #DEFAULT_SEQ = "MGSSHHHHHHSSGLVPRGSHMRGPNPTAASLEASAGPFTVRSFTVSRPSGYGAGTVYYPTNAGGTVGAIAIVPGYTARQSSIKWWGPRLASHGFVVITIDTNSTLDQPSSRSSQQMAALRQVASLNGTSSSPIYGKVDTARMGVMGWSMGGGGSLISAANNPSLKAAAPQAPWDSSTNFSSVTVPTLIFACENDSIAPVNSSALPIYDSMSRNAKQFLEINGGSHSCANSGNSNQALIGKKGVAWMKRFMDNDTRYSTFACENPNSTRVSDFRTANCSLEDPAANKARKEAELAAATAEQ"

        #sequence=DEFAULT_SEQ

       # headers = {
       # 'Content-Type': 'application/x-www-form-urlencoded',
           # }
      #  response = requests.post('https://api.esmatlas.com/foldSequence/v1/pdb/', headers=headers, data=sequence)
      #  name = sequence[:3] + sequence[-3:]
      #  pdb_string = response.content.decode('utf-8')
       # print(pdb_string)
      #  print(name)
        

        #sys.stdout = StdoutRedirector(self.text_box)
        master.mainloop()
    def InitUI(self):
        self.text_box = Text(self.parent, wrap='word', height = 11, width=50)
        self.text_box.grid(column=0, row=0, columnspan = 2, sticky='NSWE', padx=5, pady=5)
        sys.stdout = StdoutRedirector(self.text_box)
        
        
#DEFAULT_SEQ = "MGSSHHHHHHSSGLVPRGSHMRGPNPTAASLEASAGPFTVRSFTVSRPSGYGAGTVYYPTNAGGTVGAIAIVPGYTARQSSIKWWGPRLASHGFVVITIDTNSTLDQPSSRSSQQMAALRQVASLNGTSSSPIYGKVDTARMGVMGWSMGGGGSLISAANNPSLKAAAPQAPWDSSTNFSSVTVPTLIFACENDSIAPVNSSALPIYDSMSRNAKQFLEINGGSHSCANSGNSNQALIGKKGVAWMKRFMDNDTRYSTFACENPNSTRVSDFRTANCSLEDPAANKARKEAELAAATAEQ"

        #sequence=DEFAULT_SEQ        
        
def update(sequence=DEFAULT_SEQ):
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
            }
        response = requests.post('https://api.esmatlas.com/foldSequence/v1/pdb/', headers=headers, data=sequence)
        name = sequence[:3] + sequence[-3:]
        pdb_string = response.content.decode('utf-8')

        with open('predicted.pdb', 'w') as f:
            f.write(pdb_string)

        struct = bsio.load_structure('predicted.pdb', extra_fields=["b_factor"])
        b_value = round(struct.b_factor.mean(), 4)
        print(struct.b_factor.mean())
        # Display protein structure
        #st.subheader('Visualization of predicted protein structure')
        render_mol(pdb_string)
        
        
        master = tk.Tk()
        master.geometry('500x450')
        master.resizable(0,0)
        e = Entry(master)
        e.pack()
        
        
        txt = Button(master, text = "OK", width = 10, command = requests.post('https://api.esmatlas.com/foldSequence/v1/pdb/', headers=headers, data=sequence) )
        txt.pack()
        txttwo = Button(master, text = "OK", width = 10, command = update )
        txttwo.pack()
        print(name)
        print(pdb_string)
    # plDDT value is stored in the B-factor field
    #st.subheader('plDDT')
   # st.write('plDDT is a per-residue estimate of the confidence in prediction on a scale from 0-100.')
    #st.info(f'plDDT: {b_value}')

    
    
        #sys.stdout = StdoutRedirector(self.text_box)
        master.mainloop()
            
   # st.download_button(
   #     label="Download PDB",
   #     data=pdb_string,
   #     file_name='predicted.pdb',
    #    mime='text/plain',
   # )

#predict = st.sidebar.button('Predict', on_click=update)

def render_mol(pdb):
        sequence=DEFAULT_SEQ
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
            }
        response = requests.post('https://api.esmatlas.com/foldSequence/v1/pdb/', headers=headers, data=sequence)
        name = sequence[:3] + sequence[-3:]
        pdb_string = response.content.decode('utf-8')

        with open('predicted.pdb', 'w') as f:
            f.write(pdb_string)
        with open("predicted.pdb") as ifile:
            system = "".join([x for x in ifile])
        view = py3Dmol.view(width=600, height=400)
        view.addModelsAsFrames(system)
        view.setStyle({"model": -1}, {"cartoon": {"color": "spectrum"}})
        view.zoomTo()
        view.show()
    
        pdbview = py3Dmol.view()
       # pdbview.addModel(pdb,'pdb')
       # pdbview.setStyle({'cartoon':{'color':'spectrum'}})
       # pdbview.setBackgroundColor('white')#('0xeeeeee')
       # pdbview.zoomTo()
       # pdbview.zoom(2, 800)
       # pdbview.spin(True)
        showmol(pdbview, height = 500,width=800)
        #showmol(render_pdb_resn())
        

        #view = py3Dmol.view(width=400, height=300)
        #view.addModelsAsFrames(system)
        #view.setStyle({'model': -1}, {"cartoon": {'color': 'spectrum'}})
        #view.zoomTo()
        #view.show()

class StdoutRedirector(object):
    def __init__(self,text_widget):
        self.text_space = text_widget

    def write(self,string):
        self.text_space.insert('end', string)
        self.text_space.see('end')
    def flush(self):
        pass
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
