import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def create_plot(new_df):
    # Set plot style
    sns.set_style("whitegrid")

    # Iterate through columns and create plots
    # if len(new_df.columns > 1):
    if isinstance(new_df, pd.Series):
        # Create subplots
        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(8, 4))

        col = 0
        # ax = axes[i] if len(new_df.columns) > 1 else axes  # Handle single column case
        if new_df[col].dtype == 'object' or new_df[col].dtype == 'category':  # Categorical columns
            sns.countplot(data=new_df, x=col, ax=axes, palette="viridis")
            axes.set_title(f"Distribution of {col}")
            axes.set_ylabel("Count")
        else:  # Numerical columns
            sns.histplot(new_df, bins=10, kde=True, ax=axes, color="blue")
            axes.set_title(f"Distribution of {col}")
            axes.set_ylabel("Frequency")


def create_df_plot(new_df):
    sns.set_style("whitegrid")
    fig, axes = plt.subplots(nrows=len(new_df.columns), ncols=1, figsize=(8, len(new_df.columns) * 4))

    for i, col in enumerate(new_df.columns):
        # Create subplots

        ax = axes[i] if len(new_df.columns) > 1 else axes  # Handle single column case
        if new_df[col].dtype == 'object' or new_df[col].dtype == 'category':  # Categorical columns
            sns.countplot(data=new_df, x=col, ax=ax, palette="viridis")
            ax.set_title(f"Distribution of {col}")
            ax.set_ylabel("Count")
        else:  # Numerical columns
            sns.histplot(new_df[col], bins=10, kde=True, ax=ax, color="blue")
            ax.set_title(f"Distribution of {col}")
            ax.set_ylabel("Frequency")
            # if new_df[col].max() > 10000:
                # ax.set_yscale('log')
# else:

    # Adjust layout and show the plots
    plt.tight_layout()
    plt.subplots_adjust(hspace=2)
    plt.show()


# def create_df_plot(new_df):
#     sns.set_style("whitegrid")
#     fig, axes = plt.subplots(nrows=len(new_df.columns), ncols=1, figsize=(10, len(new_df.columns) * 5))

#     for i, col in enumerate(new_df.columns):
#         ax = axes[i] if len(new_df.columns) > 1 else axes  # Handle single column case
        
#         if new_df[col].dtype == 'object' or new_df[col].dtype == 'category':  # Categorical columns
#             sns.countplot(data=new_df, x=col, ax=ax, palette="viridis")
#             ax.set_title(f"Distribution of {col}", fontsize=14)
#             ax.set_ylabel("Count", fontsize=12)
#             ax.set_xlabel(col, fontsize=12)
#         else:  # Numerical columns
#             sns.histplot(new_df[col], bins=30, kde=True, ax=ax, color="blue")
#             ax.set_title(f"Distribution of {col}", fontsize=14)
#             ax.set_ylabel("Frequency", fontsize=12)
#             ax.set_xlabel(col, fontsize=12)
#             if new_df[col].max() > 1000:  # Use logarithmic scale for large ranges
#                 ax.set_yscale('log')

#     # Adjust layout and show the plots
#     plt.tight_layout()
#     plt.subplots_adjust(hspace=0.5)
#     plt.show()