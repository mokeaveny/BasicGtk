import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class ListBoxRowWithData(Gtk.ListBoxRow):
    def __init__(self, data):
        super(Gtk.ListBoxRow, self).__init__()
        self.data = data
        self.add(Gtk.Label(label = data))

class ListBoxWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="ListBox Demo")
        self.set_border_width(10)

        # Create the box widget
        box_outer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(box_outer)

        # Create the listbox widget
        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        # Add the listbox widget to the box widget
        box_outer.pack_start(listbox, True, True, 0)

        # Create a list box row
        row = Gtk.ListBoxRow()
        # Create another box widget to add to the box_outer
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        # Add a horizontal box to the row
        row.add(hbox)
        # Create a vertical box
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, True, True, 0)

        # Create two label widgets
        label1 = Gtk.Label(label="Automatic Date & Time", xalign=0)
        label2 = Gtk.Label(label="Requires internet access", xalign=0)
        # Add the two label widgets to the vertical box
        vbox.pack_start(label1, True, True, 0)
        vbox.pack_start(label2, True, True, 0)

        # Create a switch widget
        switch = Gtk.Switch()
        switch.props.valign = Gtk.Align.CENTER
        # Add the switch to the horizontal box
        hbox.pack_start(switch, False, True, 0)

        listbox.add(row)

        # Create another row widget
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        label = Gtk.Label(label = "Enable Automatic Update", xalign=0)
        check = Gtk.CheckButton()
        # Add the label and check button to the row with relative positions
        hbox.pack_start(label, True, True, 0)
        # Expand is set to False
        hbox.pack_start(check, False, True, 0)

        # Add this row to the listbox widget
        listbox.add(row)

        # Create the final row
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        label = Gtk.Label(label="Date Format", xalign=0)
        # Create a combo box
        combo = Gtk.ComboBoxText()
        combo.insert(0, "0", "24-hour")
        combo.insert(1, "1", "AM/PM")
        hbox.pack_start(label, True, True, 0)
        hbox.pack_start(combo, False, True, 0)

        listbox.add(row)

win = ListBoxWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()