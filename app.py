import folium
import jinja2

# Variables:
tooltip_1 = "informal market"
my_js = """<script>
document.getElementByID('button').addEventListener('click', function() {console.log('dajska')})
</script>"""

m = folium.Map(location=[-33.8130, 18.4990], zoom_start=14.5)

folium.Marker([-33.80706151725782, 18.513929105689666],
              icon=folium.Icon(icon_color="darkpurple", icon="glyphicon-hand-up"),
              tooltip=(tooltip_1),
              popup="<button id='market_1'>Click Me</button>"
              ).add_to(m)

folium.Marker([-33.81581371409407, 18.49843631229927],
              icon=folium.Icon(icon_color="darkpurple", icon="glyphicon-hand-up")
              ).add_to(m)

el = folium.MacroElement().add_to(m)
el._template = jinja2.Template("""
    {% macro script(this, kwargs) %}
         document.getElementById('button').addEventListener('click', function() {
             console.log('Clisa');
         }) 
    {% endmacro %}
""")


m.save("index.html")