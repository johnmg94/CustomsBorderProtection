import pandas as pd
import feature_engineering as fe
import plot_functions as pf
import analysis_functions as af
import export_to_sql as es
import os
from dotenv import load_dotenv

class FeaturePipeline:
    def __init__(self, df: pd.DataFrame):
        """Initialize with a DataFrame"""
        self.df = df

    def export_to_sql(self, table_name):
        return es.export_to_sql_from_df(self.df, table_name)


    def apply_feature_engineering(self):
        """Apply feature engineering functions"""
        self.df = fe.process_features(self.df)  # Modify as per your functions
        return self.df
    
    def get_cols(self):
        """Get Columns of Data Frame"""
        columns = self.df.columns
        return columns

    def plot_distribution(self, col=None):
        """Generate a plot for a specific column"""
        pf.create_df_plot(self.df)

    def run_linear_regression(self, x_col, y_col):
        """Run a simple linear regression"""
        return af.linear_regression(self.df, x_col, y_col)

    def correlation(self, x_col, y_col):
        return af.correlation(self.df, x_col, y_col)
    
    def save_data_dictionary(self, file_path="data_dictionary.csv"):
        """Save column mappings or transformations as a data dictionary"""
        mapping = {col: self.df[col].unique().tolist() for col in self.df.columns}
        mapping_df = pd.DataFrame(list(mapping.items()), columns=["Column", "Unique Values"])
        mapping_df.to_csv(file_path, index=False)
        print(f"Data dictionary saved to {file_path}")

# Example Usage:
file_path = r'C:\Users\johnm\Code\Research\CustomsBorderProtection\assets\nationwide-encounters-fy22-fy25-dec-aor.csv'
# file_path = os.environ.get('FILE_PATH')
df = pd.read_csv(file_path)
pipeline = FeaturePipeline(df)
pipeline.apply_feature_engineering()
print(pipeline.get_cols())
# pipeline.plot_distribution()
# pipeline.export_to_sql('nationwide_encounters_fy22_25_features')
pipeline.correlation('Demographiccount(1)', 'Encounter Countcount(1)')
# pipeline.run_linear_regression("feature1", "feature2")
# pipeline.save_data_dictionary()
