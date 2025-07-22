from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class PasswordApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=40, spacing=20)

        self.label = Label(text="Call to 0705468867", font_size=32)
        self.layout.add_widget(self.label)

        self.password_input = TextInput(password=True, hint_text="أدخل كلمة السر", font_size=24, multiline=False)
        self.layout.add_widget(self.password_input)

        self.button = Button(text="تحقق من كلمة السر", font_size=24)
        self.button.bind(on_press=self.check_password)
        self.layout.add_widget(self.button)

        return self.layout

    def check_password(self, instance):
        password = self.password_input.text
        if password == "1234":
            self.show_popup("نجاح", "تم الوصول إلى البيانات!")
        else:
            self.show_popup("خطأ", "كلمة السر غير صحيحة!")

    def show_popup(self, title, message):
        content = BoxLayout(orientation='vertical', padding=10)
        content.add_widget(Label(text=message, font_size=20))
        close_button = Button(text="إغلاق", size_hint_y=None, height=50)
        content.add_widget(close_button)

        popup = Popup(title=title, content=content, size_hint=(0.8, 0.4))
        close_button.bind(on_press=popup.dismiss)
        popup.open()

if __name__ == '__main__':
    PasswordApp().run()
