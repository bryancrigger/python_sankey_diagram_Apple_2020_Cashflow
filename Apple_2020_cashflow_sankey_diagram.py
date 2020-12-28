import pandas as pd
import plotly.graph_objects as go



# Read in data for nodes and for the links
links = pd.read_excel('...file_path\sankey_diagram_Apple_cashflow_2020_links.xlsx')
nodes = pd.read_excel('...file_path\sankey_diagram_Apple_cashflow_2020_nodes.xlsx')


# Convert the DataFrames to a list
nodes_list = [nodes.columns.values.tolist()] + nodes.values.tolist()
links_list = [links.columns.values.tolist()] + links.values.tolist()


# Retrieve headers and build dataframes
nodes_headers = nodes_list.pop(0)
links_headers = links_list.pop(0)
df_nodes = pd.DataFrame(nodes_list, columns = nodes_headers)
df_links = pd.DataFrame(links_list, columns = links_headers)


# Sankey plot setup
data_trace = dict(
    type='sankey',                                              # Sankey Plot type
    domain = dict(
      x =  [0,1],
      y =  [0,1]
    ),
    orientation = "h",                                          # 'h' = horizontal sankey plot, 'v' = vertical sankey plot
    arrangement = "snap",
    valueformat = "${,}",                                       # Formats the value shown with a dollar sign out front (ex. value = 726 -> ouput = $726)
    node = dict(
    #   pad = 30,                                               # The bigger the number the more space between each line vertically
      thickness = 10,                                           # The width of the vertical lines/nodes
      line = dict(
        color = "black",
        width = 0
      ),
      label =  df_nodes['label'].dropna(axis=0, how='any'),     # Name of the node
      x = df_nodes['x'].dropna(axis=0, how='any'),              # Horizontal position of the node's center (from left to right)
      y = df_nodes['y'].dropna(axis=0, how='any'),              # Vertical position of the node's center (from top to bottom)
      color = df_nodes['color']                                 # Color of the node
    ),
    link = dict(
      source = df_links['source'].dropna(axis=0, how='any'),    # Link starting from this node
      target = df_links['target'].dropna(axis=0, how='any'),    # Link going to this node
      value = df_links['value'].dropna(axis=0, how='any'),
      color = df_links['color'].dropna(axis=0, how='any'),
  )
)


# Option 1, with a "basic" layout with a Title and Subtitle with reference link.
layout = dict(
        title = "Apple: Still squeezing juice from the iPhone<br><span style='font-size:0.6em;color:gray'>Link and reference <a href='https://www.reddit.com/r/dataisbeautiful/comments/albi5w/apples_latest_quarterly_income_statement/'>here.</a></span><span style='font-size:0.6em;color:gray'> Hover over diagram for more info on each flow.</span>",
    height = 750,                                               # Height of the figure output
    width = 1200,                                               # Width of figure output
    font = dict(
      size = 12),)


# Option 2. A more advanced layout consisting of the Title and Subtitle with reference link and some additional button features.The buttons in this 
# layout run down the left side of the plot and allow the user to make some additional visual adjustments to the plot that are already programed
# into the plot. Included are just a few examples of buttons and plot adjustments that can be included in a Sankey plot. 

layout_w_buttons =  dict(
    title = "Apple: Still squeezing juice from the iPhone<br><span style='font-size:0.6em;color:gray'>Link and reference <a href='https://www.reddit.com/r/dataisbeautiful/comments/albi5w/apples_latest_quarterly_income_statement/'>here.</a></span><span style='font-size:0.6em;color:gray'> Hover over diagram for more info on each flow.</span>",
    font = dict(
      size = 12
    ),
    height=750,
    width = 1200,
    updatemenus= [
            dict(
                y=1,
                buttons=[
                    dict(
                        label='Light',
                        method='relayout',
                        args=['paper_bgcolor', 'white']
                    ),
                    dict(
                        label='Dark',
                        method='relayout',
                        args=['paper_bgcolor', 'black']
                    )
                ]
            
            ),
            dict(
                y=0.9,
                buttons=[
                    dict(
                        label='Thin',
                        method='restyle',
                        args=['node.thickness', 7]
                    ),
                    dict(
                        label='Medium',
                        method='restyle',
                        args=['node.thickness', 12]
                    ),
                    dict(
                        label='Thick',
                        method='restyle',
                        args=['node.thickness', 20]
                    )     
                ]
            ),
            dict(
                y=0.8,
                buttons=[
                    dict(
                        label='Small gap',
                        method='restyle',
                        args=['node.pad', 20]
                    ),
                    dict(
                        label='Large gap',
                        method='restyle',
                        args=['node.pad', 50]
                    )
                ]
            ),
            dict(
                y=0.7,
                buttons=[
                    dict(
                        label='Snap',
                        method='restyle',
                        args=['arrangement', 'snap']
                    ),
                    dict(
                        label='Perpendicular',
                        method='restyle',
                        args=['arrangement', 'perpendicular']
                    ),
                    dict(
                        label='Freeform',
                        method='restyle',
                        args=['arrangement', 'freeform']
                    ),
                    dict(
                        label='Fixed',
                        method='restyle',
                        args=['arrangement', 'fixed']
                    )       
                ]
            ),
            dict(
                y=0.6,
                buttons=[             
                    dict(
                        label='Horizontal',
                        method='restyle',
                        args=['orientation', 'h']
                    ),
                    dict(
                        label='Vertical',
                        method='restyle',
                        args=['orientation', 'v']
                    )
                ]
            
            )
        ]
)


# Here we join together the data that formats the basics of how the Sankey plot with look with the layout that customizes the figure's details.
# The layout function you can choose either the basic option "layout" or the advanced layout "layout_w_buttons" that includes the buttons with
# additional plot feature changes. 
fig1 = go.Figure(data=[data_trace], layout=layout_w_buttons)
fig1.show()


# Last step is writing/printing your Sankey Figure as an html file so that the functions within the plot can be utilized
fig1.write_html("...file_path/Apple_Cashflow_2020.html")




