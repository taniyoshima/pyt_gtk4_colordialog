# pyt_gtk4_colordialog

<br>

## 内容 

Window上に配置したGtk.Buttonを押すとGtk.ColorDialogが表示されます。Gtk.ColorDialogで色を選択すると、選択した色の情報をターミナルに出力します。

### Gtk.ColorDialogの呼び出し、表示部分

```
    colordialog = Gtk.Template.Child()

    …

    @Gtk.Template.Callback()
    def on_button_clicked(self, button):
        self.colordialog.choose_rgba(
            parent=self, cancellable=None,
            callback=self.on_colordialog_choose_rgb)
```

### Gtk.ColorDialogで選択した色の取得部分

```
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

```

### Gtk.ColorDialogのプロパティ

| プロパティ | 内容 |
| --- | --- |
| modal | カラー選択ダイアログがモーダルかどうか |
| title | カラー選択ダイアログに表示されるタイトル |
| with-alpha | 色にアルファ (半透明) があるかどうか |

<br>

## 履歴

2024/6/16 プログラム作成

## 参考にしたHP
