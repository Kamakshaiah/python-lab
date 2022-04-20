import flask
import dash
import dash_html_components as html 
import pandas as pd
import numpy as np

server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server)

app.layout = html.Div(
	children=[
            '''Just a stuff'''
		# x = np.random.normal(0, 1, 5)
		# y = np.random.normal(0, 1, 5)
		# df = pd.DataFrame({'x':x, 'y':y})
		
	]
)

if __name__ == '__main__':
	app.run_server(debug=True, port=8050, host='127.0.0.1')
	app.run_server(debug=True)
