import pandas as pd
import numpy as np
from sklearn.datasets import make_classification
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import StandardScaler

# Load the original dataset
df = pd.read_csv('../data/01-raw/Breast_cancer_dataset.csv')

# Prepare the data
X = df.drop(['Unnamed: 32', 'diagnosis'], axis=1)
y = df['diagnosis'].map({'M': 1, 'B': 0})  # Convert to binary: Malignant=1, Benign=0

# Method 1: Using make_classification to generate synthetic data
print("Generating synthetic data using make_classification...")

# Get the characteristics of the original data
n_features = X.shape[1]
n_samples = 15000
class_ratio = y.value_counts(normalize=True).values

# Generate synthetic data with similar characteristics
X_synth1, y_synth1 = make_classification(
    n_samples=n_samples,
    n_features=n_features,
    n_informative=min(20, n_features),  # Use most features as informative
    n_redundant=2,
    n_repeated=0,
    n_clusters_per_class=1,
    weights=class_ratio,  # Maintain original class distribution
    flip_y=0.01,  # Small amount of noise
    random_state=42
)

# Scale the synthetic data to match the original data's scale
scaler = StandardScaler()
X_original_scaled = scaler.fit_transform(X)
X_synth1_scaled = scaler.fit_transform(X_synth1)

# Adjust the scale to be more similar to the original data
X_original_mean = np.mean(X_original_scaled, axis=0)
X_original_std = np.std(X_original_scaled, axis=0)

X_synth1_final = X_synth1_scaled * X_original_std + X_original_mean

# Method 2: Using SMOTE to generate synthetic data
print("Generating synthetic data using SMOTE...")

# Apply SMOTE to generate more samples
smote = SMOTE(
    sampling_strategy='auto',  # Balance the classes
    random_state=42,
    k_neighbors=5
)

# Generate synthetic samples using SMOTE
X_synth2, y_synth2 = smote.fit_resample(X, y)

# If we need exactly 10,000 samples, we can oversample further
if len(X_synth2) < n_samples:
    # Calculate how many more samples we need
    additional_samples = n_samples - len(X_synth2)
    
    # Apply SMOTE again to get the required number
    X_temp, y_temp = smote.fit_resample(X_synth2, y_synth2)
    
    # Take the first n_samples samples
    X_synth2 = X_temp[:n_samples]
    y_synth2 = y_temp[:n_samples]
else:
    # Take exactly n_samples samples
    X_synth2 = X_synth2[:n_samples]
    y_synth2 = y_synth2[:n_samples]

# Create DataFrames for both synthetic datasets
feature_names = X.columns.tolist()

# Dataset 1: make_classification
df_synth1 = pd.DataFrame(X_synth1_final, columns=feature_names)
df_synth1['diagnosis'] = y_synth1
df_synth1['diagnosis'] = df_synth1['diagnosis'].map({1: 'M', 0: 'B'})
df_synth1['Unnamed: 32'] = range(n_samples*100, n_samples*100 + len(df_synth1))  # Generate unique IDs

# Reorder columns to match original
df_synth1 = df_synth1[['Unnamed: 32', 'diagnosis'] + feature_names]

# Dataset 2: SMOTE
df_synth2 = pd.DataFrame(X_synth2, columns=feature_names)
df_synth2['diagnosis'] = y_synth2
df_synth2['diagnosis'] = df_synth2['diagnosis'].map({1: 'M', 0: 'B'})
df_synth2['Unnamed: 32'] = range(2000000, 2000000 + len(df_synth2))  # Generate unique IDs

# Reorder columns to match original
df_synth2 = df_synth2[['Unnamed: 32', 'diagnosis'] + feature_names]

# Save both datasets
df_synth1.to_csv('../data/augmented/synthetic_breast_cancer_make_classification.csv', index=False)
df_synth2.to_csv('../data/augmented/synthetic_breast_cancer_smote.csv', index=False)

# Print summary statistics
print("\n=== Original Dataset ===")
print(f"Shape: {df.shape}")
print("Class distribution:")
print(df['diagnosis'].value_counts())
print(f"Malignant ratio: {df['diagnosis'].value_counts(normalize=True)['M']:.3f}")

print("\n=== Synthetic Dataset 1 (make_classification) ===")
print(f"Shape: {df_synth1.shape}")
print("Class distribution:")
print(df_synth1['diagnosis'].value_counts())
print(f"Malignant ratio: {df_synth1['diagnosis'].value_counts(normalize=True)['M']:.3f}")

print("\n=== Synthetic Dataset 2 (SMOTE) ===")
print(f"Shape: {df_synth2.shape}")
print("Class distribution:")
print(df_synth2['diagnosis'].value_counts())
print(f"Malignant ratio: {df_synth2['diagnosis'].value_counts(normalize=True)['M']:.3f}")

# Compare feature statistics
print("\n=== Feature Statistics Comparison ===")
print("Original dataset - Mean of first 5 features:")
print(X.iloc[:, :5].mean())

print("\nSynthetic dataset 1 - Mean of first 5 features:")
print(df_synth1.iloc[:, 2:7].mean())  # Skip id and diagnosis columns

print("\nSynthetic dataset 2 - Mean of first 5 features:")
print(df_synth2.iloc[:, 2:7].mean())  # Skip id and diagnosis columns

print(f"\nSynthetic datasets saved as:")
print("- synthetic_breast_cancer_make_classification.csv")
print("- synthetic_breast_cancer_smote.csv")