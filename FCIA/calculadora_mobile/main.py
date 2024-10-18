from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.animation import Animation
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import math


class CalculatorScreen(Screen):
    memory = 0
    last_result = 0
    dark_mode = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Layout da calculadora
        self.calc_layout = BoxLayout(orientation='vertical')

        # Campo de entrada
        self.input_box = TextInput(font_size=32, halign='right', multiline=False,
                                   background_color=(1, 1, 1, 1), foreground_color=(0, 0, 0, 1))
        self.calc_layout.add_widget(self.input_box)

        # Layout para botões
        buttons = [
            ['7', '8', '9', '/', 'M+'],
            ['4', '5', '6', '*', 'M-'],
            ['1', '2', '3', '-', 'MR'],
            ['0', '.', 'C', '+', 'ANS'],
            ['(', ')', '√', '^', 'Dec'],
            ['%', 'DEL', '=', 'Histórico']
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                if label:  # Ignora o espaço vazio
                    button = Button(text=label, font_size=24, on_press=self.on_button_press)
                    button.background_normal = ''
                    button.background_color = [0.7, 0.7, 0.7, 1]  # Botões em cinza
                    button.bind(on_press=self.animate_button)  # Animação ao pressionar
                    h_layout.add_widget(button)
            self.calc_layout.add_widget(h_layout)

        # Botão para alternar modo noturno
        self.dark_mode_button = Button(text="Dark Mode", size_hint=(1, 0.1), font_size=24,
                                       on_press=self.toggle_dark_mode, background_color=(0.7, 0.7, 0.7, 1))
        self.calc_layout.add_widget(self.dark_mode_button)

        self.add_widget(self.calc_layout)

    def on_button_press(self, instance):
        current_text = self.input_box.text
        button_text = instance.text

        try:
            if button_text == 'C':
                self.input_box.text = ''
            elif button_text == 'DEL':
                self.input_box.text = current_text[:-1]
            elif button_text == '√':
                self.input_box.text = str(math.sqrt(float(current_text)))
            elif button_text == '^':
                self.input_box.text += '**'
            elif button_text == '=':
                result = eval(self.input_box.text)
                self.add_to_history(self.input_box.text, result)  # Adiciona expressão e resultado ao histórico
                self.input_box.text = str(result)
                self.last_result = result
            elif button_text == 'ANS':
                self.input_box.text += str(self.last_result)
            elif button_text == 'M+':
                self.memory += float(self.input_box.text)
            elif button_text == 'M-':
                self.memory -= float(self.input_box.text)
            elif button_text == 'MR':
                self.input_box.text = str(self.memory)
            elif button_text == 'Dec':
                self.input_box.text = str(round(float(self.input_box.text), 2))  # Define 2 casas decimais
            elif button_text == 'Histórico':
                self.manager.current = 'history'  # Muda para a tela de histórico
            else:
                self.input_box.text += button_text
        except ZeroDivisionError:
            self.input_box.text = 'Erro: Divisão por zero'
        except Exception as e:
            self.input_box.text = f'Erro: {str(e)}'

    def add_to_history(self, expression, result):
        """Adiciona o cálculo ao histórico"""
        self.manager.get_screen('history').add_to_history(f'{expression} = {result}')

    def toggle_dark_mode(self, instance):
        """Altera entre modo claro e escuro"""
        self.dark_mode = not self.dark_mode
        bg_color = (0, 0, 0, 1) if self.dark_mode else (1, 1, 1, 1)
        fg_color = (1, 1, 1, 1) if self.dark_mode else (0, 0, 0, 1)

        # Atualiza o fundo e as cores do texto
        self.input_box.background_color = bg_color
        self.input_box.foreground_color = fg_color
        self.dark_mode_button.text = 'Light Mode' if self.dark_mode else 'Dark Mode'
        self.dark_mode_button.background_color = (0.7, 0.7, 0.7, 1)

        # Atualiza os botões
        for child in self.calc_layout.children[:-1]:  # Exclui o botão de dark mode
            if isinstance(child, BoxLayout):
                for btn in child.children:
                    btn.background_color = [0.7, 0.7, 0.7, 1]  # Botões continuam cinza

        # Atualiza a cor do histórico
        self.manager.get_screen('history').update_history_background()

    def animate_button(self, instance):
        anim = Animation(size=(instance.width + 10, instance.height + 10), duration=0.1) + Animation(
            size=(instance.width, instance.height), duration=0.1)
        anim.start(instance)


class HistoryScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Layout do histórico
        self.history_layout = GridLayout(cols=1, size_hint_y=None)
        self.history_layout.bind(minimum_height=self.history_layout.setter('height'))

        # ScrollView para o histórico
        self.scroll_view = ScrollView(size_hint=(1, 1), do_scroll_x=True, do_scroll_y=True)
        self.scroll_view.add_widget(self.history_layout)
        self.add_widget(self.scroll_view)

        # Botão para voltar
        self.back_button = Button(text="Voltar", size_hint=(1, 0.1), on_press=self.go_back)
        self.add_widget(self.back_button)

    def add_to_history(self, text):
        """Adiciona o cálculo ao histórico"""
        history_item = Label(
            text=text,
            font_size=18,
            size_hint_y=None,
            height=40,
            text_size=(self.width, None),  # Define o tamanho do texto para autoquebra
            halign='left',
            valign='middle'
        )
        history_item.bind(size=self.adjust_text_size)  # Ajuste automático da fonte
        self.history_layout.add_widget(history_item)
        self.scroll_view.scroll_to(history_item)  # Rolagem automática para o novo item

    def go_back(self, instance):
        """Retorna para a tela da calculadora"""
        self.manager.current = 'calculator'

    def adjust_text_size(self, instance, size):
        """Ajusta a fonte dependendo do tamanho do texto"""
        instance.text_size = (instance.width, None)

    def update_history_background(self):
        """Atualiza o fundo do histórico com base no modo atual"""
        if self.manager.get_screen('calculator').dark_mode:
            self.history_layout.canvas.before.clear()
            with self.history_layout.canvas.before:
                from kivy.graphics import Color, Rectangle
                Color(0, 0, 0, 1)  # Fundo preto
                self.history_layout.rect = Rectangle(size=self.history_layout.size, pos=self.history_layout.pos)
        else:
            self.history_layout.canvas.before.clear()
            with self.history_layout.canvas.before:
                from kivy.graphics import Color, Rectangle
                Color(1, 1, 1, 1)  # Fundo branco
                self.history_layout.rect = Rectangle(size=self.history_layout.size, pos=self.history_layout.pos)


class CalculadoraApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(CalculatorScreen(name='calculator'))
        sm.add_widget(HistoryScreen(name='history'))
        return sm


if __name__ == '__main__':
    CalculadoraApp().run()
