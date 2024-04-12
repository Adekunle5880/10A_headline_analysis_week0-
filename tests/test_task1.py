import os
import unittest
import pandas as pd

class TestTask1(unittest.TestCase):
    def setUp(self):
        # Set up the data file paths
        self.data = os.path.join(os.path.dirname(__file__), "data_folder")
        self.data_csv_path = os.path.join(self.data, "/Users/expert/Desktop/10-Academy-Week0/data/data.csv")
        self.domains_location_csv_path = os.path.join(self.data, "/Users/expert/Desktop/10-Academy-Week0/data/domains_location.csv")
        self.traffic_data_csv_path = os.path.join(self.data, "/Users/expert/Desktop/10-Academy-Week0/data/traffic.csv")
        
    def test_data_loading(self):
        # Load the data
        data = pd.read_csv(self.data_csv_path)
        domains_location = pd.read_csv(self.domains_location_csv_path)
        traffic_data = pd.read_csv(self.traffic_data_csv_path)
        
        # Ensure dataframes are not empty
        self.assertFalse(data.empty, "Data dataframe is empty.")
        self.assertFalse(domains_location.empty, "Domains Location dataframe is empty.")
        self.assertFalse(traffic_data.empty, "Traffic Data dataframe is empty.")
        
        # Check if all expected columns are present
        expected_columns_data = ['article_id', 'source_id', 'source_name', 'author', 'title', 
                                 'description', 'url', 'url_to_image', 'published_at', 'content', 
                                 'category', 'article', 'title_sentiment']
        expected_columns_domains_location = ['SourceCommonName', 'location', 'Country']
        expected_columns_traffic_data = ['GlobalRank', 'TldRank', 'Domain', 'TLD', 
                                         'RefSubNets', 'RefIPs', 'IDN_Domain', 
                                         'IDN_TLD', 'PrevGlobalRank', 'PrevTldRank', 
                                         'PrevRefSubNets', 'PrevRefIPs']
        
        self.assertCountEqual(data.columns.tolist(), expected_columns_data, 
                              "Columns mismatch in Data dataframe.")
        self.assertCountEqual(domains_location.columns.tolist(), expected_columns_domains_location, 
                              "Columns mismatch in Domains Location dataframe.")
        self.assertCountEqual(traffic_data.columns.tolist(), expected_columns_traffic_data, 
                              "Columns mismatch in Traffic Data dataframe.")


if __name__ == '__main__':
    unittest.main()