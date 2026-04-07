CATALOG = "edu260323"
SCHEMA = "hjh"
VOLUME = "volume"
DATA_DIR = "inv"

BASE_VOLUME_PATH = f"/Volumes/{CATALOG}/{SCHEMA}/{VOLUME}/{DATA_DIR}"
BASE_TABLE_NAMESPACE = f"{CATALOG}.{SCHEMA}"

BRONZE_CONTENTS_PATH = f"{BASE_VOLUME_PATH}/bronze_ott_contents.csv"
BRONZE_LOGS_PATH = f"{BASE_VOLUME_PATH}/bronze_ott_logs.csv"
BRONZE_USERS_PATH = f"{BASE_VOLUME_PATH}/bronze_ott_users.csv"

BRONZE_OTT_CONTENTS_TABLE = f"{BASE_TABLE_NAMESPACE}.bronze_ott_contents"
BRONZE_OTT_LOGS_TABLE = f"{BASE_TABLE_NAMESPACE}.bronze_ott_logs"
BRONZE_OTT_USERS_TABLE = f"{BASE_TABLE_NAMESPACE}.bronze_ott_users"

SILVER_OTT_CONTENTS_TABLE = f"{BASE_TABLE_NAMESPACE}.silver_ott_contents"
SILVER_OTT_LOGS_TABLE = f"{BASE_TABLE_NAMESPACE}.silver_ott_logs"
SILVER_OTT_USERS_TABLE = f"{BASE_TABLE_NAMESPACE}.silver_ott_users"

SILVER_OTT_CONTENTS_DUP_TABLE = f"{BASE_TABLE_NAMESPACE}.silver_ott_contents_dup"
SILVER_OTT_LOGS_DUP_TABLE = f"{BASE_TABLE_NAMESPACE}.silver_ott_logs_dup"
SILVER_OTT_USERS_DUP_TABLE = f"{BASE_TABLE_NAMESPACE}.silver_ott_users_dup"

GOLD_MONTHLY_CONTENT_TABLE = f"{BASE_TABLE_NAMESPACE}.gold_cnt_mon_content"


def genre_top3_table_name(country: str, month_safe: str) -> str:
    return f"{BASE_TABLE_NAMESPACE}.silver_{country}_genre_{month_safe}_top3"
