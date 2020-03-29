from src.data_prep import prep_data
from src.sidebar import create_sidebar
from src.main_area import create_main_area


data = prep_data()

# create sidebar
canton, masks, gloves, sanitizer = create_sidebar(data)

# create main area
create_main_area(data, canton, masks, gloves, sanitizer)
