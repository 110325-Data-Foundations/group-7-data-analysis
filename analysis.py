import pandas as pd

def analyze_data(file_path):
    """
    Analyzes the data from a CSV file and returns basic statistics.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    dict: A dictionary containing basic statistics of the data.
    """
    # Load the data
    data = pd.read_csv(file_path)

    # get columns
    columns = data.columns.tolist()
    print(f"Columns in the dataset: {columns}")

    # Clean data
    data = data.dropna()

    # count duplicates for each column
        # count duplicates for each column
    for col in columns:
        col_dup_count = data[col].duplicated().sum()
        print(f"Number of duplicate values in column '{col}': {col_dup_count}")
    
    
    #remove duplicates
    data = data.drop_duplicates()

    # count duplicates after removal
    duplicate_count_after = data.duplicated().sum()
    print(f"Number of duplicate rows after removal: {duplicate_count_after}")

    # check data types
    data = data.convert_dtypes()

    # save updated csv
    data.to_csv('cleaned_data.csv', index=False)

    print(data.head())

def simplify_data(file_path):
    df = pd.read_csv(file_path)

    df.drop(columns=['City','CO AQI Value','CO AQI Category','Ozone AQI Value','Ozone AQI Category','NO2 AQI Value','NO2 AQI Category','PM2.5 AQI Value','PM2.5 AQI Category'], inplace=True)

    country_aqi_df = df.groupby('Country', as_index=False)['AQI Value'].mean().rename(columns={'AQI Value': 'Average AQI'}).round(1)

    country_aqi_df.to_csv('Country_AQI_data.csv', index=False)

def split_by_continent(file_path):
    df = pd.read_csv(file_path)

    # Dictionary mapping countries to continents
    continent_map = {
        # --- Africa (54) ---
        'Algeria':'Africa','Angola':'Africa','Benin':'Africa','Botswana':'Africa','Burkina Faso':'Africa',
        'Burundi':'Africa','Cabo Verde':'Africa','Cameroon':'Africa','Central African Republic':'Africa',
        'Chad':'Africa','Comoros':'Africa','Congo':'Africa','Côte d\'Ivoire':'Africa',
        'Democratic Republic of the Congo':'Africa','Egypt':'Africa','Equatorial Guinea':'Africa',
        'Eritrea':'Africa','Eswatini':'Africa','Ethiopia':'Africa','Gabon':'Africa','Gambia':'Africa',
        'Ghana':'Africa','Guinea':'Africa','Guinea-Bissau':'Africa','Kenya':'Africa','Lesotho':'Africa',
        'Liberia':'Africa','Libya':'Africa','Madagascar':'Africa','Malawi':'Africa','Mali':'Africa',
        'Mauritania':'Africa','Mauritius':'Africa','Morocco':'Africa','Mozambique':'Africa','Namibia':'Africa',
        'Niger':'Africa','Nigeria':'Africa','Rwanda':'Africa','Senegal':'Africa','Seychelles':'Africa',
        'Sierra Leone':'Africa','Somalia':'Africa','South Africa':'Africa','South Sudan':'Africa','Sudan':'Africa',
        'Togo':'Africa','Tunisia':'Africa','Uganda':'Africa','United Republic of Tanzania':'Africa',
        'Zambia':'Africa','Zimbabwe':'Africa',

        # --- Asia (45) ---
        'Afghanistan':'Asia','Armenia':'Asia','Azerbaijan':'Asia','Bahrain':'Asia','Bangladesh':'Asia',
        'Bhutan':'Asia','Cambodia':'Asia','China':'Asia','Cyprus':'Asia','Georgia':'Asia','India':'Asia',
        'Indonesia':'Asia','Iran (Islamic Republic of)':'Asia','Iraq':'Asia','Israel':'Asia','Japan':'Asia',
        'Jordan':'Asia','Kazakhstan':'Asia','Kuwait':'Asia','Kyrgyzstan':'Asia',"Lao People's Democratic Republic":'Asia',
        'Lebanon':'Asia','Malaysia':'Asia','Maldives':'Asia','Mongolia':'Asia','Myanmar':'Asia','Nepal':'Asia',
        'Oman':'Asia','Pakistan':'Asia','Palau':'Asia','Philippines':'Asia','Qatar':'Asia',
        'Republic of Korea':'Asia','Saudi Arabia':'Asia','Singapore':'Asia','Sri Lanka':'Asia','State of Palestine':'Asia',
        'Syrian Arab Republic':'Asia','Tajikistan':'Asia','Thailand':'Asia','Turkmenistan':'Asia','United Arab Emirates':'Asia',
        'Uzbekistan':'Asia','Viet Nam':'Asia','Yemen':'Asia',

        # --- Europe (40) ---
        'Albania':'Europe','Andorra':'Europe','Austria':'Europe','Belarus':'Europe','Belgium':'Europe',
        'Bosnia and Herzegovina':'Europe','Bulgaria':'Europe','Croatia':'Europe','Czechia':'Europe',
        'Denmark':'Europe','Estonia':'Europe','Finland':'Europe','France':'Europe','Germany':'Europe',
        'Greece':'Europe','Hungary':'Europe','Iceland':'Europe','Ireland':'Europe','Italy':'Europe',
        'Latvia':'Europe','Lithuania':'Europe','Luxembourg':'Europe','Malta':'Europe','Monaco':'Europe',
        'Montenegro':'Europe','Netherlands':'Europe','Norway':'Europe','Poland':'Europe','Portugal':'Europe',
        'Republic of Moldova':'Europe','Romania':'Europe','Russian Federation':'Europe',
        'Serbia':'Europe','Slovakia':'Europe','Slovenia':'Europe','Spain':'Europe','Sweden':'Europe',
        'Switzerland':'Europe','Ukraine':'Europe','United Kingdom of Great Britain and Northern Ireland':'Europe',

        # --- North America (18) ---
        'Barbados':'North America','Belize':'North America','Canada':'North America','Costa Rica':'North America',
        'Cuba':'North America','Dominican Republic':'North America','El Salvador':'North America','Guatemala':'North America',
        'Haiti':'North America','Honduras':'North America','Jamaica':'North America','Mexico':'North America',
        'Nicaragua':'North America','Panama':'North America','Saint Kitts and Nevis':'North America',
        'Saint Lucia':'North America','Trinidad and Tobago':'North America','United States of America':'North America',

        # --- South America (12) ---
        'Argentina':'South America','Bolivia (Plurinational State of)':'South America','Brazil':'South America',
        'Chile':'South America','Colombia':'South America','Ecuador':'South America','Guyana':'South America',
        'Paraguay':'South America','Peru':'South America','Suriname':'South America','Uruguay':'South America',
        'Venezuela (Bolivarian Republic of)':'South America',

        # --- Oceania (6) ---
        'Australia':'Oceania','New Zealand':'Oceania','Papua New Guinea':'Oceania','Solomon Islands':'Oceania',
        'Vanuatu':'Oceania','Palau':'Oceania'
    }

    #Create a dataframe with two columns Country and Continent
    df['Continent'] = df['Country'].map(continent_map)

    for continent, sub_df in df.groupby('Continent'):
        filename = f"{continent.replace(' ', '_')}_AQI.csv" #create file for each continent
        sub_df.to_csv(filename, index=False) #create csv file in repo based on the sub dataframe from main df

simplify_data('dataset.csv')
split_by_continent('Country_AQI_data.csv')

analyze_data('dataset.csv')