import pyttsx3
from flet import *
import flet as ft
import math
from time import *
import googletrans
import openai
import datetime
from plyer import *
import plyer
openai.api_key = "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"


class Home(Container):
		def __init__(self, page):
				
				super().__init__()
				
				self.page = page
				
				self.alignment = alignment.Alignment(x=0, y=-1)
				self.bgcolor = '#1E0A59'
				self.border_radius = 20
				self.expand = True
				self.width1 = 250
				self.translator = googletrans.Translator()
				self.width2 = None
				self.send_button =  IconButton(
																													icon=ft.icons.SEND_ROUNDED,
																														icon_color="grey",
																															tooltip="send", 
																														on_click=self.send,
																														disabled=True
																											)
				self.status = ft.Text("Online",
															color="green",font_family='Poppins BlackItalic')
				self.question = None
				self.drop_down_language = ft.Dropdown(

						height=90,
						border_radius=10,
						border_color="blue",
						hint_text="Choose languages",
						bgcolor="yellow",
						autofocus=True,
						border_width=2,
						focused_border_color="blue",
						helper_style=TextStyle(
								color="white",
								weight="w600"

						),)
				

				self.audio =  ft.Audio(
				src="https://luan.xyz/files/audio/ambient_c_motion.mp3", 
		)   
			 
				self.about = ft.Text(
						value="Get answers to your questions as fast as possible",
						color="#e3dbdb",
						size=10,

				)
				self.fast_answer =  ft.Text(value="fast Answer",
																																							color="white",
																																							size=20,)

				self.langage = "en"
			 

				self.drop_down_language = ft.Dropdown(

						height=90,
						border_radius=10,
						border_color="blue",
						hint_text="Choose languages",
						bgcolor="yellow",
						autofocus=True,
						border_width=2,
						focused_border_color="blue",
						helper_style=TextStyle(
								color="white",
								weight="w600"

						),
						prefix_icon=ft.icons.LANGUAGE_ROUNDED,
						on_change=self.language_changed,



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
				self.answer = ""

				self.clear_dialong = ft.AlertDialog(
						modal=True,
						
					 
						title=ft.Text("Please confirm"),
						content=ft.Column(scroll="auto",controls=[
						
						
				
						]),
						actions=[
								ft.TextButton("Yes", on_click=self.clear_chats),
								ft.TextButton("No", on_click=self.close_clear_dlg),
						],
						actions_alignment=ft.MainAxisAlignment.CENTER,

				)

				self.message_container = None
				self.allmsg = ft.Column(
						alignment="start",
						spacing=0,
						controls=[
								ft.Text("...")
						]
				)

				self.message = ft.TextField(
						expand=True,
						autofocus=True,
						border_color="transparent",
						border_radius=30,
						hint_text="message",
						on_submit=self.send,
						on_change=self.enable_send_button,
						
				)

				self.content = (
						ft.Column(

								expand=True,
								alignment="spaceBetween",
								spacing=0,
								controls=[
										Container(

												height=60,
												bgcolor='#0C029B',
												border_radius=border_radius.only(10, 10, 0, 0),

												content=(
														ft.Column(
																alignment=alignment.Alignment(x=0, y=0),
																controls=[
																		ft.Row(alignment="start",
																					 height=45,
																					 controls=[IconButton(
																							 icon=ft.icons.ARROW_BACK_OUTLINED,
																							 tooltip="Back",
																							 icon_color="white",
																							 on_click= self.homepage,
																							 
																					 ), ft.CircleAvatar(
																							 foreground_image_url="https://cdn-icons-png.flaticon.com/512/1698/1698535.png"),
																							 ft.Row(alignment="center",
																											expand=True,

																											controls=[ft.Container(
																													content=(ft.Column(
																															height=50,
																															spacing=0,
																															alignment=alignment.Alignment(
																																	x=0, y=0),
																															controls=[ft.Column(
																																	spacing=2,
																																	controls=[
																																		 self.fast_answer,
																																			self.status
																																	]
																															)

																															]
																													)),)]),
																							 ft.Row(
																							 alignment="spaceBetween",
																							 height=50,

																							 controls=[
																									 IconButton(
																											 icon=ft.icons.SUPPORT_AGENT_OUTLINED,
																											 tooltip="support agent",
																											 icon_color="white",
																											 on_click=lambda e: e.page.launch_url("https://wa.link/wz1vl2")),


																									 ft.PopupMenuButton(
																											 items=[
																													 ft.PopupMenuItem(
																															 icon=ft.icons.CLEAR_ALL_ROUNDED, text="Clear chats", on_click=self.open_clear_dlg),
																													 ft.PopupMenuItem(
																															 icon=ft.icons.LANGUAGE_ROUNDED, text="Change language", on_click=self.change_langage),
																													 ft.PopupMenuItem(
																															 icon=ft.icons.SHARE_OUTLINED, text="Share", on_click=self.Check_battery),

																											 ]

																									 )]
																					 )
																					 ])

																]
														)
												)

										), ft.Container(
												height=15,
												bgcolor="#2b2b2b00",

												border_radius=border_radius.only(0, 0, 10, 10),
												content=(
														ft.Row(
																alignment=ft.MainAxisAlignment.CENTER,
																controls=[
self.about                                ]
														)
												)



										),
										Container(
												expand=True,
												bgcolor='#1E0A59',


												content=(
														ft.ListView(
																auto_scroll=True,
																
																
																controls=[
																		self.allmsg
																]
														)
												)
										),
										Container(height=60,
															bgcolor='#0C029B',
															border_radius=30,
															content=(ft.Row(alignment="spaceBetween",
																							controls=[ft.Container(
																									width=55,
																									height=55,
																									border_radius=20,
																									bgcolor="blue",

																									content=(
																											IconButton(
																												icon=ft.icons.MIC_ROUNDED, icon_color="white", on_click=self.speak)

																									)
																							), self.message,
																							 ft.Container(
																									width=55,
																									height=55,
																									border_radius=55/2,
																									bgcolor="blue",

																									content=(
																											self.send_button

																									)
																							)

																								 
																							]))
															),

								]
						)
				)

		def send(self, e):
				self.send_button.disabled = True
				self.send_button.icon_color =  'grey'
				self.send_button.update()
				self.page.update()
				time = datetime.datetime.now()
				my_time = time.strftime("%H:%M:%S")
				translator = googletrans.Translator()

				question = self.message.value
				self.question = question

				length = len(question)

				self.message.value = ""
				if length >= 40:

						self.width1 = 250
				else:
						self.width1 = None
				self.message_container = ft.Row(controls=[ft.Container(
						padding=8,
						width=self.width1,
						gradient=ft.LinearGradient(
								begin=ft.alignment.top_center,
								end=ft.alignment.bottom_center,
								colors=[
										"blue", "#0032FF"],
						),

						border_radius=border_radius.only(20, 0, 20, 20),

						content=(ft.Text(self.question, selectable=True))),

				])
				self.allmsg.controls.append(
						ft.Row(
								alignment="end",
								controls=[
										ft.CircleAvatar(
												foreground_image_url='https://i.pinimg.com/originals/12/eb/6d/12eb6d9a47e880e74c60987729c64b00.jpg',
												radius=15
										)
								]
						)
				)
				self.allmsg.controls.append(
						ft.Row(alignment="end",

									 controls=[ft.Container(
											 margin=margin.only(0, 0, 30, 0),
											 content=(self.message_container)
									 )]),)
				self.message.update()
				
				sleep(0.1)

				self.allmsg.update()
				question1 = translator.translate(question, dest="en")
				question = question1.text

			
				response = openai.Completion.create(
						model="text-davinci-003",
						prompt=question,
						temperature=0.7,
						max_tokens=3000,
						top_p=1,
						frequency_penalty=0,
						presence_penalty=0,
				)

				answer = response.choices[0].text
				answer = answer[2:]
				self.answer = answer
				result = translator.translate(answer, dest=self.langage)
				answer = result.text
				length2 = len(answer)

				if length2 >= 40:
						self.width2 = 280
				else:
						self.width2 = None

				self.allmsg.update()
				self.allmsg.controls.append(
						ft.Row(
								alignment="start",
								controls=[
										ft.CircleAvatar(
												foreground_image_url='https://cdn-icons-png.flaticon.com/512/1698/1698535.png',
												radius=15
										)
								]
						)
				)
				bot =       ft.Text(value='', selectable=True)
				self.allmsg.controls.append(
						ft.Row(alignment="start",

									 controls=[ft.Container(
											 margin=margin.only(30, 0, 0, 0),
											 
									 
											 content=(
													 ft.Row(controls=[ft.Container(
															 padding=8,
															 width=self.width2,
															 gradient=ft.LinearGradient(
																	 begin=ft.alignment.top_center,
																	 end=ft.alignment.bottom_center,
																	 colors=[
																			 "#A400FF", "#7D00FF"],
															 ),
															 border_radius=border_radius.only(0, 20, 20, 20),

															 content=(ft.Column(
																	 controls=[
						Text("@kilex",
								color="black",
								italic=True
								),
																 bot,
																			 ft.Row(alignment=ft.MainAxisAlignment.END,
																							controls=[])]))),

													 ])
											 )
									 )]),)
				for letter in answer:
						bot.value = bot.value +letter
			
						self.page.update()
						sleep(0.03
									)
				
				self.allmsg.controls.append(Container(height=2))
			 
				self.allmsg.update()

		def delete(self,e):
				self.allmsg.remove(e)
				self.page.update()

		def speak(self, e):

				engine = pyttsx3.init()
				voices = engine.getProperty('voices')
				engine.setProperty('voice', voices[0].id)
				engine.setProperty('rate', 140)
				engine.say(self.answer)
				engine.runAndWait()
				print(self.question)

		def close_clear_dlg(self, e):

				self.clear_dialong.open = False
				self.page.update()

		def open_clear_dlg(self, e):
				self.page.dialog = self.clear_dialong
				self.clear_dialong.open = True
				self.page.update()

		def clear_chats(self, e):
				self.allmsg.clean()
				self.allmsg.update()
				self.clear_dialong.open = False
				self.page.update()

		def change_langage(self, e):
				self.allmsg.controls.append(
						ft.Container(height=20)
				)

				self.allmsg.controls.append(
						self.drop_down_language
				)
				self.allmsg.update()

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
				self.allmsg.controls.remove(self.drop_down_language)
				print(self.langage)
				self.status.value = self.translator.translate(
						"Online", dest=self.langage).text
			 
				self.about.value = self.translator.translate(
						"Get answers to your questions as fast as possible",
						 dest=self.langage).text
				
				self.fast_answer.value = self.translator.translate(
						"Fast Answer",
						 dest=self.langage).text
				
				self.message.hint_text = self.translator.translate(
						"message",
						 dest=self.langage).text
				self.page.update()
				self.allmsg.controls.append(
						ft.Container(height=9)
				)
			 
				
				alter = self.translator.translate(
						"Language change to"+choosed_language, dest=self.langage)
				alter = alter.text
				
				self.allmsg.controls.append(
						ft.Row(
								alignment=ft.MainAxisAlignment.CENTER,
								controls=[
										ft.Container(
												border_radius=15,
												padding=padding.only(5, 0, 5, 0),
												bgcolor="#33109f",
												content=(
														ft.Text(alter


																		)
												)
										)
								])
				)
				self.allmsg.controls.append(
						ft.Container(height=20)
				)
				self.allmsg.update()
			 

		def Check_battery(self, e):
				shd = ft.ShakeDetector(
						minimum_shake_count=2,
						shake_slop_time_ms=300,
						shake_count_reset_time_ms=1000,
						on_shake=lambda _: print("SHAKE DETECTED!"),
				)
				self.page.overlay.append(shd)
		def enable_send_button(self,e):
				
				if len(self.message.value.replace(" ", "")) > 0:
						self.send_button.disabled = False
						self.send_button.icon_color = "white"
						self.send_button.update()
				else:
						self.send_button.disabled = True
						self.send_button.icon_color = "grey"
						self.send_button.update()
						print(len(self.message.value))
		def homepage(self,e):
				print("hey")
				self.page.go("/community_chat")
				self.page.update()
