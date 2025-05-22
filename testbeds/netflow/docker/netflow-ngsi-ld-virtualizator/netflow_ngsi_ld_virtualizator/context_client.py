import requests
import logging

logger = logging.getLogger(__name__)
class ContextCatalogClient:
    def __init__(self, base_url):
        self.base_url = base_url

    # Method to make the GET query to the context-catalog service
    def fetch_data(self, endpoint="context.jsonld"):
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.get(url)
            response.raise_for_status()  
            return response.json() 
        except requests.exceptions.RequestException as e:
            logger.exception(f"Error in GET request: {e}")
            return None

    # Traverses Context URLs
    def search_context_urls(self, data):
        if "@context" in data:
            for context_url in data["@context"]:
                try:
                    logger.info(f"Context URL: {context_url}")
                    response = requests.get(context_url)
                    response.raise_for_status()
                except requests.exceptions.RequestException as e:
                    logger.exception(f"Error in GET request: {e}")
                    return None
        else: 
            logger.error("No '@context' found in the data.")

    # Traverses Context URLs and stores @context keys and values ​​in a dictionary
    def search_context_data(self, data):
        context_urls = data.get("@context", [])
        all_context_data = {}
        for context_url in context_urls:
            try:
                # Make a GET request to each URL in the list
                logger.info(f"Fetching context from {context_url}")
                response = requests.get(context_url)
                response.raise_for_status()
                context_data = response.json()

                # Loop through the @context keys in each response
                '''
                if "@context" in context_data:
                    #if isinstance(context_data, dict):
                    #    all_context_data.update(context_data)
                    for key, value in context_data["@context"].items():
                        #logger.info(f"Key: {key}, Value: {value}")
                        if key in all_context_data:
                            if isinstance(all_context_data[key], list):
                                all_context_data[key].append(value)
                            else:
                                all_context_data[key] = [all_context_data[key], value]
                        else:
                            all_context_data[key] = value
                '''
                if "@context" in context_data:
                    '''
                    if isinstance(context_data, dict):
                        all_context_data.update(context_data)
                    '''
                    if isinstance(context_data["@context"], list):
                        for cd in context_data["@context"]:
                            if isinstance(cd, dict):
                                for key, value in cd.items():
                                    #logger.info(f"Key: {key}, Value: {value}")
                                    if key in all_context_data:
                                        # Check if it's already a list, if not, convert to list
                                        if not isinstance(all_context_data[key], list):
                                            all_context_data[key] = [all_context_data[key]]
                                        
                                        # Add only unique values to the list
                                        if value not in all_context_data[key]:
                                            all_context_data[key].append(value)
                                        '''
                                        if isinstance(all_context_data[key], list):
                                            all_context_data[key].append(value)
                                        else:
                                            all_context_data[key] = [all_context_data[key], value]
                                        '''
                                    else:
                                        all_context_data[key] = value
                    elif isinstance(context_data["@context"], dict):
                        for key, value in context_data["@context"].items():
                            #logger.info(f"Key: {key}, Value: {value}")
                            if key in all_context_data:
                                # Check if it's already a list, if not, convert to list
                                if not isinstance(all_context_data[key], list):
                                    all_context_data[key] = [all_context_data[key]]
                                
                                # Add only unique values to the list
                                if value not in all_context_data[key]:
                                    all_context_data[key].append(value)
                                '''
                                if isinstance(all_context_data[key], list):
                                    all_context_data[key].append(value)
                                else:
                                    all_context_data[key] = [all_context_data[key], value]
                                '''
                            else:
                                all_context_data[key] = value
                    else:
                        logger.warning(f"No '@context' found in the response from {context_url}")

            except requests.exceptions.RequestException as e:
                logger.exception(f"Error fetching context from {context_url}: {e}")
        
        return all_context_data

    # Traverses Context URLs and stores @context registries ​​in list
    def store_context_registries_in_list(self, data):
        context_urls = data.get("@context", [])
        all_context_registries = []
        for context_url in context_urls:
            try:
                # Make a GET request to each URL in the list
                logger.info(f"Fetching context from {context_url}")
                response = requests.get(context_url)
                response.raise_for_status()
                context_data = response.json()

                if "@context" in context_data:
                    all_context_registries.append(context_data["@context"])
                    
                else:
                    logger.warning(f"No '@context' found in the response from {context_url}")

            except requests.exceptions.RequestException as e:
                logger.exception(f"Error fetching context from {context_url}: {e}")
        
        return all_context_registries
    
    # Traverses contextdata metadata URLs and stores context matadata registries ​​in list
    def store_metadata_registries_in_list(self, data):
        context_urls = data.get("@context", [])
        all_context_registries = []
        for context_url in context_urls:
            try:
                context_url = context_url.replace("context.jsonld", "metadata.json")
                # Make a GET request to each URL in the list
                logger.info(f"Fetching context metadata from {context_url}")
                response = requests.get(context_url)
                response.raise_for_status()
                context_metadata = response.json()

                if "@context" in context_metadata:
                    all_context_registries.append(context_metadata)
                    
                else:
                    logger.warning(f"No '@context' found in the response from {context_url}")

            except requests.exceptions.RequestException as e:
                logger.exception(f"Error fetching context from {context_url}: {e}")
        
        return all_context_registries