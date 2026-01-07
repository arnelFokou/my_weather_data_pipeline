import sys

from pathlib import Path
import pandas as pd

# load_dotenv()
path = Path(__file__).resolve()
archive_dir = path.parent.parent
sys.path.append(str(archive_dir))

def load(**args):
    data_cleaned = args['ti'].xcom_pull(task_ids = "transform")
   
    df = pd.DataFrame([data_cleaned])
   
    name_file = data_cleaned['extract_date'].replace(" ","_").split(":")[0] 

    df.to_csv(f"files_extracted/extraction_{name_file+"h"}.csv")
    

