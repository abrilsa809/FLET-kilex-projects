from flet import *
from pages.chat import Home
from pages.home import Home2


def views_handler(page):
  return {
    '/':View(
        route='/',
        bgcolor ='#1E0A59',
        controls=[
          Home(page)
        ]
      ),
      "/community_chat":View(
    route="/community_chat",
    bgcolor="green",
    controls=[
   
    ]
      )
    
  }