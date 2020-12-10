# Import the Gtk module
import gi

# Import version 3.0 of the library
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# Define a MyWindow class. A child class of the class Gtk Window class
class MyWindow(Gtk.Window):
    # Constructor that sets the title of the window to Hello World
    def __init__(self):
        Gtk.Window.__init__(self, title = "Hello World")

        # Create a button widget, which when clicked will call the method on_button_clicked
        self.button = Gtk.Button(label = "Click Here")
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)

    # Method outputs hello world to the console
    def on_button_clicked(self, widget):
        print("Hello World")

win = MyWindow()
# Ensure the window is closed when the exit button is clicked
win.connect("destroy", Gtk.main_quit)
# Display the window
win.show_all()
# Processing loop that displays the window until we close it
Gtk.main()



