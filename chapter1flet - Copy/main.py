from flet import *
from views import views_handler

def main(page: Page):
  page.theme_mode = "dark"
  
  def route_change(route):
    print(page.route)
    page.theme =Theme(use_material3=True)
    page.views.clear()
    page.views.append(
      views_handler(page)[page.route]
    )


  page.on_route_change = route_change
  page.go('/')

app(target=main,view=WEB_BROWSER,port=8080)
