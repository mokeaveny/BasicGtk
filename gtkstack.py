# Stacks are containers that only shows one of its children at a time
# The Gtk.StackSwitcher widget can be used with Gtk.Stack to change the widget

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class StackWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Stack Demo")
        self.set_border_width(10)

        # Add the vertical box to the window
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        # Create a stack widget
        stack = Gtk.Stack()
        # Transition that changes the child of the stack
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration(1000)

        # Check button that is added to the stack
        checkbutton = Gtk.CheckButton(label="Click Here!")
        stack.add_titled(checkbutton, "check", "Check Button")

        # Label widget that is added to the stack
        label = Gtk.Label()
        label.set_markup("<big>A fancy label</big>")
        stack.add_titled(label, "label", "A label")

        # Set the switcher and the stack the switcher operates on
        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(stack)
        vbox.pack_start(stack_switcher, True, True, 0)
        vbox.pack_start(stack, True, True, 0)

win = StackWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()