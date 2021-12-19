from os import path, mkdir, remove
import glob
import shutil
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot, QTimer
from UIs.SetupWindow import Ui_SetupWindow
from mods.ScanBond import AtomBond
from mods.common_functions import atom_distance, random_color, write_file
import copy
import sys 

class CalcSetupWindow(QtWidgets.QMainWindow, Ui_SetupWindow):
    def __init__(self, parent, filepath):
        super(CalcSetupWindow, self).__init__(parent)
        self.react = parent
        self.filepath = filepath
        self.settings = self.react.settings

        self.pymol = False
        if self.react.pymol:
            self.pymol = self.react.pymol
            self.pymol.pymol_cmd("set mouse_selection_mode, 0")
            self.pymol.pymol_cmd("hide cartoon")

            # Monitor clicks in pymol stdout_handler
            self.pymol.monitor_clicks()
            # Connect signals from pymol:
            self.pymol.atomsSelectedSignal.connect(self.pymol_atom_clicked)

        self.ui = Ui_SetupWindow()
        self.ui.setupUi(self)

        # TODO optimize this?:
        screen_size = QtWidgets.QDesktopWidget().screenGeometry()
        window_size = self.geometry()
        self.move(int(((screen_size.width() - window_size.width()) / 2)) - 250, 100)

        self.setWindowTitle("REACT - Calculation setup")

        self.mol_obj = self.react.states[self.react.state_index].get_molecule_object(self.filepath)
        self.charge = self.mol_obj.charge
        self.multiplicity = self.mol_obj.multiplicity
        self.filename = self.mol_obj.filename.split(".")[0] 

        # we need to make a local copy of all info job-related stuff,
        # So that we dont change the attributes in Settings object
        self.functional = copy.deepcopy(self.settings.functional)
        self.basis = copy.deepcopy(self.settings.basis)
        self.basis_diff = copy.deepcopy(self.settings.basis_diff)
        self.basis_pol1 = copy.deepcopy(self.settings.basis_pol1)
        self.basis_pol2 = copy.deepcopy(self.settings.basis_pol2)
        # -2 = low (#t), -3 = normal (# or #n), -4 = high (#p) 
        self.output_print = "#" # TODO add this to settings class?
        self.additional_keys = copy.deepcopy(self.settings.additional_keys)
        self.job_type = "Opt"
        self.opt_freq_combi = False
        self.job_options = copy.deepcopy(self.settings.job_options)
        self.link0_options = copy.deepcopy(self.settings.link0_options)

        self.Qbutton_group = QtWidgets.QButtonGroup(self)
        self.Qbutton_group.addButton(self.ui.radioButton)
        self.Qbutton_group.addButton(self.ui.radioButton_2)
        self.Qbutton_group.addButton(self.ui.radioButton_3)
        self.link0_checkboxes = {self.ui.checkBox_chk: self.ui.lineEdit_chk,
                      self.ui.checkBox_mem_2: self.ui.lineEdit_mem_2,
                      self.ui.checkBox_oldchk: self.ui.lineEdit_oldchk}

        self.opt_freq_details = {"checked": False, "keywords": []}
        self.num_files = 1
        self.multiple_files = {}
        self.atom_bonds = {}
        self.Qbutton_scan_group = QtWidgets.QButtonGroup(self)
        self.Qbutton_scan_group.addButton(self.ui.radioButton_plus)
        self.Qbutton_scan_group.addButton(self.ui.radioButton_minus)
        self.Qbutton_scan_group.addButton(self.ui.radioButton_both)

        self.insert_model_atoms()
        self.fill_main_tab()

        self.ui.Button_add_job.clicked.connect(lambda: self.add_item_to_list(self.ui.LineEdit_add_job, self.ui.List_add_job, self.job_options[self.job_type]))
        self.ui.Button_del_job.clicked.connect(lambda:  self.del_item_from_list(self.ui.List_add_job, self.job_options[self.job_type]))
        self.ui.Button_add_link0.clicked.connect(lambda: self.add_item_to_list(self.ui.LineEdit_link0, self.ui.list_link0, self.link0_options))
        self.ui.Button_del_link0.clicked.connect(lambda: self.del_item_from_list(self.ui.list_link0, self.link0_options))
        self.ui.Button_add_job_2.clicked.connect(lambda: self.add_item_to_list(self.ui.LineEdit_add_job_2, self.ui.List_add_job_2, self.additional_keys))
        self.ui.Button_del_job_2.clicked.connect(lambda: self.del_item_from_list(self.ui.List_add_job_2, self.additional_keys))
        self.ui.comboBox_basis1.currentIndexChanged.connect(self.update_basis1)
        self.ui.comboBox_basis2.currentIndexChanged.connect(self.update_basis2)
        self.ui.comboBox_basis3.currentIndexChanged.connect(self.update_basis3)
        self.ui.comboBox_basis4.currentIndexChanged.connect(self.update_basis4)
        self.ui.comboBox_funct.currentTextChanged.connect(self.update_functional)
        self.ui.comboBox_job_type.currentTextChanged.connect(self.update_job_details)
        self.ui.ComboBox_files.currentTextChanged.connect(self.update_preview_combobox)
        self.ui.button_close.clicked.connect(self.on_close)
        self.ui.button_write.clicked.connect(self.on_write)
        self.ui.checkBox_mem_2.clicked.connect(lambda: self.route_checkboxes_update(self.ui.checkBox_mem_2, self.ui.lineEdit_mem_2))
        self.ui.checkBox_chk.clicked.connect(lambda: self.route_checkboxes_update(self.ui.checkBox_chk, self.ui.lineEdit_chk))
        self.ui.checkBox_oldchk.clicked.connect(lambda: self.route_checkboxes_update(self.ui.checkBox_oldchk, self.ui.lineEdit_oldchk))
        self.ui.button_add_freeze.clicked.connect(self.add_freeze_atoms)
        self.ui.button_delete_freeze.clicked.connect(self.remove_freeze_atoms)
        self.ui.button_auto_freeze.clicked.connect(self.auto_freeze_atoms)
        self.ui.button_add_scan.clicked.connect(self.add_scan_atoms)
        self.ui.button_delete_scan.clicked.connect(self.remove_scan_atoms)
        self.ui.lineEdit_filename.textChanged.connect(self.filename_update)
        self.ui.lineEdit_charge.textChanged.connect(self.update_charge)
        self.ui.lineEdit_multiplicity.textChanged.connect(self.update_multiplicity)
        self.ui.tabWidget.currentChanged.connect(self.update_preview)
        self.Qbutton_group.buttonClicked.connect(self.update_print_button)
        self.ui.checkbox_freq.clicked.connect(self.toggle_raman)
        self.Qbutton_scan_group.buttonClicked.connect(self.on_scan_mode_changed)
        self.ui.spinbox_scan_pm.valueChanged.connect(lambda: self.on_spinbox_changed(self.ui.spinbox_scan_pm))
        self.ui.spinbox_scan_increment.valueChanged.connect(lambda: self.on_spinbox_changed(self.ui.spinbox_scan_increment))
        self.ui.button_invert.clicked.connect(self.on_invert_atoms)
        self.ui.checkBox_moveboth.clicked.connect(self.on_move_both_changed)


        self.ui.list_model.itemSelectionChanged.connect(self.model_atom_clicked)
        self.ui.list_model.setSelectionMode(1)

        self.ui.list_freeze_atoms.itemSelectionChanged.connect(self.freeze_list_clicked)
        self.ui.list_scan_bonds.itemSelectionChanged.connect(self.scan_list_clicked)

        self.atoms_to_select = 1
        self.enable_scan(enable=False)
        self.ui.comboBox_freezetype.currentTextChanged.connect(self.change_selection_mode)

        # Keep track of atoms selected (for multiple selection options)
        self.selected_indexes = list()

        # Pymol returns ordered atom id list, so we need to keep track of click order
        self.selected_ids = list()

        self.toggle_raman()

    @property
    def scan_bond(self):
        """
        Return AtomBond obj representing the bond selected from the scan list
        """
        return self.atom_bonds[self.ui.list_scan_bonds.currentItem().text()]

    def on_invert_atoms(self):

        if self.ui.list_scan_bonds.count() < 1:
            return

        self.scan_bond.invert_atoms()
        self.ui.lineEdit_freeze.setText(str(self.scan_bond.atom1_idx))
        self.ui.lineEdit_move.setText(str(self.scan_bond.atom2_idx))
        self.update_scan()

    def on_move_both_changed(self):

        if self.ui.list_scan_bonds.count() < 1:
            return

        if self.ui.checkBox_moveboth.isChecked():
            self.scan_bond.move_both == True
            disable = True
        else:
            self.scan_bond.move_both == False
            disable = False

        self.ui.button_invert.setDisabled(disable)
        self.ui.lineEdit_freeze.setDisabled(disable)
        self.ui.lineEdit_move.setDisabled(disable)
        self.update_scan()

    def change_selection_mode(self):
        if self.ui.comboBox_freezetype.currentText() == "Atoms":
            self.ui.list_model.setSelectionMode(1)
        else:
            self.ui.list_model.setSelectionMode(2)

        select = {"Atom": 1, "Bond": 2, "Angle": 3, "Dihedral": 4}
        self.atoms_to_select = select[self.ui.comboBox_freezetype.currentText()]

    def enable_scan(self, enable=True):
        self.ui.button_add_scan.setEnabled(enable)
        #self.ui.button_delete_scan.setEnabled(enable)
        self.ui.spinbox_radius.setEnabled(enable)
        self.ui.spinbox_scan_pm.setEnabled(enable)
        self.ui.spinbox_scan_increment.setEnabled(enable)

    @pyqtSlot(list)
    def pymol_atom_clicked(self, ids):
        """
        Get atoms selected in pymol and select deselect in model atom listwidget
        """
        if not ids or None in ids:
            return

        ids = [int(x) - 1 for x in ids]

        # Effective when len(ids) > len(self.selected_ids)
        unsele = list(set(self.selected_ids) - set(ids))
        for id in unsele:
            self.ui.list_model.item(id).setSelected(False)
            self.selected_ids.pop(self.selected_ids.index(id))

        # Effective when len(ids) < len(self.selected_ids)
        new_select = list(set(ids) - set(self.selected_ids))
        for id in new_select:
            self.selected_ids.append(id)
            if len(self.selected_ids) > self.atoms_to_select:
                self.selected_ids.pop(0)
            self.ui.list_model.item(id).setSelected(True)

    def model_atom_clicked(self):
        """
        When selection i atom list is changed, update, and communicate with pymol
        """

        sele = self.ui.list_model.selectedIndexes()

        while len(sele) > self.atoms_to_select:
            if len(self.selected_indexes) > 0:
                self.ui.list_model.item(self.selected_indexes.pop(0).row()).setSelected(False)
            else:
                self.ui.list_model.item(sele.pop(0).row()).setSelected(False)
            sele = self.ui.list_model.selectedIndexes()

        self.selected_indexes = sele

        atoms = list()
        coordinates = list()
        for i in self.selected_indexes:
            atoms.append(self.mol_obj.molecule[i.row() + 1].atom_index)
            coordinates.append(self.mol_obj.molecule[i.row() + 1].coordinate)

        if self.ui.comboBox_freezetype.currentText() == "Bond" and len(atoms) == 2:
            self.enable_scan(enable=True)
            r = atom_distance(coordinates[0], coordinates[1])
            self.ui.spinbox_radius.setValue(r)
        else:
            self.enable_scan(enable=False)

        if self.pymol:
            self.update_pymol_selection(atoms=atoms)

    def freeze_list_clicked(self):
        """
        When entry in "Atoms to freeze" is clicked, update to selected in "Atoms in model" list and pymol
        """
        try:
            indexes = [int(x) - 1 for x in self.ui.list_freeze_atoms.currentItem().text().split()[1:-1]]
        except AttributeError:
            return
        freeze_type = {1: "Atom", 2: "Bond", 3: "Angle", 4: "Dihedral"}
        self.ui.comboBox_freezetype.setCurrentText(freeze_type[len(indexes)])

        self.selected_indexes = indexes
        self.ui.list_model.clearSelection()

        for index in indexes:
            self.ui.list_model.item(index).setSelected(True)

    def update_pymol_selection(self, atoms):
        group = "state_%d" % self.react.get_current_state
        self.pymol.set_selection(atoms=atoms, sele_name="sele", object_name=self.mol_obj.molecule_name, group=group)

    def add_freeze_atoms(self):
        """
        Adds selected atoms to freeze section - append F to end of str for freeze
        """
        if len(self.selected_indexes) < 1:
            return
        type = "F"
        g_cmd = {"Atom": "X", "Bond": "B", "Angle": "A", "Dihedral": "D"}
        atoms = ""
        for i in self.selected_indexes:
            atomnr = self.mol_obj.molecule[i.row() + 1].atom_index
            if self.pymol:
                self.pymol_spheres(atomnr)
            atoms += f"{atomnr } "

        self.ui.list_freeze_atoms.insertItem(0, f"{g_cmd[self.ui.comboBox_freezetype.currentText()]} {atoms} {type}")

    def remove_freeze_atoms(self):
        """
        Removes selected freeze atoms/bonds/angles/torsions
        """
        # Get rows for selected to delete:
        to_del = [self.ui.list_freeze_atoms.row(x) for x in self.ui.list_freeze_atoms.selectedItems()]
        for row in to_del:
            print(row)
            if self.pymol:
                for i in self.ui.list_freeze_atoms.item(row).text().split()[1:-1]:
                    self.pymol_spheres(atom_nr=i, hide=True)

            self.ui.list_freeze_atoms.takeItem(row)
    
    def on_spinbox_changed(self, spinbox):
        if spinbox == self.ui.spinbox_scan_pm:
            self.scan_bond.scan_dist = spinbox.value()
        elif spinbox == self.ui.spinbox_scan_increment:
            self.scan_bond.step_size = spinbox.value()
        
        self.update_scan()

    def add_scan_atoms(self):
        """
        First, gather information from the UI. Then, pass all information
        to a new instance of AtomBond object.
        """

        freeze = ""
        atoms = list()
        bond_size = self.ui.spinbox_radius.value()
        scan_size = self.ui.spinbox_scan_pm.value()
        scan_increment = self.ui.spinbox_scan_increment.value()

        for i in self.selected_indexes:
            atoms.append(self.mol_obj.molecule[i.row() + 1].atom_index)
            freeze += f"{self.mol_obj.molecule[i.row() + 1].atom_name} ({self.mol_obj.molecule[i.row() + 1].atom_index})    "

        if self.ui.radioButton_plus.isChecked():
            scan_mode = '+'
        elif self.ui.radioButton_minus.isChecked():
            scan_mode = '-'
        else:
            scan_mode = '+/-'

        self.atom_bonds[freeze] = AtomBond(self.mol_obj.formatted_xyz,
                                           atoms[0], atoms[1], bond_size, scan_size,
                                           scan_increment, self.ui.checkBox_moveboth.isChecked(),
                                           scan_mode)


        list_item = QtWidgets.QListWidgetItem(freeze)
        self.ui.list_scan_bonds.addItem(list_item)
        self.ui.list_scan_bonds.setCurrentItem(list_item)
        self.ui.lineEdit_freeze.setText(str(atoms[0]))
        self.ui.lineEdit_move.setText(str(atoms[1]))

        self.update_scan()

    def update_scan(self):
        """
        Remove all old files before making new ones
        """
        if not path.isdir(f"{self.settings.workdir}/.scan_temp"):
            mkdir(f"{self.settings.workdir}/.scan_temp")
        else:
            tempfiles = glob.glob(f"{self.settings.workdir}/.scan_temp/*")
            for f in tempfiles:
                remove(f)

        self.scan_bond.write_xyzfiles(self.settings.workdir + '/.scan_temp/')

    def remove_scan_atoms(self):
        try:
            del self.atom_bonds[self.ui.list_scan_bonds.currentItem.text()]
            self.ui.list_scan_bonds.takeItem(self.ui.list_scan_bonds.currentRow())
        except:
            pass

    def scan_list_clicked(self):
        self.ui.list_model.clearSelection()

        self.ui.lineEdit_freeze.setText(str(self.scan_bond.atom1_idx))
        self.ui.lineEdit_move.setText(str(self.scan_bond.atom2_idx))

        self.ui.checkBox_moveboth.setChecked(self.scan_bond.move_both)
        self.ui.spinbox_radius.setValue(self.scan_bond.bond_dist)
        self.ui.spinbox_scan_pm.setValue(self.scan_bond.scan_dist)
        self.ui.spinbox_scan_increment.setValue(self.scan_bond.step_size)
        if self.scan_bond.scan_mode == '+':
            self.ui.radioButton_plus.setChecked(True)
        elif self.scan_bond.scan_mode == '-':
            self.ui.radioButton_plus.setChecked(True)
        else:
            self.ui.radioButton_both.setChecked(True)

        for i in [self.scan_bond.atom1_idx - 1, self.scan_bond.atom2_idx - 1]:
            self.ui.list_model.item(i).setSelected(True)

        #self.scan_bond.write_xyzfiles()


        
    def pymol_spheres(self, atom_nr, hide=False):
        """
        Indicate withe spheres atoms to be frozen / modredundant
        """
        group = "state_%d" % self.react.get_current_state
        _cmd = "show"
        if hide:
            _cmd = "hide"
        self.pymol.pymol_cmd(f"{_cmd} spheres, id {atom_nr} and {group} and {self.mol_obj.filename.split('.')[0]}")
        if not hide:
            self.pymol.pymol_cmd(f"set sphere_scale, 0.3, id {atom_nr} and {group} and "
                                 f"{self.mol_obj.filename.split('.')[0]}")

    def update_job_details(self):
        """
        Activated when job option combobox is updated. Will fill Qlist,
        Enable multiple files in case IRC is chosen, and hide Opt+freq 
        buttons whenever job != opt. 
        :return:
        """
        self.multiple_files.clear()
        self.ui.ComboBox_files.blockSignals(True)
        self.ui.ComboBox_files.clear()
        self.ui.ComboBox_files.blockSignals(False)

        self.job_type = self.ui.comboBox_job_type.currentText()

        if self.job_type == "IRC":
            self.multiple_files[self.filename + "_frwd"] = ["forward"] 
            self.multiple_files[self.filename + "_rev"] = ["reverse"] 

        if self.job_type in ["Opt", "Opt (TS)", "Single point"]:
            self.ui.checkbox_freq.setHidden(False)
            self.ui.checkBox_raman.setHidden(False)
            self.toggle_raman()
        elif self.job_type in ["Freq"]:
            self.ui.checkbox_freq.setChecked(True)
            self.ui.checkbox_freq.setHidden(False)
            self.ui.checkBox_raman.setHidden(False)
        else:
            self.ui.checkbox_freq.setHidden(True)
            self.ui.checkBox_raman.setHidden(True)

        self.ui.List_add_job.clear()
        self.ui.List_add_job.addItems(self.job_options[self.job_type])

    def toggle_raman(self):
        if "Freq" in self.ui.comboBox_job_type.currentText():
            self.ui.checkbox_freq.setChecked(True)

        if self.ui.checkbox_freq.isChecked():
            self.ui.checkBox_raman.setEnabled(True)
        else:
            self.ui.checkBox_raman.setChecked(False)
            self.ui.checkBox_raman.setEnabled(False)

    def update_functional(self):
        self.functional = self.ui.comboBox_funct.currentText()

    def fill_main_tab(self):
        """
        Fill all widgets in main tab.
        Every link0 checkboxes is crossed-checked with entries in self.link0_options.
        If any entry in link0_options has a dedicated checkbox, set the checkbox to True,
        and omit this entry from the additional link 0 QlistWidget. 
        :return:
        """
        self.ui.lineEdit_filename.setText(self.filename)
        self.ui.comboBox_funct.addItems(self.settings.functional_options)
        self.ui.comboBox_basis1.addItems(self.settings.basis_options)
        self.ui.comboBox_basis2.addItems(self.settings.basis_options[self.basis]["diff"])
        self.ui.comboBox_basis3.addItems(self.settings.basis_options[self.basis]["pol1"])
        self.ui.comboBox_basis4.addItems(self.settings.basis_options[self.basis]["pol2"])
        self.ui.List_add_job_2.addItems(self.additional_keys)
        self.ui.comboBox_job_type.addItems(self.job_options)
        self.ui.List_add_job.addItems(self.job_options[self.ui.comboBox_job_type.currentText()])
        self.ui.ComboBox_files.addItem(self.filename)

        self.ui.comboBox_job_type.setCurrentText(self.settings.job_type)
        self.ui.comboBox_funct.setCurrentText(self.functional)
        self.ui.comboBox_basis1.setCurrentText(self.basis)
        self.ui.comboBox_basis2.setCurrentText(self.basis_diff)
        self.ui.comboBox_basis3.setCurrentText(self.basis_pol1)
        self.ui.comboBox_basis4.setCurrentText(self.basis_pol2)
        self.ui.radioButton_2.setChecked(True)
        self.ui.lineEdit_charge.setText(self.charge)
        self.ui.lineEdit_multiplicity.setText(self.multiplicity)
    
        link0_to_add_to_list = [x for x in self.link0_options]

        for checkbox, lineEdit in self.link0_checkboxes.items():

            checkbox.setChecked(False)
            if lineEdit:
                lineEdit.setEnabled(False)

            found_keyword = False

            for keyword_0 in link0_to_add_to_list:

                keyword = keyword_0.lower()
                if "=" in keyword:
                    temp = keyword.split("=")
                    keyword = temp[0]
                    value = temp[1]
                else:
                    value = None

                if keyword == "mem" and checkbox.text() == "Memory":
                    found_keyword = True
                    value = value.upper()

                elif keyword == checkbox.text().lower():
                    found_keyword = True
                    if keyword == "chk" and not value:
                        value = self.filename + ".chk"
                    elif keyword == "oldchk" and not value:
                        value = self.filename + "_old.chk"

                if found_keyword:
                    checkbox.setChecked(True)
                    link0_to_add_to_list.remove(keyword_0)
                    if value and lineEdit:
                        lineEdit.setEnabled(True)
                        lineEdit.setText(value)
                    
                    found_keyword = False

        self.ui.list_link0.addItems(link0_to_add_to_list)

    def update_print_button(self):

        key = self.Qbutton_group.checkedId()
        print_button_dict = {-2: "#t", -3: "#", -4: "#p"}

        self.output_print = print_button_dict[key]

    def on_scan_mode_changed(self):

        scan_mode_map = {-2: "+", -3: "-", -4: "+/-"}
        key = self.Qbutton_scan_group.checkedId()
        self.scan_bond.scan_mode = scan_mode_map[key]
        self.update_scan()


    def update_preview(self):
        """
        Update preview tab. Combobox is cleared and loaded again everytime. 
        In case of multiple files, add correct num of items to combobox,
        but make only file content for the last file in combobox, and load
        this to text preview box.
        """

        # check if preview tab is selected. if not, return
        if not self.ui.tabWidget.currentIndex() == 2:
            return

        self.ui.ComboBox_files.blockSignals(True)
        self.ui.ComboBox_files.clear()
        self.ui.ComboBox_files.blockSignals(False)

        if self.multiple_files:
            for filename, keywords in self.multiple_files.items():
                self.ui.ComboBox_files.addItem(filename)

            self.ui.ComboBox_files.setCurrentText(filename)
            file_content = self.make_input_content(keywords)
        else:
            file_content = self.make_input_content()
            self.ui.ComboBox_files.addItem(self.filename)

        self.ui.text_preview.setPlainText(file_content)

    def update_preview_combobox(self):
        """
        This function is called everytime any change to combobox is made.
        Program crashes if runs with only one file in comobox, thus the 
        if statement is neccesarry!
        """
        if self.ui.ComboBox_files.count() > 1:
            filename = self.ui.ComboBox_files.currentText()
            file_content = self.make_input_content(self.multiple_files[filename])
            self.ui.text_preview.setPlainText(file_content)

    def update_charge(self):
        self.charge = self.ui.lineEdit_charge.text()

    def update_multiplicity(self):
        self.multiplicity = self.ui.lineEdit_multiplicity.text()

    def make_files(self):
        """
        Writes one or multiple inputfiles (found in self.multiplefiles)
        New files are loaded into react again using the exsisting add_files()
        function in REACT.py
        """
        files = []
        if self.multiple_files:
            for filename, keywords in self.multiple_files.items():
                content = self.make_input_content(keywords)
                filepath = self._make_file(filename, content)
                files.append(filepath)
        else:
            content = self.make_input_content()
            filepath = self._make_file(self.filename, content)
            files.append(filepath)

        # Add files separate to avoid issues relating to multithreading prosess in REACT.py 
        for filepath in files:
            self.react.add_file(filepath)

    def _make_file(self, filename, file_content):
        """
        Private function. Makes sure that no files are overwritten, and 
        makes an unique filepath by adding _1, _2, _3 etc until an unique
        filepath is found.
        """
        i = 0
        new_filepath = self.react.settings.workdir + '/' + filename

        while path.isfile(new_filepath + ".com") == True:
            i += 1
            new_filepath = new_filepath + f'_{i}'

        with open(new_filepath + ".com", "w+") as f:
            f.write(file_content)
            f.write("\n")
        
        return new_filepath + ".com"


    def make_input_content(self, extra_job_keywords=False):
        """
        Make content (not file) for one Gaussian inputfile.
        :return: str
        The code is divided into the following parts: link0, route, molecule and restraint.
        Each part prepares it's respective part as a string. named for ex. link0_str. 
        Finally, all sub-strings are jointed into one string, containing the whole file content
        """

        # sub-strings that will be edited by their respective part
        link0_str = ""
        route_str = ""
        molecule_str = ""
        restraints_str = ""


        ### This part creates prepares all link0 keyword by adding them first to the 'link0_list' ###
        ### It also adds "%" to the keyword if its missing                                        ###
        link0_list = []
        value = None

        for checkbox, LineEdit in self.link0_checkboxes.items():
            if checkbox.isChecked():
                if LineEdit:
                    value = LineEdit.text()

                    if not value or value.isspace():
                        return  # TODO some error window to indicate that LineEdit is empty

                    value = LineEdit.text()

                    if "=" in value:
                        value = value.split("=")[1]
                        value.replace(" ", "")

                if checkbox.text() == "Memory":

                    if value.isnumeric():
                        value = value + "GB"
                    link0_list.append("%mem=" + value)

                elif checkbox.text().lower() == "chk":
                    link0_list.append("%chk=" + value)
                elif checkbox.text().lower() == "oldchk":
                    link0_list.append("%oldchk=" + value)
                elif checkbox.text().lower() == "rwf":
                    link0_list.append("%rwf=" + value)

        for item in [self.ui.list_link0.item(x).text() for x in range(self.ui.list_link0.count())]:
            item.replace(" ", "")
            if not item[0] == '%':
                item = '%' + item
            link0_list.append(item)

        link0_str = "\n".join(link0_list)


        ### This part prepares all part of the route comment, by first adding them to route_list ###
        ### Then, all items  in route_list are joined into one str.                              ###

        job_str = ""
        job_keywords = []
        job_type = self.job_type

        if extra_job_keywords:
            job_keywords.extend(extra_job_keywords)

        if self.ui.list_freeze_atoms.count() > 0:
            job_keywords.append("modredundant")

        if self.job_type == "Opt (TS)":
            job_keywords.append("TS")
            job_type = "Opt"
        
        for i in self.job_options[job_type]:
            job_keywords.append(i)

        freq = False
        if self.opt_freq_details["checked"]:
            if self.opt_freq_details["keywords"]:
                freq = "Freq=(" + ", ".join(self.opt_freq_details["keywords"] + ")")
            else:
                freq = "Freq"
                

        if job_keywords:
            keywords = ", ".join(job_keywords)
            if freq:
                job_str = f"Opt=({keywords}) {freq}"
            else:
                job_str = f"{job_type}=({keywords})"

        else:
            if freq:
                job_str = f"Opt {freq}"
            else:
                job_str = f"{job_type}" 


        if self.basis_diff and not self.basis_diff.isspace():
            tmp = list(self.basis)
            if tmp[-1] == 'G':
                tmp[-1] = self.basis_diff
                tmp.append('G')
            else:
                tmp.append(self.basis_diff)
            basis = "".join(tmp)
        else:
            basis = self.basis

        if self.basis_pol1 and not self.basis_pol1.isspace() and self.basis_pol2\
           and not self.basis_pol2.isspace():
            basis_pol = f"({self.basis_pol1},{self.basis_pol2})"
        elif self.basis_pol1 and not self.basis_pol1.isspace():
            basis_pol = f"({self.basis_pol1})"
        elif self.basis_pol2 and not self.basis_pol2.isspace():
            basis_pol = f"({self.basis_pol2})"
        else:
            basis_pol = False

        if basis_pol:
            basis_str = f"{basis}{basis_pol}"
        else:
            basis_str = f"{basis}"

        route_str = f"{self.output_print} {job_str} {self.functional}/{basis_str} "\
                    + " ".join(self.additional_keys)


        ### This part prepares the molecule ###
        molecule_str = f"{self.charge} {self.multiplicity}\n" + "\n".join(self.mol_obj.formatted_xyz)

        ### This part prepares the restraints, if there are any ###
        restraints_list = []
        
        for item in [self.ui.list_freeze_atoms.item(x).text() for x in range(self.ui.list_freeze_atoms.count())]:
            restraints_list.append(item)

        restraints_str = "\n".join(restraints_list)


        return f"{link0_str}\n{route_str}\n\n{molecule_str}\n\n{restraints_str}\n\n"
    

    def route_checkboxes_update(self, checkbox, lineEdit):

        if checkbox.isChecked():
            lineEdit.setEnabled(True)
        else:
            lineEdit.setEnabled(False)
        
    def update_basis1(self):
        """
        Updates self.basis1 according to basis selected by user
        On update of main basis comboBox, update all other basis comboBoxes

        :return:
        """
        self.basis = self.ui.comboBox_basis1.currentText()

        self.ui.comboBox_basis2.clear()
        self.ui.comboBox_basis3.clear()
        self.ui.comboBox_basis4.clear()

        self.ui.comboBox_basis2.addItems(self.settings.basis_options[self.basis]['diff'])
        self.ui.comboBox_basis3.addItems(self.settings.basis_options[self.basis]['pol1'])
        self.ui.comboBox_basis4.addItems(self.settings.basis_options[self.basis]['pol2'])

        #self.ui.comboBox_basis2.setCurrentText(self.basis_diff)
        #self.ui.comboBox_basis3.setCurrentText(self.basis_pol1)
        #self.ui.comboBox_basis4.setCurrentText(self.basis_pol2)

    def update_basis2(self):
        """
        Update basis attribute self.basis_diff
        """
        self.basis_diff = self.ui.comboBox_basis2.currentText()

    def update_basis3(self):
        """
        Update basis attribute self.basis_pol1
        """
        self.basis_pol1 = self.ui.comboBox_basis3.currentText()

    def update_basis4(self):
        """
        Update basis attribute self.basis_pol2
        """
        self.basis_pol2 = self.ui.comboBox_basis4.currentText()


    def filename_update(self):
        
        self.filename = self.ui.lineEdit_filename.text()

        self.ui.lineEdit_chk.setText(self.filename + ".chk")
        self.ui.lineEdit_oldchk.setText(self.filename + "_old.chk")


    def insert_model_atoms(self):
        """
        :return:
        """

        if "pdb" in self.filepath.split(".")[-1]:
            atoms = self.mol_obj.formatted_pdb
        else:
            self.ui.button_auto_freeze.setEnabled(False)
            atoms = self.mol_obj.formatted_xyz

        for i in range(len(atoms)):
            self.ui.list_model.insertItem(i, atoms[i])

    def auto_freeze_atoms(self):
        """
        Goes through PDB atoms and tries to figure out base on pdb atom names and distances what atoms
        are terminal/chopped region atoms that should be frozen.
        """
        expected = ["CA", "C", "H", "N", "O"]
        atoms = self.mol_obj.atoms
        for atom in atoms:
            pdb_name = atom.get_pdb_atom_name
            if pdb_name in ["C", "N"]:
                atoms.pop(0)
                for next_atom in atoms:
                    radius = atom_distance(atom.get_coordinate, next_atom.get_coordinate)
                    if radius < 1.7:
                        if next_atom.get_pdb_atom_name not in expected:
                            atom_nr = next_atom.get_atom_index
                            self.ui.list_freeze_atoms.insertItem(0, f"X {atom_nr} F")
                            if self.pymol:
                                self.pymol_spheres(atom_nr)


    def add_item_to_list(self, Qtextinput, Qlist, job_list):
        """
        :param Qtextinput: QLineEdit
        :param Qlist: QListWidget
        :param original_list: list to store item
        Adds the text input from user (past to Qtextinput) to correct
        QlistWidget and append item to list.
        """
        user_input = Qtextinput.text()
        if user_input and user_input not in job_list:
            job_list.append(user_input)
            Qlist.addItem(user_input)
        Qtextinput.clear()

    def del_item_from_list(self, Qlist, job_list):
        """
        :param Qlist: QListWidget
        :param job_list: list to delete from
        Removes item in QlistWdiget and updates self.settings accordingly.
        """
        item_text = Qlist.currentItem().text()
        if item_text in job_list:
            job_list.remove(item_text)
        Qlist.takeItem(Qlist.currentRow())


    def del_tempfiles(self):
        try:
            shutil.rmtree(self.react.react_path + '/scan_temp')
        except OSError as e:
            print("Error: %s" % (e.strerror))

    def on_close(self):

        self.del_tempfiles()
        self.close()

    def on_write(self):
        """
        Write all data to Inputfile object.
        # TODO how to return this object to react after closing the window?
        # TODO reply --> just open the .com file in the current state (tab) of REACT after write?
        # TODO on_write should probably just write whatever is in the preview window to a file.
        """
        #self.mol_obj.filename = self.ui.lineEdit_filename.text()
        #self.mol_obj.job_type = self.ui.comboBox_job_type.currentText()
        #self.mol_obj.basis = self.ui.comboBox_basis1.currentText()
        #self.mol_obj.basis_diff = self.ui.comboBox_basis2.currentText()
        #self.mol_obj.basis_pol1 = self.ui.comboBox_basis3.currentText()
        #self.mol_obj.basis_pol2 = self.ui.comboBox_basis4.currentText()
        #self.react.states[self.react.state_index].add_instance(self.mol_obj)

        self.make_files()
        self.del_tempfiles()

        
        #self.close()

    def closeEvent(self, event):
        if self.pymol:
            self.pymol.pymol_cmd("set mouse_selection_mode, 1")
            self.pymol.pymol_cmd("hide spheres,")
            self.pymol.unmonitor_clicks()

