from app.core.config import get_app_settings
from supabase import Client, create_client

settings = get_app_settings()


class SupabaseDB:
    """
    class instance for database connection to supabase

    :str: url: configuration for database url for data inside supafast project
    :str: key: configuration for database secret key for authentication
    :object: supabase: Supabase instance for connection to database environment
    """

    url: str = settings.supabase_url
    key: str = settings.supabase_apikey
    supabase: Client = create_client(url, key)
