import pandas as pd
import plotly.express as px


class MapPlotter:

    def __init__(self, merged_file):
        """
        Initialize MapPlotter Class with paths to Excel files.

        :param merged_file: The path to Excel file with dictionaries and coordinates.
        """
        self.merged_file = merged_file
        self.df = None

    def process_and_plot(self):
        """
        Read data from Excel file containing river dictionaries and respective coordinates,
        process them to create a DataFrame with split coordinates, and plot a map with 'Frequency'.
        """
        df = pd.read_excel(self.merged_file)
        # Create a new DataFrame to store the split rows
        new_rows = []

        # Iterate through each row to convert the coord values to strings and split into lists with separator
        for index, row in df.iterrows():
            river = row['name_en']
            frequency = row['Frequency']
            latitudes = str(row['latitude']).split(',')
            longitudes = str(row['longitude']).split(',')

            # Check the lengths of lists if there are multiple coordinates
            if len(latitudes) > 1 and len(longitudes) > 1:
                for lat, lon in zip(latitudes, longitudes):
                    new_rows.append({'Frequency': frequency, 'name_en': river, 'latitude': lat, 'longitude': lon})
            else:
                new_rows.append(
                    {'Frequency': frequency, 'name_en': river, 'latitude': latitudes[0], 'longitude': longitudes[0]})

        # Create a new DataFrame from the split rows
        self.df = pd.DataFrame(new_rows)

        # Convert latitude and longitude columns to numeric type
        self.df['latitude'] = pd.to_numeric(self.df['latitude'], errors='coerce')
        self.df['longitude'] = pd.to_numeric(self.df['longitude'], errors='coerce')

        # Drop the rows which have missing values
        self.df.dropna(subset=['latitude', 'longitude', 'Frequency'], inplace=True)

        # Create and customize an intensity or frequency map and layout
        fig = px.scatter_mapbox(self.df,
                                lat='latitude',
                                lon='longitude',
                                size_max='Frequency',
                                color='Frequency',
                                color_continuous_scale='plasma',
                                range_color=[0, 70],  # Customize according to min and max range
                                color_continuous_midpoint=35,
                                hover_name='name_en',
                                zoom=1)

        fig.update_layout(mapbox_style="open-street-map",
                          mapbox_zoom=1,
                          mapbox_center_lat=self.df['latitude'].mean(),
                          mapbox_center_lon=self.df['longitude'].mean(),
                          title="Intensity Map of River Connectivity Study",
                          title_x=0.5,
                          title_y=0.95
                          )

        # Write and produce a map in HTML format
        fig.write_html('Outputs/river_connectivity_studies.html')
        fig.show()
        # pio.write_image(fig, "Outputs/river_connectivity_studies.png", format='png', width=900, height=600, scale=2)
