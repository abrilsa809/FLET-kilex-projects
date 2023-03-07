from flet import *
import googletrans
import flet as ft
import os
from plyer import notification
from  asyncio import *
from time import sleep
import openai
from dotenv import load_dotenv
load_dotenv()


openai.api_key = "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"

bg = '#444654'
fg = '#202123'
side_bar_width = 260


class Main(UserControl):
    def __init__(self, page: Page,):
        page.padding = 0
        page.title = 'KILEX'
        page.theme_mode ="dark"
        page.update()
        self.blinking = False
        self.chat_response = ''
        self.langage = "en"

        self.page = page
        self.transaltor =  googletrans.Translator()
        self.prompt = [
            {
                "role": "system",
                'content': 'As a large AI language model. You know almost everything. Your job is to provide solution / suggestion to problems.'
            }
        ]
        self.init()

    def init(self):
        self.chat_gpt_label = Container(
            padding=padding.only(top=120),
            alignment=alignment.center,
            content=Text(
                value='KILEX',
                size=35, weight=FontWeight.BOLD,
            )
        )
        self.cursor = Container(
            width=8, height=20, bgcolor='white', )
        self.message_field = TextField(
            border=InputBorder.NONE,
            expand=True,
            on_change=self.textfieledchanged,
           
            content_padding=0,
            on_submit=self.send_clicked,
            # max_lines=5,
            # max_length=100,
            # min_lines=5,


        )
        self.history_chats= Column(spacing=3,
                                  scroll="auto",
                                   auto_scroll=True,
                                   expand=True
                                   
                                 )
        self.drop_down_language = Dropdown(

            height=65,
            border_radius=10,
            width=250,
            border_color="white",
            
            hint_text="Choose languages",
            bgcolor="yellow",
         
            hint_style=TextStyle(
            color="white",
            
            ),
            on_change=self.language_changed,
            border_width=1,
            focused_border_color="white",
            helper_style=TextStyle(
                color="white",
              
               size=10

            ),
         prefix_icon=ft.icons.LANGUAGE_ROUNDED,
           


            options=[
                ft.dropdown.Option("English"),
                ft.dropdown.Option("Swahili"),
                ft.dropdown.Option("Afrikaans"),
                ft.dropdown.Option("Albanian"),
                ft.dropdown.Option("Italian"),
                ft.dropdown.Option("Arabic"),
                ft.dropdown.Option("Japanese"),
                ft.dropdown.Option("Azerbaijani"),
                ft.dropdown.Option("Kannada"),
                ft.dropdown.Option("Basque"),
                ft.dropdown.Option("Korean"),
                ft.dropdown.Option("Bengali"),
                ft.dropdown.Option("Latin"),
                ft.dropdown.Option("Belarusian"),
                ft.dropdown.Option("Latvian"),
                ft.dropdown.Option("Bulgarian"),
                ft.dropdown.Option("Lithuanian"),
                ft.dropdown.Option("Catalan"),
                ft.dropdown.Option("Macedonian"),
                ft.dropdown.Option("Chinese Simplified"),
                ft.dropdown.Option("Malay"),
                ft.dropdown.Option("Malay"),
                ft.dropdown.Option("Maltese"),
                ft.dropdown.Option("Croatian"),
                ft.dropdown.Option("Norwegian"),
                ft.dropdown.Option("Czech"),
                ft.dropdown.Option("Persian"),
                ft.dropdown.Option("Danish"),
                ft.dropdown.Option("Polish"),
                ft.dropdown.Option("Dutch"),
                ft.dropdown.Option("Portuguese"),
                ft.dropdown.Option("Romanian"),
                ft.dropdown.Option("Esperanto"),
                ft.dropdown.Option("Russian"),
                ft.dropdown.Option("Estonian"),
                ft.dropdown.Option("Serbian"),
                ft.dropdown.Option("Filipino"),
                ft.dropdown.Option("Slovak"),
                ft.dropdown.Option("Finnish"),
                ft.dropdown.Option("Slovenian"),
                ft.dropdown.Option("French"),
                ft.dropdown.Option("Spanish"),
                ft.dropdown.Option("Galician"),
                ft.dropdown.Option("Georgian"),
                ft.dropdown.Option("Swedish"),
                ft.dropdown.Option("German"),
                ft.dropdown.Option("Tamil"),
                ft.dropdown.Option("Greek"),
                ft.dropdown.Option("Telugu"),
                ft.dropdown.Option("Gujarati"),
                ft.dropdown.Option("Thai"),
                ft.dropdown.Option("Haitian Creole"),
                ft.dropdown.Option("Turkish"),
                ft.dropdown.Option("Hebrew"),
                ft.dropdown.Option("Ukrainian"),
                ft.dropdown.Option("Hindi"),
                ft.dropdown.Option("Urdu"),
                ft.dropdown.Option("Hungarian"),
                ft.dropdown.Option("Vietnamese"),
                ft.dropdown.Option("Icelandic"),
                ft.dropdown.Option("Welsh"),
                ft.dropdown.Option("Indonesian"),
                ft.dropdown.Option("Yiddish"),

            ],
        )
        self.sendbutton= Container(
                                                    on_click=self.send_clicked,
                                                    height=40,
                                                    width=40,
                                                    content=Icon(
                                                        icons.SEND,
                                                    ),
                                                    on_hover=self.hover,
                                                    border_radius=8

                                                )
        self.voicebutton= Container(
                                                    on_click=self.send_clicked,
                                                    height=40,
                                                    width=40,
                                                    content=Icon(icons.DANGEROUS_OUTLINED),
                                                    on_hover=self.hover,
                                                    border_radius=8

                                                )
        self.side_bar = Container(
            width=side_bar_width,
            bgcolor=fg,
            padding=8,
            content=Column(
                controls=[
                    self.drop_down_language,

                    Column(
                       
                      
                        expand=True,

                        controls=[

                            Container(
                                on_hover=self.hover,
                                height=45,
                                border_radius=8,

                                padding=8,
                                content=Row(
                                    # spacing=14,
                                    controls=[
                                        Icon(
                                            icons.CHAT_BUBBLE_OUTLINE_ROUNDED,
                                            size=16,
                                        ),
                                        Text(
                                            value='Conversation History',
                                            weight=FontWeight.W_100,
                                            width=200,
                                            no_wrap=True,
                                            size=16,

                                        )
                                    ]
                                )

                            ),
                            self.history_chats

                        ]
                    ),

                    # Container(height=0.2, bgcolor='#4d4d4f'),

                    Divider(color='#4d4d4f', height=1),



                    Container(
                        on_hover=self.new_chat_hover,
                        height=45,
                        border_radius=8,
                        on_click=self.clearchat,
                        padding=8,
                        content=Row(
                            controls=[
                                Icon(
                                    icons.DELETE_OUTLINE_OUTLINED,
                                    size=18,
                                ),
                                Text(
                                    value='Clear conversations',
                                    weight=FontWeight.W_100
                                )
                            ]
                        )

                    ),
                    Container(
                        on_hover=self.new_chat_hover,
                        height=45,
                        border_radius=8,
                        padding=8,
                        content=Row(
                            alignment='spaceBetween',
                            controls=[
                                Row(
                                      controls=[
                                          Icon(
                                              icons.PERSON_OUTLINE_OUTLINED,
                                              size=18,
                                          ),
                                          Text(
                                              value='Upgrade to Plus',
                                              weight=FontWeight.W_100
                                          ),
                                      ]
                                ),
                                Container(
                                    width=40, height=20, bgcolor='#fae69e', border_radius=5,
                                    alignment=alignment.center,
                                    content=Text(
                                        'NEW', size=12, color=fg
                                    )
                                ),
                            ]
                        )

                    ),
                    Container(
                        on_hover=self.new_chat_hover,
                        height=45,
                        border_radius=8,
                        padding=8,
                        content=Row(
                            controls=[
                                Icon(
                                    icons.OPEN_IN_NEW_OUTLINED,
                                    size=18,
                                ),
                                Text(
                                    value='Updates & FAQ',
                                    weight=FontWeight.W_100
                                ),
                            ]
                        )

                    ),
                    Container(
                        on_hover=self.new_chat_hover,
                        height=45,
                        border_radius=8,
                        padding=8,
                        content=Row(
                            controls=[
                                Icon(
                                    icons.LOGOUT_OUTLINED,
                                    size=18,
                                ),
                                Text(
                                    value='Logout',
                                    weight=FontWeight.W_100
                                ),
                            ]
                        )

                    ),

                ]
            ),
        )
        self.content_area = Column(
            auto_scroll=True,
            spacing=30,
            scroll='auto',
            controls=[
                self.chat_gpt_label,
                Row(
                    alignment='center',
                    controls=[
                        Column(
                            controls=[
                                Container(
                                    alignment=alignment.center,
                                    width=250,
                                    content=Column(
                                        horizontal_alignment='center',
                                        controls=[
                                            Icon(icons.BRIGHTNESS_7_OUTLINED),
                                            Text('Examples')
                                        ]
                                    )
                                ),
                                Container(
                                    alignment=alignment.center,
                                    width=250,
                                    # height=100,
                                    padding=padding.only(
                                        top=20, bottom=30, left=20, right=20),
                                    border_radius=8,
                                    on_hover=self.hover2,
                                    on_click=self.creative,
                                    bgcolor='#3e3f4b',
                                    content=Text(
                                        '"Explain quantum computing in simple terms"',
                                        text_align='center',
                                    )
                                ),

                                Container(
                                    alignment=alignment.center,
                                    width=250,
                                    # height=100,
                                    padding=padding.only(
                                        top=20, bottom=30, left=20, right=20),
                                    border_radius=8,
                                    on_hover=self.hover2,
                                    on_click=self.creative,
                                    bgcolor='#3e3f4b',
                                    content=Text(
                                      value =  '"Got any creative ideas for a 10 year old\'s birthday?"',
                                        text_align='center',
                                    )
                                ),

                                Container(
                                    alignment=alignment.center,
                                    width=250,
                                    # height=100,
                                    padding=padding.only(
                                        top=20, bottom=30, left=20, right=20),
                                    border_radius=8,
                                    on_hover=self.hover2,
                                    on_click=self.creative,
                                    bgcolor='#3e3f4b',
                                    content=Text(
                                        '"How do I make an HTTP request in JavaScript?"',
                                        text_align='center',
                                    )
                                ),

                            ]
                        ),
                        Column(
                            controls=[
                                Container(
                                    alignment=alignment.center,
                                    width=250,
                                    content=Column(
                                        horizontal_alignment='center',
                                        controls=[
                                            Icon(icons.FLASH_ON_OUTLINED),
                                            Text('Capabilities')
                                        ]
                                    )
                                ),
                                Container(
                                    alignment=alignment.center,
                                    width=250,
                                    # height=100,
                                    padding=padding.only(
                                        top=20, bottom=30, left=20, right=20),
                                    border_radius=8,
                                    on_hover=self.hover2,
                                    bgcolor='#3e3f4b',
                                    content=Text(
                                        'Remember what user said earlier in the conversation',
                                        text_align='center',
                                    )
                                ),

                                Container(
                                    alignment=alignment.center,
                                    width=250,
                                    # height=100,
                                    padding=padding.only(
                                        top=20, bottom=30, left=20, right=20),
                                    border_radius=8,
                                    on_hover=self.hover2,
                                    bgcolor='#3e3f4b',
                                    content=Text(
                                        'Allows user to provide follow-up corrections',
                                        text_align='center',
                                    )
                                ),

                                Container(
                                    alignment=alignment.center,
                                    width=250,
                                    # height=100,
                                    padding=padding.only(
                                        top=20, bottom=30, left=20, right=20),
                                    border_radius=8,
                                    on_hover=self.hover2,
                                    bgcolor='#3e3f4b',
                                    content=Text(
                                        'Trained to decline inappropriate requests',
                                        text_align='center',
                                    )
                                ),

                            ]
                        ),
                        Column(
                            controls=[
                                Container(
                                    alignment=alignment.center,
                                    width=250,
                                    content=Column(
                                        horizontal_alignment='center',
                                        controls=[
                                            Icon(icons.DANGEROUS_OUTLINED),
                                            Text('Limitations')
                                        ]
                                    )
                                ),
                                Container(
                                    alignment=alignment.center,
                                    width=250,
                                    # height=100,
                                    padding=padding.only(
                                        top=20, bottom=30, left=20, right=20),
                                    border_radius=8,
                                    on_hover=self.hover2,
                                    bgcolor='#3e3f4b',
                                    content=Text(
                                        'May occationally generate incorrect information',
                                        text_align='center',
                                    )
                                ),

                                Container(
                                    alignment=alignment.center,
                                    width=250,
                                    # height=100,
                                    padding=padding.only(
                                        top=20, bottom=30, left=20, right=20),
                                    border_radius=8,
                                    on_hover=self.hover2,
                                    bgcolor='#3e3f4b',
                                    content=Text(
                                        'May occasionally produce harmful instruction or biased content',
                                        text_align='center',
                                    )
                                ),

                                Container(
                                    alignment=alignment.center,
                                    width=250,
                                    # height=100,
                                    padding=padding.only(
                                        top=20, bottom=30, left=20, right=20),
                                    border_radius=8,
                                    on_hover=self.hover2,
                                    bgcolor='#3e3f4b',
                                    content=Text(
                                        'Limited knowledge of world and events after 2021',
                                        text_align='center',
                                    )
                                ),

                            ]
                        ),
                    ]
                ),
               



            ]
        )
        self.textfieldrow = Row(
                                            controls=[
                                                self.message_field,
                                                self.voicebutton
                                                
                                            ]
                                        )
        self.main_content = Container(
            padding=padding.only(top=20,),
            expand=True,
            bgcolor=bg,
            content=Column(
                alignment='spaceBetween',
                horizontal_alignment='center',
                controls=[
                    Container(
                        width=1000,
                        expand=True,
                        content=self.content_area


                    ),

                    Container(
                        margin=margin.only(top=30),
                        height=100,
                        content=Column(
                            horizontal_alignment='center',
                            spacing=0,
                            controls=[
                                Card(
                                    elevation=5,
                                    content=Container(
                                        border_radius=10,
                                        bgcolor='#40414f',
                                        padding=padding.only(
                                            top=5, right=4, left=10, bottom=5),
                                        height=50,
                                        width=1000,
                                        content=self.textfieldrow,
                                    )
                                ),
                                Row(
                                    expand=True,
                                    controls=[
                                        Text(
                                            expand=True,
                                            value='This is running on free plan. Created by @Kilex (Baraka Kileo)',
                                            text_align='center'
                                        )
                                    ]
                                )
                            ]
                        )


                    ),

                ]
            )


        )

        self.page.add(
            Container(
                expand=True,
                bgcolor=bg,
                content=Row(
                    spacing=0,
                    controls=[
                        self.side_bar,
                        self.main_content,
                    ]
                )

            )
        )

    def new_chat_hover(self, e: HoverEvent):
        if e.data == 'true':
            e.control.bgcolor = '#2b2c2f'
        else:
            e.control.bgcolor = None
        e.control.update()

    def hover(self, e):
        if e.data == 'true':
            e.control.bgcolor = '#2a2b32'
        else:
            e.control.bgcolor = None
        e.control.update()

    def hover2(self, e):
        if e.data == 'true':
            e.control.bgcolor = '#2a2b32'
        else:
            e.control.bgcolor = '#3e3f4b'
        e.control.update()

    def send_clicked(self, e: TapEvent):
        self.textfieldrow.controls.remove(self.sendbutton)
        self.textfieldrow.controls.append(self.voicebutton)
        self.textfieldrow.update()
        message = self.message_field.value
        if message != '':
            self.message_field.value = ''
            self.message_field.update()

            if self.chat_gpt_label in self.content_area.controls:
                self.content_area.controls.clear()
                self.content_area.update()

            gpt_message = Row(
                vertical_alignment='center',
                controls=[
                    Container(
                        height=35, width=35,
                      
                        
                        content=Image(src="assets/chatgpt.png")

                    ),
                    self.cursor
                ]
            )

            response_label = Text('', expand=True, size=16,
                                  
                                  selectable=True)
            if self.blinking is False:
                self.blinking = True

                self.content_area.controls.append(
                    Container(
                        bgcolor='#343541',
                        padding=padding.only(
                                top=20, bottom=60, left=20, right=20
                        ),
                        content=Row(
                            controls=[
                                Container(
                                    border_radius=8,
                                    clip_behavior=ClipBehavior.ANTI_ALIAS,
                                    height=35, width=35,
                                    content=Image(
                                        src='https://cdn-icons-png.flaticon.com/512/1698/1698535.png',
                                        fit=ImageFit.COVER,
                                    )

                                ),
                                Text(
                                    message,
                                    expand=True,
                                    size=16,
                                    selectable=True
                                )
                            ]
                        )
                    )

                )
                self.content_area.update()

                sleep(.1)

                self.content_area.controls.append(
                    Container(
                        padding=padding.only(
                            top=20, bottom=10, left=20, right=20),

                        content=gpt_message
                    ),
                )
                self.content_area.update()

                

                chat_response = self.call_chatgpt(message)

                self.blinking = False
                sleep(0.4)
                self.blinking = True
                if self.cursor in gpt_message.controls:
                    gpt_message.controls.remove(self.cursor)
                    gpt_message.update()
                if response_label not in gpt_message.controls:
                    gpt_message.controls.append(response_label)
                    gpt_message.vertical_alignment = 'start'
                    gpt_message.update()
                    for char in chat_response:
                        response_label.value += char
                        response_label.update()
                        sleep(0.02)
                self.content_area.controls.append(Container(height=1))
                self.content_area.update()
                self.blinking = False
                

    def call_chatgpt(self, text):
        self.history_chats.controls.append(
                    Container(
                                on_hover=self.hover,
                                height=45,
                                border_radius=8,
              
                                on_click=self.history,


                                padding=8,
                                content=Row(
                                    # spacing=14,
                                    controls=[
                                        Icon(
                                            icons.CHAT_BUBBLE_OUTLINE_ROUNDED,
                                            size=16,
                                        ),
                                        Text(
                                            value=text,
                                            weight=FontWeight.W_100,
                                            width=200,
                                            no_wrap=True,
                                            size=16,

                                        )
                                    ]
                                )

                            )
                    )
        self.history_chats.update()
        self.prompt.append(
            {
                "role": "user",
                "content": text
            }
        )

        translator = googletrans.Translator()
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=text,
            temperature=0.7,
            max_tokens=3000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )
        finalresponse = translator.translate(response.choices[0].text,dest=self.langage)
        chat_response = finalresponse.text
       
       
      
        self.prompt.append(
            {
                'role': 'assistant',
                'content': chat_response
            }
        )
        return chat_response

    def blink(self,):
        while True:
            if self.blinking == False:
                break
            if self.cursor.opacity == 100:
                self.cursor.opacity = 0
            else:
                self.cursor.opacity = 100
            self.cursor.update()

            sleep(.4)
    def clearchat(self,e):  
        self.content_area.clean()
        self.history_chats.clean()
        self.content_area.update()
        self.history_chats.update()

    
    def creative(self,e):  
        e.control.bgcolor = 'blue'
        t =  e.control.content.value    
        self.message_field.value = t.replace('''"''', " ")
        self.message_field.update()
        self.page.update()
    def history(self,e):
        e.control.content.controls[1].value
        print(e.control.content.controls[1].value)
        value =  e.control.content.controls[1].value
        self.message_field.value =  value
      
        self.message_field.update()
    def newchat(self,e):
        
        self.content_area.update()
       
    def language_changed(self, e):
        choosed_language = self.drop_down_language.value
        if "English" in choosed_language:
            self.langage = "en"
        elif "Afrika" in choosed_language:
            self.langage = "af"
        elif "Swahili" in choosed_language:
            self.langage = "sw"
        elif "Albani" in choosed_language:
            self.langage = "sq"
        elif "Italian" in choosed_language:
            self.langage = "it"
        elif "Arabic" in choosed_language:
            self.langage = "ar"
        elif "Japan" in choosed_language:
            self.langage = "ja"
        elif "Azerba" in choosed_language:
            self.langage = "az"
        elif "Kannada" in choosed_language:
            self.langage = "kn"
        elif "Basque" in choosed_language:
            self.langage = "eu"
        elif "Korean" in choosed_language:
            self.langage = "ko"
        elif "Bengali" in choosed_language:
            self.langage = "bn"
        elif "Latin" in choosed_language:
            self.langage = "la"
        elif "Belarus" in choosed_language:
            self.langage = "be"
        elif "Latvian" in choosed_language:
            self.langage = "iv"
        elif "Bulgarian" in choosed_language:
            self.langage = "bg"
        elif "Lithuani" in choosed_language:
            self.langage = "it"
        elif "Catalan" in choosed_language:
            self.langage = "ca"
        elif "Macedo" in choosed_language:
            self.langage = "mk"
        elif "Simplified" in choosed_language:
            self.langage = "zh-CN"
        elif "Malay" in choosed_language:
            self.langage = "ms"
        elif "Traditi" in choosed_language:
            self.langage = "zh-TW"
        elif "Maltese" in choosed_language:
            self.langage = "mt"
        elif "Croatian" in choosed_language:
            self.langage = "hr"
        elif "Norwegian" in choosed_language:
            self.langage = "no"
        elif "Czech" in choosed_language:
            self.langage = "cz"
        elif "Persian" in choosed_language:
            self.langage = "fa"
        elif "Danish" in choosed_language:
            self.langage = "da"
        elif "Polish" in choosed_language:
            self.langage = "pl"
        elif "Dutch" in choosed_language:
            self.langage = "nl"
        elif "Portuguese" in choosed_language:
            self.langage = "pt"
        elif "Romanian" in choosed_language:
            self.langage = "ro"
        elif "Esperanto" in choosed_language:
            self.langage = "eo"
        elif "Russian" in choosed_language:
            self.langage = "ru"
        elif "Estonian" in choosed_language:
            self.langage = "et"
        elif "Serbian" in choosed_language:
            self.langage = "sr"
        elif "Filipino" in choosed_language:
            self.langage = "tl"
        elif "Slovak" in choosed_language:
            self.langage = "sk"
        elif "Finnish" in choosed_language:
            self.langage = "fi"
        elif "Slovenian" in choosed_language:
            self.langage = "sl"
        elif "French" in choosed_language:
            self.langage = "fr"
        elif "Spanish" in choosed_language:
            self.langage = "es"
        elif "Galician" in choosed_language:
            self.langage = "gl"
        elif "Georgian" in choosed_language:
            self.langage = "ka"
        elif "Swedish" in choosed_language:
            self.langage = "sv"
        elif "Greek" in choosed_language:
            self.langage = "el"
        elif "Tamil" in choosed_language:
            self.langage = "ta"
        elif "German" in choosed_language:
            self.langage = "de"
        elif "Slovak" in choosed_language:
            self.langage = "sk"
        elif "Telugu" in choosed_language:
            self.langage = "te"
        elif "Gujarati" in choosed_language:
            self.langage = "gu"
        elif "Thai" in choosed_language:
            self.langage = "th"
        elif "Haitian Creole" in choosed_language:
            self.langage = "ht"
        elif "Turkish" in choosed_language:
            self.langage = "tr"
        elif "Hebrew" in choosed_language:
            self.langage = "iw"
        elif "Hindi" in choosed_language:
            self.langage = "hi"
        elif "Urdu" in choosed_language:
            self.langage = "ur"
        elif "Hungarian" in choosed_language:
            self.langage = "hu"
        elif "Vietnamese" in choosed_language:
            self.langage = "vi"
        elif "Icelandic" in choosed_language:
            self.langage = "is"
        elif "Welsh" in choosed_language:
            self.langage = "cy"
        elif "Indonesian" in choosed_language:
            self.langage = "id"
        elif "Yiddish" in choosed_language:
            self.langage = "yi"
        notification.notify(title = "FAST ANSWER",message ="You changed language to " +choosed_language ,timeout=1)
        self.page.update()
        
    def  textfieledchanged(self,e):
        if int(len(self.message_field.value.replace(' ', "")) > 0):
            if self.voicebutton in self.textfieldrow.controls:
                self.textfieldrow.controls.remove(self.voicebutton)
            self.textfieldrow.controls.append(self.sendbutton)
            self.textfieldrow.update()
        else:
            self.textfieldrow.controls.remove(self.sendbutton)
            self.textfieldrow.controls.append(self.voicebutton)
            self.textfieldrow.update()


app(target=Main, view=WEB_BROWSER,assets_dir="assets",)
