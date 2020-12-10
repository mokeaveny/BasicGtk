import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
label = Gtk.Label()
text = "Fu\u00dfb\u00e4lle"
label.set_text(text)
txt = label.get_text()
type(txt), txt
print(txt)