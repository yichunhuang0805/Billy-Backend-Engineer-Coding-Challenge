import unittest
from count import load_data, clean_data, update_counts, generate_results

class TestBitlyDataProcessing(unittest.TestCase):

    def test_load_data(self):
        df, df2, count_dict = load_data()
        self.assertFalse(df.empty, "DataFrame df should not be empty")
        self.assertFalse(df2.empty, "DataFrame df2 should not be empty")
        self.assertIsInstance(count_dict, dict, "count_dict should be a dictionary")
        self.assertTrue('key' in df.columns, "'key' should be a column in the DataFrame df")

    def test_clean_data(self):
        _, df2, _ = load_data()
        cleaned_df2 = clean_data(df2)
        self.assertFalse(cleaned_df2.empty, "DataFrame cleaned_df2 should not be empty")
        self.assertTrue(cleaned_df2['bitlink'].str.startswith('http://').all(), "All 'bitlink' entries should start with 'http://'")
    
    def test_update_counts(self):
        _, df2, count_dict = load_data()
        cleaned_df2 = clean_data(df2)
        updated_counts = update_counts(cleaned_df2, count_dict)
        self.assertIsInstance(updated_counts, dict, "updated_counts should be a dictionary")
        self.assertTrue(all(value >= 0 for value in updated_counts.values()), "All counts should be non-negative")

    def test_generate_results(self):
        df, df2, count_dict = load_data()
        cleaned_df2 = clean_data(df2)
        updated_counts = update_counts(cleaned_df2, count_dict)
        results_df = generate_results(df, updated_counts)
        self.assertFalse(results_df.empty, "results_df should not be empty")
        self.assertTrue('count' in results_df.columns, "'count' should be a column in the results DataFrame")

if __name__ == '__main__':
    unittest.main()
