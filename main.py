import os
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, GLib


APPID = 'com.github.taniyoshima.pyt_gtk4_colordialog'


@Gtk.Template(filename=os.path.dirname(__file__) + '/ui_file.ui')
class Gtk4TestTest(Gtk.ApplicationWindow):

    __gtype_name__ = "window"
    colordialog = Gtk.Template.Child()

    def __init__(self, app):
        Gtk.ApplicationWindow.__init__(self, application=app)

    @Gtk.Template.Callback()
    def on_button_clicked(self, button):
        self.colordialog.choose_rgba(
            parent=self, cancellable=None,
            callback=self.on_colordialog_choose_rgb)

    def on_colordialog_choose_rgb(self, colordialog, task):
        try:
            color = colordialog.choose_rgba_finish(task)
        except GLib.GError:
            return

        if color is not None:
            print(color.to_string())
            print(f"R: {color.red}, G: {color.green}, B: {color.blue}")
            print(f"R: {int(color.red * 255)}, G: {int(color.green * 255)}, "
                  + f"B: {int(color.blue * 255)}")


class Gtk4TestApp(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self, application_id=APPID)

    def do_activate(self):
        window = Gtk4TestTest(self)
        window.present()


def main():
    app = Gtk4TestApp()
    app.run()


if __name__ == '__main__':
    main()
