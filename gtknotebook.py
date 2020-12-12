import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Simple Notebook")
        self.set_border_width(3)

        # Creat the notebook
        self.notebook = Gtk.Notebook()
        # Add the notebook to the main window
        self.add(self.notebook)

        self.page1 = Gtk.Box()
        self.page1.set_border_width(10)
        self.page1.add(Gtk.Label(label="First Page!"))
        # Add the first page to the notebook
        self.notebook.append_page(self.page1, Gtk.Label(label="Plain Title"))

        self.page2 = Gtk.Box()
        self.page2.set_border_width(10)
        self.page2.add(Gtk.Label(label="Second Page!"))
        # Add the second page to the notebook
        self.notebook.append_page(
            self.page2, Gtk.Image.new_from_icon_name("help-about", Gtk.IconSize.MENU)
        )

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()