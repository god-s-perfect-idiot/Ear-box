import gi
import random
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk

captcha_count=random.randint(1,3)
actual=["smwm","Google","CUnaH"]


class MyWindow(Gtk.Window):

    def __init__(self):
        # init the base class (Gtk.Window)
        super().__init__()
        self.set_default_size(400,300)

        # state affected by shortcuts
        self.button_press = 0

        # Tell Gtk what to do when the window is closed (in this case quit the main loop)
        self.connect("delete-event", Gtk.main_quit)

        # connect the key-press event - this will call the keypress
        # handler when any key is pressed
        self.connect("key-press-event",self.on_key_press_event)

        # Window content goes in a vertical box
        box = Gtk.VBox()

        # a helpful label
        instruct = Gtk.Label(label="Captcha here")
        box.add(instruct)

        # the label that will respond to the event
        self.label = Gtk.Label()

        #importing captcha
        self.image=Gtk.Image()
        self.image.set_from_file("res/c"+str(captcha_count)+".png")

        #Add captcha to window
        box.add(self.image)

        #Add textbox
        self.entry = Gtk.Entry()
        box.add(self.entry)

        #Add submit button
        self.button = Gtk.Button.new_with_label("Submit")
        self.button.connect("clicked",self.on_submit_clicked)
        box.add(self.button)

        # Add the label to the window
        box.add(self.label)

        self.add(box)

    def on_key_press_event(self, widget, event):

        # check the event modifiers (can also use SHIFTMASK, etc)
        ctrl = (event.state & Gdk.ModifierType.CONTROL_MASK)

        # see if we recognise a keypress
        self.button_press += 1
        
        #if captcha is submitted
        if event.keyval == Gdk.KEY_Return:
            entered=self.entry.get_text()

        #check if captcha is right and a key press occured
            if(entered == actual[captcha_count-1] and self.button_press>3):
                self.label.set_text("Captcha Verified")
            else:
                self.label.set_text("Captcha Failed")    

    def on_submit_clicked(self, button):

        entered=self.entry.get_text()

        #check if captcha is right and a key press occured
        if(entered == actual[captcha_count-1] and self.button_press>3):
            self.label.set_text("Captcha Verified")
        else:
            self.label.set_text("Captcha Failed")  


if __name__ == "__main__":
    win = MyWindow()
    win.set_title("EarBox")
    win.show_all()

    # Start the Gtk main loop
    Gtk.main()
